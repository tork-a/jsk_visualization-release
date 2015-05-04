Name:           ros-hydro-jsk-interactive
Version:        1.0.20
Release:        0%{?dist}
Summary:        ROS jsk_interactive package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_interactive
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-dynamic-tf-publisher
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-jsk-interactive-marker
Requires:       ros-hydro-rospy
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-dynamic-tf-publisher
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-jsk-interactive-marker
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-rosbuild
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-visualization-msgs

%description
jsk_interactive

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon May 04 2015 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.19-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.18-1
- Autogenerated by Bloom

* Fri Jan 30 2015 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.18-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.17-0
- Autogenerated by Bloom

* Sun Jan 04 2015 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.16-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.15-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Yusuke Furuta <furua@jsk.imi.i.u-tokyo.ac.jp> - 1.0.14-0
- Autogenerated by Bloom

