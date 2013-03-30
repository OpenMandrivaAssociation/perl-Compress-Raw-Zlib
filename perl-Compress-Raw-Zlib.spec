%define	modname	Compress-Raw-Zlib
%define	modver	2.060

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Low-Level Interface to zlib compression library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	pkgconfig(zlib)

%description
Low-Level Interface to zlib compression library.

%prep
%setup -q -n %{modname}-%{modver}

%build
BUILD_ZLIB=False perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.59.0-1
- build against system zlib
- cleanups
- new version

* Tue Mar 13 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.49.0-1
+ Revision: 784852
- new version
- clean out spec

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-4
+ Revision: 765105
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-3
+ Revision: 763562
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-2
+ Revision: 763234
- force it
- rebuild

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.37.0-1
+ Revision: 686970
- update to new version 2.037

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.35.0-1
+ Revision: 672607
- update to new version 2.035

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.33.0-2
+ Revision: 657124
- rebuild

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.33.0-1
+ Revision: 634215
- update to new version 2.033

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 629479
- update to new version 2.032

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-4mdv2011.0
+ Revision: 597092
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-3mdv2011.0
+ Revision: 562440
- rebuild

* Mon Jul 26 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 560761
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2.030

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-2mdv2011.0
+ Revision: 555699
- rebuild

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-1mdv2010.1
+ Revision: 539068
- update to 2.027

* Thu Apr 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.26.0-1mdv2010.1
+ Revision: 533043
- update to 2.026

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 2.25.0-1mdv2010.1
+ Revision: 528755
- update to 2.025

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 2.24.0-1mdv2010.1
+ Revision: 488598
- update to 2.024

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.23.0-1mdv2010.1
+ Revision: 464024
- update to 2.023

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.21.0-1mdv2010.0
+ Revision: 422797
- update to 2.021

* Fri Jun 05 2009 Olivier Thauvin <nanardon@mandriva.org> 2.020-1mdv2010.0
+ Revision: 383073
- 2.020
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.019-1mdv2010.0
+ Revision: 371906
- update to new version 2.019

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.015-2mdv2009.1
+ Revision: 351689
- rebuild

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.015-1mdv2009.0
+ Revision: 281100
- update to new version 2.015

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.012-1mdv2009.0
+ Revision: 236262
- update to new version 2.012

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.011-1mdv2009.0
+ Revision: 209321
- update to new version 2.011

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.010-1mdv2009.0
+ Revision: 201846
- update to new version 2.010

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.009-1mdv2009.0
+ Revision: 196821
- update to new version 2.009
- update to new version 2.009

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.008-2mdv2008.1
+ Revision: 151353
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.008-1mdv2008.1
+ Revision: 107972
- update to new version 2.008

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.006-1mdv2008.0
+ Revision: 78094
- update to new version 2.006

* Thu Jul 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.005-1mdv2008.0
+ Revision: 48383
- 2.005


* Mon Mar 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.004-1mdv2007.0
+ Revision: 132887
- 2.004

* Sat Jan 06 2007 Olivier Thauvin <nanardon@mandriva.org> 2.003-1mdv2007.1
+ Revision: 104828
- 2.003

* Mon Nov 13 2006 Olivier Thauvin <nanardon@mandriva.org> 2.001-1mdv2007.1
+ Revision: 83896
- first mdv rpm
- Create perl-Compress-Raw-Zlib

