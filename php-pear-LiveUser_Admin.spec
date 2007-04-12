%define		_class		LiveUser
%define		_subclass	Admin
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(LiveUser.php)

Summary:	%{_pearname} - user authentication and permission management framework
Name:		php-pear-%{_pearname}
Version:	0.3.8
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/LiveUser_Admin/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
LiveUser_Admin is meant to be used with the LiveUser package. It is
composed of all the classes necessary to administrate data used by
LiveUser.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}

install -d %{buildroot}%{_datadir}/pear/%{_class}/Auth/Storage
install -d %{buildroot}%{_datadir}/pear/%{_class}/Perm/Storage
install -d %{buildroot}%{_datadir}/pear/%{_class}/Storage

install -m0644 %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install -m0644 %{_pearname}-%{version}/Auth/*.php %{buildroot}%{_datadir}/pear/%{_class}/Auth/
install -m0644 %{_pearname}-%{version}/Auth/Storage/*.php %{buildroot}%{_datadir}/pear/%{_class}/Auth/Storage/
install -m0644 %{_pearname}-%{version}/Perm/*.php %{buildroot}%{_datadir}/pear/%{_class}/Perm/
install -m0644 %{_pearname}-%{version}/Perm/Storage/*.php %{buildroot}%{_datadir}/pear/%{_class}/Perm/Storage/
install -m0644 %{_pearname}-%{version}/Storage/*.php %{buildroot}%{_datadir}/pear/%{_class}/Storage/

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/examples/* %{_pearname}-%{version}/*.txt
%dir %{_datadir}/pear/%{_class}/Auth
%dir %{_datadir}/pear/%{_class}/Auth/Storage
%dir %{_datadir}/pear/%{_class}/Perm
%dir %{_datadir}/pear/%{_class}/Perm/Storage
%dir %{_datadir}/pear/%{_class}/Storage
%{_datadir}/pear/%{_class}/Auth/*.php
%{_datadir}/pear/%{_class}/Auth/Storage/*.php
%{_datadir}/pear/%{_class}/Perm/*.php
%{_datadir}/pear/%{_class}/Perm/Storage/*.php
%{_datadir}/pear/%{_class}/Storage/*.php
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


