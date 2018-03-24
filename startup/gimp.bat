:  !/bin/bash

:  Gimp Launcher configure
:  Version=2.8.0 Release.
:  Date : February 07, 2018
:  Last modified: March 23, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:	WARNING! All changes made in this file will be lost!

:   Description
:		This module contain all input value for the Gimp.  


rem call Z:\packages\startup\environ.bat
call environ.bat

set GIMP_PLUGIN_PATH=$GIMP_PLUGIN_PATH
set PYTHONPATH=%PACKAGE_PATH%;%PLUGIN_PATH%;%GIMP_PYTHONPATH%

echo ""
echo "................................................................"
echo "Gimp"
echo %GIMP_VERSION%
echo %GIMP_PATH%
echo "Loading Gimp, please wait .............................."
echo ""

echo %GIMP_PATH%

start "" "%GIMP_PATH%"

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :