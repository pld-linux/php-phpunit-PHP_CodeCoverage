%define		status		stable
%define		pearname	PHP_CodeCoverage
Summary:	%{pearname} - Library that provides collection, processing, and rendering functionality for PHP code coverage information
Name:		php-phpunit-PHP_CodeCoverage
Version:	1.2.17
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	9512f9398319e735e1bf61b19dd6811c
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-File_Iterator >= 1.3.0
Requires:	php-phpunit-PHP_TokenStream >= 1.1.3
Requires:	php-phpunit-Text_Template >= 1.1.1
Suggests:	php(dom)
Suggests:	php(reflection)
Suggests:	php(spl)
Suggests:	php(xdebug)
Suggests:	php-ezc-ConsoleTools >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library that provides collection, processing, and rendering
functionality for PHP code coverage information.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/PHP_CodeCoverage/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PHP/CodeCoverage.php
%{php_pear_dir}/PHP/CodeCoverage
