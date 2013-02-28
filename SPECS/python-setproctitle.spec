%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname setproctitle

Name:           python-%{srcname}
Version:        1.1.7
Release:        1.vortex%{?dist}
Summary:        A setproctitle implementation for Python
Vendor:         Vortex RPM

Group:          Development/Libraries
License:        MIT
URL:            http://code.google.com/p/py-setproctitle
Source0:        http://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools, python-devel

%description
The library allows a process to change its title (as displayed by system tools
such as ps and top).

Changing the title is mostly useful in multi-process systems, for example when
a master process is forked: changing the children's title allows to identify
the task each process is busy with. The technique is used by PostgreSQL and
the OpenSSH Server for example.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p %{buildroot}/usr/lib/python2.6
mv %{buildroot}/usr/lib64/python2.6/site-packages %{buildroot}/usr/lib/python2.6

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst COPYRIGHT
%{python_sitelib}/%{srcname}*

%changelog
* Thu Feb 28 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.1.7-1.vortex
- Initial packaging.

