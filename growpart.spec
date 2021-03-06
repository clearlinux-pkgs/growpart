#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD65861883E014DB9 (paride@fsfe.org)
#
Name     : growpart
Version  : 0.32
Release  : 3
URL      : https://launchpad.net/cloud-utils/trunk/0.32/+download/cloud-utils-0.32.tar.gz
Source0  : https://launchpad.net/cloud-utils/trunk/0.32/+download/cloud-utils-0.32.tar.gz
Source1  : growpartfs@.service
Source2  : https://launchpad.net/cloud-utils/trunk/0.32/+download/cloud-utils-0.32.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: growpart-bin = %{version}-%{release}
Requires: growpart-license = %{version}-%{release}
Requires: growpart-man = %{version}-%{release}
Requires: growpart-services = %{version}-%{release}
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
Patch1: 0001-Add-growpartfs.patch

%description
Extends a partition to fill available space

%package bin
Summary: bin components for the growpart package.
Group: Binaries
Requires: growpart-license = %{version}-%{release}
Requires: growpart-services = %{version}-%{release}

%description bin
bin components for the growpart package.


%package license
Summary: license components for the growpart package.
Group: Default

%description license
license components for the growpart package.


%package man
Summary: man components for the growpart package.
Group: Default

%description man
man components for the growpart package.


%package services
Summary: services components for the growpart package.
Group: Systemd services

%description services
services components for the growpart package.


%prep
%setup -q -n cloud-utils-0.32
cd %{_builddir}/cloud-utils-0.32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644187800
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1644187800
rm -rf %{buildroot}
## install_prepend content
rm -rf $(ls {bin,man}/*|grep -v growpart)
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/growpart
cp %{_builddir}/cloud-utils-0.32/LICENSE %{buildroot}/usr/share/package-licenses/growpart/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/cloud-utils-0.32/debian/copyright %{buildroot}/usr/share/package-licenses/growpart/ed7b8475e64170f6f399b68e50d6c4d4dc6a44cf
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/growpartfs@.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/growpart
/usr/bin/growpartfs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/growpart/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/growpart/ed7b8475e64170f6f399b68e50d6c4d4dc6a44cf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/growpart.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/growpartfs@.service
