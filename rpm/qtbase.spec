# Version is the date of latest commit in qtbase, followed by 'g' + few
# characters of the last git commit ID.
# NOTE: tarball's prefix is 'qt5-base' until version number starts to
# make sense. This allows to update spec contents easily as snapshots
# evolve.

Name:       qt5
Summary:    Cross-platform application and UI framework
Version:    5.6.3
Release:    1%{?dist}
License:    LGPLv2 with exception or LGPLv3 or GPLv3 or Qt Commercial
URL:        https://www.qt.io/
Source0:    %{name}-%{version}.tar.bz2
Source1:    macros.qt5-default
Source2:    qt.conf
Source100:  qtbase-rpmlintrc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl) < 3
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libjpeg-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  sharutils
BuildRequires:  pkgconfig(fontconfig)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.


%package tools
Summary:    Development tools for qtbase
Requires:   qtchooser

%description tools
This package contains useful tools for Qt development

%package qtcore
Summary:    The QtCore library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
Requires:   xdg-utils

%description qtcore
This package contains the QtCore library

%package qtcore-devel
Summary:    Development files for QtCore
Requires:   %{name}-qmake
Requires:   %{name}-tools
Requires:   %{name}-qtcore = %{version}-%{release}
Requires:   fontconfig-devel
Requires:   qtchooser

%description qtcore-devel
This package contains the files necessary to develop applications
that use the QtCore


%package qmake
Summary:    QMake
Requires:   qtchooser

%description qmake
This package contains qmake


%package plugin-bearer-connman
Summary:    Connman bearer plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-connman
This package contains the connman bearer plugin


%package plugin-bearer-generic
Summary:    Connman generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-generic
This package contains the connman generic bearer plugin


%package plugin-bearer-nm
Summary:    Connman generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-nm
This package contains the connman NetworkManager bearer plugin


%package plugin-imageformat-gif
Summary:    Gif image format plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-gif
This package contains the gif imageformat plugin


%package plugin-imageformat-ico
Summary:    Ico image format plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-ico
This package contains the ico imageformat plugin


%package plugin-imageformat-jpeg
Summary:    JPEG image format plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-jpeg
This package contains the JPEG imageformat plugin


%package plugin-platform-minimal
Summary:    Minimal platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimal
This package contains the minimal platform plugin

%package plugin-platform-offscreen
Summary:    Offscreen platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-offscreen
This package contains the offscreen platform plugin

%package plugin-platform-eglfs
Summary:    Eglfs platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description plugin-platform-eglfs
This package contains the eglfs platform plugin

%package plugin-platform-minimalegl
Summary:    Minimalegl platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimalegl
This package contains the minimalegl platform plugin

%package plugin-platform-linuxfb
Summary:    Linux framebuffer platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-linuxfb
This package contains the linuxfb platform plugin for Qt

%package plugin-printsupport-cups
Summary:    CUPS print support plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-printsupport-cups
This package contains the CUPS print support plugin

%package plugin-sqldriver-sqlite
Summary:    Sqlite sql driver plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-sqldriver-sqlite
This package contains the sqlite sql driver plugin


%package plugin-platforminputcontext-ibus
Summary:    ibus platform import context plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platforminputcontext-ibus
This package contains the ibus platform input context plugin

%package plugin-generic-evdev
Summary:    evdev generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-generic-evdev
This package contains evdev plugins

%package plugin-generic-tuiotouch
Summary:    tuio touch generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-generic-tuiotouch
This package contains tuio touch plugins


%package qtdbus
Summary:    The QtDBus library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtdbus
This package contains the QtDBus library


%package qtdbus-devel
Summary:    Development files for QtDBus
Requires:   %{name}-qtdbus = %{version}-%{release}
Requires:   pkgconfig(dbus-1)

%description qtdbus-devel
This package contains the files necessary to develop
applications that use QtDBus


%package qtgui
Summary:    The QtGui Library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtgui
This package contains the QtGui library


%package qtgui-devel
Summary:    Development files for QtGui
Requires:   %{name}-qtgui = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description qtgui-devel
This package contains the files necessary to develop
applications that use QtGui


%package qtnetwork
Summary:    The QtNetwork library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtnetwork
This package contains the QtNetwork library


%package qtnetwork-devel
Summary:    Development files for QtNetwork
Requires:   %{name}-qtnetwork = %{version}-%{release}

%description qtnetwork-devel
This package contains the files necessary to develop
applications that use QtNetwork



%package qtopengl
Summary:    The QtOpenGL library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtopengl
This package contains the QtOpenGL library


