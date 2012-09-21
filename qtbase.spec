%define _qtmodule_snapshot_version 5.0.0-beta1
%ifarch armv7l armv7el armv7hl amv7nhl armv7thl armv7tnhl
%define arch_arg armv6
%endif
%ifarch i586
%define arch_arg i386
%endif

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
Version:    5.0.0~beta1
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
#Source0:    %{name}-qtbase-%{version}.tar.xz
Source0:    qtbase-opensource-src-%{_qtmodule_snapshot_version}.tar.xz
Source1:    macros.qmake
Source100:  qtbase-rpmlintrc
Patch1:     0001-Always-use-QPA-for-systrayicon.patch
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
# Package not available but installed in OBS?
#BuildRequires:  gcc-g++
BuildRequires:  libjpeg-devel
#BuildRequires:  libtiff-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  sharutils
#BuildRequires:  gdb
BuildRequires:  python

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.


%package tools
Summary:    Development tools for qtbase
Group:      Qt/Qt

%description tools
This package contains useful tools for Qt development

%package qtcore
Summary:    The QtCore library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtcore
This package contains the QtCore library

%package qtcore-devel
Summary:    Development files for QtCore
Group:      Qt/Qt
Requires:   %{name}-qmake
Requires:   %{name}-tools
Requires:   %{name}-qtcore = %{version}-%{release}
Requires:   fontconfig-devel

%description qtcore-devel
This package contains the files necessary to develop applications
that use the QtCore


%package qmake
Summary:    QMake
Group:      Qt/Qt
Conflicts:  qt-qmake
#Requires:   gdb

%description qmake
This package contains qmake


%package plugin-bearer-connman
Summary:    Connman bearer plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-connman
This package contains the connman bearer plugin


%package plugin-bearer-generic
Summary:    Connman generic plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-generic
This package contains the connman generic bearer plugin


%package plugin-bearer-nm
Summary:    Connman generic plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-nm
This package contains the connman NetworkManager bearer plugin


%package plugin-imageformat-gif
Summary:    Gif image format plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-gif
This package contains the gif imageformat plugin


%package plugin-imageformat-ico
Summary:    Ico image format plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-ico
This package contains the ico imageformat plugin


%package plugin-imageformat-jpeg
Summary:    JPEG image format plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-jpeg
This package contains the JPEG imageformat plugin


#%package plugin-imageformat-tiff
#Summary:    TIFF image format plugin
#Group:      Qt/Qt
#
#%description plugin-imageformat-tiff
#This package contains the TIFF imageformat plugin


%package plugin-platform-minimal
Summary:    Minimal platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimal
This package contains the minimal platform plugin


%package plugin-platform-inputcontext-maliit
Summary:    MALIIT input context platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-inputcontext-maliit
This package contains MALIIT platform inputcontext plugin


#%package plugin-platform-wayland
#Summary:    Wayland platform plugin
#Group:      Qt/Qt
#
#%description plugin-platform-wayland
#This package contains the wayland platform plugin


%package plugin-platform-eglfs
Summary:    Eglfs platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-eglfs
This package contains the eglfs platform plugin

%package plugin-platform-minimalegl
Summary:    Minimalegl platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimalegl
This package contains the minimalegl platform plugin

%package plugin-platform-xcb
Summary:    XCB platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-xcb
This package contains the XCB platform plugin

%package plugin-platform-linuxfb
Summary:    Linux framebuffer platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-linuxfb
This package contains the linuxfb platform plugin for Qt

%package plugin-printsupport-cups
Summary:    CUPS print support plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-printsupport-cups
This package contains the CUPS print support plugin


# %package plugin-platform-xlib
# Summary:    Xlib platform plugin
# Group:      Qt/Qt
# 
# %description plugin-platform-xlib
# This package contains the Xlib platform plugin



%package plugin-sqldriver-sqlite
Summary:    Sqlite sql driver plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-sqldriver-sqlite
This package contains the sqlite sql driver plugin


