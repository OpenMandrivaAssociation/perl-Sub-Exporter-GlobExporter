%define upstream_name    Sub-Exporter-GlobExporter
%define upstream_version 0.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Export shared globs with Sub::Exporter collectors
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


