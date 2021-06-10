#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ruamel.yaml
Version  : 0.17.9
Release  : 44
URL      : https://files.pythonhosted.org/packages/ea/7f/4bcd7276603b4324ac12839a949b3e58f03cda1d87218c89a8a1efe31c1a/ruamel.yaml-0.17.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/ea/7f/4bcd7276603b4324ac12839a949b3e58f03cda1d87218c89a8a1efe31c1a/ruamel.yaml-0.17.9.tar.gz
Summary  : ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order
Group    : Development/Tools
License  : MIT
Requires: ruamel.yaml-license = %{version}-%{release}
Requires: ruamel.yaml-python = %{version}-%{release}
Requires: ruamel.yaml-python3 = %{version}-%{release}
Requires: ruamel.yaml.clib
BuildRequires : buildreq-distutils3
BuildRequires : ruamel.yaml.clib

%description
ruamel.yaml
        ===========
        
        ``ruamel.yaml`` is a YAML 1.2 loader/dumper package for Python.

%package license
Summary: license components for the ruamel.yaml package.
Group: Default

%description license
license components for the ruamel.yaml package.


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
Provides: pypi(ruamel.yaml)
Requires: pypi(ruamel.yaml.clib)

%description python3
python3 components for the ruamel.yaml package.


%prep
%setup -q -n ruamel.yaml-0.17.9
cd %{_builddir}/ruamel.yaml-0.17.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623339800
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ruamel.yaml
cp %{_builddir}/ruamel.yaml-0.17.9/LICENSE %{buildroot}/usr/share/package-licenses/ruamel.yaml/626b87d7b11d112fb2e938a309373614f788e1ef
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ruamel.yaml/626b87d7b11d112fb2e938a309373614f788e1ef

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
