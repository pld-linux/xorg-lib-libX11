#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Core X11 protocol client library
Summary(pl.UTF-8):	Podstawowa biblioteka kliencka protokołu X11
Name:		xorg-lib-libX11
Version:	1.6.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libX11-%{version}.tar.bz2
# Source0-md5:	f7c7a614f5c609e759dadb99436eb9c1
# sync locales and their encodings with glibc
Patch0:		%{name}-glibc-locale_sync.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	libxcb-devel >= 1.2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.21
BuildRequires:	xorg-sgml-doctools >= 1.10
BuildRequires:	xorg-util-util-macros >= 1.15
Requires:	libxcb >= 1.2
Obsoletes:	libX11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core X11 protocol client library.

%description -l pl.UTF-8
Podstawowa biblioteka kliencka protokołu X11.

%package devel
Summary:	Header files for libX11 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libX11
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-kbproto-devel
Requires:	xorg-proto-xproto-devel >= 7.0.21
Requires:	libxcb-devel >= 1.2
Obsoletes:	libX11-devel

%description devel
Core X11 protocol client library.

This package contains the header files needed to develop programs that
use libX11.

%description devel -l pl.UTF-8
Podstawowa biblioteka kliencka protokołu X11.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libX11.

%package static
Summary:	Static libX11 library
Summary(pl.UTF-8):	Biblioteka statyczna libX11
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libX11-static

%description static
Core X11 protocol client library.

This package contains the static libX11 library.

%description static -l pl.UTF-8
Podstawowa biblioteka kliencka protokołu X11.

Pakiet zawiera statyczną bibliotekę libX11.

%prep
%setup -q -n libX11-%{version}
# do we need this patch for anything? (aka is any pld user in need for these new locales)
# https://bugs.freedesktop.org/show_bug.cgi?id=7415
#%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libX11

cd specs
for dir in XIM i18n/framework i18n/localedb i18n/trans libX11; do
	install -d rpm-doc/$dir
	cp -a $dir/*.html rpm-doc/$dir
	cp -a $dir/*.svg rpm-doc/$dir || :
	sed -i -e "s#$RPM_BUILD_ROOT##g" rpm-doc/$dir/*.html
done

# for xorg-app-x11perf and possibly others
install -d $RPM_BUILD_ROOT%{_libdir}/X11

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%pretrans
# this needs to be a dir
if [ -L %{_libdir}/X11 ]; then
	umask 022
	mv -f %{_libdir}/X11{,.rpmsave}
	mkdir %{_libdir}/X11
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libX11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libX11.so.6
%attr(755,root,root) %{_libdir}/libX11-xcb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libX11-xcb.so.1
%dir %{_libdir}/X11
%dir %{_datadir}/X11
%{_datadir}/X11/XErrorDB
%{_datadir}/X11/Xcms.txt
%dir %{_datadir}/X11/locale
%{_datadir}/X11/locale/compose.dir
%{_datadir}/X11/locale/locale.alias
%{_datadir}/X11/locale/locale.dir
%{_datadir}/X11/locale/C
%{_datadir}/X11/locale/en_US.UTF-8

# encodings, not really lang taggable
%{_datadir}/X11/locale/armscii-8
%{_datadir}/X11/locale/georgian-academy
%{_datadir}/X11/locale/georgian-ps
%{_datadir}/X11/locale/ibm-cp1133
%{_datadir}/X11/locale/iscii-dev
%{_datadir}/X11/locale/isiri-3342
%{_datadir}/X11/locale/iso8859-1
%{_datadir}/X11/locale/iso8859-10
%{_datadir}/X11/locale/iso8859-11
%{_datadir}/X11/locale/iso8859-13
%{_datadir}/X11/locale/iso8859-14
%{_datadir}/X11/locale/iso8859-15
#%{_datadir}/X11/locale/iso8859-16
%{_datadir}/X11/locale/iso8859-2
%{_datadir}/X11/locale/iso8859-3
%{_datadir}/X11/locale/iso8859-4
%{_datadir}/X11/locale/iso8859-5
%{_datadir}/X11/locale/iso8859-6
%{_datadir}/X11/locale/iso8859-7
%{_datadir}/X11/locale/iso8859-8
%{_datadir}/X11/locale/iso8859-9
%{_datadir}/X11/locale/iso8859-9e
%{_datadir}/X11/locale/koi8-c
%{_datadir}/X11/locale/koi8-r
#%{_datadir}/X11/locale/koi8-t
%{_datadir}/X11/locale/koi8-u
%{_datadir}/X11/locale/microsoft-cp1251
%{_datadir}/X11/locale/microsoft-cp1255
%{_datadir}/X11/locale/microsoft-cp1256
%{_datadir}/X11/locale/mulelao-1
%{_datadir}/X11/locale/nokhchi-1
%{_datadir}/X11/locale/tatar-cyr
%{_datadir}/X11/locale/tscii-0

%lang(am) %{_datadir}/X11/locale/am_ET.UTF-8
%lang(el) %{_datadir}/X11/locale/el_GR.UTF-8
%lang(fi) %{_datadir}/X11/locale/fi_FI.UTF-8
%lang(ja) %{_datadir}/X11/locale/ja
%lang(ja) %{_datadir}/X11/locale/ja.JIS
#%lang(ja) %{_datadir}/X11/locale/ja.S90
%lang(ja) %{_datadir}/X11/locale/ja.SJIS
#%lang(ja) %{_datadir}/X11/locale/ja.U90
%lang(ja) %{_datadir}/X11/locale/ja_JP.UTF-8
%lang(ko) %{_datadir}/X11/locale/ko
%lang(ko) %{_datadir}/X11/locale/ko_KR.UTF-8
%lang(pt_BR) %{_datadir}/X11/locale/pt_BR.UTF-8
%lang(ru) %{_datadir}/X11/locale/ru_RU.UTF-8
%lang(th) %{_datadir}/X11/locale/th_TH
%lang(th) %{_datadir}/X11/locale/th_TH.UTF-8
%lang(vi) %{_datadir}/X11/locale/vi_VN.tcvn
%lang(vi) %{_datadir}/X11/locale/vi_VN.viscii
%lang(zh_CN) %{_datadir}/X11/locale/zh_CN
%lang(zh_CN) %{_datadir}/X11/locale/zh_CN.UTF-8
%lang(zh_CN) %{_datadir}/X11/locale/zh_CN.gb18030
%lang(zh_CN) %{_datadir}/X11/locale/zh_CN.gbk
%lang(zh_HK) %{_datadir}/X11/locale/zh_HK.UTF-8
%lang(zh_HK) %{_datadir}/X11/locale/zh_HK.big5
%lang(zh_HK) %{_datadir}/X11/locale/zh_HK.big5hkscs
%lang(zh_TW) %{_datadir}/X11/locale/zh_TW
%lang(zh_TW) %{_datadir}/X11/locale/zh_TW.UTF-8
%lang(zh_TW) %{_datadir}/X11/locale/zh_TW.big5
%{_mandir}/man5/*Compose.5*

%files devel
%defattr(644,root,root,755)
%doc specs/rpm-doc/*
%attr(755,root,root) %{_libdir}/libX11.so
%attr(755,root,root) %{_libdir}/libX11-xcb.so
%{_libdir}/libX11.la
%{_libdir}/libX11-xcb.la
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/X*.h
%{_includedir}/X11/cursorfont.h
%{_pkgconfigdir}/x11.pc
%{_pkgconfigdir}/x11-xcb.pc
%{_mandir}/man3/*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libX11.a
%{_libdir}/libX11-xcb.a
%endif
