Name:           ros-hydro-jsk-rviz-plugins
Version:        1.0.18
Release:        0%{?dist}
Summary:        ROS jsk_rviz_plugins package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-image-geometry
Requires:       ros-hydro-jsk-footstep-msgs
Requires:       ros-hydro-jsk-gui-msgs
Requires:       ros-hydro-jsk-hark-msgs
Requires:       ros-hydro-jsk-pcl-ros
Requires:       ros-hydro-jsk-recognition-msgs
Requires:       ros-hydro-jsk-topic-tools
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-people-msgs
Requires:       ros-hydro-roseus
Requires:       ros-hydro-rviz
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-urdfdom-py
Requires:       ros-hydro-view-controller-msgs
Requires:       wxGTK-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-image-geometry
BuildRequires:  ros-hydro-jsk-footstep-msgs
BuildRequires:  ros-hydro-jsk-gui-msgs
BuildRequires:  ros-hydro-jsk-hark-msgs
BuildRequires:  ros-hydro-jsk-pcl-ros
BuildRequires:  ros-hydro-jsk-recognition-msgs
BuildRequires:  ros-hydro-jsk-topic-tools
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-people-msgs
BuildRequires:  ros-hydro-rosbuild
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rviz
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-urdfdom-py
BuildRequires:  ros-hydro-view-controller-msgs
BuildRequires:  wxGTK-devel

%description
The jsk_rviz_plugins package

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
* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.18-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.17-0
- Autogenerated by Bloom

* Sun Jan 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.16-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.15-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.14-0
- Autogenerated by Bloom

