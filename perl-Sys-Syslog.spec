%{?scl:%scl_package perl-Sys-Syslog}

Name:           %{?scl_prefix}perl-Sys-Syslog
Version:        0.34
Release:        5%{?dist}
Summary:        Perl interface to the UNIX syslog(3) calls
# README:               GPL+ or Artistic
# ppport.h:             GPL+ or Artistic
# Syslog.pm:            GPL+ or Artistic
## Unbundled
# fallback/syslog.h:    BSD
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-Syslog/
Source0:        http://www.cpan.org/authors/id/S/SA/SAPER/Sys-Syslog-%{version}.tar.gz
# Avoid loading optional modules from default . (CVE-2016-1238)
Patch0:         Sys-Syslog-0.34-CVE-2016-1238-avoid-loading-optional-modules-from.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Constant)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(warnings::register)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# DynaLoader not used
# Tests:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::Distribution)
BuildRequires:  %{?scl_prefix}perl(Test::NoWarnings)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.14
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.06
BuildRequires:  %{?scl_prefix}perl(Test::Portability::Files)
# POE::Component::Server::Syslog is not packaged yet
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Fcntl)
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}

%description
Sys::Syslog is an interface to the UNIX syslog(3) function. Call syslog() with
a string priority and a list of printf() arguments just like at syslog(3).

%prep
%setup -q -n Sys-Syslog-%{version}
%patch0 -p1

chmod -x eg/*
# Inhibit bundled syslog.h
rm -rf fallback
sed -i -e '/^fallback\//d' MANIFEST
# Recode files
for F in Changes; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" >"${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes eg README 
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-5
- Avoid loading optional modules from default . (CVE-2016-1238)

* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 0.34-4
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.24 rebuild

* Fri May 06 2016 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-312
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.33-2
- Perl 5.18 rebuild

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Tue Apr 09 2013 Petr Pisar <ppisar@redhat.com> 0.32-1
- Specfile autogenerated by cpanspec 1.78.
