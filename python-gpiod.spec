%define module gpiod

Name:		python-gpiod
Version:	2.4.1
Release:	1
Summary:	These are the official Python bindings for libgpiod
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/gpiod/
Source0:	https://files.pythonhosted.org/packages/source/g/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
These are the official Python bindings for libgpiod.

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%doc README.md
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
