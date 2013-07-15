Summary:	Utilities for manipulating Macintosh file formats
Name:		macutils
Version:	2.0b3
Release:	23
License:	GPL-style
Group:		Networking/Other
Url:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/macutils.tar.gz
Patch0:		macutils-misc.patch
Patch1:		macutils-2.0b3-gcc3.4-fix.patch
Patch2:		macutils-2.0b3-gcc4.0-fixes.patch

%description
The macutils package includes a set of utilities for manipulating
files that are commonly used by Macintosh machines.  Macutils includes
utilities like binhex, hexbin, macunpack, etc.

Install macutils if you need to manipulate files that are commonly used
by Macintosh machines.

%prep
%setup -qn %{name}
%apply_patches
sed - -i -e "s/CF =/CF = $RPM_OPT_FLAGS/" makefile

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 755 binhex/binhex  %{buildroot}%{_bindir}
install -m 755 hexbin/hexbin %{buildroot}%{_bindir}
install -m 755 comm/frommac %{buildroot}%{_bindir}
install -m 755 mixed/macsave %{buildroot}%{_bindir}
install -m 755 mixed/macstream %{buildroot}%{_bindir}
install -m 755 macunpack/macunpack %{buildroot}%{_bindir}

install -m 644 man/* %{buildroot}%{_mandir}/man1/

%files
%doc README
%{_bindir}/*
%{_mandir}/man1/*

