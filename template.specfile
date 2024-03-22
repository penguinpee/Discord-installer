%global         debug_package   %{nil}
%global         lowercase_name  [lowercase_name]

Name:           [name]
Epoch:          1
Version:        [version]
Release:        1
Summary:        It's time to ditch Skype and TeamSpeak

License:        Custom
URL:            https://discordapp.com/
Source0:        [url]#/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64
Requires:       Discord-installer
Requires:       glibc
Requires:       libappindicator.so.1()(64bit)
Requires:       libasound.so.2()(64bit)
Requires:       libatomic.so.1()(64bit)
Requires:       libc++.so.1()(64bit)
Requires:       libgconf-2.so.4()(64bit)
Requires:       libnotify.so.4()(64bit)
Requires:       libnspr4.so()(64bit)
Requires:       libnss3.so()(64bit)
Requires:       libstdc++.so.6()(64bit)
Requires:       libXss.so.1()(64bit)
Requires:       libXtst.so.6()(64bit)
AutoReqProv:    no

%description
All-in-one voice and text chat for gamers that's free, secure, and works on both
your desktop and phone. Stop paying for TeamSpeak servers and hassling with
Skype. Simplify your life.


%prep
%autosetup -n %{name}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/{%{lowercase_name},applications,pixmaps}
cp -R $RPM_BUILD_DIR/%{name}/* $RPM_BUILD_ROOT/%{_datadir}/%{lowercase_name}
cp $RPM_BUILD_DIR/%{name}/*.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{lowercase_name}.png
cp $RPM_BUILD_DIR/%{name}/*.desktop $RPM_BUILD_ROOT/%{_datadir}/applications
rm $RPM_BUILD_ROOT/%{_datadir}/%{lowercase_name}/postinst.sh
ln -s %{_datadir}/%{lowercase_name}/%{name} $RPM_BUILD_ROOT/%{_bindir}


%files
%{_bindir}/%{name}
%attr(0755, root, root) %{_datadir}/%{lowercase_name}/%{name}
%{_datadir}/%{lowercase_name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
