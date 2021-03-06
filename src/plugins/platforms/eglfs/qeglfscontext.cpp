/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the plugins of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL21$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 or version 3 as published by the Free
** Software Foundation and appearing in the file LICENSE.LGPLv21 and
** LICENSE.LGPLv3 included in the packaging of this file. Please review the
** following information to ensure the GNU Lesser General Public License
** requirements will be met: https://www.gnu.org/licenses/lgpl.html and
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** As a special exception, The Qt Company gives you certain additional
** rights. These rights are described in The Qt Company LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "qeglfsglobal.h"
#include <QtGui/QSurface>
#include <QtPlatformSupport/private/qeglconvenience_p.h>
#include <QtPlatformSupport/private/qeglpbuffer_p.h>

#include "qeglfscontext.h"
#include "qeglfswindow.h"
#include "qeglfshooks.h"
#include "qeglfscursor.h"
#include "qeglfsintegration.h"

#include <QtPlatformSupport/private/qeglpbuffer_p.h>
#include <QtGui/QSurface>
#include <QtDebug>
#include <QOpenGLFramebufferObject>
#include <QOpenGLShaderProgram>

QT_BEGIN_NAMESPACE


class Blitter : public QOpenGLFunctions
{
public:
    Blitter(QEglFSContext *context)
        : m_context(context)
    {
        initializeOpenGLFunctions();
        m_blitProgram = new QOpenGLShaderProgram();
        m_blitProgram->addShaderFromSourceCode(QOpenGLShader::Vertex, "attribute vec4 position;\n\
                                                                    attribute vec2 texCoords;\n\
                                                                    varying vec2 outTexCoords;\n\
                                                                    void main()\n\
                                                                    {\n\
                                                                        gl_Position = position;\n\
                                                                        outTexCoords = texCoords;\n\
                                                                    }");
        m_blitProgram->addShaderFromSourceCode(QOpenGLShader::Fragment, "varying highp vec2 outTexCoords;\n\
                                                                        uniform sampler2D texture;\n\
                                                                        void main()\n\
                                                                        {\n\
                                                                            gl_FragColor = texture2D(texture, outTexCoords);\n\
                                                                        }");

        m_blitProgram->bindAttributeLocation("position", 0);
        m_blitProgram->bindAttributeLocation("texCoords", 1);

        if (!m_blitProgram->link()) {
            qDebug() << "Shader Program link failed.";
            qDebug() << m_blitProgram->log();
        }
    }
    ~Blitter()
    {
        delete m_blitProgram;
    }
    void blit(QOpenGLFramebufferObject *fbo, const QSize &size)
    {
        glViewport(0, 0, size.width(), size.height());

        glDisable(GL_DEPTH_TEST);
        glDisable(GL_BLEND);
        glDisable(GL_CULL_FACE);
        glDisable(GL_SCISSOR_TEST);
        glDepthMask(GL_FALSE);
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE);

        m_context->m_useNativeDefaultFbo = true;
        glBindFramebuffer(GL_FRAMEBUFFER, 0);
        m_context->m_useNativeDefaultFbo = false;

        static const GLfloat squareVertices[] = {
            -1.f, -1.f,
            1.0f, -1.f,
            -1.f,  1.0f,
            1.0f,  1.0f
        };

        static const GLfloat textureVertices[] = {
            0.0f,  0.0f,
            1.0f,  0.0f,
            0.0f,  1.0f,
            1.0f,  1.0f,
        };

        glBindBuffer(GL_ARRAY_BUFFER, 0);
        m_blitProgram->bind();

        m_blitProgram->enableAttributeArray(0);
        m_blitProgram->enableAttributeArray(1);
        m_blitProgram->setAttributeArray(1, textureVertices, 2);

        glActiveTexture(GL_TEXTURE0);

        //Draw Content
        m_blitProgram->setAttributeArray(0, squareVertices, 2);
        glBindTexture(GL_TEXTURE_2D, fbo->texture());
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);

        //Cleanup
        m_blitProgram->disableAttributeArray(0);
        m_blitProgram->disableAttributeArray(1);
    }

    QOpenGLShaderProgram *m_blitProgram;
    QEglFSContext *m_context;
};

#define STATE_GUARD_VERTEX_ATTRIB_COUNT 2

