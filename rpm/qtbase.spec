# libQtPlatformSupport is not built as a shared library, only as a
# static .a lib-archive. By default the OBS build removes all discovered
# libFOO.a files and as such rpmlint never complains about
# installed-but-unpackaged static libs.
# This flag tells rpmbuild to behave.
%define keepstatic 1

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
BuildRequires:  pkgconfig(openssl)
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

%define qt5_prefix         %{_prefix}
%define qt5_bindir         %{_libdir}/qt5/bin
%define qt5_libdir         %{_libdir}
%define qt5_archdatadir    %{qt5_libdir}/qt5
%define qt5_libexecdir     %{_libexecdir}/qt5
%define qt5_docdir         %{_prefix}/share/doc/qt5
%define qt5_includedir     %{_includedir}/qt5
%define qt5_datadir        %{_prefix}/share/qt5
%define qt5_translationdir %{qt5_datadir}/translations
%define qt5_plugindir      %{qt5_archdatadir}/plugins
%define qt5_importdir      %{qt5_archdatadir}/imports
%define qt5_demosdir       %{qt5_archdatadir}/demos
%define qt5_examplesdir    %{qt5_archdatadir}/examples
%define qt5_sysconfdir     %{_sysconfdir}/xdg

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
    -prefix "%{qt5_prefix}" \
    -bindir "%{qt5_bindir}" \
    -libdir "%{qt5_libdir}" \
    -docdir "%{qt5_docdir}" \
    -headerdir "%{qt5_includedir}" \
    -datadir "%{qt5_datadir}" \
    -plugindir "%{qt5_plugindir}" \
    -importdir "%{qt5_importdir}" \
    -translationdir "%{qt5_translationsdir}" \
    -sysconfdir "%{qt5_sysconfdir}" \
    -examplesdir "%{qt5_examplesdir}" \
    -archdatadir "%{qt5_archdatadir}" \
    -testsdir "%{qt5_archdatadir}/tests" \
    -qmldir "%{qt5_archdatadir}/qml" \
    -libexecdir "%{qt5_libexecdir}" \
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

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
#
# We don't need qt5/Qt/
rm -rf %{buildroot}%{qt5_includedir}/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{qt5_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# these manage to really royally screw up cmake
find %{buildroot}%{qt5_libdir} -type f -name "*_*Plugin.cmake" \
-exec rm {} \;

find %{buildroot}%{_docdir}/qt5/ -type f -exec chmod ugo-x {} \;

# Make sure these are around
mkdir -p %{buildroot}%{qt5_includedir}
mkdir -p %{buildroot}%{qt5_datadir}
mkdir -p %{buildroot}%{qt5_archdatadir}/plugins/
mkdir -p %{buildroot}%{qt5_archdatadir}/imports/
mkdir -p %{buildroot}%{qt5_archdatadir}/translations/
mkdir -p %{buildroot}%{qt5_archdatadir}/examples/
#
# Install qmake rpm macros
install -D -p -m 0644 %{_sourcedir}/macros.qt5-default \
%{buildroot}/%{_sysconfdir}/rpm/macros.qt5-default

# Add a configuration link for qtchooser - the 5.conf is installed by qtchooser
mkdir -p %{buildroot}%{qt5_sysconfdir}/qtchooser
ln -s %{qt5_sysconfdir}/qtchooser/5.conf %{buildroot}%{qt5_sysconfdir}/qtchooser/default.conf

# Help accelerated qmake find the configuration
%if "%{qt5_libdir}" == "/usr/lib64"
install -D -p -m 0644 %{_sourcedir}/qt.conf %{buildroot}%{qt5_bindir}/qt.conf
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
%{qt5_bindir}/moc
%{qt5_bindir}/rcc
%{qt5_bindir}/syncqt.pl
%{qt5_bindir}/uic
%{qt5_bindir}/qlalr
%{qt5_bindir}/fixqt4headers.pl
%{qt5_docdir}/*

%files qtcore
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LICENSE.LGPLv3 LGPL_EXCEPTION.txt LICENSE.GPLv3
%dir %{qt5_includedir}/
%dir %{_datadir}/qt5/
%dir %{qt5_archdatadir}/
%dir %{qt5_bindir}/
%dir %{qt5_archdatadir}/plugins/
%dir %{qt5_archdatadir}/plugins/platforms/
%dir %{qt5_archdatadir}/imports/
%dir %{qt5_archdatadir}/translations/
%dir %{qt5_archdatadir}/examples/
%{qt5_libdir}/libQt5Core.so.*

%files qtcore-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtCore/
%{qt5_libdir}/libQt5Core.prl
%{qt5_libdir}/libQt5Core.so
%{qt5_libdir}/pkgconfig/Qt5Core.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_core.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_core_private.pri
%{qt5_libdir}/cmake/Qt5
%{qt5_libdir}/cmake/Qt5Core

%files qmake
%defattr(-,root,root,-)
%{qt5_bindir}/qmake
%if "%{qt5_libdir}" == "/usr/lib64"
%{qt5_bindir}/qt.conf
%endif
%{qt5_archdatadir}/mkspecs/aix-*/
%{qt5_archdatadir}/mkspecs/android-clang/*
%{qt5_archdatadir}/mkspecs/blackberry*/
%{qt5_archdatadir}/mkspecs/common/
%{qt5_archdatadir}/mkspecs/cygwin-*/
%{qt5_archdatadir}/mkspecs/darwin-*/
%{qt5_archdatadir}/mkspecs/features/
%{qt5_archdatadir}/mkspecs/freebsd-*/
%{qt5_archdatadir}/mkspecs/haiku-g++/
%{qt5_archdatadir}/mkspecs/hpux-*
%{qt5_archdatadir}/mkspecs/hpuxi-*
%{qt5_archdatadir}/mkspecs/hurd-g++/
%{qt5_archdatadir}/mkspecs/irix-*/
%{qt5_archdatadir}/mkspecs/linux-*/
%{qt5_archdatadir}/mkspecs/lynxos-*/
%{qt5_archdatadir}/mkspecs/macx-*/
%{qt5_archdatadir}/mkspecs/netbsd-*/
%{qt5_archdatadir}/mkspecs/openbsd-*/
%{qt5_archdatadir}/mkspecs/qconfig.pri
%{qt5_archdatadir}/mkspecs/qmodule.pri
%{qt5_archdatadir}/mkspecs/qnx*/
%{qt5_archdatadir}/mkspecs/sco-*/
%{qt5_archdatadir}/mkspecs/solaris-*/
%{qt5_archdatadir}/mkspecs/tru64-*/
%{qt5_archdatadir}/mkspecs/unixware-*/
%{qt5_archdatadir}/mkspecs/unsupported/
%{qt5_archdatadir}/mkspecs/win32-g++/
%{qt5_archdatadir}/mkspecs/win32-icc/
%{qt5_archdatadir}/mkspecs/win32-msvc20*/
%{qt5_archdatadir}/mkspecs/wince*/
%{qt5_archdatadir}/mkspecs/winphone*/
%{qt5_archdatadir}/mkspecs/winrt*/
%{qt5_archdatadir}/mkspecs/devices/
%{qt5_archdatadir}/mkspecs/qdevice.pri
%{qt5_archdatadir}/mkspecs/qfeatures.pri
%config %{_sysconfdir}/rpm/macros.qt5-default

%files qtdbus
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5DBus.so.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{qt5_bindir}/qdbuscpp2xml
%{qt5_bindir}/qdbusxml2cpp
%{qt5_includedir}/QtDBus/
%{qt5_libdir}/libQt5DBus.so
%{qt5_libdir}/libQt5DBus.prl
%{qt5_libdir}/pkgconfig/Qt5DBus.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_dbus.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_dbus_private.pri
%{qt5_libdir}/cmake/Qt5DBus


%files qtgui
%defattr(-,root,root,-)
%dir %{qt5_plugindir}/imageformats/
%dir %{qt5_plugindir}/platforminputcontexts/
%{qt5_libdir}/libQt5Gui.so.*


%files qtgui-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtGui/
%{qt5_includedir}/QtPlatformHeaders/
%{qt5_libdir}/libQt5Gui.prl
%{qt5_libdir}/libQt5Gui.so
%{qt5_libdir}/pkgconfig/Qt5Gui.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_gui.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_gui_private.pri
%{qt5_libdir}/cmake/Qt5Gui


%files qtnetwork
%defattr(-,root,root,-)
%dir %{qt5_plugindir}/bearer/
%{qt5_libdir}/libQt5Network.so.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtNetwork/
%{qt5_libdir}/libQt5Network.prl
%{qt5_libdir}/libQt5Network.so
%{qt5_libdir}/pkgconfig/Qt5Network.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_network.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_network_private.pri
%{qt5_libdir}/cmake/Qt5Network


%files qtopengl
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5OpenGL.so.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtOpenGL/
%{qt5_includedir}/QtOpenGLExtensions/
%{qt5_libdir}/libQt5OpenGL.prl
%{qt5_libdir}/libQt5OpenGLExtensions.prl
%{qt5_libdir}/libQt5OpenGL.so
%{qt5_libdir}/libQt5OpenGLExtensions.a
%{qt5_libdir}/pkgconfig/Qt5OpenGL.pc
%{qt5_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_opengl.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_opengl_private.pri
%{qt5_archdatadir}/mkspecs/android-g++/qmake.conf
%{qt5_archdatadir}/mkspecs/android-g++/qplatformdefs.h
%{qt5_archdatadir}/mkspecs/modules/qt_lib_openglextensions.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_openglextensions_private.pri
%{qt5_libdir}/cmake/Qt5OpenGL
%{qt5_libdir}/cmake/Qt5OpenGLExtensions


%files qtsql
%defattr(-,root,root,-)
%dir %{qt5_plugindir}/sqldrivers/
%{qt5_libdir}/libQt5Sql.so.*


%files qtsql-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtSql/
%{qt5_libdir}/libQt5Sql.prl
%{qt5_libdir}/libQt5Sql.so
%{qt5_libdir}/pkgconfig/Qt5Sql.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_sql.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_sql_private.pri
%{qt5_libdir}/cmake/Qt5Sql


%files qttest
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5Test.so.*

%files qttest-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtTest/
%{qt5_libdir}/libQt5Test.prl
%{qt5_libdir}/libQt5Test.so
%{qt5_libdir}/pkgconfig/Qt5Test.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_testlib.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_testlib_private.pri
%{qt5_libdir}/cmake/Qt5Test

%files qtxml
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5Xml.so.*

%files qtxml-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtXml/
%{qt5_libdir}/libQt5Xml.prl
%{qt5_libdir}/libQt5Xml.so
%{qt5_libdir}/pkgconfig/Qt5Xml.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_xml.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_xml_private.pri
%{qt5_libdir}/cmake/Qt5Xml

%files qtwidgets
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5Widgets.so.*

%files qtwidgets-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtWidgets/
%{qt5_libdir}/libQt5Widgets.prl
%{qt5_libdir}/libQt5Widgets.so
%{qt5_libdir}/pkgconfig/Qt5Widgets.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_widgets.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_widgets_private.pri
%{qt5_libdir}/cmake/Qt5Widgets

%files qtplatformsupport-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtPlatformSupport/
%{qt5_libdir}/libQt5PlatformSupport.prl
%{qt5_libdir}/libQt5PlatformSupport.a
%{qt5_archdatadir}/mkspecs/modules/qt_lib_platformsupport_private.pri

%files qtbootstrap-devel
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5Bootstrap.prl
%{qt5_libdir}/libQt5Bootstrap.a
%{qt5_archdatadir}/mkspecs/modules/qt_lib_bootstrap_private.pri

%files qtprintsupport
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5PrintSupport.so.*

%files qtprintsupport-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtPrintSupport/
%{qt5_libdir}/libQt5PrintSupport.prl
%{qt5_libdir}/libQt5PrintSupport.so
%{qt5_libdir}/pkgconfig/Qt5PrintSupport.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_printsupport.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_printsupport_private.pri
%{qt5_libdir}/cmake/Qt5PrintSupport

%files qtconcurrent
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5Concurrent.so.*

%files qtconcurrent-devel
%defattr(-,root,root,-)
%{qt5_includedir}/QtConcurrent/
%{qt5_libdir}/libQt5Concurrent.prl
%{qt5_libdir}/libQt5Concurrent.so
%{qt5_libdir}/pkgconfig/Qt5Concurrent.pc
%{qt5_archdatadir}/mkspecs/modules/qt_lib_concurrent.pri
%{qt5_archdatadir}/mkspecs/modules/qt_lib_concurrent_private.pri
%{qt5_libdir}/cmake/Qt5Concurrent




%files plugin-bearer-connman
%defattr(-,root,root,-)
%{qt5_plugindir}/bearer/libqconnmanbearer.so

%files plugin-bearer-generic
%defattr(-,root,root,-)
%{qt5_plugindir}/bearer/libqgenericbearer.so

%files plugin-bearer-nm
%defattr(-,root,root,-)
%{qt5_plugindir}/bearer/libqnmbearer.so

%files plugin-imageformat-gif
%defattr(-,root,root,-)
%{qt5_plugindir}/imageformats/libqgif.so

%files plugin-imageformat-ico
%defattr(-,root,root,-)
%{qt5_plugindir}/imageformats/libqico.so

%files plugin-imageformat-jpeg
%defattr(-,root,root,-)
%{qt5_plugindir}/imageformats/libqjpeg.so

%files plugin-platform-minimal
%defattr(-,root,root,-)
%{qt5_plugindir}/platforms/libqminimal.so

%files plugin-platform-offscreen
%defattr(-,root,root,-)
%{qt5_plugindir}/platforms/libqoffscreen.so

%files plugin-platform-eglfs
%defattr(-,root,root,-)
%{qt5_libdir}/libQt5EglDeviceIntegration.so*
%{qt5_libdir}/libQt5EglDeviceIntegration.prl
%{qt5_plugindir}/platforms/libqeglfs.so
%if %{with X11}
%{qt5_plugindir}/egldeviceintegrations/libqeglfs-x11-integration.so
%endif
%{qt5_plugindir}/egldeviceintegrations/libqeglfs-kms-integration.so
%{qt5_plugindir}/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so
%{qt5_archdatadir}/mkspecs/modules/qt_lib_eglfs_device_lib_private.pri

%files plugin-platform-minimalegl
%defattr(-,root,root,-)
%{qt5_plugindir}/platforms/libqminimalegl.so

%files plugin-platform-linuxfb
%defattr(-,root,root,-)
%{qt5_plugindir}/platforms/libqlinuxfb.so

%files plugin-printsupport-cups
%defattr(-,root,root,-)
%{qt5_plugindir}/printsupport/libcupsprintersupport.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{qt5_plugindir}/sqldrivers/libqsqlite.so

%files plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{qt5_plugindir}/platforminputcontexts/libibusplatforminputcontextplugin.so

%files plugin-generic-evdev
%defattr(-,root,root,-)
%{qt5_plugindir}/generic/libqevdev*plugin.so

%files plugin-generic-tuiotouch
%defattr(-,root,root,-)
%{qt5_plugindir}/generic/libqtuiotouchplugin.so

%files -n qt5-default
%defattr(-,root,root,-)
%{qt5_sysconfdir}/qtchooser/default.conf

#### No changelog section, separate $pkg.changes contains the history
