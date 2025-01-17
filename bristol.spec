%define major 0
%define libname %mklibname %{name} %{major}

Name:       bristol
Summary:    Synthesizer Emulator Pack
Version:    0.60.11
Release:    3

URL:        https://%{name}.sourceforge.net/
Source:     https://sourceforge.net/projects/bristol/files/bristol/0.60/%{name}-%{version}.tar.gz
Patch0:     bristol-remove-legacy-header.patch
Patch1:     bristol-0.60.11-compile.patch
License:    GPLv2
Group:      Sound

BuildRequires:  pkgconfig(x11)
BuildRequires:  jackit-devel
BuildRequires:  pkgconfig(alsa)

Requires:       %{libname} >= %{version}
Requires:       jackit

Obsoletes:      %{name}-aks
Obsoletes:      %{name}-poly
Obsoletes:      %{name}-mixer
Obsoletes:      %{name}-hammond

%description
Bristol emulates several vintage synthesizers, mainly keyboards:
Various Moog, Sequencial Circuits, Oberheim, Arp, Rhodes,
Yamaha, Roland, Hammond, Korg, and Vox algorithms are provided.
Each has its own graphical interface. A central interface is provided
by Brighton.

#---------------------------------
%package -n %{libname}
Summary:    Dynamic libraries used by bristol
License:    GPLv2
Group:      System/Libraries
Requires:   jackit
Provides:   lib%{name} = %{version}

