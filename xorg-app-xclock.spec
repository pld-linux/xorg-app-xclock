Summary:	xclock application
Summary(pl.UTF-8):	Aplikacja xclock
Name:		xorg-app-xclock
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xclock-%{version}.tar.bz2
# Source0-md5:	2b1a3d030d87e62a591db8ee4c0072e6
Source1:	xclock.desktop
Source2:	xclock.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xclock appliaction.

%description -l pl.UTF-8
Aplikacja xclock.

%prep
%setup -q -n xclock-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xclock.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xclock.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xclock
%{_datadir}/X11/app-defaults/XClock*
%{_desktopdir}/xclock.desktop
%{_pixmapsdir}/xclock.png
%{_mandir}/man1/xclock.1x*
