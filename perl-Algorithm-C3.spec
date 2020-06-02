#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-C3
Version  : 0.10
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Algorithm-C3-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Algorithm-C3-0.10.tar.gz
Summary  : 'A module for merging hierarchies using the C3 algorithm'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Algorithm-C3-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::More)

%description
NAME
Algorithm::C3 - A module for merging hierarchies using the C3 algorithm
SYNOPSIS
use Algorithm::C3;

%package dev
Summary: dev components for the perl-Algorithm-C3 package.
Group: Development
Provides: perl-Algorithm-C3-devel = %{version}-%{release}
Requires: perl-Algorithm-C3 = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-C3 package.


%package perl
Summary: perl components for the perl-Algorithm-C3 package.
Group: Default
Requires: perl-Algorithm-C3 = %{version}-%{release}

%description perl
perl components for the perl-Algorithm-C3 package.


%prep
%setup -q -n Algorithm-C3-0.10
cd %{_builddir}/Algorithm-C3-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::C3.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Algorithm/C3.pm
