Name: kiwix-tools
Version: 3.1.2
Release: 6%{?dist}

License: GPLv3+
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: libmicrohttpd-devel
BuildRequires: kiwix-lib-devel
BuildRequires: pugixml-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
The Kiwix tools is a collection of Kiwix related command line
tools.

%prep
%autosetup -p1

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc AUTHORS Changelog README.md
%license COPYING
%{_bindir}/kiwix*
%{_mandir}/man1/kiwix*.1*
%{_mandir}/*/man1/kiwix*.1*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.2-4
- Rebuilt due to kiwix-lib update.

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.2-3
- Rebuilt due to kiwix-lib update.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.2-1
- Updated to version 3.1.2.

* Wed Jul 01 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.1-1
- Updated to version 3.1.1.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-1
- Updated to version 3.1.0.

* Mon Feb 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.1-3
- Rebuilt due to kiwix-lib update.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.1-1
- Updated to version 3.0.1.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-1
- Updated to version 2.0.0.

* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.1-1
- Updated to version 1.2.1.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0-1
- Updated to version 1.1.0.

* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial SPEC release.
