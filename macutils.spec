%define	name	macutils
%define	version	2.0b3
%define	release	%mkrel 20

Summary:	Utilities for manipulating Macintosh file formats
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL-style
Group:		Networking/Other
Url:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/macutils.tar.bz2
Patch0:		macutils-misc.patch
Patch1:		macutils-2.0b3-gcc3.4-fix.patch
Patch2:		macutils-2.0b3-gcc4.0-fixes.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The macutils package includes a set of utilities for manipulating
files that are commonly used by Macintosh machines.  Macutils includes
utilities like binhex, hexbin, macunpack, etc.

Install macutils if you need to manipulate files that are commonly used
by Macintosh machines.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1 -b .gcc34
%patch2 -p1 -b .gcc40

%build
perl -p -i -e "s/CF =/CF = $RPM_OPT_FLAGS/" makefile

%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -m 755 binhex/binhex  $RPM_BUILD_ROOT%{_bindir}
install -m 755 hexbin/hexbin $RPM_BUILD_ROOT%{_bindir}
install -m 755 comm/frommac $RPM_BUILD_ROOT%{_bindir}
install -m 755 mixed/macsave $RPM_BUILD_ROOT%{_bindir}
install -m 755 mixed/macstream $RPM_BUILD_ROOT%{_bindir}
install -m 755 macunpack/macunpack $RPM_BUILD_ROOT%{_bindir}

install -m 644 man/* $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*


