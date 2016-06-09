Name: fingerterm
Version:    1.1.21
Release: 1
Summary: A terminal emulator with a custom virtual keyboard
Group: System/Base
License: GPLv2
Source0: %{name}-%{version}.tar.gz
URL: https://git.merproject.org/mer-core/fingerterm
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt0Feedback)
BuildRequires: pkgconfig(nemonotifications-qt5) >= 1.0.4
Requires: qt5-qtdeclarative-import-xmllistmodel
Requires: qt5-qtdeclarative-import-window2

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*.desktop


%prep
%setup -q -n %{name}-%{version}


%build
sed -i 's,/opt/fingerterm/,/usr/,' fingerterm.pro
qmake -qt=5 MEEGO_EDITION=nemo CONFIG+=enable-feedback CONFIG+=enable-nemonotifications
# Inject version number from RPM into source
sed -i -e 's/PROGRAM_VERSION="[^"]*"/PROGRAM_VERSION="%{version}"/g' version.h
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install
%changelog
* Wed May 17 2016 Pekka Vuorela <pekka.vuorela@jollamobile.com> - 1.1.21
- [fingerterm] Set window size before showing it. Fixes JB#35253
* Wed May 11 2016 Pekka Vuorela <pekka.vuorela@jollamobile.com> - 1.1.20
- [fingerterm] Avoid most warnings on startup. Contributes to JB#35198
* Wed May  6 2016 Pekka Vuorela <pekka.vuorela@jollamobile.com> - 1.1.19
- [fingerterm] Fullscreen window by default. Fixes MER#1582
* Wed May  3 2016 Pekka Vuorela <pekka.vuorela@jollamobile.com> - 1.1.18
- [fingerterm] remove QtComponents dependency. Contributes to JB#10224
* Wed Oct 15 2015 Pekka Vuorela <pekka.vuorela@jollamobile.com> - 1.1.17
- [fingerterm] Cyrillic support and other keyboard fixes. Fixes MER#1372
* Wed Jun  3 2015 Thomas Perl <m@thp.io> - 1.1.16
- [terminal] Fix Terminal::keyPress() for non-ASCII chars (Fixes JB#28668)
* Tue Jun  2 2015 Thomas Perl <m@thp.io> - 1.1.15
- [util] Improve scrolling on high-DPI screens (Fixes JB#29417)
* Thu Mar 19 2015 Matt Vogt <matthew.vogt@jollamobile.com> - 1.1.14
- [fingerterm] Use libnemonotifications rather than MNotification
* Tue Feb 17 2015 Thomas Perl <m@thp.io> - 1.1.13
- [spec] Inject RPM version number to version.h (Fixes #30)
* Thu Jan  8 2015 Antti Seppälä <antti.seppala@jollamobile.com> - 1.1.12
- [fingerterm] Implemented scalable UI layout
* Mon Mar 31 2014 Thomas Perl <thomas.perl@jolla.com> - 1.1.11
- [fingerterm] Add 256-colour support (xterm SGRs 38;5;c and 48;5;c)
- [fingerterm] Add aixterm high-intensity non-bold SGR codes.
* Mon Mar 31 2014 Thomas Perl <thomas.perl@jolla.com> - 1.1.9
- [clipboard] Disable mimeData checking before copying
- [fingerterm] Don't re-define local variables in clipboard code
- [fingerterm] make copy to clipboard working
- [keylayouts] Add french to deployment list / qrc
- [keylayouts] Add german and qwertz to deployment list / qrc
* Tue Dec 10 2013 Thomas Perl <m@thp.io> - 1.1.8
- [behavior] Change default behavior to be more user-friendly
- [debug] Remove "unprintable char 0" in debug messages
* Mon Oct 14 2013 Simonas Leleiva <simonas.leleiva@gmail.com> - 1.1.7
- [nemo] Fix single-instance by removing explicit invoker usage
- [nemo] Remove unnecessary key/value pairs in .desktop file
- [nemo] Rename icon from "FingerTerm" to generic "Terminal"
* Thu Oct 10 2013 Simonas Leleiva <simonas.leleiva@gmail.com> - 1.1.6
- [orientation] enable orientation handling in fingerterm
* Tue Oct  1 2013 Bernd Wachter <bwachter@lart.info> - 1.1.5
- [vkb] Key shift transition behavior
- [vkb] Updated icons (completely white to blend with text, smaller)
* Wed Sep 25 2013 Bernd Wachter <bwachter@lart.info> - 1.1.4
- [cursor] Fix cursor position, size and fill color
- [vkb] Fix toggle keyboard by tapping outside keyboard
* Sat Sep 21 2013 Bernd Wachter <bwachter@lart.info> - 1.1.3
- [ui] Make "fader" background black instead of white
- [vkb] Basic multi-touch support (no modifiers yet)
- [vkb] Hide keyboard when window doesn't have focus
- [vkb] Multi-touch handling for modifier keys
- [vkb] Remove exitedPressedKeyArea
* Fri Aug 23 2013 Bernd Wachter <bernd.wachter@jollamobile.com> - 1.1.2
- [haptics] Add haptic feedback on key presses
* Fri Aug 16 2013 Bernd Wachter <bwachter@lart.info> - 1.1.1
- [orientation] bug fixing and qml refactoring
- [port] Now uses qtcomponents, added preliminary orientationLock support, qml code more robust
* Wed Aug  7 2013 faenil <and.bernabei@gmail.com> - 1.1.0
- [port] Port to Qt5/QtQuick2 + disables clipboard support
- [port] WIP more work on QtQuick2 port + disables clipboard support
* Sun Jun 16 2013 Bernd Wachter <bwachter@lart.info> - 1.0.6
- [qt5] Allow building with Qt5
- [qt5] Update packaging to build qt5 fingerterm
* Mon May 13 2013 Robin Burchell <robin+git@viroteck.net> - 1.0.5
- [fingeterm] Add multiple window support
* Wed Apr  3 2013 Robin Burchell <robin+git@viroteck.net> - 1.0.4
- [fingerterm] Replace meego-terminal as the terminal on device.
* Sun Mar  3 2013 Bernd Wachter <bernd.wachter@jollamobile.com> - 1.0.3
- Move to Nemo specific target
* Mon Jul  9 2012 Bernd Wachter <bernd.wachter@jollamobile.com> - 1.0.2
- Initial package for Nemo
