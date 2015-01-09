#
# Conditional build:
%bcond_with	python	# Python CLI ("doesn't work currently" says configure, only ghttp supported)
#
Summary:	SBLIM WBEM Command Line Interface
Summary(pl.UTF-8):	SBLIM WBEM CLI - interfejs linii poleceń
Name:		sblim-wbemcli
Version:	1.6.3
Release:	1
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	521e64351e663e12f6a19ed1a2fa8e79
Patch0:		%{name}-python.patch
URL:		http://sblim.sourceforge.net/
BuildRequires:	curl-devel >= 7.9.3
BuildRequires:	libstdc++-devel
%if %{with python}
BuildRequires:	python-devel >= 2
BuildRequires:	swig-python
%endif
Requires:	curl-libs >= 7.9.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WBEM Command Line Interface is a standalone, command line WBEM client.
It is specially suited for basic systems management tasks as it can be
used in scripts.

%description -l pl.UTF-8
WBEM Command Line Interface to samodzielny klient WBEM działający z
linii poleceń. Jest przydatny zwłaszcza do podstawowych zadań
zarządzania systemem, które można wykonywać w skryptach.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_python:--enable-pythoncli}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README README.pycli
%attr(755,root,root) %{_bindir}/wbem*
%{_mandir}/man1/wbemcli.1*
