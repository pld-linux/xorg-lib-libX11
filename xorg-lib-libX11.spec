Summary:	X11 Base library
Summary(pl):	Podstawowa biblioteka X11
Name:		xorg-lib-libX11
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libX11-%{version}.tar.bz2
# Source0-md5:	0bb745ed34f8bf09d0c0d89ff91c56b4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libX11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X11 Base library.

%description -l pl
Podstawowa biblioteka X11.

%package devel
Summary:	Header files libX11 development
Summary(pl):	Pliki nag³ówkowe do biblioteki libX11
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libXdmcp-devel
Requires:	xorg-proto-kbproto-devel
Obsoletes:	libX11-devel

%description devel
X11 Base library.

This package contains the header files needed to develop programs that
use these libX11.

%description devel -l pl
Podstawowa biblioteka X11.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libX11.

%package static
Summary:	Static libX11 library
Summary(pl):	Biblioteka statyczna libX11
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libX11-static

%description static
X11 Base library.

This package contains the static libX11 library.

%description static -l pl
Podstawowa biblioteka X11.

Pakiet zawiera statyczn± bibliotekê libX11.

%prep
%setup -q -n libX11-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-man-pages=3

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
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libX11.so.*.*.*
%{_libdir}/X11/locale
%{_datadir}/X11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libX11.so
%{_libdir}/libX11.la
%{_includedir}/X11/*.h
%{_pkgconfigdir}/x11.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libX11.a
