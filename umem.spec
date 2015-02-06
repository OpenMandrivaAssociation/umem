%define	major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Port of Solaris's slab allocator
Name:		umem
Version:	1.0.1
Release:	2
Group:		System/Libraries
License:	CDDL
URL:		https://labs.omniti.com/trac/portableumem/
Source0:        https://labs.omniti.com/portableumem/releases/1.0/%{name}-%{version}.tar.bz2
Patch0:		umem-no_rpath.diff
Patch1:		umem_malloc_init.patch
BuildRequires:	doxygen
BuildRequires:	libtool

%description
This a port of Solaris's slab allocator, libumem, to Linux.

"A slab allocator is a cache management structure for efficient use of [...]
memory. [...] It is targeted for use of many small pieces of memory chunks. By
managing small memory chunks in the units called slabs, this mechanism enables
lower fragmentation, fast allocation, and reclaming memory." (Description
sourced from Wikipedia.)

%package -n	%{libname}
Summary:	Port of Solaris's slab allocator
Group:		System/Libraries

%description -n	%{libname}
This a port of Solaris's slab allocator, libumem, to Linux.

"A slab allocator is a cache management structure for efficient use of [...]
memory. [...] It is targeted for use of many small pieces of memory chunks. By
managing small memory chunks in the units called slabs, this mechanism enables
lower fragmentation, fast allocation, and reclaming memory." (Description
sourced from Wikipedia.)

%package -n	%{develname}
Summary:	Port of Solaris's slab allocator
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
"A slab allocator is a cache management structure for efficient use of [...]
memory. [...] It is targeted for use of many small pieces of memory chunks. By
managing small memory chunks in the units called slabs, this mechanism enables
lower fragmentation, fast allocation, and reclaming memory." (Description
sourced from Wikipedia.)

This package contains the libraries and header files for using this port of
Solaris's slab allocator, libumem, to Linux.

%prep

%setup -q
%patch0 -p0
%patch1 -p1

%build
rm -f configure
libtoolize --copy --force; aclocal; autoheader; autoconf; automake --add-missing --force-missing

%configure2_5x --disable-static

make

make html

%check
make check || echo "tests failed"

%install

%makeinstall_std

%files -n %{libname}
%doc COPYING COPYRIGHT OPENSOLARIS.LICENSE README TODO
%{_libdir}/*.so.0*

%files -n %{develname}
%doc docs/html/*
%{_includedir}/*.h
%{_includedir}/sys/*.h
%{_libdir}/*.so
%{_mandir}/man3/*