%package qtopengl-devel
Summary:    Development files for QtOpenGL
Requires:   %{name}-qtopengl = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description qtopengl-devel
This package contains the files necessary to develop
applications that use QtOpenGL


%package qtsql
Summary:    The QtSql library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtsql
This package contains the QtSql library


%package qtsql-devel
Summary:    Development files for QtSql
Requires:   %{name}-qtsql = %{version}-%{release}

%description qtsql-devel
This package contains the files necessary to develop
applications that use QtSql


%package qttest
Summary:    The QtTest library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qttest
This package contains the QtTest library


%package qttest-devel
Summary:    Development files for QtTest
Requires:   %{name}-qttest = %{version}-%{release}

%description qttest-devel
This package contains the files necessary to develop
applications that use QtTest


%package qtxml
Summary:    The QtXml library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtxml
This package contains the QtXml library

%package qtxml-devel
Summary:    Development files for QtXml
Requires:   %{name}-qtxml = %{version}-%{release}

%description qtxml-devel
This package contains the files necessary to develop
applications that use QtXml


%package qtwidgets
Summary:    The QtWidgets library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtwidgets
This package contains the QtWidgets library

%package qtwidgets-devel
Summary:    Development files for QtWidgets
Requires:   %{name}-qtwidgets = %{version}-%{release}

%description qtwidgets-devel
This package contains the files necessary to develop
applications that use QtWidgets

%package qtplatformsupport-devel
Summary:    Development files for QtPlatformSupport

%description qtplatformsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport

%package qtbootstrap-devel
Summary:    Development files for QtBootstrap

%description qtbootstrap-devel
This package contains the files necessary to develop
applications that use QtBootstrap

%package qtprintsupport
Summary:    The QtPrintSupport
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtprintsupport
This package contains the QtPrintSupport library

%package qtprintsupport-devel
Summary:    Development files for QtPrintSupport
Requires:   %{name}-qtprintsupport = %{version}-%{release}

%description qtprintsupport-devel
This package contains the files necessary to develop
applications that use QtPrintSupport

%package qtconcurrent
Summary:    QtConcurrent library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtconcurrent
This package contains the QtConcurrent library

%package qtconcurrent-devel
Summary:    Development files for QtConcurrent
Requires:   %{name}-qtconcurrent = %{version}-%{release}

%description qtconcurrent-devel
This package contains the files necessary to develop
applications that use QtConcurrent

%package -n qt5-default
Summary:    Qt5 development defaults packafge
Requires:   qtchooser
Provides:   qt-default
Conflicts:   qt4-default

%description -n qt5-default
Qt is a cross-platform application and UI framework. Using Qt, you can write
web-enabled applications once and deploy them across desktop, mobile and
embedded operating systems without rewriting the source code.

This package contains the Qt5 development defaults package



##### Build section

%prep
%setup -q -n qt5-%{version}

%build
touch .git

if [ -f "./config.status" ]; then
    echo "config.status already exists, not running configure to save time";
else
MAKEFLAGS=%{?_smp_mflags} \
./configure --disable-static \
    -confirm-license \
    -platform linux-g++ \
    -prefix "%{_prefix}" \
    -bindir "%{_libdir}/qt5/bin" \
    -libdir "%{_libdir}" \
    -docdir "%{_docdir}/qt5/" \
    -headerdir "%{_includedir}/qt5" \
    -datadir "%{_datadir}/qt5" \
    -plugindir "%{_libdir}/qt5/plugins" \
    -importdir "%{_libdir}/qt5/imports" \
    -translationdir "%{_datadir}/qt5/translations" \
    -sysconfdir "%{_sysconfdir}/xdg" \
    -examplesdir "%{_libdir}/qt5/examples" \
    -archdatadir "%{_datadir}/qt5" \
    -testsdir "%{_libdir}/qt5/tests" \
    -qmldir "%{_libdir}/qt5/qml" \
    -libexecdir "%{_libdir}/qt5/libexec" \
    -opensource \
    -no-sql-ibase \
    -no-sql-mysql \
    -no-sql-odbc \
    -no-sql-psql \
    -plugin-sql-sqlite \
    -no-sql-sqlite2 \
    -no-sql-tds \
    -system-sqlite \
    -audio-backend \
    -system-zlib \
    -system-libpng \
    -system-libjpeg \
    -system-proxies \
    -no-rpath \
    -optimized-qmake \
    -dbus-linked \
    -openssl-linked \
    -no-strip \
    -no-separate-debug-info \
    -verbose \
    -no-gtkstyle \
    -opengl es2 \
    -no-openvg \
    -lfontconfig \
    -I/usr/include/freetype2 \
    -nomake tests \
    -nomake examples \
    -no-xkbcommon \
    -no-xcb \
    -no-xinput2 \
    -largefile \