%package plugin-platforminputcontext-ibus
Summary:    ibus platform import context plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platforminputcontext-ibus
This package contains the ibus platform input context plugin

%package plugin-generic-evdev
Summary:    evdev generic plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-generic-evdev
This package contains evdev plugins




%package qtdbus
Summary:    The QtDBus library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtdbus
This package contains the QtDBus library


%package qtdbus-devel
Summary:    Development files for QtDBus
Group:      Qt/Qt
Requires:   %{name}-qtdbus = %{version}-%{release}
Requires:   pkgconfig(dbus-1)

%description qtdbus-devel
This package contains the files necessary to develop
applications that use QtDBus


%package qtgui
Summary:    The QtGui Library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtgui
This package contains the QtGui library


%package qtgui-devel
Summary:    Development files for QtGui
Group:      Qt/Qt
Requires:   %{name}-qtgui = %{version}-%{release}
Requires:   %{name}-qtopengl-devel

%description qtgui-devel
This package contains the files necessary to develop
applications that use QtGui


%package qtnetwork
Summary:    The QtNetwork library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtnetwork
This package contains the QtNetwork library


%package qtnetwork-devel
Summary:    Development files for QtNetwork
Group:      Qt/Qt
Requires:   %{name}-qtnetwork = %{version}-%{release}

%description qtnetwork-devel
This package contains the files necessary to develop
applications that use QtNetwork



%package qtopengl
Summary:    The QtOpenGL library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtopengl
This package contains the QtOpenGL library


%package qtopengl-devel
Summary:    Development files for QtOpenGL
Group:      Qt/Qt
Requires:   %{name}-qtopengl = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description qtopengl-devel
This package contains the files necessary to develop
applications that use QtOpenGL


%package qtsql
Summary:    The QtSql library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtsql
This package contains the QtSql library


%package qtsql-devel
Summary:    Development files for QtSql
Group:      Qt/Qt
Requires:   %{name}-qtsql = %{version}-%{release}

%description qtsql-devel
This package contains the files necessary to develop
applications that use QtSql


%package qttest
Summary:    The QtTest library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qttest
This package contains the QtTest library


%package qttest-devel
Summary:    Development files for QtTest
Group:      Qt/Qt
Requires:   %{name}-qttest = %{version}-%{release}

%description qttest-devel
This package contains the files necessary to develop
applications that use QtTest


%package qtxml
Summary:    The QtXml library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtxml
This package contains the QtXml library

%package qtxml-devel
Summary:    Development files for QtXml
Group:      Qt/Qt
Requires:   %{name}-qtxml = %{version}-%{release}

%description qtxml-devel
This package contains the files necessary to develop
applications that use QtXml


%package qtwidgets
Summary:    The QtWidgets library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtwidgets
This package contains the QtWidgets library

%package qtwidgets-devel
Summary:    Development files for QtWidgets
Group:      Qt/Qt
Requires:   %{name}-qtwidgets = %{version}-%{release}

%description qtwidgets-devel
This package contains the files necessary to develop
applications that use QtWidgets

%package qtplatformsupport-devel
Summary:    The QtWidgets library
Group:      Qt/Qt

%description qtplatformsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport

%package qtprintsupport
Summary:    The QtPrintSupport
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtprintsupport
This package contains the QtPrintSupport library

%package qtprintsupport-devel
Summary:    Development files for QtPrintSupport
Group:      Qt/Qt
Requires:   %{name}-qtprintsupport = %{version}-%{release}

%description qtprintsupport-devel
This package contains the files necessary to develop
applications that use QtPrintSupport

%package qtconcurrent
Summary:    QtConcurrent library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtconcurrent
This package contains the QtConcurrent library

%package qtconcurrent-devel
Summary:    Development files for QtConcurrent
Group:      Qt/Qt
Requires:   %{name}-qtconcurrent = %{version}-%{release}

%description qtconcurrent-devel
This package contains the files necessary to develop
applications that use QtConcurrent


##### Build section

%prep
%setup -q -n  qtbase-opensource-src-%{_qtmodule_snapshot_version}
%patch1 -p1


