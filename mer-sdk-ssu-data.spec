Name: mer-sdk-ssu-data
Version: 0.1.1
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
%{_datadir}/ssu/board-mappings.d/05-sdk-vm.ini
%{_datadir}/ssu/kickstart/part/sdk_vbox_vm

%prep
%setup -q -n src

%build
echo no build

%install
mkdir -p %{buildroot}/%{_datadir}/ssu/board-mappings.d
mkdir -p %{buildroot}/%{_datadir}/ssu/kickstart/part
install -D -m 644 05-sdk-vm.ini %{buildroot}/%{_datadir}/ssu/board-mappings.d/
install -D -m 644 sdk_vbox_vm %{buildroot}/%{_datadir}/ssu/kickstart/part/

