Name:           ros-melodic-jsk-interactive
Version:        2.1.5
Release:        0%{?dist}
Summary:        ROS jsk_interactive package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_interactive
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-dynamic-tf-publisher
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-jsk-interactive-marker
Requires:       ros-melodic-rospy
Requires:       ros-melodic-visualization-msgs
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamic-tf-publisher
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-jsk-interactive-marker
BuildRequires:  ros-melodic-mk
BuildRequires:  ros-melodic-rosbuild
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-visualization-msgs

%description
jsk_interactive

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Feb 18 2019 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 2.1.5-0
- Autogenerated by Bloom

