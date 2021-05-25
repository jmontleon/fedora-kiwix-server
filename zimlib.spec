%global appname libzim

Name: zimlib
Version: 7.0.0
Release: 1%{?dist}

License: GPLv2 and ASL 2.0 and BSD
Summary: Reference implementation of the ZIM specification

URL: https://github.com/openzim/%{appname}
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: xapian-core-devel
BuildRequires: libzstd-devel
BuildRequires: libicu-devel
BuildRequires: gtest-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
The ZIM library is the reference implementation for the ZIM file
format. It's a solution to read and write ZIM files on many systems
and architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/%{appname}.so.7*

%files devel
%{_includedir}/zim
%{_libdir}/%{appname}.so
%{_libdir}/pkgconfig/%{appname}.pc

%changelog
* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 6.3.0-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.3.0-1
- Updated to version 6.3.0.

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.2-1
- Updated to version 6.2.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.8-1
- Updated to version 6.1.8.

* Wed Jul 01 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.7-1
- Updated to version 6.1.7.

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 6.1.1-2
- Rebuild for ICU 67

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.1-1
- Updated to version 6.1.1.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.0-1
- Updated to version 6.1.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 6.0.2-2
- Rebuild for ICU 65

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 6.0.2-1
- Updated to version 6.0.2.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.1-1
- Updated to version 5.0.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.0-1
- Updated to version 5.0.0.

* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.7-1
- Updated to version 4.0.7.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.6-3
- Removed Werror build flag.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.6-2
- Removed rpath.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.6-1
- Updated to version 4.0.6.

* Tue Mar 19 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.5-1
- Updated to version 4.0.5.
- Major SPEC cleanup.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Micah Roth <micah.roth_ucla.edu> 1.0-5
- forced INSTALL to preserve timestamps for non-compiled files

* Thu Apr 25 2013 Micah Roth <micah.roth_ucla.edu> 1.0-4
- --formal review volter--
- removed INSTALL, NEWS, README files from %%docs
- added COPYING file to %%docs
- removed unnecessary commented lines and empty sections
- improved %%files devel section with asterisk removal and more specificity
- added spaces in the %%changelog area between updates

* Tue Apr 23 2013 Micah Roth <micah.roth_ucla.edu> 1.0-3
- --informal review volter--
- updated descriptions to match %%files lists
- added --disable-static to %%configure

* Sat Apr 20 2013 Micah Roth <micah.roth_ucla.edu> 1.0-2
- added %%doc files
- removed commented lines
- removed --disable-static because it doesn't apply (right?)
- ---volter's informal review---
- moved binaries to base package %%files list
- commented libtool BR
- uncommented removal of *la file(s)
- added macros into Source0
- commented *a %%files list entry

* Sat Apr 20 2013 Micah Roth <micah.roth_ucla.edu> 1.0-1
- created spec file
- commented automake and autotools BRs as recommended by rdieter 
