%global _enable_debug_package 0
%global debug_package %{nil}

Summary:            URIparser library
Name:               uriparser
Version:            0.8.4
Release:            1%{?dist}
License:            BSD
Group:              Development/Tools
Source:             gru-%{version}.tar.gz
URL:                http://uriparser.sourceforge.net/
BuildRequires:      autogen
BuildRequires:      make
BuildRequires:      gcc
BuildRequires:      doxygen


%description
Uriparser is a strictly RFC 3986 compliant URI parsing library written in C. uriparser is cross-platform, fast, supports Unicode and is licensed under the New BSD license.


%package devel
Summary:            URI parsing utility development kit
Requires:           gcc
Group:              Development/Libraries

%description devel
Development packages for the URI parsing utility

%prep
%autosetup -n uriparser-%{version}

%build
./autogen.sh
./configure --disable-test --disable-doc --prefix=%{buildroot}/usr
make

%install
make install

%files
%doc AUTHORS COPYING
%{_libdir}/*


%files devel
%{_includedir}/*

%changelog
* Tue Feb 23 2017 Otavio R. Piske <angusyoung@gmail.com> - 20170223
- Packaged for EL6 on COPR
