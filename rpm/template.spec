Name:           ros-hydro-jsk-rqt-plugins
Version:        1.0.15
Release:        0%{?dist}
Summary:        ROS jsk_rqt_plugins package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-qt-gui-py-common
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
Requires:       ros-hydro-rqt-plot
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-rosbuild

%description
The jsk_rqt_plugins package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Dec 21 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.15-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.14-0
- Autogenerated by Bloom

