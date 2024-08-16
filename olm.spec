Summary:	Implementation of the olm and megolm cryptographic ratchets
Summary(pl.UTF-8):	Implementacja zapadek kryptograficznych olm i megolm
Name:		olm
Version:	3.2.16
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://gitlab.matrix.org/matrix-org/olm/-/tags
Source0:	https://gitlab.matrix.org/matrix-org/olm/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	6d16eee08cb58d1d124c88d7e7afe060
URL:		https://gitlab.matrix.org/matrix-org/olm
BuildRequires:	cmake >= 3.4
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-cffi
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the Double Ratchet cryptographic ratchet
described by <https://signal.org/docs/specifications/doubleratchet/>,
written in C and C++11 and exposed as a C API.

This library also includes an implementation of the Megolm
cryptographic ratchet.

%description -l pl.UTF-8
Implementacja zapadki kryptograficznej Double Ratchet, opisanej w
<https://signal.org/docs/specifications/doubleratchet/>, napisana w C
oraz C++11, udostępniająca API w języku C.

Biblioteka zawiera także implementację zapadki kryptograficznej
Megolm.

%package devel
Summary:	Development files for olm library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki olm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use olm library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę olm.

%package -n python3-%{name}
Summary:        Python 3 bindings for olm library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki olm
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
Requires:       python3-modules >= %{py3_ver}

%description -n python3-%{name}
Python 3 bindings for olm library.

%description -n python3-%{name} -l pl.UTF-8
Wiązania Pythona 3 do biblioteki olm.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}
cd ..

cd python
%py3_build
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cd python
%py3_install
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.md docs/*.md
%attr(755,root,root) %{_libdir}/libolm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libolm.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libolm.so
%{_includedir}/olm
%{_pkgconfigdir}/olm.pc
%{_libdir}/cmake/Olm

%files -n python3-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_libolm.abi3.so
%{py3_sitedir}/olm
%{py3_sitedir}/python_olm-%{version}-py*.egg-info
