%undefine _debugsource_packages
%define	modname	Compress-Raw-Zlib

Summary:	Low-Level Interface to zlib compression library
Name:		perl-%{modname}
Version:	2.204
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{modname}-%{version}.tar.gz
Patch0:		perl-Compress-Raw-Zlib-2.204-compile.patch
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(zlib)

%description
Low-Level Interface to zlib compression library.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Leaving the unused zlib source in the tree causes its zlib.h to be preferred
# over the system version we want.
rm -rf zlib-src

%build
BUILD_ZLIB=False perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc README Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/man3/*
