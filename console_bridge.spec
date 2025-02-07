#
# spec file for package console_bridge
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global srcname console_bridge
%global so_name 1_0

Name:           %{srcname}
Version:        0.4.4
Release:        0
Summary:        A ROS-independent package for logging
License:        BSD-3-Clause
Group:          Development/Libraries
Url:            http://ros.org/wiki/%{srcname}
Source:         %{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
#Requires:       %{name}%{so_name}

%package -n lib%{name}%{so_name}
Summary: %{summary} (runtime package)
Provides: lib%{name} = %{version}-%{release}

%package  -n lib%{name}-devel
Summary: %{summary} (devel package)
Requires:  lib%{name}%{so_name}
Provides:  pkgconfig(%{srcname}) = %{version}

%description 
A ROS-independent package for logging that seamlessly pipes into
rosconsole/rosout for ROS-dependent packages.

%description -n lib%{name}%{so_name}
A ROS-independent runtime library

%description  -n lib%{name}-devel
A ROS-independent developlemnt library

%prep
%setup -qn %{srcname}-%{version}

%build
%cmake .. -DUSE_GNU_INSTALL_DIRS=ON
make %{?_smp_mflags}

%install
make -C build install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig  -n lib%{name}%{so_name}
%postun -p /sbin/ldconfig -n lib%{name}%{so_name}

%files

%files -n lib%{name}%{so_name}
%{_libdir}/*.so.*

%files  -n lib%{name}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{srcname}

%changelog