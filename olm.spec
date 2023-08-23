Summary:	Implementation of the olm and megolm cryptographic ratchets
Name:		olm
Version:	3.2.15
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://gitlab.matrix.org/matrix-org/olm/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	18e62ee5128157f218176d736a9cbe02
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
described by https://signal.org/docs/specifications/doubleratchet/,
written in C and C++11 and exposed as a C API.

This library also includes an implementation of the Megolm
cryptographic ratchet.

%package devel
Summary:	Development files for olm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use olm.

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name} library
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
Requires:       python3-modules >= %py3_ver

%description -n python3-%{name}
Python 3 bindings for %{name} library.

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
%doc README.md
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
