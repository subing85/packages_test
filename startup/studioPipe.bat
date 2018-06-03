:  !/bin/bash

:  StudioPipe configure
:  Date : May 31, 2018
:  Last modified: May 31, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:   WARNING! All changes made in this file will be lost!

:  Description
:      This module contain all input value for the StudioPipe.  


rem call Z:\packages\startup\environ.bat
call environ.bat

set PYTHONPATH=%PYTHONPATH%;%NATRON_PYTHONPATH%;%COMMON_PYTHONPATH%

echo ""
echo "................................................................"
echo "Studio Pipe"
echo %STUDIOPIPE_VERSION%
echo %STUDIOPIPE_PATH%
echo "Loading Natron, please wait .............................."
echo ""

"C:\Python27\python.exe" "%STUDIOPIPE_PATH%"

rem start "" "%STUDIOPIPE_PATH%"

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :