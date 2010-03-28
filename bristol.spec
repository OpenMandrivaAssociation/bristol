%define name    bristol
%define version 0.50.2
%define release %mkrel 3

Name:       %{name}
Summary:    Synthesiser Emulator Pack
Version:    %{version}
Release:    %{release}

URL:        http://%{name}.sourceforge.net/
Source:     http://prdownloads.sourceforge.net/bristol/%{name}-%{version}.tar.gz
Source1:    bristol.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
License:    GPLv2
Group:      Sound

BuildRequires:  X11-devel
BuildRequires:  jackit-devel
BuildRequires:  libjack-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libsndfile-devel

Requires:   jackit

%description
Bristol emulates severals Vintage Synthesizer Keyboards : 
Various Moog, Sequencial Circuits, Oberheim,
Yamaha, Roland, Hammond, Korg, and Vox algorithms are provided. 
Each has its own graphical interface. A central interface is provided
by Brighton. 

%package arp2600
Summary: Bristol - arp 2600
Group:      Sound
Requires: bristol

%description arp2600
* arp 2600

%package aks
Summary: Bristol - ems synthi-A
Group:      Sound
Requires: bristol

%description aks
* ems synthi-A

%package axxe
Summary: Bristol - arp axxe
Group:      Sound
Requires: bristol

%description axxe
* axxe - arp axxe

%package b3
Summary: Bristol - hammond B3
Group:      Sound
Requires: bristol

%description b3
* b3 - hammond B3

%package dx
Summary: Bristol - yamaha DX-7
Group:      Sound
Requires: bristol

%description dx
* dx - yamaha DX-7

%package explorer
Summary: Bristol - moog voyager
Group:      Sound
Requires: bristol

%description explorer
* explorer - moog voyager

%package hammond
Summary: Bristol - hammond module
Group:      Sound
Requires: bristol

%description hammond
* hammond - hammond module

%package juno
Summary: Bristol - roland juno-6
Group:      Sound
Requires: bristol

%description juno
* juno - roland juno-6

%package memory
Summary: Bristol - moog memory
Group:      Sound
Requires: bristol

%description memory
* memory - moog memory

%package mini
Summary: Bristol - moog mini
Group:      Sound
Requires: bristol

%description mini
* mini - moog mini

%package mixer
Summary: Bristol - 16 track mixer
Group:      Sound
Requires: bristol

%description mixer
Summary: Bristol - test mixer
Group:      Sound
Requires: bristol
* mixer - 16 track mixer

%package mono
Summary: Bristol - korg monopoly
Group:      Sound
Requires: bristol

%description mono
* mono - korg monopoly

%package obx
Summary: Bristol - oberheim OB-X
Group:      Sound
Requires: bristol

%description obx
* obx - oberheim OB-X

%package obxa
Summary: Bristol - oberheim OB-X-A
Group:      Sound
Requires: bristol

%description obxa
* obxa - oberheim OB-Xa

%package odyssey
Summary: Bristol - arp odyssey
Group:      Sound
Requires: bristol

%description odyssey
* odyssey - arp odyssey

%package poly
Summary: Bristol - korg poly6
Group:      Sound
Requires: bristol

%description poly
* poly - korg poly6

%package prophet
Summary: Bristol- sequential circuits prophet-5/prohet-10
Group:      Sound
Requires: bristol

%description prophet
* pro52 - sequential circuits prophet-5 with chorus
* pro10 - sequential circuits prophet-10

%package roadrunner
Summary: Bristol- roadrunner electric piano
Group:      Sound
Requires: bristol

%description roadrunner
* roadrunner   - roadrunner electric piano

%package rhodes
Summary: Bristol- fender rhodes mark-I stage 73
Group:      Sound
Requires: bristol

%description rhodes
* rhodes - fender rhodes mark-I stage 73

%package rhodesbass
Summary: Bristol- fender rhodes bass piano
Group:      Sound
Requires: bristol

%description rhodesbass
* rhodesbass - fender rhodes bass piano

%package solina
Summary: Bristol- Solina string machine
Group:      Sound
Requires: bristol

%description solina
* solina - solina string machine

%package vox
Summary: Bristol- vox continental
Group:      Sound
Requires: bristol

%description vox
* vox - vox continental

%prep
%setup -q

%build
perl -pi -e 's/-march=core2//g' bristol/Makefile.am
perl -pi -e 's/-march=core2//g' libbristol/Makefile.am
./configure CONFIG_SHELL=/bin/bash \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --bindir=%{_bindir} \
    --with-gnu-ld \
    --enable-sem-open \
    --enable-static=no
    

%make

%install
rm -rf %{buildroot}

perl -p -i -e "s|%{_datadir}/share|%{_datadir}|g" bin/startBristol
make BRISTOL_DIR=%{_datadir}/bristol DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/applications/
for synth in arp2600 aks axxe b3 dx explorer hammond juno memory mini mixer mono obx obxa odyssey \
             poly prophet pro10 pro52 roadrunner rhodes rhodesbass solina vox; do
    cp %{SOURCE1} bristol-${synth}.desktop
    sed -i -e "s/@MODEL@/${synth}/g" bristol-${synth}.desktop
# sed -i "s/ICONP/%{synth}/g" bristol-${synth}.desktop
    desktop-file-install \
      --dir %{buildroot}%{_datadir}/applications \
      bristol-${synth}.desktop
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp bitmaps/bicon.svg %{buildroot}%{_datadir}/pixmaps/


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README
%{_bindir}/brighton
%{_bindir}/bristol
%{_bindir}/bristoljackstats
%{_bindir}/startBristol
%{_bindir}/bristolnotegen
%{_datadir}/pixmaps/bicon.svg
%exclude %{_libdir}/*.la
%{_libdir}/*
%{_datadir}/bristol

%files arp2600
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-arp2600.desktop

%files aks
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-aks.desktop

%files axxe
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-axxe.desktop

%files b3
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-b3.desktop

%files dx
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-dx.desktop

%files explorer
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-explorer.desktop

%files hammond
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-hammond.desktop

%files juno
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-juno.desktop

%files memory
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-memory.desktop

%files mini
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-mini.desktop

%files mixer
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-mixer.desktop

%files mono
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-mono.desktop

%files obx
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-obx.desktop

%files obxa
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-obxa.desktop

%files odyssey
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-odyssey.desktop

%files poly
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-poly.desktop

%files prophet
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-prophet.desktop
%{_datadir}/applications/bristol-pro10.desktop
%{_datadir}/applications/bristol-pro52.desktop

%files roadrunner
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-roadrunner.desktop

%files rhodes
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-rhodes.desktop

%files rhodesbass
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-rhodesbass.desktop

%files solina
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-solina.desktop

%files vox
%defattr(-,root,root,-)
%{_datadir}/applications/bristol-vox.desktop

%clean
rm -rf %{buildroot}
