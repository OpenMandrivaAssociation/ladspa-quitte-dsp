%define plugins clipper matched preamp super-60 unmatched

Summary: 	Guitar preamp plugins for ladspa
Name: 	 	ladspa-quitte-dsp
Version: 	1.0
Release: 	6
License:	GPL
Group:		Sound
URL:		https://quitte.de/dsp/
Source0:	clipper.tar.gz
Source1:	matched.tar.gz
Source2:	preamp.tar.gz
Source4:	super-60.tar.bz2
Source5:	unmatched.tar.gz
Patch0:		ladspa-quitte-dsp-1.0-cflags_fix.diff
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	sndfile-devel
Requires:	ladspa
Requires:	caps
Requires:	pvoc

%description
Digital guitar preamp plugins for ladspa courtesy of quitte.de.
preamp: a 12AX7-based preamp emulation
super-60: a 'cheap' (in the computational sense) amp/cabinet emulation
unmatched: another 'cheap' amp/cabinet emulation
spiced 12AX7: analysis and a simple hard clipper

%prep

%setup -c %name -a1 -a2 -a4 -a5 
%patch0 -p1


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
%{_libdir}/ladspa/*
