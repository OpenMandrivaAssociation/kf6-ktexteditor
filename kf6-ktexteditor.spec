%define libname %mklibname KF6TextEditor
%define devname %mklibname KF6TextEditor -d
%define git 20230707

Name: kf6-ktexteditor
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/ktexteditor/-/archive/master/ktexteditor-master.tar.bz2#/ktexteditor-%{git}.tar.bz2
Summary: Full text editor component
URL: https://invent.kde.org/frameworks/ktexteditor
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6Auth)
Requires: %{libname} = %{EVRD}

%description
Full text editor component

%package -n %{libname}
Summary: Full text editor component
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Full text editor component

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Full text editor component

%prep
%autosetup -p1 -n ktexteditor-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/ktexteditor.*
%{_datadir}/dbus-1/system-services/org.kde.ktexteditor.katetextbuffer.service
%{_datadir}/dbus-1/system.d/org.kde.ktexteditor.katetextbuffer.conf
%{_datadir}/katepart5
%{_datadir}/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy

%files -n %{devname}
%{_includedir}/KF6/KTextEditor
%{_libdir}/cmake/KF6TextEditor
%{_qtdir}/mkspecs/modules/qt_KTextEditor.pri
%{_qtdir}/doc/KF6TextEditor.*
%{_datadir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2

%files -n %{libname}
%{_libdir}/libKF6TextEditor.so*
%{_libdir}/libexec/kauth/kauth_ktexteditor_helper
%{_qtdir}/plugins/kf6/parts/katepart.so
