%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	PHP_CodeCoverage
Summary:	%{pearname} - Library that provides collection, processing, and rendering functionality for PHP code coverage information
Name:		php-phpunit-PHP_CodeCoverage
Version:	1.0.4
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	c745b86a2eb43c06a52b813e0553c8ee
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-File_Iterator >= 1.2.2
Requires:	php-phpunit-PHP_TokenStream >= 1.0.0
Requires:	php-phpunit-Text_Template >= 1.0.0
Suggests:	php-dom
Suggests:	php-ezc-ConsoleTools >= 1.6
Suggests:	php-pecl-xdebug
Suggests:	php-reflection
Suggests:	php-spl
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
install -p usr/bin/* $RPM_BUILD_ROOT%{_bindir}

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/phpcov
%{php_pear_dir}/PHP/CodeCoverage.php
%{php_pear_dir}/PHP/CodeCoverage
