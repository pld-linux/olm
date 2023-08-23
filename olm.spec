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
BuildRequires:	rpmbuild(macros) >= 1.605
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

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
