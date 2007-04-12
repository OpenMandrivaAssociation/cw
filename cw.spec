Name:           cw
Version:        1.0.14
Release:        %mkrel 3
Epoch:          0
Summary:        Non-intrusive real-time ANSI color wrapper for common Unix-based commands
URL:            http://cwrapper.sourceforge.net/
Source0:        http://cwrapper.sourceforge.net/cw-%{version}.tar.bz2
Patch0:         cw-1.0.14-build.patch
License:        GPL
Group:          Development/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
cw is a non-intrusive real-time ANSI color wrapper for common Unix-based 
commands on GNU/linux. cw is designed to simulate the environment of the 
commands being executed, so that if a person types 'du', 'df', 'ping', 
etc. in their shell it will automatically color the output in real-time 
according to a definition file containing the color format desired. cw 
has support for wildcard match coloring, tokenized coloring, 
headers/footers, case scenario coloring, command line dependent 
definition coloring, and includes over 50 pre-made definition files.

%prep
%setup -q
%patch0 -p1 -b .build

%build
%configure
%make LIBDIR=%{_datadir}

%install
%{__rm} -rf %{buildroot}
%makeinstall_std LIBDIR=%{_datadir}

%{__perl} -pi -e 's|CWLIB=.*|CWLIB="%{_datadir}/%{name}"|g' %{buildroot}%{_bindir}/colorcfg
%{__perl} -pi -e 's|%{buildroot}||g' %{buildroot}%{_datadir}/%{name}/*
%{__perl} -pi -e 's|/usr/local/lib|%{_datadir}|g' README

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTRIB COPYING cw.lsm FILES INSTALL MD5SUM PLATFORM README 
%doc VERSION doc
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*