%ifarch aarch64
	-no-pch \
%endif
    -kms \
    -gbm \
%ifnarch aarch64
    -qreal float \
%endif
    -journald \
    -no-use-gold-linker \
    -openssl-linked
fi # config.status check
#%if ! 0%{?qt5_release_build}
#    -developer-build \
#%endif

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
#
# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# these manage to really royally screw up cmake
find %{buildroot}%{_libdir} -type f -name "*_*Plugin.cmake" \
-exec rm {} \;

find %{buildroot}%{_docdir}/qt5/ -type f -exec chmod ugo-x {} \;

# Make sure these are around
mkdir -p %{buildroot}%{_includedir}/qt5/
mkdir -p %{buildroot}%{_datadir}/qt5/
mkdir -p %{buildroot}%{_libdir}/qt5/plugins/
mkdir -p %{buildroot}%{_libdir}/qt5/imports/
mkdir -p %{buildroot}%{_libdir}/qt5/translations/
mkdir -p %{buildroot}%{_libdir}/qt5/examples/
#
# Install qmake rpm macros
install -D -p -m 0644 %{_sourcedir}/macros.qt5-default \
%{buildroot}/%{_rpmmacrodir}/macros.qt5-default

# Add a configuration link for qtchooser - the 5.conf is installed by qtchooser
mkdir -p %{buildroot}/etc/xdg/qtchooser
ln -s %{_sysconfdir}/xdg/qtchooser/5.conf %{buildroot}%{_sysconfdir}/xdg/qtchooser/default.conf

# Help accelerated qmake find the configuration
%if "%{_libdir}" == "/usr/lib64"
install -D -p -m 0644 %{_sourcedir}/qt.conf %{buildroot}%{_libdir}/qt5/bin/qt.conf
%endif

#
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_datadir}


#### Pre/Post section

%post qtcore -p /sbin/ldconfig
%postun qtcore -p /sbin/ldconfig

%post qtdbus -p /sbin/ldconfig
%postun qtdbus -p /sbin/ldconfig

%post qtsql -p /sbin/ldconfig
%postun qtsql -p /sbin/ldconfig

%post qtnetwork -p /sbin/ldconfig
%postun qtnetwork -p /sbin/ldconfig

%post qtgui -p /sbin/ldconfig
%postun qtgui -p /sbin/ldconfig

%post qttest -p /sbin/ldconfig
%postun qttest -p /sbin/ldconfig

%post qtopengl -p /sbin/ldconfig
%postun qtopengl -p /sbin/ldconfig

%post qtxml -p /sbin/ldconfig
%postun qtxml -p /sbin/ldconfig

%post qtprintsupport -p /sbin/ldconfig
%postun qtprintsupport -p /sbin/ldconfig

%post qtwidgets -p /sbin/ldconfig
%postun qtwidgets -p /sbin/ldconfig

%post qtconcurrent -p /sbin/ldconfig
%postun qtconcurrent -p /sbin/ldconfig

%post plugin-platform-eglfs -p /sbin/ldconfig
%postun plugin-platform-eglfs -p /sbin/ldconfig


