%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define mod_path ibus-0.0
Name:       ibus-array
Version:    0.1.2
Release:    0
Summary:    IBus Array 30 project
License:    GPLv2+
Group:      System Environment/Libraries
URL:        https://github.com/lexical/ibus-array
Source0:    %{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  ibus-devel
BuildRequires:  libtool
BuildRequires:  sqlite3-devel

Requires:   ibus

%description
IBus Array 30 project.

%prep
%setup -q -n %{name}-release-%{version}

%build
./autogen.sh
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
# %dir %{python_sitearch}/ibus
# %{python_sitearch}/ibus/*
%dir %{_datadir}/ibus-array
%{_datadir}/ibus-array/icons
%{_datadir}/ibus-array/icons/ibus-array.png
%{_datadir}/ibus-array/setup
%{_datadir}/ibus-array/setup/config.py
%{_datadir}/ibus-array/setup/config.pyc
%{_datadir}/ibus-array/setup/config.pyo
%{_datadir}/ibus-array/setup/main.py
%{_datadir}/ibus-array/setup/main.pyc
%{_datadir}/ibus-array/setup/main.pyo
%{_datadir}/ibus-array/tables
%{_datadir}/ibus-array/tables/array.db
%{_datadir}/ibus/component/array.xml
/usr/lib/ibus-engine-array
/usr/lib/ibus-setup-array

