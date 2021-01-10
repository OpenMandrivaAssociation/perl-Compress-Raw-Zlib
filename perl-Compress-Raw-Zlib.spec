%define	modname	Compress-Raw-Zlib
%define upstream_version 2.100

Summary:	Low-Level Interface to zlib compression library
Name:		perl-%{modname}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{modname}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(zlib)

%description
Low-Level Interface to zlib compression library.

%prep
%setup -qn %{modname}-%{upstream_version}
# Leaving the unused zlib source in the tree causes its zlib.h to be preferred
# over the system version we want.
rm -rf zlib-src

%build
BUILD_ZLIB=False perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/man3/*
