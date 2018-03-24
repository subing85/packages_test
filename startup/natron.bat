:  !/bin/bash

:  Natron configure
:  Date : February 09, 2018
:  Last modified: March 23, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:   WARNING! All changes made in this file will be lost!

:  Description
:      This module contain all input value for the Natron.  


rem call Z:\packages\startup\environ.bat
call environ.bat

set NATRON_PLUGIN_PATH=%NATRON_PLUGIN_PATH%
set PYTHONPATH=%PYTHONPATH%;%NATRON_PYTHONPATH%;%COMMON_PYTHONPATH%

echo ""
echo "................................................................"
echo "Natron"
echo %NARTON_VERSION%
echo %NARTON_PATH%
echo "Loading Natron, please wait .............................."
echo ""

echo %NATRON_PATH%

start "" "%NATRON_PATH%"

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :