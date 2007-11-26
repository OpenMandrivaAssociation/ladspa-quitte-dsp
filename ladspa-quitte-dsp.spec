%define plugins preamp super-60 unmatched clipper

Name: 	 	ladspa-quitte-dsp
Version: 	1.0
Release: 	1mdk

Summary: 	Guitar preamp plugins for ladspa
URL:		http://quitte.de/dsp/
License:	GPL
Group:		Sound

Source0:	preamp.tar.bz2
Source1:	super-60.tar.bz2
Source2:	unmatched.tar.bz2
Source3:	clipper.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ladspa-devel
Requires:	ladspa

%description
Digital guitar preamp plugins for ladspa courtesy of quitte.de.
preamp: a 12AX7-based preamp emulation
super-60: a 'cheap' (in the computational sense) amp/cabinet emulation
unmatched: another 'cheap' amp/cabinet emulation
spiced 12AX7: analysis and a simple hard clipper

%prep
%setup -c %name -a 1 -a 2 -a 3

%build
for i in %plugins
do
cd $i
%make
cd ..
done
									
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ladspa
for i in %plugins
do
cd $i
%makeinstall DEST=$RPM_BUILD_ROOT/%{_libdir}/ladspa
cd ..
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/ladspa/*

