/****************************************************************************
**
** Copyright (C) 2014 Jolla Ltd, author: <robin.burchell@jollamobile.com>
** Contact: http://www.qt-project.org/legal
**
** This file is part of the QtCore module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and Digia.  For licensing terms and
** conditions see http://qt.digia.com/licensing.  For further information
** use the contact form at http://qt.digia.com/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU Lesser General Public License version 2.1 requirements
** will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Digia gives you certain additional
** rights.  These rights are described in the Digia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3.0 as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU General Public License version 3.0 requirements will be
** met: http://www.gnu.org/copyleft/gpl.html.
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "qsystrace_p.h"

#if !defined(QT_BOOTSTRAPPED) && !defined(QT_NO_DEBUG) && defined(QT_USE_LIBSYSTRACE)
# include <systrace.h>
#endif

void QSystrace::begin(const char *module, const char *tracepoint, const char *message, ...)
{
#if !defined(QT_BOOTSTRAPPED) && !defined(QT_NO_DEBUG) && defined(QT_USE_LIBSYSTRACE)
    char buffer[1024];
    va_list args;
    va_start(args, message);
    vsprintf(buffer, message, args);
    va_end(args);
    SYSTRACE_BEGIN(module, tracepoint, buffer);
#else
    Q_UNUSED(module)
    Q_UNUSED(tracepoint)
    Q_UNUSED(message)
#endif
}

void QSystrace::end(const char *module, const char *tracepoint, const char *message, ...)
{
#if !defined(QT_BOOTSTRAPPED) && !defined(QT_NO_DEBUG) && defined(QT_USE_LIBSYSTRACE)
    char buffer[1024];
    va_list args;
    va_start(args, message);
    vsprintf(buffer, message, args);
    va_end(args);
    SYSTRACE_END(module, tracepoint, message);
#else
    Q_UNUSED(module)
    Q_UNUSED(tracepoint)
    Q_UNUSED(message)
#endif
}

void QSystrace::counter(const char *module, const char *tracepoint, const char *message, ...)
{
#if !defined(QT_BOOTSTRAPPED) && !defined(QT_NO_DEBUG) && defined(QT_USE_LIBSYSTRACE)
    char buffer[1024];
    va_list args;
    va_start(args, message);
    vsprintf(buffer, message, args);
    va_end(args);
    SYSTRACE_COUNTER(module, tracepoint, message);
#else
    Q_UNUSED(module)
    Q_UNUSED(tracepoint)
    Q_UNUSED(message)
#endif
}

