### RPM external millepede 03.04.00
# CAREFUL: NO VERSION IN TARBALL !!!
# Source: http://www.desy.de/~blobel/Mptwo.tgz
# Source: http://cmsrep.cern.ch/cmssw/millepede-mirror/millepede-2.0.tar.gz

%define svnTag %(echo %realversion | tr '.' '-')
Source: svn://svnsrv.desy.de/public/MillepedeII/tags/V%svnTag/?scheme=http&module=V%svnTag&output=/millepede.tgz

Requires: castor zlib
%if "%(echo %cmsos | grep osx >/dev/null && echo true)" == "true"
Requires: gfortran-macosx
%endif

Patch: millepede_V03-04-00_makefile

%prep

%setup -n V%svnTag

%patch -p1

perl -p -i -e "s!-lshift!-L$CASTOR_ROOT/lib -lshift -lcastorrfio!" Makefile
perl -p -i -e "s!C_INCLUDEDIRS =!C_INCLUDEDIRS = -I$CASTOR_ROOT/include!" Makefile

case %cmsplatf in osx*)
    perl -p -i -e "s|-lshift|-lcastorrfio|" Makefile ;;
esac

%build
# gcc on the mac cannot be used as a fortran compiler / linker because
# gfortran is installed somewhere else.
make %makeprocesses FCOMP=gfortran LOADER=gfortran

%install
make install
mkdir -p %i/bin
cp bin/* %i/bin
