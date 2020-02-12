#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ruamel.yaml
Version  : 0.16.10
Release  : 26
URL      : https://files.pythonhosted.org/packages/16/8b/54a26c1031595e5edd0e616028b922d78d8ffba8bc775f0a4faeada846cc/ruamel.yaml-0.16.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/8b/54a26c1031595e5edd0e616028b922d78d8ffba8bc775f0a4faeada846cc/ruamel.yaml-0.16.10.tar.gz
Summary  : ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order
Group    : Development/Tools
License  : MIT
Requires: ruamel.yaml-python = %{version}-%{release}
Requires: ruamel.yaml-python3 = %{version}-%{release}
Requires: ruamel.yaml.clib
BuildRequires : buildreq-distutils3
BuildRequires : ruamel.yaml.clib

%description
ruamel.yaml
===========
``ruamel.yaml`` is a YAML 1.2 loader/dumper package for Python.

%package python
Summary: python components for the ruamel.yaml package.
Group: Default
Requires: ruamel.yaml-python3 = %{version}-%{release}

%description python
python components for the ruamel.yaml package.


%package python3
Summary: python3 components for the ruamel.yaml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ruamel.yaml package.


%prep
%setup -q -n ruamel.yaml-0.16.10
cd %{_builddir}/ruamel.yaml-0.16.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581529235
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
