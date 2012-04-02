%define _qtmodule_snapshot_version 5~git5706.g2e7b4bf
%ifarch armv7l armv7el armv7hl amv7nhl armv7thl armv7tnhl
%define arch_arg armv6
%endif
%ifarch i586
%define arch_arg i386
%endif


# Version is the date of latest commit in qtbase, followed by 'g' + few
# characters of the last git commit ID.
# NOTE: tarball's prefix is 'qt5-base' until version number starts to
# make sense. This allows to update spec contents easily as snapshots
# evolve.

Name:       qt5
Summary:    Cross-platform application and UI framework
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-qtbase-%{version}.tar.gz
Source1:    macros.qmake
Source100:  qtbase-rpmlintrc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
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
This packagea contains the QtCore library

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
#Requires:   gdb

%description qmake
This package contains qmake


%package plugin-accessible-libqtaccessiblewidgets
Summary:    Accessible widgets
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-accessible-libqtaccessiblewidgets
This package contains libqtaccessiblewidgets


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


%package plugin-platform-xcb
Summary:    XCB platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-xcb
This package contains the XCB platform plugin


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
%setup -q -n %{name}-qtbase


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
    -no-phonon-backend \
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
%{_bindir}/qtmodule-configtests
%{_bindir}/uic
%{_bindir}/qdoc

%files qtcore
%defattr(-,root,root,-)
%{_libdir}/libQtCore.so.*

