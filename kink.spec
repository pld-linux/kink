# TODO:
# - review by KDE specialist needed (BRs, dirs)
#
Summary:	KDE printer ink level utility monitor
Summary(pl):	Narzêdzie monitoruj±ce stan atramentu w drukarce dla KDE
Name:		kink
Version:	0.2.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kink/%{name}-%{version}.tar.bz2
# Source0-md5:	4a2341eb6d457e6a4b1409b45a673214
Patch0:		%{name}-compile_fix.patch
Patch1:		%{name}-desktop.patch
URL:		http://kink.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libinklevel-devel >= 0.6
BuildRequires:	kdelibs-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE frontend for libinklevel.

%description -l pl
Nak³adka graficzna na libinklevel dla KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}/kde
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/apps/kink
%{_datadir}/apps/kink/*.rc
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/apps/kink.png
