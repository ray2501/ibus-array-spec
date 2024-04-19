Name:       ibus-array
Version:    0.2.3
Release:    0
Summary:    IBus Array 30 project
License:    GPL-2.0-or-later
Group:      System Environment/Libraries
URL:        https://github.com/lexical/ibus-array
Source0:    %{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  ibus-devel
BuildRequires:  sqlite3-devel
BuildRequires:  opencc-devel

Requires:   ibus

%description
IBus Array 30 project.

%prep
%setup -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%dir %{_datadir}/ibus-array
%{_datadir}/ibus-array/icons
%{_datadir}/ibus-array/setup
%{_datadir}/ibus-array/tables
%{_datadir}/ibus/component/array.xml
/usr/libexec/ibus-engine-array
/usr/libexec/ibus-setup-array