%files qtcore-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtCore
%{_includedir}/qt5/Qt/qabstractanimation.h
%{_includedir}/qt5/Qt/qabstracteventdispatcher.h
%{_includedir}/qt5/Qt/qabstractitemmodel.h
%{_includedir}/qt5/Qt/qabstractstate.h
%{_includedir}/qt5/Qt/qabstracttransition.h
%{_includedir}/qt5/Qt/qalgorithms.h
%{_includedir}/qt5/Qt/qanimationgroup.h
%{_includedir}/qt5/Qt/qoldbasicatomic.h
%{_includedir}/qt5/Qt/qgenericatomic.h
%{_includedir}/qt5/Qt/qatomic.h
%{_includedir}/qt5/Qt/qatomic_*.h
%{_includedir}/qt5/Qt/qbasic*.h
%{_includedir}/qt5/Qt/qbitarray.h
%{_includedir}/qt5/Qt/qbuffer.h
%{_includedir}/qt5/Qt/qbytearray.h
%{_includedir}/qt5/Qt/qbytearraymatcher.h
%{_includedir}/qt5/Qt/qcache.h
%{_includedir}/qt5/Qt/qchar.h
%{_includedir}/qt5/Qt/qconfig-*.h
%{_includedir}/qt5/Qt/qconfig.h
%{_includedir}/qt5/Qt/qcompilerdetection.h
%{_includedir}/qt5/Qt/qprocessordetection.h
%{_includedir}/qt5/Qt/qsystemdetection.h
%{_includedir}/qt5/Qt/qcontainerfwd.h
%{_includedir}/qt5/Qt/qcontiguouscache.h
%{_includedir}/qt5/Qt/qcoreapplication.h
%{_includedir}/qt5/Qt/qcoreevent.h
%{_includedir}/qt5/Qt/qcryptographichash.h
%{_includedir}/qt5/Qt/qdatastream.h
%{_includedir}/qt5/Qt/qdatetime.h
%{_includedir}/qt5/Qt/qdebug.h
%{_includedir}/qt5/Qt/qdir.h
%{_includedir}/qt5/Qt/qdiriterator.h
%{_includedir}/qt5/Qt/qdnslookup.h
%{_includedir}/qt5/Qt/qtemporarydir.h
%{_includedir}/qt5/Qt/qeasingcurve.h
%{_includedir}/qt5/Qt/qelapsedtimer.h
%{_includedir}/qt5/Qt/qendian.h
%{_includedir}/qt5/Qt/qeventloop.h
%{_includedir}/qt5/Qt/qeventtransition.h
%{_includedir}/qt5/Qt/qfactoryinterface.h
%{_includedir}/qt5/Qt/qfeatures.h
%{_includedir}/qt5/Qt/qfile.h
%{_includedir}/qt5/Qt/qfileinfo.h
%{_includedir}/qt5/Qt/qfilesystemwatcher.h
%{_includedir}/qt5/Qt/qfinalstate.h
%{_includedir}/qt5/Qt/qfunctions_*.h
%{_includedir}/qt5/Qt/qfuture*.h
%{_includedir}/qt5/Qt/qglobal.h
%{_includedir}/qt5/Qt/qhash.h
%{_includedir}/qt5/Qt/qhistorystate.h
%{_includedir}/qt5/Qt/qtouchdevice.h
%{_includedir}/qt5/Qt/qiodevice.h
%{_includedir}/qt5/Qt/qiterator.h
%{_includedir}/qt5/Qt/qjsonarray.h
%{_includedir}/qt5/Qt/qjsondocument.h
%{_includedir}/qt5/Qt/qjsonobject.h
%{_includedir}/qt5/Qt/qjsonvalue.h
%{_includedir}/qt5/Qt/qlibrary.h
%{_includedir}/qt5/Qt/qlibraryinfo.h
%{_includedir}/qt5/Qt/qline.h
%{_includedir}/qt5/Qt/qlinkedlist.h
%{_includedir}/qt5/Qt/qlist.h
%{_includedir}/qt5/Qt/qlocale.h
%{_includedir}/qt5/Qt/qlogging.h
%{_includedir}/qt5/Qt/qmap.h
%{_includedir}/qt5/Qt/qmargins.h
%{_includedir}/qt5/Qt/qmath.h
%{_includedir}/qt5/Qt/qmetaobject.h
%{_includedir}/qt5/Qt/qmetatype.h
%{_includedir}/qt5/Qt/qmimedata.h
%{_includedir}/qt5/Qt/qmimedatabase.h
%{_includedir}/qt5/Qt/qmimetype.h
%{_includedir}/qt5/Qt/qmutex.h
%{_includedir}/qt5/Qt/qnamespace.h
%{_includedir}/qt5/Qt/qnumeric.h
%{_includedir}/qt5/Qt/qobject.h
%{_includedir}/qt5/Qt/qobject_impl.h
%{_includedir}/qt5/Qt/qobjectcleanuphandler.h
%{_includedir}/qt5/Qt/qobjectdefs.h
%{_includedir}/qt5/Qt/qpair.h
%{_includedir}/qt5/Qt/qparallelanimationgroup.h
%{_includedir}/qt5/Qt/qpauseanimation.h
%{_includedir}/qt5/Qt/qplugin.h
%{_includedir}/qt5/Qt/qpluginloader.h
%{_includedir}/qt5/Qt/qpoint.h
%{_includedir}/qt5/Qt/qpointer.h
%{_includedir}/qt5/Qt/qprocess.h
%{_includedir}/qt5/Qt/qpropertyanimation.h
%{_includedir}/qt5/Qt/qqueue.h
%{_includedir}/qt5/Qt/qreadwritelock.h
%{_includedir}/qt5/Qt/qrect.h
%{_includedir}/qt5/Qt/qrefcount.h
%{_includedir}/qt5/Qt/qregexp.h
%{_includedir}/qt5/Qt/qresource.h
%{_includedir}/qt5/Qt/qrunnable.h
%{_includedir}/qt5/Qt/qscopedpointer.h
%{_includedir}/qt5/Qt/qscopedvaluerollback.h
%{_includedir}/qt5/Qt/qsemaphore.h
%{_includedir}/qt5/Qt/qsequentialanimationgroup.h
%{_includedir}/qt5/Qt/qset.h
%{_includedir}/qt5/Qt/qsettings.h
%{_includedir}/qt5/Qt/qshareddata.h
%{_includedir}/qt5/Qt/qsharedmemory.h
%{_includedir}/qt5/Qt/qsharedpointer*.h
%{_includedir}/qt5/Qt/qsignalmapper.h
%{_includedir}/qt5/Qt/qsignaltransition.h
%{_includedir}/qt5/Qt/qsize.h
%{_includedir}/qt5/Qt/qsocketnotifier.h
%{_includedir}/qt5/Qt/qstandardpaths.h
%{_includedir}/qt5/Qt/qstack.h
%{_includedir}/qt5/Qt/qstate.h
%{_includedir}/qt5/Qt/qstatemachine.h
%{_includedir}/qt5/Qt/qstring.h
%{_includedir}/qt5/Qt/qstringbuilder.h
%{_includedir}/qt5/Qt/qstringlist.h
%{_includedir}/qt5/Qt/qstringmatcher.h
%{_includedir}/qt5/Qt/qsystemsemaphore.h
%{_includedir}/qt5/Qt/qsysinfo.h
%{_includedir}/qt5/Qt/qt_windows.h
%{_includedir}/qt5/Qt/qtconcurrent*.h
%{_includedir}/qt5/Qt/qtcoreversion.h
%{_includedir}/qt5/Qt/qtemporaryfile.h
%{_includedir}/qt5/Qt/qtextboundaryfinder.h
%{_includedir}/qt5/Qt/qtextcodec.h
%{_includedir}/qt5/Qt/qtextstream.h
%{_includedir}/qt5/Qt/qthread.h
%{_includedir}/qt5/Qt/qthreadpool.h
%{_includedir}/qt5/Qt/qthreadstorage.h
%{_includedir}/qt5/Qt/qtimeline.h
%{_includedir}/qt5/Qt/qtimer.h
%{_includedir}/qt5/Qt/qtranslator.h
%{_includedir}/qt5/Qt/qtypeinfo.h
%{_includedir}/qt5/Qt/qurl.h
%{_includedir}/qt5/Qt/quuid.h
%{_includedir}/qt5/Qt/qvariant.h
%{_includedir}/qt5/Qt/qvariantanimation.h
%{_includedir}/qt5/Qt/qvarlengtharray.h
%{_includedir}/qt5/Qt/qvector.h
%{_includedir}/qt5/Qt/qwaitcondition.h
%{_includedir}/qt5/Qt/qwineventnotifier.h
%{_includedir}/qt5/Qt/qxmlstream.h
%{_includedir}/qt5/Qt/qisenum.h
%{_includedir}/qt5/Qt/qregularexpression.h
%{_includedir}/qt5/Qt/qtypetraits.h
%{_includedir}/qt5/Qt/qt_mips_asm_dsp.h
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
%{_sysconfdir}/rpm/macros.qmake

