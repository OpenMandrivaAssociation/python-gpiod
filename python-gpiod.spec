Name:		python-gpiod
Version:	1.5.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/gpiod/gpiod-%{version}.tar.gz
Summary:	g
URL:		https://pypi.org/project/gpiod/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
g


%prep
%autosetup -p1 -n gpiod-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/gpiod
%{py_sitedir}/gpiod-*.*-info
