#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Cairo-GObject
Summary:	Perl Cairo-GObject bindings
Summary(pl.UTF-8):	Wiązania Cairo-GObject dla Perla
Name:		perl-Cairo-GObject
Version:	1.001
# set real perl-Cairo version and bump to 0.1 when compatible perl-Cairo is released
Release:	4
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	7e126a3424d9eab91b006b2a7ce09cb8
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	cairo-gobject-devel >= 1.10.0
BuildRequires:	perl-Cairo >= 1.080
BuildRequires:	perl-Glib-devel >= 1.224
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	cairo-gobject >= 1.10.0
Requires:	perl-Cairo >= 1.080
Requires:	perl-Glib >= 1.224
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl access to Cairo-GObject library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki Cairo-GObject.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Cairo/GObject/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorarch}/Cairo/GObject.pm
%dir %{perl_vendorarch}/Cairo/GObject
%{perl_vendorarch}/Cairo/GObject/Install
%dir %{perl_vendorarch}/auto/Cairo/GObject
%attr(755,root,root) %{perl_vendorarch}/auto/Cairo/GObject/GObject.so
%{_mandir}/man3/Cairo::GObject.3pm*
