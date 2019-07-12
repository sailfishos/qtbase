SOURCES = eglfs-egldevice.cpp

for(p, QMAKE_LIBDIR_EGL) {
    LIBS += -L$$p
}
# Avoid X11 header collision
DEFINES += MESA_EGL_NO_X11_HEADERS

INCLUDEPATH += $$QMAKE_INCDIR_EGL
LIBS += $$QMAKE_LIBS_EGL
CONFIG += link_pkgconfig
!contains(QT_CONFIG, no-pkg-config) {
    PKGCONFIG += libdrm
} else {
    LIBS += -ldrm
}
CONFIG -= qt
