Name: kiwix-lib
Version: 10.0.0
Release: 1%{?dist}

License: GPLv3+
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: libmicrohttpd-devel
BuildRequires: mustache-devel
BuildRequires: pugixml-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: zimlib-devel
BuildRequires: gtest-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: cmake
BuildRequires: aria2
BuildRequires: gcc

%description
The Kiwix library provides the Kiwix software core. It contains
the code shared by all Kiwix ports.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
#%meson -Dwerror=false
%meson_build

%install
%meson_install

# Fedora's version of pugixml package does not provide pkg-config file.
sed -e 's/pugixml //g' -i %{buildroot}%{_libdir}/pkgconfig/kiwix.pc

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/kiwix-compile-resources
%{_libdir}/libkiwix.so.10*
%{_mandir}/man1/kiwix*.1*

%files devel
%{_includedir}/kiwix
%{_libdir}/libkiwix.so
%{_libdir}/pkgconfig/kiwix.pc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 9.4.1-1
- Updated to version 9.4.1.

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.4.0-1
- Updated to version 9.4.0.

* Wed Aug 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.3.1-3
- Fixed crash on exit.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.3.1-1
- Updated to version 9.3.1.

* Fri Jul 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.3.0-1
- Updated to version 9.3.0.

* Wed Jul 01 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.2.3-1
- Updated to version 9.2.3.

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 9.1.2-2
- Rebuild for ICU 67

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.1.2-1
- Updated to version 9.1.2.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 9.1.0-1
- Updated to version 9.1.0.

* Mon Feb 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 8.2.2-1
- Updated to version 8.2.2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 8.1.0-2
- Rebuild for ICU 65

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 8.1.0-1
- Updated to version 8.1.0.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.2.0-1
- Updated to version 5.2.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.0-1
- Updated to version 5.1.0.

* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.0-1
- Updated to version 5.0.0.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1.0-1
- Updated to version 4.1.0.

* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.1-1
- Initial SPEC release.
