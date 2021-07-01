#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ConfigArgParse
Version  : 1.5.1
Release  : 52
URL      : https://files.pythonhosted.org/packages/d9/ad/d82750ad3a9e3419425eeeef7fbb5c8381dc8ec64a9894ddc3854837b10f/ConfigArgParse-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/ad/d82750ad3a9e3419425eeeef7fbb5c8381dc8ec64a9894ddc3854837b10f/ConfigArgParse-1.5.1.tar.gz
Summary  : A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.
Group    : Development/Tools
License  : MIT
Requires: ConfigArgParse-license = %{version}-%{release}
Requires: ConfigArgParse-python = %{version}-%{release}
Requires: ConfigArgParse-python3 = %{version}-%{release}
BuildRequires : PyYAML-python
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : pytest-python
BuildRequires : python-mock-python

%description
--------------

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
Provides: pypi(configargparse)

%description python3
python3 components for the ConfigArgParse package.


%prep
%setup -q -n ConfigArgParse-1.5.1
cd %{_builddir}/ConfigArgParse-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625159512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ConfigArgParse
cp %{_builddir}/ConfigArgParse-1.5.1/LICENSE %{buildroot}/usr/share/package-licenses/ConfigArgParse/374d44e6763a847adba3b724246d9c3b0273788a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ConfigArgParse/374d44e6763a847adba3b724246d9c3b0273788a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
