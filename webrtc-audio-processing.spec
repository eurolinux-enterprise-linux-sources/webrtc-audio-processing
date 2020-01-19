Name:           webrtc-audio-processing
Version:        0.1
Release:        5%{?dist}
Summary:        Library for echo cancellation

License:        BSD
URL:            http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:        http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.xz
Patch0:         webrtc-fix-typedefs-on-other-arches.patch

%description
%{name} is a library derived from Google WebRTC project that 
provides echo cancellation functionality. This library is used by for example
PulseAudio to provide echo cancellation.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .typedef

%build
%configure                                                              \
  --with-package-name='Fedora Webrtc-audio-processing package'                        \
  --with-package-origin='http://download.fedoraproject.org'             \
  --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc COPYING NEWS AUTHORS PATENTS
%{_libdir}/*.so.*

%files devel
%{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/webrtc_audio_processing/


%changelog
* Wed Feb 26 2014 Debarshi Ray <rishi@fedoraproject.org> - 0.1-5
- Fix FTBFS on non-x86/arm
  Resolves: #1068823

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.1-4
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 9 2012 Dan Horák <dan[at]danny.cz> 0.1-2
- set ExclusiveArch x86 and ARM for now

* Fri Oct 5 2012 Christian Schaller <christian.schaller@gmail.com> 0.1-1
- Initial Fedora spec.
