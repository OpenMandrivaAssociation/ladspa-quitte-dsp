%define plugins caps clipper matched preamp pvoc super-60 unmatched

Summary: 	Guitar preamp plugins for ladspa
Name: 	 	ladspa-quitte-dsp
Version: 	1.0
Release: 	3
License:	GPL
Group:		Sound
URL:		http://quitte.de/dsp/
Source0:	caps_0.4.2.tar.gz
Source1:	clipper.tar.gz
Source2:	matched.tar.gz
Source3:	preamp.tar.gz
Source4:	pvoc_0.1.12.tar.gz
Source5:	super-60.tar.bz2
Source6:	unmatched.tar.gz
Patch0:		ladspa-quitte-dsp-1.0-cflags_fix.diff
Patch1:		ladspa-quitte-dsp-1.0-no_strip_fix.diff
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	sndfile-devel
Requires:	ladspa

%description
Digital guitar preamp plugins for ladspa courtesy of quitte.de.
preamp: a 12AX7-based preamp emulation
super-60: a 'cheap' (in the computational sense) amp/cabinet emulation
unmatched: another 'cheap' amp/cabinet emulation
spiced 12AX7: analysis and a simple hard clipper

%prep

%setup -c %name -a1 -a2 -a3 -a4 -a5 -a6
%patch0 -p1
%patch1 -p1
perl -pi -e "s/stderr, formats/stderr, \"%s\", formats/g" pvoc-0.1.12/stretch.cc

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC" 

for i in %plugins; do
    pushd ${i}*
    %make OPTS="$CFLAGS"
    popd
done
									
%install

install -d %{buildroot}%{_libdir}/ladspa

for i in %plugins; do
    pushd ${i}*
    %makeinstall \
	PREFIX=%{buildroot}%{_prefix} \
	DEST=%{buildroot}%{_libdir}/ladspa \
	PLUGDEST=%{buildroot}%{_libdir}/ladspa \
	UTILDEST=%{buildroot}%{_bindir} \
	MAN1DEST=%{buildroot}%{_mandir}/man1
    popd
done
chmod 755 %{buildroot}%{_libdir}/ladspa/*.so

%files
%defattr(-,root,root)
%{_bindir}/stretch
%{_libdir}/ladspa/*
%{_datadir}/ladspa/rdf/caps.rdf
%{_mandir}/man1/stretch.1*


%changelog
* Tue Nov 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdv2009.1
+ Revision: 306685
- fix deps (sndfile-devel)
- fix build (P0,P1)
- added pvoc and caps

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - fix build on x86_64 by compiling with -fPIC
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import ladspa-quitte-dsp

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Oct 13 2003 Austin Acton <aacton@yorku.ca> 1.0-1mdk
- initial package
