Name: htop
Version: 2.0.1
Release: 5%{?dist}
Summary: Interactive process viewer
Group: Applications/System
License: GPL+
URL: http://hisham.hm/htop/
Source0: package.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: ncurses-devel
BuildRequires: python
BuildRequires: libtool

%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%prep
%setup -q
sed -i s#"INSTALL_DATA = @INSTALL_DATA@"#"INSTALL_DATA = @INSTALL_DATA@ -p"# Makefile.in

%build
autoreconf -v -f -i

%configure \
	--enable-openvz \
	--enable-vserver \
	--enable-taskstats \
	--enable-unicode \
	--enable-native-affinity \
	--enable-cgroup \
	--enable-oom

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#remove empty direcories
rm -rf $RPM_BUILD_ROOT%{libdir}
rm -rf $RPM_BUILD_ROOT%{includedir}

# remove desktop file
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/htop
%{_datadir}/pixmaps/htop.png
%{_mandir}/man1/htop.1*

%changelog
* Thu Mar 24 2016 Timofey Kirillov <timofey.kirillov@flant.com> - 2.0.1-4
- Test release for buildizer

* Fri Mar 18 2016 Timofey Kirillov <timofey.kirillov@flant.com> - 2.0.1-1
- Test release for buildizer
