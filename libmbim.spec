Name:           libmbim
Version:        1.24.2
Release:        1
Summary:        A glib-based library for talking to WWAN modems and devices
License:        LGPLv2+
URL:            http://freedesktop.org/software/libmbim
Source:         http://freedesktop.org/software/libmbim/%{name}-%{version}.tar.xz

BuildRequires:  gcc glib2-devel pkgconfig automake autoconf libtool
BuildRequires:  python3 pkgconfig(gudev-1.0) >= 147 gtk-doc
BuildRequires:  libxslt python-unversioned-command

Provides:       %{name}-utils = %{version}-%{release}
Obsoletes:      %{name}-utils < %{version}-%{release}

%description
Libmbim is a glib-based library for talking to WWAN modems and
devices which speak the Mobile Interface Broadband Model (MBIM) protocol.

%package devel
Summary:        Development package for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel

%description devel
This package contains some header and library files for the development of the %{name}.

%package_help

%prep
%autosetup -p1

%build
%configure --disable-static --enable-gtk-doc
%make_build V=1

%install
%make_install
%delete_la

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING NEWS AUTHORS README
%{_libdir}/libmbim-glib.so.*
%{_bindir}/*
%{_datadir}/bash-completion
%{_libexecdir}/mbim-proxy

%files devel
%{_includedir}/libmbim-glib/
%{_libdir}/pkgconfig/mbim-glib.pc
%{_libdir}/libmbim-glib.so
%dir %{_datadir}/gtk-doc/html/libmbim-glib
%{_datadir}/gtk-doc/html/libmbim-glib/*

%files help
%{_mandir}/man1/*

%changelog
* Tue Jul 28 2020 cuibaobao <cuibaobao1@huawei.com> - 1.24.2-1
- update to 1.24.2

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.16.0-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add patch to modify build err

* Wed Dec 11 2019 catastrowings <jianghuhao1994@163.com> - 1.16.0-4
- openEuler init
