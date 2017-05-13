### RPM cms coral CORAL_2_3_21
%define tag dde218d1e2e68404c7b8f6d63d87ac8e508c5d62
%define branch cms/%{realversion}
%define github_user cms-externals

Patch0: coral-2_3_20-macosx
Requires: coral-tool-conf

%if %(case %{cmsplatf} in (*_aarch64_*) echo 1 ;; (*) echo 0 ;; esac) == 1
%define cmsplatf_aarch64 1
%endif

%if %(case %{cmsplatf} in (*_ppc64le_*) echo 1 ;; (*) echo 0 ;; esac) == 1
%define cmsplatf_ppc64le 1
%endif

%define isdarwin %(case %{cmsos} in (osx*) echo 1 ;; (*) echo 0 ;; esac)

%define cvssrc          %{n}

# Build with debug symbols, and package them in a separate rpm:
%define subpackageDebug yes

# Disable building tests, since they bring dependency on cppunit:
%if %isdarwin
%define patchsrc2        perl -p -i -e 's!(<classpath.*/tests\\+.*>)!!;' config/BuildFile.xml
%define patchsrc3       %patch0 -p1 
%endif

# Drop Oracle interface on ARM machines and POWER machines.
# Oracle does not provide Instant Client for ARMv8 or POWER8.
%if 0%{?cmsplatf_aarch64}%{?cmsplatf_ppc64le}
%define patchsrc2       rm -rf ./src/OracleAccess
%endif

%define source1  git://github.com/%{github_user}/%{n}.git?protocol=https&obj=%{branch}/%{tag}&module=%{cvssrc}&export=%{srctree}&output=/src.tar.gz
## IMPORT scram-project-build
## SUBPACKAGE debug IF %subpackageDebug
