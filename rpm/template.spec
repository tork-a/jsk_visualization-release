Name:           ros-kinetic-jsk-rqt-plugins
Version:        2.1.0
Release:        3%{?dist}
Summary:        ROS jsk_rqt_plugins package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-urlgrabber
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-image-view2
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-qt-gui-py-common
Requires:       ros-kinetic-resource-retriever
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-rqt-image-view
Requires:       ros-kinetic-rqt-plot
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-image-view2
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-rosbuild

%description
The jsk_rqt_plugins package

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
* Mon Feb 13 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.1.0-3
- Autogenerated by Bloom

