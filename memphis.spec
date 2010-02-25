Summary:	Map renderer for OpenStreetMap data
Summary(pl.UTF-8):	Renderer map dla danych OpenStreetMap
Name:		memphis
Version:	0.1.0
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz
# Source0-md5:	c62905573c03e5374d2f9834c047f4bc
URL:		http://trac.openstreetmap.ch/trac/memphis/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	expat-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmemphis-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmemphis-0.1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmemphis-0.1.so
%{_libdir}/libmemphis-0.1.la
%{_includedir}/libmemphis-0.1
%{_pkgconfigdir}/memphis-0.1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmemphis-0.1.a