%files qtdbus
%defattr(-,root,root,-)
%{_libdir}/libQtDBus.so.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtDBus
%{_includedir}/qt5/QtDBus/
%{_includedir}/qt5/Qt/qdbus*.h
%{_includedir}/qt5/Qt/qtdbusversion.h
%{_libdir}/libQtDBus.so
%{_libdir}/libQtDBus.prl
%{_libdir}/pkgconfig/QtDBus.pc
%{_datadir}/qt5/mkspecs/modules/qt_dbus.pri


%files qtgui
%defattr(-,root,root,-)
%{_libdir}/libQtGui.so.*


%files qtgui-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtGui
%{_includedir}/qt5/QtGui/
%{_includedir}/qt5/Qt/qabstractpagesetupdialog.h
%{_includedir}/qt5/Qt/qabstractprintdialog.h
%{_includedir}/qt5/Qt/qabstractspinbox.h
%{_includedir}/qt5/Qt/qabstracttextdocumentlayout.h
%{_includedir}/qt5/Qt/qbackingstore.h
%{_includedir}/qt5/Qt/qbitmap.h
%{_includedir}/qt5/Qt/qbrush.h
%{_includedir}/qt5/Qt/qclipboard.h
%{_includedir}/qt5/Qt/qcolor.h
%{_includedir}/qt5/Qt/qcolormap.h
%{_includedir}/qt5/Qt/qcursor.h
%{_includedir}/qt5/Qt/qdesktopservices.h
%{_includedir}/qt5/Qt/qdrag.h
%{_includedir}/qt5/Qt/qevent.h
%{_includedir}/qt5/Qt/qfont.h
%{_includedir}/qt5/Qt/qfontdatabase.h
%{_includedir}/qt5/Qt/qfontinfo.h
%{_includedir}/qt5/Qt/qfontmetrics.h
%{_includedir}/qt5/Qt/qformlayout.h
%{_includedir}/qt5/Qt/qgenericmatrix.h
%{_includedir}/qt5/Qt/qgenericplugin*.h
%{_includedir}/qt5/Qt/qglyphrun.h
%{_includedir}/qt5/Qt/qguiapplication.h
%{_includedir}/qt5/Qt/qinputmethod.h
%{_includedir}/qt5/Qt/qinputpanel.h
%{_includedir}/qt5/Qt/qimage*.h
%{_includedir}/qt5/Qt/qkeysequence.h
%{_includedir}/qt5/Qt/qmac*_mac.h
%{_includedir}/qt5/Qt/qmatrix.h
%{_includedir}/qt5/Qt/qmatrix4x4.h
%{_includedir}/qt5/Qt/qmotifstyle.h
%{_includedir}/qt5/Qt/qmouse*.h
%{_includedir}/qt5/Qt/qmovie.h
%{_includedir}/qt5/Qt/qpagesetupdialog.h
%{_includedir}/qt5/Qt/qpagedpaintdevice.h
%{_includedir}/qt5/Qt/qpaint*.h
%{_includedir}/qt5/Qt/qpdfwriter*.h
%{_includedir}/qt5/Qt/qpalette.h
%{_includedir}/qt5/Qt/qpen.h
%{_includedir}/qt5/Qt/qpicture.h
%{_includedir}/qt5/Qt/qpictureformatplugin.h
%{_includedir}/qt5/Qt/qpixmap.h
%{_includedir}/qt5/Qt/qpixmapcache.h
%{_includedir}/qt5/Qt/qplaintextedit.h
%{_includedir}/qt5/Qt/qplastiquestyle.h
%{_includedir}/qt5/Qt/qplatform*_qpa.h
%{_includedir}/qt5/Qt/qpolygon.h
%{_includedir}/qt5/Qt/qprint*.h
%{_includedir}/qt5/Qt/qpushbutton.h
%{_includedir}/qt5/Qt/qquaternion.h
%{_includedir}/qt5/Qt/qradiobutton.h
%{_includedir}/qt5/Qt/qrawfont.h
%{_includedir}/qt5/Qt/qregion.h
%{_includedir}/qt5/Qt/qrgb.h
%{_includedir}/qt5/Qt/qrubberband.h
%{_includedir}/qt5/Qt/qscreen*.h
%{_includedir}/qt5/Qt/qsessionmanager.h
%{_includedir}/qt5/Qt/qshortcut.h
%{_includedir}/qt5/Qt/qsizegrip.h
%{_includedir}/qt5/Qt/qsizepolicy.h
%{_includedir}/qt5/Qt/qslider.h
%{_includedir}/qt5/Qt/qspinbox.h
%{_includedir}/qt5/Qt/qsplashscreen.h
%{_includedir}/qt5/Qt/qsplitter.h
%{_includedir}/qt5/Qt/qstackedlayout.h
%{_includedir}/qt5/Qt/qstackedwidget.h
%{_includedir}/qt5/Qt/qstatictext.h
%{_includedir}/qt5/Qt/qstatusbar.h
%{_includedir}/qt5/Qt/qstringlistmodel.h
%{_includedir}/qt5/Qt/qsyntaxhighlighter.h
%{_includedir}/qt5/Qt/qsurface*.h
%{_includedir}/qt5/Qt/qtextcursor.h
%{_includedir}/qt5/Qt/qtextdocument.h
%{_includedir}/qt5/Qt/qtextdocumentfragment.h
%{_includedir}/qt5/Qt/qtextdocumentwriter.h
%{_includedir}/qt5/Qt/qtextformat.h
%{_includedir}/qt5/Qt/qtextlayout.h
%{_includedir}/qt5/Qt/qtextlist.h
%{_includedir}/qt5/Qt/qtextobject.h
%{_includedir}/qt5/Qt/qtextoption.h
%{_includedir}/qt5/Qt/qtexttable.h
%{_includedir}/qt5/Qt/qtguiversion.h
%{_includedir}/qt5/Qt/qtransform.h
%{_includedir}/qt5/Qt/qvalidator.h
%{_includedir}/qt5/Qt/qvector2d.h
%{_includedir}/qt5/Qt/qvector3d.h
%{_includedir}/qt5/Qt/qvector4d.h
%{_includedir}/qt5/Qt/qwindow.h
%{_includedir}/qt5/Qt/qwindowdefs.h
%{_includedir}/qt5/Qt/qwindowdefs_win.h
%{_includedir}/qt5/Qt/qwindowsysteminterface_qpa.h
%{_libdir}/libQtGui.prl
%{_libdir}/libQtGui.so
%{_libdir}/pkgconfig/QtGui.pc
%{_datadir}/qt5/mkspecs/modules/qt_gui.pri


