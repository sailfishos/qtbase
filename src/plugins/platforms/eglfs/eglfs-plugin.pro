TARGET = qeglfs

QT += platformsupport-private eglfs_device_lib-private

# Avoid X11 header collision
DEFINES += MESA_EGL_NO_X11_HEADERS

SOURCES += $$PWD/qeglfsmain.cpp

OTHER_FILES += $$PWD/eglfs.json

PLUGIN_TYPE = platforms
PLUGIN_CLASS_NAME = QEglFSIntegrationPlugin
!equals(TARGET, $$QT_DEFAULT_QPA_PLUGIN): PLUGIN_EXTENDS = -
load(qt_plugin)