%build
./configure --disable-static \
    -confirm-license \
    -developer-build \
    -platform linux-g++ \
    -prefix "%{_prefix}" \
    -bindir "%{_bindir}" \
    -libdir "%{_libdir}" \
    -docdir "%{_docdir}" \
    -headerdir "%{_includedir}/qt5" \
    -datadir "%{_datadir}/qt5" \
    -plugindir "%{_libdir}/qt5/plugins" \
    -importdir "%{_libdir}/qt5/imports" \
    -translationdir "%{_datadir}/qt5/translations" \
    -sysconfdir "%{_sysconfdir}/xdg" \
    -examplesdir "%{_libdir}/qt5/examples" \
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
    -no-rpath \
    -optimized-qmake \
    -dbus-linked \
    -no-separate-debug-info \
    -verbose \
    -no-gtkstyle \
    -opengl es2 \
    -arch %{arch_arg} \
    -no-openvg \
    -lfontconfig \
    -I/usr/include/freetype2 \
    -no-neon \
    -nomake tests \
    -nomake examples \
    -nomake demos \
    -xcb
#
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
#
# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
#
# Install qmake rpm macros
install -D -p -m 0644 %{_sourcedir}/macros.qmake \
%{buildroot}/%{_sysconfdir}/rpm/macros.qmake
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

#### File section

# There is no naked qt5 package
#%files



%files tools
%defattr(-,root,root,-)
%{_bindir}/moc
%{_bindir}/rcc
%{_bindir}/syncqt
%{_bindir}/uic
%{_bindir}/qdoc

%files qtcore
%defattr(-,root,root,-)
%{_libdir}/libQtCore.so.*

%files qtcore-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtCore/
%{_libdir}/libQtCore.prl
%{_libdir}/libQtCore.so
%{_libdir}/pkgconfig/QtCore.pc
%{_datadir}/qt5/mkspecs/modules/qt_core.pri
%{_libdir}/cmake/
%{_datadir}/qt5/mkspecs/cmake/

%files qmake
%defattr(-,root,root,-)
%{_bindir}/qmake
%{_datadir}/qt5/mkspecs/aix-*/
%{_datadir}/qt5/mkspecs/common/
%{_datadir}/qt5/mkspecs/cygwin-*/
%{_datadir}/qt5/mkspecs/darwin-*/
%{_datadir}/qt5/mkspecs/default
%{_datadir}/qt5/mkspecs/features/
%{_datadir}/qt5/mkspecs/freebsd-*/
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
%{_datadir}/qt5/mkspecs/sco-*/
%{_datadir}/qt5/mkspecs/solaris-*/
%{_datadir}/qt5/mkspecs/tru64-*/
%{_datadir}/qt5/mkspecs/unixware-*/
%{_datadir}/qt5/mkspecs/unsupported/
%{_datadir}/qt5/mkspecs/win32-g++/
%{_datadir}/qt5/mkspecs/win32-icc/
%{_datadir}/qt5/mkspecs/win32-msvc20*/
%{_datadir}/qt5/mkspecs/wince*/
%{_datadir}/qt5/mkspecs/devices/
%{_datadir}/qt5/mkspecs/qdevice.pri
%{_datadir}/qt5/mkspecs/default-host
%{_sysconfdir}/rpm/macros.qmake

%files qtdbus
%defattr(-,root,root,-)
%{_libdir}/libQtDBus.so.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{_bindir}/qdbuscpp2xml
%{_bindir}/qdbusxml2cpp
%{_includedir}/qt5/QtDBus/
%{_libdir}/libQtDBus.so
%{_libdir}/libQtDBus.prl
%{_libdir}/pkgconfig/QtDBus.pc
%{_datadir}/qt5/mkspecs/modules/qt_dbus.pri


%files qtgui
%defattr(-,root,root,-)
%{_libdir}/libQtGui.so.*


