#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ruamel-yaml
Version  : 0.15.90
Release  : 8
URL      : https://files.pythonhosted.org/packages/fc/4c/0f5133e900fef3b70bc9703436d3ef1736cba6c11e4ae8ac99acd5e1576e/ruamel.yaml-0.15.90.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/4c/0f5133e900fef3b70bc9703436d3ef1736cba6c11e4ae8ac99acd5e1576e/ruamel.yaml-0.15.90.tar.gz
Summary  : ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order
Group    : Development/Tools
License  : MIT
Requires: ruamel-yaml-license = %{version}-%{release}
Requires: ruamel-yaml-python = %{version}-%{release}
Requires: ruamel-yaml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
ruamel.yaml
        ===========
        
        ``ruamel.yaml`` is a YAML 1.2 loader/dumper package for Python.

%package license
Summary: license components for the ruamel-yaml package.
Group: Default

%description license
license components for the ruamel-yaml package.


%package python
Summary: python components for the ruamel-yaml package.
Group: Default
Requires: ruamel-yaml-python3 = %{version}-%{release}

%description python
python components for the ruamel-yaml package.


%package python3
Summary: python3 components for the ruamel-yaml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ruamel-yaml package.


%prep
%setup -q -n ruamel.yaml-0.15.90

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554484554
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ruamel-yaml
cp LICENSE %{buildroot}/usr/share/package-licenses/ruamel-yaml/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ruamel-yaml/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
