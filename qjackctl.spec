Summary:	Simple application to control the JACK server
Summary(pl):	Prosty program do kontrolowania serwera JACKa
Name:		qjackctl
Version:	0.1.1a
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
# Source0-md5:	a579439847f35c368d285702ff7539b0
Source1:	%{name}.desktop
Patch0:		%{name}-build_fixes.patch
URL:		http://qjackctl.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	qt-devel >= 3.1.1
Provides:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qjackctl is a Qt application to control the JACK sound server.
Provides a simple GUI dialog for setting several JACK parameters.

%description -l pl
Qjackctl to program pozwalaj±cy kontrolowaæ serwer d¼wiêku JACKa.
Posiada proste GUI dla ustawiania poszczególnych parametrów JACKa.

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}

export QTDIR=%{_prefix}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}.xpm
