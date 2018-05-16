#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ConfigArgParse
Version  : 0.13.0
Release  : 15
URL      : https://pypi.debian.net/ConfigArgParse/ConfigArgParse-0.13.0.tar.gz
Source0  : https://pypi.debian.net/ConfigArgParse/ConfigArgParse-0.13.0.tar.gz
Summary  : A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.
Group    : Development/Tools
License  : MIT
Requires: ConfigArgParse-python3
Requires: ConfigArgParse-python
Requires: PyYAML
BuildRequires : PyYAML-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
~~~~~~~~
        
        Applications with more than a handful of user-settable options are best
        configured through a combination of command line args, config files,
        hard-coded defaults, and in some cases, environment variables.
        
        Python's command line parsing modules such as argparse have very limited
        support for config files and environment variables, so this module
        extends argparse to add these features.

%package python
Summary: python components for the ConfigArgParse package.
Group: Default
Requires: ConfigArgParse-python3
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
%setup -q -n ConfigArgParse-0.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523287316
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
