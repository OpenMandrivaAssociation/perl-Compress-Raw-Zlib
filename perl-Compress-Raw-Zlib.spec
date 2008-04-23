%define	module	Compress-Raw-Zlib
%define	name	perl-%{module}
%define	version	2.009
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Low-Level Interface to zlib compression library
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Low-Level Interface to zlib compression library.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress



