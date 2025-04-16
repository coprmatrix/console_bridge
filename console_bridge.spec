%global srcname console_bridge

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

%package  devel
Summary: %{summary} (devel package)
Requires:  lib%{name}%{so_name}
Provides:  pkgconfig(%{srcname}) = %{version}

%description
A ROS-independent package for logging that seamlessly pipes into
rosconsole/rosout for ROS-dependent packages.

%description devel
A ROS-independent developlemnt library

%prep
%setup -qn %{srcname}-%{version}

%build
%cmake -DUSE_GNU_INSTALL_DIRS=ON
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig  -n %{name}
%postun -p /sbin/ldconfig -n %{name}


%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{srcname}

%changelog
