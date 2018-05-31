:  !/bin/bash

:  Maya 2016 configure file
:  Version=2016 Release.
:  Date : May 29, 2018
:  Last modified: May 29, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:   WARNING! All changes made in this file will be lost!

:  Description
:      This module contain all input value for the Maya 2016.  


call environ.bat

rem set MAYA_PLUGIN_PATH=%MAYA_PLUGIN_PATH%
set MAYA_SCRIPT_PATH=%MAYA_SCRIPT_PATH%
rem set MAYA_USER_PLUGINS=%MAYA_SCRIPT_PATH%
set PYTHONPATH=%PACKAGE_PATH%;%PLUGIN_PATH%;%MAYA_PYTHONPATH%;%PACKAGE_PATH%/plugins/maya

echo ""
echo "................................................................"
echo "MAYA"
echo $MAYA_VERSION
echo $MAYA_PATH
echo "Loading Maya, please wait .............................."
echo ""

start "" "%MAYA_PATH%"
exit

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :