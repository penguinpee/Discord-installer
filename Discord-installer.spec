Name:           Discord-installer
Version:        1.5.3
Release:        1%{?dist}
Summary:        Some systemd services to install Discord on Redhat based systems

%global forgeurl https://github.com/penguinpee/Discord-installer
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesrc

ExcludeArch:    %{ix86}
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
Requires:       coreutils
Requires:       curl
Requires:       dos2unix
Requires:       libnotify
Requires:       polkit
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       systemd
Obsoletes:      Discord         = 0:0.0.1
Obsoletes:      DiscordCanary   = 0:0.0.15

%description
Some systemd services to install Discord on Redhat based systems.


%prep
%forgeautosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%post
for p in Discord DiscordCanary
do
    if rpm -q $p &> /dev/null
    then
        touch %{_var}/lib/discord-installer-rebuild-$p
    else
        rm -f %{_var}/lib/discord-installer-rebuild-$p
    fi
done

%systemd_post discord-installer.service
%systemd_post discord-installer.timer
%systemd_post discord-canary-installer.service
%systemd_post discord-canary-installer.timer

if [[ $1 = 1 ]]
then
    systemctl enable --now --no-block discord-installer.service
    systemctl enable --now --no-block discord-installer.timer
fi


%preun
%systemd_preun discord-installer.service
%systemd_preun discord-installer.timer
%systemd_preun discord-canary-installer.service
%systemd_preun discord-canary-installer.timer


%files
%{_unitdir}/discord*
%{_libexecdir}/discord*
%{_datadir}/discord*



%changelog
* Mon Mar 24 2025 Sandro <devel@penguinpee.nl> - 1.5.3-1
- Improve script and spec file

* Sun Mar 23 2025 Sandro <devel@penguinpee.nl> - 1.5.2-2
- Update download URL
- Make package noarch and exclude i686

* Fri Mar 22 2024 Sandro <devel@penguinpee.nl> - 1.5.2-1
- Fix issue with special characters in URL being passed.
- Fix use of `uname`
- Some pedantic changes to build.sh
- Add Packit automation
- Update spec file

* Sat Feb 02 2019 Laurent Tréguier <laurent@treguier.org> - 1.5.1-1
- new version

* Tue Oct 30 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0-1
- new version

* Sat May 19 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.3-1
- new version

* Tue Apr 17 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.2-1
- new version

* Tue Apr 17 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.1-1
- new version

* Wed Jan 24 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.0-1
- new version

* Thu Aug 03 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.4-1
- new version

* Thu Aug 03 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.3-1
- new version

* Thu Aug 03 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.2-1
- new version

* Wed Aug 02 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1
- new version

* Mon Jul 31 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-1
- new version
- changed systemd build dependency to pkgconfig(systemd) to fix package on Mageia

* Wed Jul 19 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.2-1
- new version

* Sat Jul 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.1-1
- new version

* Sat Jul 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.0-1
- new version

* Fri Jul 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.1.0-2
- correctly fixed potential rebuilds issue

* Sat Jun 10 2017 Laurent Tréguier <laurent@treguier.org> - 1.1.0-1
- new version
- fixed unnecessary potential package rebuilds

* Fri Jun 09 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.2-3
- added forgotten curl dependency
- changed BuildArch to ExclusiveArch

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.2-2
- started using systemd_* macros
- fixed source archive named into [...].zip instead of .tar.gz

* Sat Apr 01 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.2-1
- new version

* Sat Apr 01 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.1-1
- new version

* Sat Apr  1 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.0-1
- created specfile
