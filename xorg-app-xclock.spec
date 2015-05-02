Summary:	xclock application - analog/digital clock for X
Summary(pl.UTF-8):	Aplikacja xclock - analogowy lub cyfrowy zegar dla X
Name:		xorg-app-xclock
Version:	1.0.7
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xclock-%{version}.tar.bz2
# Source0-md5:	6f150d063b20d08030b98c45b9bee7af
Source1:	xclock.desktop
Source2:	xclock.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xclock is the classic X Window System clock utility. It displays the
time in analog or digital form. The time is continuously updated at a
frequency which may be specified by the user.

%description -l pl.UTF-8
xclock to klasyczny zegar dla systemu X Window. Wyświetla czas w
postaci analogowej lub cyfrowej. Czas jest stale uaktualniany z
częstotliwością określoną przez użytkownika.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xclock
%{_datadir}/X11/app-defaults/XClock*
%{_desktopdir}/xclock.desktop
%{_pixmapsdir}/xclock.png
%{_mandir}/man1/xclock.1*
