%define		php_name	php%{?php_suffix}
%define		modname		html_parse
%define		status		stable
Summary:	%{modname} - HTML parser extension
Summary(pl.UTF-8):	%{modname} - parser HTML
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.0
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	d19772cb926d775313af0fda207e2a90
URL:		http://pecl.php.net/package/html_parse/
BuildRequires:	%{php_name}-devel >= 4:5.0.4
BuildRequires:	ekhtml-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML parser extension based on the ekhtml library
<http://ekhtml.sourceforge.net/>.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Parser HTML bazowany na bibliotece ekhtml
<http://ekhtml.sourceforge.net/>.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
