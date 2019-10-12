#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ConfigArgParse
Version  : 0.15.1
Release  : 26
URL      : https://files.pythonhosted.org/packages/24/f2/91071498c99fdff7bf8bddb4b981e68bb095b6204233b5d9ce6747f97836/ConfigArgParse-0.15.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/24/f2/91071498c99fdff7bf8bddb4b981e68bb095b6204233b5d9ce6747f97836/ConfigArgParse-0.15.1.tar.gz
Summary  : A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.
Group    : Development/Tools
License  : MIT
Requires: ConfigArgParse-license = %{version}-%{release}
Requires: ConfigArgParse-python = %{version}-%{release}
Requires: ConfigArgParse-python3 = %{version}-%{release}
Requires: PyYAML
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3

%description
ConfigArgParse
--------------
.. image:: https://img.shields.io/pypi/v/ConfigArgParse.svg?style=flat
:alt: PyPI version
:target: https://pypi.python.org/pypi/ConfigArgParse

%package license
Summary: license components for the ConfigArgParse package.
Group: Default

%description license
license components for the ConfigArgParse package.


%package python
Summary: python components for the ConfigArgParse package.
Group: Default
Requires: ConfigArgParse-python3 = %{version}-%{release}
Provides: configargparse-python

%description python
python components for the ConfigArgParse package.


%package python3
Summary: python3 components for the ConfigArgParse package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ConfigArgParse package.


%prep
%setup -q -n ConfigArgParse-0.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570906886
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ConfigArgParse
cp LICENSE %{buildroot}/usr/share/package-licenses/ConfigArgParse/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ConfigArgParse/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
