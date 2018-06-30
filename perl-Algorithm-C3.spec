#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-C3
Version  : 0.10
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Algorithm-C3-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Algorithm-C3-0.10.tar.gz
Summary  : 'A module for merging hierarchies using the C3 algorithm'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Algorithm-C3-man

%description
NAME
Algorithm::C3 - A module for merging hierarchies using the C3 algorithm
SYNOPSIS
use Algorithm::C3;

%package man
Summary: man components for the perl-Algorithm-C3 package.
Group: Default

%description man
man components for the perl-Algorithm-C3 package.


%prep
%setup -q -n Algorithm-C3-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Algorithm/C3.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::C3.3
