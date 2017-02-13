Name:           ros-jade-jsk-interactive-marker
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS jsk_interactive_marker package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/interactive_marker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-dynamic-tf-publisher
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-interactive-markers
Requires:       ros-jade-jsk-footstep-msgs
Requires:       ros-jade-jsk-recognition-msgs >= 1.0.0
Requires:       ros-jade-jsk-rviz-plugins
Requires:       ros-jade-jsk-topic-tools
Requires:       ros-jade-message-filters
Requires:       ros-jade-message-runtime
Requires:       ros-jade-moveit-msgs
Requires:       ros-jade-pr2eus-moveit
Requires:       ros-jade-roscpp
Requires:       ros-jade-roseus
Requires:       ros-jade-roslib
Requires:       ros-jade-rviz
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
Requires:       ros-jade-urdf
Requires:       ros-jade-visualization-msgs
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-dynamic-tf-publisher
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-interactive-markers
BuildRequires:  ros-jade-jsk-footstep-msgs
BuildRequires:  ros-jade-jsk-recognition-msgs >= 1.0.0
BuildRequires:  ros-jade-jsk-rviz-plugins
BuildRequires:  ros-jade-jsk-topic-tools
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-moveit-msgs
BuildRequires:  ros-jade-pr2eus-moveit
BuildRequires:  ros-jade-rosbuild
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roseus
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rviz
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions
BuildRequires:  ros-jade-urdf
BuildRequires:  ros-jade-visualization-msgs
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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Feb 13 2017 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Thu Dec 15 2016 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Wed Dec 14 2016 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Thu Sep 29 2016 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.34-0
- Autogenerated by Bloom

* Wed Sep 21 2016 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

