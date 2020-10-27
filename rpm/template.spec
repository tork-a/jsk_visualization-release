%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-jsk-interactive-marker
Version:        2.1.7
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS jsk_interactive_marker package

License:        BSD
URL:            http://ros.org/wiki/interactive_marker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-dynamic-tf-publisher
Requires:       ros-noetic-eigen-conversions
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-interactive-markers
Requires:       ros-noetic-jsk-footstep-msgs
Requires:       ros-noetic-jsk-recognition-msgs >= 1.0.0
Requires:       ros-noetic-jsk-recognition-utils
Requires:       ros-noetic-jsk-rviz-plugins
Requires:       ros-noetic-jsk-topic-tools
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-moveit-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rviz
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf-conversions
Requires:       ros-noetic-urdf
Requires:       ros-noetic-visualization-msgs
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-dynamic-tf-publisher
BuildRequires:  ros-noetic-eigen-conversions
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-interactive-markers
BuildRequires:  ros-noetic-jsk-footstep-msgs
BuildRequires:  ros-noetic-jsk-recognition-msgs >= 1.2.0
BuildRequires:  ros-noetic-jsk-recognition-utils
BuildRequires:  ros-noetic-jsk-rviz-plugins
BuildRequires:  ros-noetic-jsk-topic-tools
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-mk
BuildRequires:  ros-noetic-moveit-msgs
BuildRequires:  ros-noetic-rosbuild
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-rviz
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf-conversions
BuildRequires:  ros-noetic-urdf
BuildRequires:  ros-noetic-visualization-msgs
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
jsk interactive markers

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Oct 27 2020 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.1.7-4
- Autogenerated by Bloom