%description -n %{libname}
Dynamic libraries required by the Bristol vintage keyboard emulation
package

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.%major
%{_libdir}/*.so.%major.*

#--------------
%package arp2600
Summary: Bristol - arp 2600
Group:      Sound
Requires: bristol

%description arp2600
* arp 2600

%files arp2600
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-arp2600.desktop
#--------------

%package axxe
Summary: Bristol - arp axxe
Group:      Sound
Requires: bristol

%description axxe
* axxe - arp axxe

%files axxe
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-axxe.desktop
#--------------

%package b3
Summary: Bristol - hammond B3
Group:      Sound
Requires: bristol

%description b3
* b3 - hammond B3

%files b3
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-b3.desktop
#--------------

%package bitone
Summary: Bristol - crumar bit 01
Group:      Sound
Requires: bristol

%description bitone
* bitone - crumar bit 01

%files bitone
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-bitone.desktop
#--------------

%package bit100
Summary: Bristol - crumar bit + mods
Group:      Sound
Requires: bristol

%description bit100
* bit100 - crumar bit + mods

%files bit100
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-bit100.desktop
#--------------

%package bit99
Summary: Bristol - crumar bit 99
Group:      Sound
Requires: bristol

%description bit99
* bit99 - crumar bit 99

%files bit99
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-bit99.desktop
#--------------

%package stratus
Summary: Bristol - crumar stratus synth/organ combo
Group:      Sound
Requires: bristol

%description stratus
* stratus - crumar stratus synth/organ combo

%files stratus
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-stratus.desktop
#--------------

%package trilogy
Summary: Bristol - crumar trilogy synth/organ/string combo
Group:      Sound
Requires: bristol

%description trilogy
* trilogy - crumar trilogy synth/organ/string combo

%files trilogy
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-trilogy.desktop
#--------------

%package dx
Summary: Bristol - yamaha DX-7
Group:      Sound
Requires: bristol

%description dx
* dx - yamaha DX-7

%files dx
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-dx.desktop
#--------------

%package explorer
Summary: Bristol - moog voyager
Group:      Sound
Requires: bristol

%description explorer
* explorer - moog voyager

%files explorer
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-explorer.desktop
#--------------

%package voyager
Summary: Bristol - moog voyager electric blue
Group:      Sound
Requires: bristol

%description voyager
* voyager - moog voyager electric blue

%files voyager
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-voyager.desktop
#--------------

%package sonic6
Summary: Bristol - moog sonic 6
Group:      Sound
Requires: bristol

%description sonic6
* sonic6 - moog sonic 6

%files sonic6
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-sonic6.desktop
#--------------

%package mg1
Summary: Bristol - moog/realistic mg-1 concertmate
Group:      Sound
Requires: bristol

%description mg1
* mg1 - moog/realistic mg-1 concertmate

%files mg1
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-mg1.desktop
#--------------

%package juno
Summary: Bristol - roland juno-60
Group:      Sound
Requires: bristol

%description juno
* juno - roland juno-60

%files juno
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-juno.desktop
#--------------

%package jupiter
Summary: Bristol - roland jupiter-8
Group:      Sound
Requires: bristol

%description jupiter
* jupiter - roland jupiter-8

%files jupiter
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-jupiter.desktop
#--------------

%package bme700
Summary: Bristol - Baumann bme-700
Group:      Sound
Requires: bristol

%description bme700
* bme700 - Baumann bme-700

%files bme700
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-bme700.desktop
#--------------

%package bm
Summary: Bristol - bristol bassmaker sequencer
Group:      Sound
Requires: bristol

%description bm
* bm - bristol bassmaker sequencer

%files bm
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-bm.desktop
#--------------

%package memory
Summary: Bristol - moog memory
Group:      Sound
Requires: bristol

%description memory
* memory - moog memory

%files memory
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-memory.desktop
#--------------

%package mini
Summary: Bristol - moog mini
Group:      Sound
Requires: bristol

%description mini
* mini - moog mini

%files mini
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-mini.desktop
#--------------

%package mono
Summary: Bristol - korg monopoly
Group:      Sound
Requires: bristol

%description mono
* mono - korg monopoly

%files mono
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-mono.desktop
#--------------

%package obx
Summary: Bristol - oberheim OB-X
Group:      Sound
Requires: bristol

%description obx
* obx - oberheim OB-X

%files obx
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-obx.desktop
#--------------

%package obxa
Summary: Bristol - oberheim OB-X-A
Group:      Sound
Requires: bristol

%description obxa
* obxa - oberheim OB-X-A

%files obxa
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-obxa.desktop
#--------------

%package odyssey
Summary: Bristol - arp odyssey
Group:      Sound
Requires: bristol

%description odyssey
* odyssey - arp odyssey

%files odyssey
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-odyssey.desktop
#--------------

%package polysix
Summary: Bristol - korg polysix
Group:      Sound
Requires: bristol

%description polysix
* polysix - korg polysix

%files polysix
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-polysix.desktop
#--------------

%package poly800
Summary: Bristol - korg poly-800
Group:      Sound
Requires: bristol

%description poly800
* poly800 - korg poly-800

%files poly800
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-poly800.desktop
#--------------

%package monopoly
Summary: Bristol - korg mono/poly
Group:      Sound
Requires: bristol

%description monopoly
* poly - korg mono/poly

%files monopoly
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-monopoly.desktop
#--------------

%package prophet
Summary: Bristol- sequential circuits prophet-5
Group:      Sound
Requires: bristol

%description prophet
* prophet - sequential circuits prophet-5

%files prophet
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-prophet.desktop
#--------------

%package pro10
Summary: Bristol- sequential circuits prophet-10
Group:      Sound
Requires: bristol

%description pro10
* pro10 - sequential circuits prophet-10

%files pro10
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-pro10.desktop
#--------------

%package pro52
Summary: Bristol- sequential circuits prophet-5/fx
Group:      Sound
Requires: bristol

%description pro52
* pro52 - sequential circuits prophet-5 with chorus

%files pro52
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-pro52.desktop
#--------------

%package pro1
Summary: Bristol- sequential circuits pro-one
Group:      Sound
Requires: bristol

%description pro1
* pro1 - sequential circuits pro-one

%files pro1
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-pro1.desktop
#--------------

%package roadrunner
Summary: Bristol- roadrunner electric piano
Group:      Sound
Requires: bristol

%description roadrunner
* roadrunner   - roadrunner electric piano

%files roadrunner
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-roadrunner.desktop
#--------------

%package rhodes
Summary: Bristol- fender rhodes mark-I stage 73
Group:      Sound
Requires: bristol

%description rhodes
* rhodes - fender rhodes mark-I stage 73

%files rhodes
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-rhodes.desktop
#--------------

%package rhodesbass
Summary: Bristol- fender rhodes bass piano
Group:      Sound
Requires: bristol

%description rhodesbass
* rhodesbass - fender rhodes bass piano

%files rhodesbass
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-rhodesbass.desktop
#--------------

%package solina
Summary: Bristol- Solina string machine
Group:      Sound
Requires: bristol

%description solina
* solina - solina string machine

%files solina
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-solina.desktop
#--------------

%package sidney
Summary: Bristol- Comodore-64 SID chip synth
Group:      Sound
Requires: bristol

%description sidney
* sidney - Comodore-64 SID chip synth

%files sidney
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-sidney.desktop
#--------------

%package voxM2
Summary: Bristol- vox continental super/300/II
Group:      Sound
Requires: bristol

%description voxM2
* vox - vox continental super/300/II

%files voxM2
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-voxM2.desktop
#--------------

%package vox
Summary: Bristol- vox continental
Group:      Sound
Requires: bristol

%description vox
* vox - vox continental

%files vox
%defattr(-,root,root,-)
%{_datadir}/applications/mandriva-bristol-vox.desktop
#--------------

%prep
%autosetup -p1
chmod  a-x bitmaps/*/*
chmod  a-x bitmaps/bicon.svg bitmaps/icon_bitmap.xbm
chmod  a-x COPYING AUTHORS NEWS

perl -pi -e 's/-march=core2//g' bristol/Makefile.*
perl -pi -e 's/-march=core2//g' libbristol/Makefile.*

%build
autoreconf -fi
%define _disable_ld_no_undefined 1
%configure CONFIG_SHELL=/bin/bash \
    --disable-version-check \
    --enable-static=no

%make

%install

make BRISTOL_DIR=%{_datadir}/bristol DESTDIR=%{buildroot} install

rm -f %buildroot%_libdir/*.la %buildroot%_libdir/*.so

mkdir -p %{buildroot}/etc/xdg/menus/applications-merged
cat > %{buildroot}/etc/xdg/menus/applications-merged/%{name}.menu << EOF
<!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
"http://www.freedesktop.org/standards/menu-spec/menu-1.0.dtd">
<Menu>
    <Name>Applications</Name>
    <Menu>
        <Name>SoundVideo</Name>
        <Menu>
            <Name>Bristol</Name>
                <Directory>mandriva-%{name}.directory</Directory>
                <Include>
                    <Category>X-Bristol</Category>
                </Include>
        </Menu>
    </Menu>
</Menu>
EOF

mkdir -p %{buildroot}%{_datadir}/desktop-directories
cat > %{buildroot}%{_datadir}/desktop-directories/mandriva-%{name}.directory << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Bristol
Icon=bicon.svg
Type=Directory
EOF


mkdir -p %{buildroot}%{_datadir}/applications/
for synth in    arp2600 axxe b3 dx explorer voyager mg1 juno jupiter \
                trilogy stratus memory mini sonic6\
                bitone bit99 bit100 sidney bm bme700 \
                mono obx obxa odyssey poly800 monopoly \
                polysix prophet pro10 pro52 pro1 roadrunner rhodes rhodesbass \
                solina vox voxM2; do

cat > %{buildroot}%{_datadir}/applications/mandriva-bristol-${synth}.desktop << EOF
[Desktop Entry]
Name=Bristol ${synth}
Comment=Emulator for diverse keyboard instruments
Icon=bicon.svg
Type=Application
Exec=startBristol -jack -autoconn -priority 70 -${synth}
Terminal=false
Encoding=UTF-8
Categories=X-Bristol;
EOF

done

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp bitmaps/bicon.svg %{buildroot}%{_datadir}/pixmaps/

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* NEWS README
%docdir %{_mandir}/man1/*
%{_mandir}/man1/*
%{_bindir}/brighton
%{_bindir}/bristol
%{_bindir}/bristoljackstats
%{_bindir}/startBristol
%{_datadir}/pixmaps/bicon.svg
%{_datadir}/bristol
%{_datadir}/desktop-directories/mandriva-%{name}.directory
%config(noreplace) /etc/xdg/menus/applications-merged/%{name}.menu

%clean


%changelog
* Thu Dec 15 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.60.9-1mdv2012.0
+ Revision: 741503
- update to 0.60.9

* Wed Mar 23 2011 Frank Kober <emuse@mandriva.org> 0.60.8-1
+ Revision: 648179
- new version 0.60.8

* Wed Jan 05 2011 Funda Wang <fwang@mandriva.org> 0.60.6-2mdv2011.0
+ Revision: 628673
- tighten BR
- partial fix linkage

* Sat Aug 14 2010 Frank Kober <emuse@mandriva.org> 0.60.6-1mdv2011.0
+ Revision: 569591
- new version 0.60.6
  o adjust file list
  o adjust permission fix

  + Funda Wang <fwang@mandriva.org>
    - update to new version 0.60.5

* Thu Jul 15 2010 Frank Kober <emuse@mandriva.org> 0.60.5-1mdv2011.0
+ Revision: 553529
- new version 0.60.5

* Thu May 13 2010 Frank Kober <emuse@mandriva.org> 0.60.3-1mdv2010.1
+ Revision: 544715
- new version 0.60.3 adding CLI and fixing crashes on KDE4
- manpages added to spec

* Fri Apr 16 2010 Frank Kober <emuse@mandriva.org> 0.50.6-2mdv2010.1
+ Revision: 535353
- begin lint cleaning, obsolete old desktop pkgs

* Sun Apr 11 2010 Frank Kober <emuse@mandriva.org> 0.50.6-1mdv2010.1
+ Revision: 533599
- sync sources
- adjust desktop file list (thanks to Philippe Didier), new version 0.50.6, create submenu entry

* Mon Apr 05 2010 Frank Kober <emuse@mandriva.org> 0.50.5-1mdv2010.1
+ Revision: 531721
- add missing new item to file list
- new version 0.50.5
- new version 0.50.5

* Fri Apr 02 2010 Frank Kober <emuse@mandriva.org> 0.50.3-1mdv2010.1
+ Revision: 530789
- update to new version 0.50.3

* Sun Mar 28 2010 Frank Kober <emuse@mandriva.org> 0.50.2-3mdv2010.1
+ Revision: 528481
- do Makefile.am modification BEFORE configure

* Sun Mar 28 2010 Frank Kober <emuse@mandriva.org> 0.50.2-2mdv2010.1
+ Revision: 528475
- drop patches, use perl to only remove -march flag

* Sun Mar 28 2010 Frank Kober <emuse@mandriva.org> 0.50.2-1mdv2010.1
+ Revision: 528458
- import bristol, initial specfile provided by Yvan Munoz
- import bristol



