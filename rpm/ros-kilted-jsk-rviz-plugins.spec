%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/kilted/.*$
%global __requires_exclude_from ^/opt/ros/kilted/.*$

%global __cmake_in_source_build 1

Name:           ros-kilted-jsk-rviz-plugins
Version:        3.0.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS jsk_rviz_plugins package

License:        BSD-3-Clause and OFL-1.1 and CC-BY-SA-3.0 and CC-BY-4.0
URL:            https://jsk-visualization.readthedocs.io/en/latest/jsk_rviz_plugins/index.html
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-scipy
Requires:       qt5-qtbase-devel
Requires:       ros-kilted-action-msgs
Requires:       ros-kilted-ament-index-cpp
Requires:       ros-kilted-ament-index-python
Requires:       ros-kilted-cv-bridge
Requires:       ros-kilted-diagnostic-msgs
Requires:       ros-kilted-geometry-msgs
Requires:       ros-kilted-image-publisher
Requires:       ros-kilted-image-transport
Requires:       ros-kilted-jsk-footstep-msgs
Requires:       ros-kilted-jsk-gui-msgs
Requires:       ros-kilted-jsk-hark-msgs
Requires:       ros-kilted-jsk-recognition-msgs
Requires:       ros-kilted-jsk-recognition-utils
Requires:       ros-kilted-jsk-ros1-ros2-compat
Requires:       ros-kilted-launch
Requires:       ros-kilted-launch-ros
Requires:       ros-kilted-pluginlib
Requires:       ros-kilted-rclcpp
Requires:       ros-kilted-resource-retriever
Requires:       ros-kilted-rosidl-default-runtime
Requires:       ros-kilted-rviz-common
Requires:       ros-kilted-rviz-default-plugins
Requires:       ros-kilted-rviz-ogre-vendor
Requires:       ros-kilted-rviz-rendering
Requires:       ros-kilted-rviz2
Requires:       ros-kilted-sensor-msgs
Requires:       ros-kilted-std-msgs
Requires:       ros-kilted-std-srvs
Requires:       ros-kilted-visualization-msgs
Requires:       ros-kilted-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  eigen3-devel
BuildRequires:  opencv-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-kilted-action-msgs
BuildRequires:  ros-kilted-ament-cmake
BuildRequires:  ros-kilted-ament-index-cpp
BuildRequires:  ros-kilted-cv-bridge
BuildRequires:  ros-kilted-diagnostic-msgs
BuildRequires:  ros-kilted-geometry-msgs
BuildRequires:  ros-kilted-image-transport
BuildRequires:  ros-kilted-jsk-footstep-msgs
BuildRequires:  ros-kilted-jsk-gui-msgs
BuildRequires:  ros-kilted-jsk-hark-msgs
BuildRequires:  ros-kilted-jsk-recognition-msgs
BuildRequires:  ros-kilted-jsk-recognition-utils
BuildRequires:  ros-kilted-jsk-ros1-ros2-compat
BuildRequires:  ros-kilted-pluginlib
BuildRequires:  ros-kilted-rclcpp
BuildRequires:  ros-kilted-resource-retriever
BuildRequires:  ros-kilted-ros-environment
BuildRequires:  ros-kilted-rosidl-default-generators
BuildRequires:  ros-kilted-rviz-common
BuildRequires:  ros-kilted-rviz-default-plugins
BuildRequires:  ros-kilted-rviz-ogre-vendor
BuildRequires:  ros-kilted-rviz-rendering
BuildRequires:  ros-kilted-sensor-msgs
BuildRequires:  ros-kilted-std-msgs
BuildRequires:  ros-kilted-std-srvs
BuildRequires:  ros-kilted-visualization-msgs
BuildRequires:  ros-kilted-ros-workspace
BuildRequires:  ros-kilted-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-kilted-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-kilted-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-kilted-launch-testing
BuildRequires:  ros-kilted-launch-testing-ament-cmake
BuildRequires:  xorg-x11-server-Xvfb
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-kilted-rosidl-interface-packages(all)
%endif

%description
The jsk_rviz_plugins package

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/kilted" \
    -DAMENT_PREFIX_PATH="/opt/ros/kilted" \
    -DCMAKE_PREFIX_PATH="/opt/ros/kilted" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/kilted

%changelog
* Thu Nov 26 2026 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.0.2-1
- Autogenerated by Bloom

* Thu Nov 19 2026 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.0.1-1
- Autogenerated by Bloom

