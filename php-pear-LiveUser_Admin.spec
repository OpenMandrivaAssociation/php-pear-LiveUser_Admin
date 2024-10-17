%define		_class		LiveUser
%define		_subclass	Admin
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.9
Release:	11
Summary:	User authentication and permission management framework
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/LiveUser_Admin/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
LiveUser_Admin is meant to be used with the LiveUser package. It is
composed of all the classes necessary to administrate data used by
LiveUser.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/*.txt
%doc %{upstream_name}-%{version}/docs/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-9mdv2012.0
+ Revision: 742030
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-8
+ Revision: 679383
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-7mdv2011.0
+ Revision: 613699
- the mass rebuild of 2010.1 packages

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.9-6mdv2010.1
+ Revision: 473553
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.9-5mdv2010.0
+ Revision: 441253
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-4mdv2009.1
+ Revision: 322273
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-3mdv2009.0
+ Revision: 236906
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-2mdv2008.0
+ Revision: 53917
- put the files where they belong to fix deps

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-1mdv2008.0
+ Revision: 15683
- 0.3.9


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.8-2mdv2007.1
+ Revision: 144929
- revert to 0.3.8 due to version freeze
- 0.3.9
- package some forgotten files

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.8-1mdv2007.0
+ Revision: 81995
- Import php-pear-LiveUser_Admin

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.8-1mdk
- 0.3.8

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-1mdk
- 0.3.6
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdk
- initial Mandriva package (PLD import)