class StateGuard
{
public:
    StateGuard() {
        QOpenGLFunctions glFuncs(QOpenGLContext::currentContext());

        glGetIntegerv(GL_CURRENT_PROGRAM, (GLint *) &m_program);
        glGetIntegerv(GL_ACTIVE_TEXTURE, (GLint *) &m_activeTextureUnit);
        glGetIntegerv(GL_TEXTURE_BINDING_2D, (GLint *) &m_texture);
        glGetIntegerv(GL_FRAMEBUFFER_BINDING, (GLint *) &m_fbo);
        glGetIntegerv(GL_VIEWPORT, m_viewport);
        glGetIntegerv(GL_DEPTH_WRITEMASK, &m_depthWriteMask);
        glGetIntegerv(GL_COLOR_WRITEMASK, m_colorWriteMask);
        m_blend = glIsEnabled(GL_BLEND);
        m_depth = glIsEnabled(GL_DEPTH_TEST);
        m_cull = glIsEnabled(GL_CULL_FACE);
        m_scissor = glIsEnabled(GL_SCISSOR_TEST);
        for (int i = 0; i < STATE_GUARD_VERTEX_ATTRIB_COUNT; ++i) {
            glFuncs.glGetVertexAttribiv(i, GL_VERTEX_ATTRIB_ARRAY_ENABLED, (GLint *) &m_vertexAttribs[i].enabled);
            glFuncs.glGetVertexAttribiv(i, GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING, (GLint *) &m_vertexAttribs[i].arrayBuffer);
            glFuncs.glGetVertexAttribiv(i, GL_VERTEX_ATTRIB_ARRAY_SIZE, &m_vertexAttribs[i].size);
            glFuncs.glGetVertexAttribiv(i, GL_VERTEX_ATTRIB_ARRAY_STRIDE, &m_vertexAttribs[i].stride);
            glFuncs.glGetVertexAttribiv(i, GL_VERTEX_ATTRIB_ARRAY_TYPE, (GLint *) &m_vertexAttribs[i].type);
            glFuncs.glGetVertexAttribiv(i, GL_VERTEX_ATTRIB_ARRAY_NORMALIZED, (GLint *) &m_vertexAttribs[i].normalized);
            glFuncs.glGetVertexAttribPointerv(i, GL_VERTEX_ATTRIB_ARRAY_POINTER, &m_vertexAttribs[i].pointer);
        }
        glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, (GLint *) &m_minFilter);
        glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, (GLint *) &m_magFilter);
        glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, (GLint *) &m_wrapS);
        glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, (GLint *) &m_wrapT);
    }

    ~StateGuard() {
        QOpenGLFunctions glFuncs(QOpenGLContext::currentContext());

        glFuncs.glUseProgram(m_program);
        glActiveTexture(m_activeTextureUnit);
        glBindTexture(GL_TEXTURE_2D, m_texture);
        glFuncs.glBindFramebuffer(GL_FRAMEBUFFER, m_fbo);
        glViewport(m_viewport[0], m_viewport[1], m_viewport[2], m_viewport[3]);
        glDepthMask(m_depthWriteMask);
        glColorMask(m_colorWriteMask[0], m_colorWriteMask[1], m_colorWriteMask[2], m_colorWriteMask[3]);
        if (m_blend)
            glEnable(GL_BLEND);
        if (m_depth)
            glEnable(GL_DEPTH_TEST);
        if (m_cull)
            glEnable(GL_CULL_FACE);
        if (m_scissor)
            glEnable(GL_SCISSOR_TEST);
        for (int i = 0; i < STATE_GUARD_VERTEX_ATTRIB_COUNT; ++i) {
            if (m_vertexAttribs[i].enabled)
                glFuncs.glEnableVertexAttribArray(i);
            GLuint prevBuf;
            glGetIntegerv(GL_ARRAY_BUFFER_BINDING, (GLint *) &prevBuf);
            glFuncs.glBindBuffer(GL_ARRAY_BUFFER, m_vertexAttribs[i].arrayBuffer);
            glFuncs.glVertexAttribPointer(i, m_vertexAttribs[i].size, m_vertexAttribs[i].type,
                                          m_vertexAttribs[i].normalized, m_vertexAttribs[i].stride,
                                          m_vertexAttribs[i].pointer);
            glFuncs.glBindBuffer(GL_ARRAY_BUFFER, prevBuf);
        }
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, m_minFilter);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, m_magFilter);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, m_wrapS);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, m_wrapT);
    }

private:
    GLuint m_program;
    GLenum m_activeTextureUnit;
    GLuint m_texture;
    GLuint m_fbo;
    GLint m_depthWriteMask;
    GLint m_colorWriteMask[4];
    GLboolean m_blend;
    GLboolean m_depth;
    GLboolean m_cull;
    GLboolean m_scissor;
    GLint m_viewport[4];
    struct VertexAttrib {
        bool enabled;
        GLuint arrayBuffer;
        GLint size;
        GLint stride;
        GLenum type;
        bool normalized;
        void *pointer;
    } m_vertexAttribs[STATE_GUARD_VERTEX_ATTRIB_COUNT];
    GLenum m_minFilter;
    GLenum m_magFilter;
    GLenum m_wrapS;
    GLenum m_wrapT;
};

