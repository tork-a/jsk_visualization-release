Name:           ros-kinetic-jsk-interactive-marker
Version:        2.1.3
Release:        0%{?dist}
Summary:        ROS jsk_interactive_marker package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/interactive_marker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-dynamic-tf-publisher
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-interactive-markers
Requires:       ros-kinetic-jsk-footstep-msgs
Requires:       ros-kinetic-jsk-recognition-msgs >= 1.0.0
Requires:       ros-kinetic-jsk-rviz-plugins
Requires:       ros-kinetic-jsk-topic-tools
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-moveit-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roseus
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rviz
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf-conversions
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-visualization-msgs
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-dynamic-tf-publisher
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-interactive-markers
BuildRequires:  ros-kinetic-jsk-footstep-msgs
BuildRequires:  ros-kinetic-jsk-recognition-msgs >= 1.0.0
BuildRequires:  ros-kinetic-jsk-rviz-plugins
BuildRequires:  ros-kinetic-jsk-topic-tools
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-moveit-msgs
BuildRequires:  ros-kinetic-rosbuild
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roseus
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rviz
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf-conversions
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel

%description
jsk interactive markers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 18 2018 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.1.3-0
- Autogenerated by Bloom

* Wed Feb 15 2017 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Mon Feb 13 2017 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.1.0-3
- Autogenerated by Bloom