%files qtnetwork
%defattr(-,root,root,-)
%{_libdir}/libQtNetwork.so.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtNetwork
%{_includedir}/qt5/QtNetwork/
%{_includedir}/qt5/Qt/qtnetworkversion.h
%{_includedir}/qt5/Qt/qabstractsocket.h
%{_includedir}/qt5/Qt/qlocalserver.h
%{_includedir}/qt5/Qt/qlocalsocket.h
%{_includedir}/qt5/Qt/qtcpserver.h
%{_includedir}/qt5/Qt/qtcpsocket.h
%{_includedir}/qt5/Qt/qudpsocket.h
%{_includedir}/qt5/Qt/qssl*.h
%{_includedir}/qt5/Qt/qnetworkconfigmanager.h
%{_includedir}/qt5/Qt/qnetworkconfiguration.h
%{_includedir}/qt5/Qt/qnetworksession.h
%{_includedir}/qt5/Qt/qauthenticator.h
%{_includedir}/qt5/Qt/qhostaddress.h
%{_includedir}/qt5/Qt/qhostinfo.h
%{_includedir}/qt5/Qt/qnetworkinterface.h
%{_includedir}/qt5/Qt/qnetworkproxy.h
%{_includedir}/qt5/Qt/qurlinfo.h
%{_includedir}/qt5/Qt/qabstractnetworkcache.h
%{_includedir}/qt5/Qt/qhttpmultipart.h
%{_includedir}/qt5/Qt/qnetworkaccessmanager.h
%{_includedir}/qt5/Qt/qnetworkcookie.h
%{_includedir}/qt5/Qt/qnetworkcookiejar.h
%{_includedir}/qt5/Qt/qnetworkdiskcache.h
%{_includedir}/qt5/Qt/qnetworkreply.h
%{_includedir}/qt5/Qt/qnetworkrequest.h
%{_libdir}/libQtNetwork.prl
%{_libdir}/libQtNetwork.so
%{_libdir}/pkgconfig/QtNetwork.pc
%{_datadir}/qt5/mkspecs/modules/qt_network.pri


