### RPM external py2-scipy 0.19.0
## INITENV +PATH PYTHONPATH %{i}/${PYTHON_LIB_SITE_PACKAGES}

%define pip_name scipy
Requires: py2-numpy

## IMPORT build-with-pip
%define PipPostBuild \
perl -p -i -e "s|^#!.*python(.*)|#!/usr/bin/env python$1|" `grep -r -e "#\!.*python" %i | cut -d: -f1`
