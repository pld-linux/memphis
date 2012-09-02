#
# Conditional build:
%bcond_with	vala	# Vala binding
#
Summary:	Map renderer for OpenStreetMap data
Summary(pl.UTF-8):	Renderer map dla danych OpenStreetMap
Name:		memphis
Version:	0.2.3
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz
# Source0-md5:	dbed61f37d07801c1f660c0b5a5d81bc
URL:		http://trac.openstreetmap.ch/trac/memphis/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	expat-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_vala:BuildRequires:	vala >= 0.8.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memphis is a map-rendering library for OpenStreetMap data.

%description -l pl.UTF-8
Memphis jest biblioteką renderującą mapy dla danych OpenStreetMap.

%package devel
Summary:	Header files for libmemphis library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmemphis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.4.0
Requires:	glib2-devel >= 1:2.16.0

%description devel
Header files for libmemphis library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmemphis.

%package static
Summary:	Static libmemphis library
Summary(pl.UTF-8):	Statyczna biblioteka libmemphis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmemphis library.

%description static -l pl.UTF-8
Statyczna biblioteka libmemphis.

%package apidocs
Summary:	libmemphis library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmemphis
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmemphis library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmemphis.

%package -n vala-memphis
Summary:	libmemphis API for Vala language
Summary(pl.UTF-8):	API libmemphis dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 0.8.0

%description -n vala-memphis
libmemphis API for Vala language.

%description -n vala-memphis -l pl.UTF-8
API libmemphis dla języka Vala.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	%{?with_vala:--enable-vala} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmemphis-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmemphis-0.2.so.0
%{_libdir}/girepository-1.0/Memphis-0.2.typelib
%{_datadir}/memphis

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmemphis-0.2.so
%{_includedir}/libmemphis-0.2
%{_pkgconfigdir}/memphis-0.2.pc
%{_datadir}/gir-1.0/Memphis-0.2.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libmemphis-0.2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmemphis

%if %{with vala}
%files -n vala-memphis
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/memphis-0.2.deps
%{_datadir}/vala/vapi/memphis-0.2.vapi
%endif