%files tools
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/moc
%{_libdir}/qt5/bin/rcc
%{_libdir}/qt5/bin/syncqt.pl
%{_libdir}/qt5/bin/uic
%{_libdir}/qt5/bin/qlalr
%{_libdir}/qt5/bin/fixqt4headers.pl
%{_docdir}/qt5/*

%files qtcore
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LICENSE.LGPLv3 LGPL_EXCEPTION.txt LICENSE.GPLv3
%dir %{_includedir}/qt5/
%dir %{_datadir}/qt5/
%dir %{_libdir}/qt5/
%dir %{_libdir}/qt5/bin/
%dir %{_libdir}/qt5/plugins/
%dir %{_libdir}/qt5/plugins/platforms/
%dir %{_libdir}/qt5/imports/
%dir %{_libdir}/qt5/translations/
%dir %{_libdir}/qt5/examples/
%{_libdir}/libQt5Core.so.*

%files qtcore-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtCore/
%{_libdir}/libQt5Core.prl
%{_libdir}/libQt5Core.so
%{_libdir}/pkgconfig/Qt5Core.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_core.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_core_private.pri
%{_libdir}/cmake/Qt5
%{_libdir}/cmake/Qt5Core

%files qmake
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qmake
%if "%{_libdir}" == "/usr/lib64"
%{_libdir}/qt5/bin/qt.conf
%endif
%{_datadir}/qt5/mkspecs/aix-*/
%{_datadir}/qt5/mkspecs/android-clang/*
%{_datadir}/qt5/mkspecs/blackberry*/
%{_datadir}/qt5/mkspecs/common/
%{_datadir}/qt5/mkspecs/cygwin-*/
%{_datadir}/qt5/mkspecs/darwin-*/
%{_datadir}/qt5/mkspecs/features/
%{_datadir}/qt5/mkspecs/freebsd-*/
%{_datadir}/qt5/mkspecs/haiku-g++/
%{_datadir}/qt5/mkspecs/hpux-*
%{_datadir}/qt5/mkspecs/hpuxi-*
%{_datadir}/qt5/mkspecs/hurd-g++/
%{_datadir}/qt5/mkspecs/irix-*/
%{_datadir}/qt5/mkspecs/linux-*/
%{_datadir}/qt5/mkspecs/lynxos-*/
%{_datadir}/qt5/mkspecs/macx-*/
%{_datadir}/qt5/mkspecs/netbsd-*/
%{_datadir}/qt5/mkspecs/openbsd-*/
%{_datadir}/qt5/mkspecs/qconfig.pri
%{_datadir}/qt5/mkspecs/qmodule.pri
%{_datadir}/qt5/mkspecs/qnx*/
%{_datadir}/qt5/mkspecs/sco-*/
%{_datadir}/qt5/mkspecs/solaris-*/
%{_datadir}/qt5/mkspecs/tru64-*/
%{_datadir}/qt5/mkspecs/unixware-*/
%{_datadir}/qt5/mkspecs/unsupported/
%{_datadir}/qt5/mkspecs/win32-g++/
%{_datadir}/qt5/mkspecs/win32-icc/
%{_datadir}/qt5/mkspecs/win32-msvc20*/
%{_datadir}/qt5/mkspecs/wince*/
%{_datadir}/qt5/mkspecs/winphone*/
%{_datadir}/qt5/mkspecs/winrt*/
%{_datadir}/qt5/mkspecs/devices/
%{_datadir}/qt5/mkspecs/qdevice.pri
%{_datadir}/qt5/mkspecs/qfeatures.pri
%{_rpmmacrodir}/macros.qt5-default

%files qtdbus
%defattr(-,root,root,-)
%{_libdir}/libQt5DBus.so.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qdbuscpp2xml
%{_libdir}/qt5/bin/qdbusxml2cpp
%{_includedir}/qt5/QtDBus/
%{_libdir}/libQt5DBus.so
%{_libdir}/libQt5DBus.prl
%{_libdir}/pkgconfig/Qt5DBus.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_dbus.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_dbus_private.pri
%{_libdir}/cmake/Qt5DBus


%files qtgui
%defattr(-,root,root,-)
%dir %{_libdir}/qt5/plugins/imageformats/
%dir %{_libdir}/qt5/plugins/platforminputcontexts/
%{_libdir}/libQt5Gui.so.*


%files qtgui-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtGui/
%{_includedir}/qt5/QtPlatformHeaders/
%{_libdir}/libQt5Gui.prl
%{_libdir}/libQt5Gui.so
%{_libdir}/pkgconfig/Qt5Gui.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_gui.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_gui_private.pri
%{_libdir}/cmake/Qt5Gui


%files qtnetwork
%defattr(-,root,root,-)
%dir %{_libdir}/qt5/plugins/bearer/
%{_libdir}/libQt5Network.so.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtNetwork/
%{_libdir}/libQt5Network.prl
%{_libdir}/libQt5Network.so
%{_libdir}/pkgconfig/Qt5Network.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_network.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_network_private.pri
%{_libdir}/cmake/Qt5Network