%files qtopengl
%defattr(-,root,root,-)
%{_libdir}/libQtOpenGL.so.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtOpenGL
%{_includedir}/qt5/QtOpenGL/
%{_includedir}/qt5/Qt/qgl.h
%{_includedir}/qt5/Qt/qglbuffer.h
%{_includedir}/qt5/Qt/qglcolormap.h
%{_includedir}/qt5/Qt/qglframebufferobject.h
%{_includedir}/qt5/Qt/qglfunctions.h
%{_includedir}/qt5/Qt/qglpixelbuffer.h
%{_includedir}/qt5/Qt/qglshaderprogram.h
%{_includedir}/qt5/Qt/qtopenglversion.h
%{_includedir}/qt5/Qt/qopengl*.h
%{_libdir}/libQtOpenGL.prl
%{_libdir}/libQtOpenGL.so
%{_libdir}/pkgconfig/QtOpenGL.pc
%{_datadir}/qt5/mkspecs/modules/qt_opengl.pri


%files qtsql
%defattr(-,root,root,-)
%{_libdir}/libQtSql.so.*


%files qtsql-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtSql
%{_includedir}/qt5/QtSql/
%{_includedir}/qt5/Qt/qtsqlversion.h
%{_includedir}/qt5/Qt/qsqlquerymodel.h
%{_includedir}/qt5/Qt/qsqlrelationaldelegate.h
%{_includedir}/qt5/Qt/qsqlrelationaltablemodel.h
%{_includedir}/qt5/Qt/qsqltablemodel.h
%{_includedir}/qt5/Qt/qsql.h
%{_includedir}/qt5/Qt/qsqldatabase.h
%{_includedir}/qt5/Qt/qsqldriver.h
%{_includedir}/qt5/Qt/qsqldriverplugin.h
%{_includedir}/qt5/Qt/qsqlerror.h
%{_includedir}/qt5/Qt/qsqlfield.h
%{_includedir}/qt5/Qt/qsqlindex.h
%{_includedir}/qt5/Qt/qsqlquery.h
%{_includedir}/qt5/Qt/qsqlrecord.h
%{_includedir}/qt5/Qt/qsqlresult.h
%{_includedir}/qt5/Qt/qsql_*.h
%{_libdir}/libQtSql.prl
%{_libdir}/libQtSql.so
%{_libdir}/pkgconfig/QtSql.pc
%{_datadir}/qt5/mkspecs/modules/qt_sql.pri


%files qttest
%defattr(-,root,root,-)
%{_libdir}/libQtTest.so.*

%files qttest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtTest
%{_includedir}/qt5/QtTest/
%{_includedir}/qt5/Qt/qttestversion.h
%{_includedir}/qt5/Qt/qbenchmark.h
%{_includedir}/qt5/Qt/qbenchmarkmetric.h
%{_includedir}/qt5/Qt/qsignalspy.h
%{_includedir}/qt5/Qt/qtest*.h
%{_libdir}/libQtTest.prl
%{_libdir}/libQtTest.so
%{_libdir}/pkgconfig/QtTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_testlib.pri

%files qtxml
%defattr(-,root,root,-)
%{_libdir}/libQtXml.so.*

%files qtxml-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtXml
%{_includedir}/qt5/QtXml/
%{_includedir}/qt5/Qt/qtxmlversion.h
%{_includedir}/qt5/Qt/qxmlstream.h
%{_includedir}/qt5/Qt/qxml.h
%{_includedir}/qt5/Qt/qdom.h
%{_libdir}/libQtXml.prl
%{_libdir}/libQtXml.so
%{_libdir}/pkgconfig/QtXml.pc
%{_datadir}/qt5/mkspecs/modules/qt_xml.pri

%files qtwidgets
%defattr(-,root,root,-)
%{_libdir}/libQtWidgets.so.*