QEglFSContext::QEglFSContext(const QSurfaceFormat &format, QPlatformOpenGLContext *share, EGLDisplay display,
                             EGLConfig *config, const QVariant &nativeHandle)
    : QEGLPlatformContext(format, share, display, config, nativeHandle,
                          qt_egl_device_integration()->supportsSurfacelessContexts() ? Flags(0) : QEGLPlatformContext::NoSurfaceless),
      m_tempWindow(0),
      m_useNativeDefaultFbo(false),
      m_fbo(0),
      m_blitter(0)
{
    m_scale = qgetenv("QT_QPA_EGLFS_SCALE").toInt();
}

QEglFSContext::~QEglFSContext()
{
    delete m_blitter;
    delete m_fbo;
}

bool QEglFSContext::makeCurrent(QPlatformSurface *surface)
{
    bool success = QEGLPlatformContext::makeCurrent(surface);

    if (m_scale > 1)
        fbo(surface)->bind();

    return success;
}

EGLSurface QEglFSContext::eglSurfaceForPlatformSurface(QPlatformSurface *surface)
{
    if (surface->surface()->surfaceClass() == QSurface::Window)
        return static_cast<QEglFSWindow *>(surface)->surface();
    else
        return static_cast<QEGLPbuffer *>(surface)->pbuffer();
}

EGLSurface QEglFSContext::createTemporaryOffscreenSurface()
{
    if (qt_egl_device_integration()->supportsPBuffers())
        return QEGLPlatformContext::createTemporaryOffscreenSurface();

    if (!m_tempWindow) {
        m_tempWindow = qt_egl_device_integration()->createNativeOffscreenWindow(format());
        if (!m_tempWindow) {
            qWarning("QEglFSContext: Failed to create temporary native window");
            return EGL_NO_SURFACE;
        }
    }
    EGLConfig config = q_configFromGLFormat(eglDisplay(), format());
    return eglCreateWindowSurface(eglDisplay(), config, m_tempWindow, 0);
}

void QEglFSContext::destroyTemporaryOffscreenSurface(EGLSurface surface)
{
    if (qt_egl_device_integration()->supportsPBuffers()) {
        QEGLPlatformContext::destroyTemporaryOffscreenSurface(surface);
    } else {
        eglDestroySurface(eglDisplay(), surface);
        qt_egl_device_integration()->destroyNativeWindow(m_tempWindow);
        m_tempWindow = 0;
    }
}

void QEglFSContext::runGLChecks()
{
    // Note that even though there is an EGL context current here,
    // QOpenGLContext and QOpenGLFunctions are not yet usable at this stage.
    const char *renderer = reinterpret_cast<const char *>(glGetString(GL_RENDERER));
    // Be nice and warn about a common source of confusion.
    if (renderer && strstr(renderer, "llvmpipe"))
        qWarning("Running on a software rasterizer (LLVMpipe), expect limited performance.");
}

void QEglFSContext::swapBuffers(QPlatformSurface *surface)
{
    if (m_scale > 1) {
        // Must save & restore all state. Applications are usually not prepared
        // for random context state changes in a swapBuffers() call.
        StateGuard stateGuard;

        if (!m_blitter)
            m_blitter = new Blitter(this);
        m_blitter->blit(m_fbo, surface->surface()->size() / m_scale);
    }

    // draw the cursor
    if (surface->surface()->surfaceClass() == QSurface::Window) {
        QPlatformWindow *window = static_cast<QPlatformWindow *>(surface);
        if (QEglFSCursor *cursor = qobject_cast<QEglFSCursor *>(window->screen()->cursor()))
            cursor->paintOnScreen();
    }

    qt_egl_device_integration()->waitForVSync(surface);
    QEGLPlatformContext::swapBuffers(surface);
    qt_egl_device_integration()->presentBuffer(surface);
}

QOpenGLFramebufferObject *QEglFSContext::fbo(QPlatformSurface *surface) const
{
    QSize size = surface->surface()->size();
    if (!m_fbo || m_fbo->size() != size) {
        delete m_fbo;
        m_fbo = new QOpenGLFramebufferObject(size);
        m_fbo->setAttachment(QOpenGLFramebufferObject::CombinedDepthStencil);
    }
    return m_fbo;
}

GLuint QEglFSContext::defaultFramebufferObject(QPlatformSurface *surface) const
{
    if (m_useNativeDefaultFbo || m_scale <= 1)
        return 0;
    return fbo(surface)->handle();
}

QT_END_NAMESPACE
