Name:           ros-indigo-jsk-interactive-test
Version:        1.0.25
Release:        0%{?dist}
Summary:        ROS jsk_interactive_test package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_interactive_test
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-jsk-interactive
Requires:       ros-indigo-jsk-interactive-marker
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rviz
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-jsk-interactive
BuildRequires:  ros-indigo-jsk-interactive-marker
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-rosbuild
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-visualization-msgs

%description
jsk_interactive_test

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Oct 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.25-0
- Autogenerated by Bloom

* Tue Sep 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.24-0
- Autogenerated by Bloom

* Wed Jul 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.23-0
- Autogenerated by Bloom

* Wed Jun 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.22-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.21-1
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.21-0
- Autogenerated by Bloom

* Mon May 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.18-1
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.18-0
- Autogenerated by Bloom

