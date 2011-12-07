Summary:	Simple application to control the JACK server
Summary(pl.UTF-8):	Prosty program do kontrolowania serwera JACK-a
Name:		qjackctl
Version:	0.3.8
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
# Source0-md5:	8a0992c01e50d8be22064ab7b08fbc78
Source1:	%{name}.desktop
Patch0:		%{name}-qt4.patch
Patch1:		%{name}-locale.patch
URL:		http://qjackctl.sourceforge.net
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel >= 0.118.3
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= 4.3.3-3
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
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}

%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/qjackctl.1*
