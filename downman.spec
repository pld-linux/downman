Summary:	Download Manager is a suite of programs to download files
Summary(pl):	Download Manager jest zbiorem program�w do �ciagania plik�w
Name:		downman
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d9a4a9f9a958f88f43bf2a75d425a5da
Patch0:		%{name}-ac.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel
URL:		http://downman.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Download Manager is a suite of programs to download files.

%description -l pl
Download Manager jest zbiorem program�w do �ciagania plik�w.

%prep
%setup -q
%patch0 -p1

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