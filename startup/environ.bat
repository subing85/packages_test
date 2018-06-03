:  !/bin/bash

:  Environ configure file
:  Date : February 09, 2018
:  Last modified: March 23, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:   WARNING! All changes made in this file will be lost!

:  Description
:      This module contain all input value for the project.  


echo Environ configure file
echo Last modified: March 05, 2018
echo Author: Subin. Gopi (subing85@gmail.com)

set DRIVE=Z:

set PACKAGE_PATH=Z:/packages

rem set PROJECT_NAME=A Teeth Pain Stroy
rem set PROJECT_NICE_NAME=TPS
rem set PROJECT_PATH=Z:/TPS

set PROJECT_ADMIN=meera

set SOFTWARE_PATH=C:/Program Files

set PLUGIN_PATH=%PACKAGE_PATH%/plugins
set RESOURCES_PATH=%PACKAGE_PATH%/resources

set PYTHON_VERSION=2.7.6
set PYTHON_PATH=%PACKAGE_PATH%/resources/Python27/python.exe

set COMMON_PYTHONPATH=%RESOURCES_PATH%
set STARTUP_PYTHONPATH=%RESOURCES_PATH%/PyQt4-4.10-gpl-Py2.7-Qt4.8.4-x64
set GIMP_PYTHONPATH=%RESOURCES_PATH%/PyQt4-4.10-gpl-Py2.7-Qt4.8.4-x32
rem set BLENDER_PYTHONPATH=%RESOURCES_PATH%/PyQt4-4.10-gpl-Py3.3-Qt4.8.4-x64
set BLENDER_PYTHONPATH=%RESOURCES_PATH%/PyQt5-5.8.0-Py35_amd-x64
set MAYA_PYTHONPATH=%RESOURCES_PATH%/PyQt4-4.10-gpl-Py2.7-Qt4.8.4-x64
set NATRON_PYTHONPATH=%RESOURCES_PATH%/PyQt4-4.10-gpl-Py2.7-Qt4.8.4-x64

set PYTHONPATH=%PACKAGE_PATH%;%PLUGIN_PATH%;%COMMON_PYTHONPATH%

set GIMP_VERSION=2.9.8
set GIMP_PATH=C:/Program Files/GIMP 2/bin/gimp-2.8.exe
set GIMP_PLUGIN_PATH=%PACKAGE_PATH%/setup/gimp

set BLENDER_VERSION=2.79
set BLENDER_PATH=C:/Program Files/Blender Foundation/Blender/blender.exe
set BLENDER_PLUGIN_PATH=%PACKAGE_PATH%/setup/blender
set BLENDER_SYSTEM_PLUGINS=%PACKAGE_PATH%/setup/blender
set BLENDER_USER_PLUGINS=%PACKAGE_PATH%/setup/blender

set MAYA_VERSION=2016
set MAYA_PATH=C:/Program Files/Autodesk/Maya2016/bin/maya.exe
rem set MAYA_PLUGIN_PATH=%PACKAGE_PATH%/plugins/maya
set MAYA_SCRIPT_PATH=%PACKAGE_PATH%/setup/maya
set MAYA_SYSTEM_PLUGINS=%PACKAGE_PATH%/setup/maya
set MAYA_USER_PLUGINS=%PACKAGE_PATH%/setup/maya

set NARTON_VERSION=1.5
set NATRON_PATH=C:/Program Files/INRIA/Natron-2.3.7/bin/Natron.exe
set NATRON_PLUGIN_PATH=%PACKAGE_PATH%/setup/natron

set STUDIOPIPE_VERSION=1.5
set STUDIOPIPE_PATH=%PACKAGE_PATH%/pipe/studioPipe.py
set STUDIOPIPE_PLUGIN_PATH=%PACKAGE_PATH%/setup/studioPipe

set DATA_PATH=%PACKAGE_PATH%/data
set PLUGINS_PATH=%PACKAGE_PATH%/plugins

set ASSET_PATH=%PROJECT_PATH%/Asset
set ANIMATION_PATH=%PROJECT_PATH%/Animation
set RENDERING_PATH=%PROJECT_PATH%/Rendering
set COMPOSITING_PATH=%PROJECT_PATH%/Composting

set DATABASE_PATH=%PROJECT_PATH%/DataBase
set TOOLKIT_PATH=%PACKAGE_PATH%/toolKit
set ICON_PATH=%PACKAGE_PATH%/icons
set BIN_PATH=%PACKAGE_PATH%/bin

set PIPEINPUT_FILE=%PACKAGE_PATH%/pipe/pipeInput.json

set PACKAGE_BACKUP_PATH=Z:/package_backup

:  echo %PROJECT_NAME%
:  echo %PYTHONPATH%
: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :