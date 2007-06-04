#
# Conditional build:
%bcond_without	xcb	# XCB for low-level protocol implementation
#
Summary:	X11 Base library
Summary(pl.UTF-8):	Podstawowa biblioteka X11
Name:		xorg-lib-libX11
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libX11-%{version}.tar.bz2
# Source0-md5:	710bf38a9477a5a1b235bc94f1d0593c
Patch0:		%{name}-glibc-locale_sync.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
%{?with_xcb:BuildRequires:	libxcb-devel >= 1.0}
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.6
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros >= 1.1.0
Obsoletes:	libX11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 Base library.

%description -l pl.UTF-8
Podstawowa biblioteka X11.

%package devel
Summary:	Header files for libX11 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libX11
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_xcb:Requires:	libxcb-devel >= 1.0}
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libXdmcp-devel
Requires:	xorg-proto-kbproto-devel
Requires:	xorg-proto-xproto-devel >= 7.0.6
Obsoletes:	libX11-devel

%description devel
X11 Base library.

This package contains the header files needed to develop programs that
use libX11.

%description devel -l pl.UTF-8
Podstawowa biblioteka X11.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libX11.

%package static
Summary:	Static libX11 library
Summary(pl.UTF-8):	Biblioteka statyczna libX11
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libX11-static

%description static
X11 Base library.

This package contains the static libX11 library.

%description static -l pl.UTF-8
Podstawowa biblioteka X11.

Pakiet zawiera statyczną bibliotekę libX11.

%prep
%setup -q -n libX11-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_xcb:--without-xcb}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}
	
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libX11.so.*.*.*
%if %{with xcb}
%attr(755,root,root) %{_libdir}/libX11-xcb.so.*.*.*
%endif
%dir %{_libdir}/X11
%{_libdir}/X11/Xcms.txt
%dir %{_datadir}/X11
%{_datadir}/X11/XErrorDB
%{_datadir}/X11/XKeysymDB
%{_datadir}/X11/locale

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libX11.so
%{_libdir}/libX11.la
%{_includedir}/X11/*.h
%{_pkgconfigdir}/x11.pc
%if %{with xcb}
%attr(755,root,root) %{_libdir}/libX11-xcb.so
%{_libdir}/libX11-xcb.la
#%{_includedir}/X11/Xlib-xcb.h (already included in *.h above)
%{_pkgconfigdir}/x11-xcb.pc
%endif
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libX11.a
%if %{with xcb}
%{_libdir}/libX11-xcb.a
%endif
