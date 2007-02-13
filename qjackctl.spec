Summary:	Simple application to control the JACK server
Summary(pl.UTF-8):	Prosty program do kontrolowania serwera JACK-a
Name:		qjackctl
Version:	0.2.20
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
# Source0-md5:	04141b66ba0b06d8acc92fdd442192fe
Source1:	%{name}.desktop
URL:		http://qjackctl.sourceforge.net
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.1.1
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

export QTDIR=%{_prefix}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}.png