%files qtwidgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtWidgets
%{_includedir}/qt5/QtWidgets/
%{_includedir}/qt5/Qt/qaccessible*.h
%{_includedir}/qt5/Qt/qabstractbutton.h
%{_includedir}/qt5/Qt/qabstractitemdelegate.h
%{_includedir}/qt5/Qt/qabstractitemview.h
%{_includedir}/qt5/Qt/qabstractproxymodel.h
%{_includedir}/qt5/Qt/qabstractscrollarea.h
%{_includedir}/qt5/Qt/qabstractslider.h
%{_includedir}/qt5/Qt/qabstractspinbox.h
%{_includedir}/qt5/Qt/qaction.h
%{_includedir}/qt5/Qt/qactiongroup.h
%{_includedir}/qt5/Qt/qapplication.h
%{_includedir}/qt5/Qt/qboxlayout.h
%{_includedir}/qt5/Qt/qbuttongroup.h
%{_includedir}/qt5/Qt/qcalendarwidget.h
%{_includedir}/qt5/Qt/qcdestyle.h
%{_includedir}/qt5/Qt/qcheckbox.h
%{_includedir}/qt5/Qt/qcleanlooksstyle.h
%{_includedir}/qt5/Qt/qcolordialog.h
%{_includedir}/qt5/Qt/qcolormap.h
%{_includedir}/qt5/Qt/qcolumnview.h
%{_includedir}/qt5/Qt/qcombobox.h
%{_includedir}/qt5/Qt/qcommandlinkbutton.h
%{_includedir}/qt5/Qt/qcommonstyle.h
%{_includedir}/qt5/Qt/qcompleter.h
%{_includedir}/qt5/Qt/qdatawidgetmapper.h
%{_includedir}/qt5/Qt/qdatetimeedit.h
%{_includedir}/qt5/Qt/qdesktopwidget.h
%{_includedir}/qt5/Qt/qdial.h
%{_includedir}/qt5/Qt/qdialog.h
%{_includedir}/qt5/Qt/qdialogbuttonbox.h
%{_includedir}/qt5/Qt/qdirmodel.h
%{_includedir}/qt5/Qt/qdockwidget.h
%{_includedir}/qt5/Qt/qdrawutil.h
%{_includedir}/qt5/Qt/qerrormessage.h
%{_includedir}/qt5/Qt/qfiledialog.h
%{_includedir}/qt5/Qt/qfileiconprovider.h
%{_includedir}/qt5/Qt/qfilesystemmodel.h
%{_includedir}/qt5/Qt/qfocusframe.h
%{_includedir}/qt5/Qt/qfontcombobox.h
%{_includedir}/qt5/Qt/qfontdialog.h
%{_includedir}/qt5/Qt/qformlayout.h
%{_includedir}/qt5/Qt/qframe.h
%{_includedir}/qt5/Qt/qgesture.h
%{_includedir}/qt5/Qt/qgesturerecognizer.h
%{_includedir}/qt5/Qt/qgraphics*.h
%{_includedir}/qt5/Qt/qgridlayout.h
%{_includedir}/qt5/Qt/qgroupbox.h
%{_includedir}/qt5/Qt/qgtkstyle.h
%{_includedir}/qt5/Qt/qheaderview.h
%{_includedir}/qt5/Qt/qicon.h
%{_includedir}/qt5/Qt/qiconengine.h
%{_includedir}/qt5/Qt/qiconengineplugin.h
%{_includedir}/qt5/Qt/qidentityproxymodel.h
%{_includedir}/qt5/Qt/qinputdialog.h
%{_includedir}/qt5/Qt/qitemdelegate.h
%{_includedir}/qt5/Qt/qitemeditorfactory.h
%{_includedir}/qt5/Qt/qitemselectionmodel.h
%{_includedir}/qt5/Qt/qkeyeventtransition.h
%{_includedir}/qt5/Qt/qlabel.h
%{_includedir}/qt5/Qt/qlayout.h
%{_includedir}/qt5/Qt/qlayoutitem.h
%{_includedir}/qt5/Qt/qlcdnumber.h
%{_includedir}/qt5/Qt/qlineedit.h
%{_includedir}/qt5/Qt/qlistview.h
%{_includedir}/qt5/Qt/qlistwidget.h
%{_includedir}/qt5/Qt/qmaccocoaviewcontainer_mac.h
%{_includedir}/qt5/Qt/qmacnativewidget_mac.h
%{_includedir}/qt5/Qt/qmacstyle_mac.h
%{_includedir}/qt5/Qt/qmainwindow.h
%{_includedir}/qt5/Qt/qmdiarea.h
%{_includedir}/qt5/Qt/qmdisubwindow.h
%{_includedir}/qt5/Qt/qmenu.h
%{_includedir}/qt5/Qt/qmenubar.h
%{_includedir}/qt5/Qt/qmessagebox.h
%{_includedir}/qt5/Qt/qmotifstyle.h
%{_includedir}/qt5/Qt/qmouseeventtransition.h
%{_includedir}/qt5/Qt/qplaintextedit.h
%{_includedir}/qt5/Qt/qplastiquestyle.h
%{_includedir}/qt5/Qt/qplatformmenu_qpa.h
%{_includedir}/qt5/Qt/qprogressbar.h
%{_includedir}/qt5/Qt/qprogressdialog.h
%{_includedir}/qt5/Qt/qproxymodel.h
%{_includedir}/qt5/Qt/qproxystyle.h
%{_includedir}/qt5/Qt/qpushbutton.h
%{_includedir}/qt5/Qt/qradiobutton.h
%{_includedir}/qt5/Qt/qrubberband.h
%{_includedir}/qt5/Qt/qscrollarea.h
%{_includedir}/qt5/Qt/qscrollbar.h
%{_includedir}/qt5/Qt/qscroller.h
%{_includedir}/qt5/Qt/qscrollerproperties.h
%{_includedir}/qt5/Qt/qshortcut.h
%{_includedir}/qt5/Qt/qsizegrip.h
%{_includedir}/qt5/Qt/qsizepolicy.h
%{_includedir}/qt5/Qt/qslider.h
%{_includedir}/qt5/Qt/qsortfilterproxymodel.h
%{_includedir}/qt5/Qt/qspinbox.h
%{_includedir}/qt5/Qt/qsplashscreen.h
%{_includedir}/qt5/Qt/qsplitter.h
%{_includedir}/qt5/Qt/qstacked*.h
%{_includedir}/qt5/Qt/qstandarditemmodel.h
%{_includedir}/qt5/Qt/qstatusbar.h
%{_includedir}/qt5/Qt/qstringlistmodel.h
%{_includedir}/qt5/Qt/qstyle*.h
%{_includedir}/qt5/Qt/qsystemtrayicon.h
%{_includedir}/qt5/Qt/qtabbar.h
%{_includedir}/qt5/Qt/qtableview.h
%{_includedir}/qt5/Qt/qtablewidget.h
%{_includedir}/qt5/Qt/qtabwidget.h
%{_includedir}/qt5/Qt/qtextbrowser.h
%{_includedir}/qt5/Qt/qtextedit.h
%{_includedir}/qt5/Qt/qtoolbar.h
%{_includedir}/qt5/Qt/qtoolbox.h
%{_includedir}/qt5/Qt/qtoolbutton.h
%{_includedir}/qt5/Qt/qtooltip.h
%{_includedir}/qt5/Qt/qtreeview.h
%{_includedir}/qt5/Qt/qtreewidget.h
%{_includedir}/qt5/Qt/qtreewidgetitemiterator.h
%{_includedir}/qt5/Qt/qundo*.h
%{_includedir}/qt5/Qt/qwhatsthis.h
%{_includedir}/qt5/Qt/qwidget.h
%{_includedir}/qt5/Qt/qwidgetaction.h
%{_includedir}/qt5/Qt/qwindowscestyle.h
%{_includedir}/qt5/Qt/qwindowsmobilestyle.h
%{_includedir}/qt5/Qt/qwindowsstyle.h
%{_includedir}/qt5/Qt/qwindowsvistastyle.h
%{_includedir}/qt5/Qt/qwindowsxpstyle.h
%{_includedir}/qt5/Qt/qwizard.h
%{_includedir}/qt5/Qt/qworkspace.h
%{_includedir}/qt5/Qt/qtwidgetsversion.h
%{_includedir}/qt5/Qt/qwidgetsfunctions_wince.h
%{_libdir}/libQtWidgets.prl
%{_libdir}/libQtWidgets.so
%{_libdir}/pkgconfig/QtWidgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_widgets.pri

