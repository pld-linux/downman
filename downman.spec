Summary:	Download Manager is a suite of programs to download files
Summary(pl):	Download Manager jest zbiorem programów do ¶ci±gania plików
Name:		downman
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4c60ea7bc1375199a8dcbb937124680b
URL:		http://downman.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Download Manager is a suite of programs to download files.

%description -l pl
Download Manager jest zbiorem programów do ¶ci±gania plików.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gdownman
%{_desktopdir}/*
%{_pixmapsdir}/*
