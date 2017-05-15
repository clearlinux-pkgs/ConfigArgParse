#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ConfigArgParse
Version  : 0.12.0
Release  : 3
URL      : https://pypi.debian.net/ConfigArgParse/ConfigArgParse-0.12.0.tar.gz
Source0  : https://pypi.debian.net/ConfigArgParse/ConfigArgParse-0.12.0.tar.gz
Summary  : A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.
Group    : Development/Tools
License  : MIT
Requires: ConfigArgParse-python
Requires: PyYAML
BuildRequires : PyYAML-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Overview
~~~~~~~~
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files,
hard-coded defaults, and in some cases, environment variables.

%package python
Summary: python components for the ConfigArgParse package.
Group: Default
Provides: configargparse-python

%description python
python components for the ConfigArgParse package.


%prep
%setup -q -n ConfigArgParse-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494865253
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1494865253
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
