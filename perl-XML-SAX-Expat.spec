#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-SAX-Expat
Version  : 0.51
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/XML-SAX-Expat-0.51.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/XML-SAX-Expat-0.51.tar.gz
Summary  : SAX Driver for Expat
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::NamespaceSupport)
BuildRequires : perl(XML::Parser)
BuildRequires : perl(XML::SAX)
BuildRequires : perl(XML::SAX::Base)

%description
XML::SAX::Expat
===============
See `perldoc Expat.pm`.

%package dev
Summary: dev components for the perl-XML-SAX-Expat package.
Group: Development
Provides: perl-XML-SAX-Expat-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-SAX-Expat package.


%prep
%setup -q -n XML-SAX-Expat-0.51

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
/usr/lib/perl5/vendor_perl/5.28.1XML/SAX/Expat.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::SAX::Expat.3
