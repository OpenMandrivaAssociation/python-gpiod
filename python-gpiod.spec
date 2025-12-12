Name:		python-gpiod
Version:	2.3.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/g/gpiod/gpiod-%{version}.tar.gz
Summary:	These are the official Python bindings for libgpiod.
URL:		https://pypi.org/project/gpiod/
License:	MIT
Group:		Development/Python
BuildSystem:    python
BuildRequires:  pkgconfig(python)

%description
These are the official Python bindings for libgpiod

%files
%doc README.md
%{python_sitearch}/gpiod
%{python_sitearch}/gpiod-*.dist-info