%files qtplatformsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtPlatformSupport
%{_includedir}/qt5/QtPlatformSupport/
%{_includedir}/qt5/Qt/qtplatformsupportversion.h
%{_libdir}/libQtPlatformSupport.prl
%{_libdir}/pkgconfig/QtPlatformSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_platformsupport.pri

%files qtprintsupport
%defattr(-,root,root,-)
%{_libdir}/libQtPrintSupport.so.*

%files qtprintsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtPrintSupport
%{_includedir}/qt5/QtPrintSupport/
%{_includedir}/qt5/Qt/qtprintsupportversion.h
%{_libdir}/libQtPrintSupport.prl
%{_libdir}/libQtPrintSupport.so
%{_libdir}/pkgconfig/QtPrintSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_printsupport.pri

%files qtconcurrent
%defattr(-,root,root,-)
%{_libdir}/libQtConcurrent.so.*

%files qtconcurrent-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtConcurrent
%{_includedir}/qt5/QtConcurrent/
%{_libdir}/libQtConcurrent.prl
%{_libdir}/libQtConcurrent.so
%{_libdir}/pkgconfig/QtConcurrent.pc
%{_datadir}/qt5/mkspecs/modules/qt_concurrent.pri




# Plugin packages

%files plugin-accessible-libqtaccessiblewidgets
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/libqtaccessiblewidgets.so

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

%files plugin-platform-xcb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libxcb.so

# %files plugin-platform-xlib
# %defattr(-,root,root,-)
# %{_libdir}/qt5/plugins/platforms/libqxlib.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%files plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so




#### No changelog section, separate $pkg.changes contains the history