%files qtgui-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtGui/
%{_libdir}/libQtGui.prl
%{_libdir}/libQtGui.so
%{_libdir}/pkgconfig/QtGui.pc
%{_datadir}/qt5/mkspecs/modules/qt_gui.pri


%files qtnetwork
%defattr(-,root,root,-)
%{_libdir}/libQtNetwork.so.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtNetwork/
%{_libdir}/libQtNetwork.prl
%{_libdir}/libQtNetwork.so
%{_libdir}/pkgconfig/QtNetwork.pc
%{_datadir}/qt5/mkspecs/modules/qt_network.pri


%files qtopengl
%defattr(-,root,root,-)
%{_libdir}/libQtOpenGL.so.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtOpenGL/
%{_libdir}/libQtOpenGL.prl
%{_libdir}/libQtOpenGL.so
%{_libdir}/pkgconfig/QtOpenGL.pc
%{_datadir}/qt5/mkspecs/modules/qt_opengl.pri


%files qtsql
%defattr(-,root,root,-)
%{_libdir}/libQtSql.so.*


%files qtsql-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtSql/
%{_libdir}/libQtSql.prl
%{_libdir}/libQtSql.so
%{_libdir}/pkgconfig/QtSql.pc
%{_datadir}/qt5/mkspecs/modules/qt_sql.pri


%files qttest
%defattr(-,root,root,-)
%{_libdir}/libQtTest.so.*

%files qttest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtTest/
%{_libdir}/libQtTest.prl
%{_libdir}/libQtTest.so
%{_libdir}/pkgconfig/QtTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_testlib.pri

%files qtxml
%defattr(-,root,root,-)
%{_libdir}/libQtXml.so.*

%files qtxml-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtXml/
%{_libdir}/libQtXml.prl
%{_libdir}/libQtXml.so
%{_libdir}/pkgconfig/QtXml.pc
%{_datadir}/qt5/mkspecs/modules/qt_xml.pri

%files qtwidgets
%defattr(-,root,root,-)
%{_libdir}/libQtWidgets.so.*

%files qtwidgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtWidgets/
%{_libdir}/libQtWidgets.prl
%{_libdir}/libQtWidgets.so
%{_libdir}/pkgconfig/QtWidgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_widgets.pri

%files qtplatformsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPlatformSupport/
%{_libdir}/libQtPlatformSupport.prl
%{_libdir}/libQtPlatformSupport.a
%{_libdir}/pkgconfig/QtPlatformSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_platformsupport.pri

%files qtprintsupport
%defattr(-,root,root,-)
%{_libdir}/libQtPrintSupport.so.*

%files qtprintsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPrintSupport/
%{_libdir}/libQtPrintSupport.prl
%{_libdir}/libQtPrintSupport.so
%{_libdir}/pkgconfig/QtPrintSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_printsupport.pri

%files qtconcurrent
%defattr(-,root,root,-)
%{_libdir}/libQtConcurrent.so.*

%files qtconcurrent-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtConcurrent/
%{_libdir}/libQtConcurrent.prl
%{_libdir}/libQtConcurrent.so
%{_libdir}/pkgconfig/QtConcurrent.pc
%{_datadir}/qt5/mkspecs/modules/qt_concurrent.pri




# Plugin packages

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

#%files plugin-imageformat-tiff
#%defattr(-,root,root,-)
#%{_libdir}/qt5/plugins/imageformats/libqtiff.so

%files plugin-platform-minimal
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimal.so

%files plugin-platform-inputcontext-maliit
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so

%files plugin-platform-eglfs
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqeglfs.so

%files plugin-platform-minimalegl
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimalegl.so

%files plugin-platform-xcb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libxcb.so

%files plugin-platform-linuxfb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqlinuxfb.so

%files plugin-printsupport-cups
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/printsupport/libcupsprintersupport.so

# %files plugin-platform-xlib
# %defattr(-,root,root,-)
# %{_libdir}/qt5/plugins/platforms/libqxlib.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%files plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so

%files plugin-generic-evdev
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/generic/libqevdev*plugin.so



#### No changelog section, separate $pkg.changes contains the history
