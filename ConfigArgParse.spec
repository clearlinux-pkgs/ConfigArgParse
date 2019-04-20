#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ConfigArgParse
Version  : 0.14.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/55/ea/f0ade52790bcd687127a302b26c1663bf2e0f23210d5281dbfcd1dfcda28/ConfigArgParse-0.14.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/55/ea/f0ade52790bcd687127a302b26c1663bf2e0f23210d5281dbfcd1dfcda28/ConfigArgParse-0.14.0.tar.gz
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
~~~~~~~~
        
        Applications with more than a handful of user-settable options are best
        configured through a combination of command line args, config files,
        hard-coded defaults, and in some cases, environment variables.
        
        Python's command line parsing modules such as argparse have very limited
        support for config files and environment variables, so this module
        extends argparse to add these features.

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
%setup -q -n ConfigArgParse-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550194058
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
