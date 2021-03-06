Summary:	Check-0.12.0
Name:		check
Version:	0.14.0
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://check.sourceforge.net/
Source0:	https://github.com/libcheck/check/archive/%{name}-%{version}.tar.gz
%define sha1 check=f88dec20faa3ffb81b539242687f2504032fdea4
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: Photon
Requires:       gawk
%description
Check is a unit testing framework for C. It features a simple interface for defining unit tests,
putting little in the way of the developer. Tests are run in a separate address space,
so both assertion failures and code errors that cause segmentation faults or other signals can be caught.
%prep
%setup -q
%build
autoreconf --install
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete
rm %{buildroot}%{_infodir}/dir

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*so*
%exclude %{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_mandir}/man1/*
%{_infodir}/*
/usr/share/doc/%{name}/*
/usr/share/aclocal/*
%changelog
*   Wed Jul 08 2020 Gerrit Photon <photon-checkins@vmware.com> 0.14.0-1
-   Automatic Version Bump
*   Thu Nov 08 2018 Alexey Makhalov <amakhalov@vmware.com> 0.12.0-2
-   Cross compilation support
-   Added required gawk
*   Wed Sep 19 2018 Ajay Kaher <akaher@vmware.com> 0.12.0-1
-   Upgraded to version 0.12.0
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.10.0-2
-   GA - Bump release of all rpms
*   Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 0.10.0-1
-   Updated to version 0.10.0
*   Wed May 20 2015 Touseef Liaqat <tliaqat@vmware.com> 0.9.14-2
-   Updated group.
*   Tue Nov 25 2014 Divya Thaluru <dthaluru@vmware.com> 0.9.14-1
-   Initial build. First version
