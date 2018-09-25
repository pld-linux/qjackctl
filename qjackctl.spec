Summary:	Simple application to control the JACK server
Summary(pl.UTF-8):	Prosty program do kontrolowania serwera JACK-a
Name:		qjackctl
Version:	0.5.4
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
# Source0-md5:	3c1f8dfeb03f3ea45f9e0e14e60e05e0
Source1:	%{name}.desktop
URL:		http://qjackctl.sourceforge.net
BuildRequires:	Qt5Core-devel >= 5.1
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel >= 0.118.3
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake >= 5.1
BuildRequires:	sed >= 4.0
Provides:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qjackctl is a Qt application to control the JACK sound server.
Provides a simple GUI dialog for setting several JACK parameters.

%description -l pl.UTF-8
Qjackctl to program pozwalający kontrolować serwer dźwięku JACK-a.
Posiada proste GUI dla ustawiania poszczególnych parametrów JACK-a.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure \
	--with-qt5=%{_libdir}/qt5

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/fr/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-qm

mv $RPM_BUILD_ROOT%{_mandir}/man1/qjackctl.fr.1.gz $RPM_BUILD_ROOT%{_mandir}/fr/man1/qjackctl.1.gz1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/qjackctl.1*
%lang(fr) %{_mandir}/fr/man1/qjackctl.1*
%{_datadir}/metainfo/%{name}.appdata.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