%files qtopengl
%defattr(-,root,root,-)
%{_libdir}/libQt5OpenGL.so.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtOpenGL/
%{_includedir}/qt5/QtOpenGLExtensions/
%{_libdir}/libQt5OpenGL.prl
%{_libdir}/libQt5OpenGLExtensions.prl
%{_libdir}/libQt5OpenGL.so
%{_libdir}/libQt5OpenGLExtensions.a
%{_libdir}/pkgconfig/Qt5OpenGL.pc
%{_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_opengl.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_opengl_private.pri
%{_datadir}/qt5/mkspecs/android-g++/qmake.conf
%{_datadir}/qt5/mkspecs/android-g++/qplatformdefs.h
%{_datadir}/qt5/mkspecs/modules/qt_lib_openglextensions.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_openglextensions_private.pri
%{_libdir}/cmake/Qt5OpenGL
%{_libdir}/cmake/Qt5OpenGLExtensions


%files qtsql
%defattr(-,root,root,-)
%dir %{_libdir}/qt5/plugins/sqldrivers/
%{_libdir}/libQt5Sql.so.*


%files qtsql-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtSql/
%{_libdir}/libQt5Sql.prl
%{_libdir}/libQt5Sql.so
%{_libdir}/pkgconfig/Qt5Sql.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_sql.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_sql_private.pri
%{_libdir}/cmake/Qt5Sql


%files qttest
%defattr(-,root,root,-)
%{_libdir}/libQt5Test.so.*

%files qttest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtTest/
%{_libdir}/libQt5Test.prl
%{_libdir}/libQt5Test.so
%{_libdir}/pkgconfig/Qt5Test.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_testlib.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_testlib_private.pri
%{_libdir}/cmake/Qt5Test

%files qtxml
%defattr(-,root,root,-)
%{_libdir}/libQt5Xml.so.*

%files qtxml-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtXml/
%{_libdir}/libQt5Xml.prl
%{_libdir}/libQt5Xml.so
%{_libdir}/pkgconfig/Qt5Xml.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_xml.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_xml_private.pri
%{_libdir}/cmake/Qt5Xml

%files qtwidgets
%defattr(-,root,root,-)
%{_libdir}/libQt5Widgets.so.*

%files qtwidgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtWidgets/
%{_libdir}/libQt5Widgets.prl
%{_libdir}/libQt5Widgets.so
%{_libdir}/pkgconfig/Qt5Widgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_widgets.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_widgets_private.pri
%{_libdir}/cmake/Qt5Widgets

%files qtplatformsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPlatformSupport/
%{_libdir}/libQt5PlatformSupport.prl
%{_libdir}/libQt5PlatformSupport.a
%{_datadir}/qt5/mkspecs/modules/qt_lib_platformsupport_private.pri

%files qtbootstrap-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Bootstrap.prl
%{_libdir}/libQt5Bootstrap.a
%{_datadir}/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri

%files qtprintsupport
%defattr(-,root,root,-)
%{_libdir}/libQt5PrintSupport.so.*

%files qtprintsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPrintSupport/
%{_libdir}/libQt5PrintSupport.prl
%{_libdir}/libQt5PrintSupport.so
%{_libdir}/pkgconfig/Qt5PrintSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_printsupport.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_printsupport_private.pri
%{_libdir}/cmake/Qt5PrintSupport

%files qtconcurrent
%defattr(-,root,root,-)
%{_libdir}/libQt5Concurrent.so.*

%files qtconcurrent-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtConcurrent/
%{_libdir}/libQt5Concurrent.prl
%{_libdir}/libQt5Concurrent.so
%{_libdir}/pkgconfig/Qt5Concurrent.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_concurrent.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_concurrent_private.pri
%{_libdir}/cmake/Qt5Concurrent




%files plugin-bearer-connman
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqconnmanbearer.so

%files plugin-bearer-generic
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqgenericbearer.so

%files plugin-bearer-nm
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqnmbearer.so

%files plugin-imageformat-gif
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqgif.so

%files plugin-imageformat-ico
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqico.so

%files plugin-imageformat-jpeg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqjpeg.so

%files plugin-platform-minimal
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimal.so

%files plugin-platform-offscreen
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqoffscreen.so

%files plugin-platform-eglfs
%defattr(-,root,root,-)
%{_libdir}/libQt5EglDeviceIntegration.so*
%{_libdir}/libQt5EglDeviceIntegration.prl
%{_libdir}/qt5/plugins/platforms/libqeglfs.so
%if %{with X11}
%{_libdir}/qt5/plugins/egldeviceintegrations/libqeglfs-x11-integration.so
%endif
%{_libdir}/qt5/plugins/egldeviceintegrations/libqeglfs-kms-integration.so
%{_libdir}/qt5/plugins/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so
%{_datadir}/qt5/mkspecs/modules/qt_lib_eglfs_device_lib_private.pri

%files plugin-platform-minimalegl
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimalegl.so

%files plugin-platform-linuxfb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqlinuxfb.so

%files plugin-printsupport-cups
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/printsupport/libcupsprintersupport.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%files plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so

%files plugin-generic-evdev
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/generic/libqevdev*plugin.so

%files plugin-generic-tuiotouch
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/generic/libqtuiotouchplugin.so

%files -n qt5-default
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/qtchooser/default.conf

#### No changelog section, separate $pkg.changes contains the history
