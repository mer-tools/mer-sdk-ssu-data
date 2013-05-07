Name: mer-sdk-ssu-data
Version: 0.1.2
Release: 1
Summary: Mer SDK SSU data
Summary: ssu vendor configuration data for Mer SDK
URL: https://github.com/mer-tools/mer-sdk-ssu-data
Group: System/Base
BuildArch: noarch
License: GPLv2
Source0: %{name}.tar.bz2
Requires: ssu >= 0.31
Provides: ssu-vendor-data

%description
ssu data for Mer SDK

%files
%defattr(-,root,root,-)
%attr(0664, root, ssu) %config(noreplace) %{_sysconfdir}/ssu/ssu.ini
%{_datadir}/ssu/*.ini

%prep
# Adjusting %%setup since git-pkg unpacks to src/
# %%setup -q -n src
%setup -q -n src -n src

%build
echo no build

%install
make DESTDIR=%{buildroot} install

