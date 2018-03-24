: !/bin/bash

: Studio Launcher configure
: Date : February 07, 2018
: Last modified: March 23, 2018
: Author: Subin. Gopi (subing85@gmail.com)
: Copyright (c) 2018, Subin Gopi
: All rights reserved.

:   WARNING! All changes made in this file will be lost!

:  Description
:      This module contain all input value for the Studo Launcher.  


call Z:\packages\startup\environ.bat

set PACKAGE_PATH=%PACKAGE_PATH%

set PROJECT_NAME=%PROJECT_NAME%
set PROJECT_NICENAME=%PROJECT_NICENAME%
set PROJECT_PATH=%PROJECT_PATH%

set ICON_PATH=%ICON_PATH%

set PYTHON_VERSION=%PYTHON_VERSION%
set PYTHON_PATH=%PYTHON_PATH%

set PYTHONPATH=%PYTHONPATH%;%STARTUP_PYTHONPATH%

set PACKAGE_PATH=%PACKAGE_PATH%
set DATA_PATH=%DATA_PATH%
set PLUGINS_PATH=%PLUGINS_PATH%

set DATABASE_PATH=%DATABASE_PATH%
set TOOLKIT_PATH=%TOOLKIT_PATH%
set ICON_PATH="%ICON_PATH%
set BIN_PATH="%BIN_PATH%

set PIPEINPUT_FILE=%PIPEINPUT_FILE%
set PACKAGE_BACKUP_PATH=%PACKAGE_BACKUP_PATH%

set LAUNCHER_PATH=%PACKAGE_PATH%/startup/studioLauncher.py

echo ""
echo "................................................................"
echo %PROJECT_NAME
echo %PROJECT_PATH
echo "Studio Launcher"
echo "0.0.1 Release"
echo ""

start "" %PYTHON_PATH% %LAUNCHER_PATH%
: pause
: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :