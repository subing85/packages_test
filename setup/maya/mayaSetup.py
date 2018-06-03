'''

userSetup v0.1 
Date : May 31, 2018
Last modified: May 31, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module to manage the startup script, ie any script can run with Maya launch.
'''

import os
from pymel import core as pymel

def customSetup():

    PROJECT_PATH = os.environ['PROJECT_PATH']
    PROJECT_NICE_NAME = os.environ['PROJECT_NICE_NAME']
    PROJECT_FULL_NAME = os.environ['PROJECT_FULL_NAME']
    
    pymel.mel.eval('setProject(\"{}\")'.format(PROJECT_PATH))
    pymel.workspace(fr=('images', 'renderData'))
    pymel.workspace(fr=('scripts', 'scripts'))
    pymel.workspace(fr=('renderData', 'renderData'))
    pymel.workspace(fr=('fluidCache', 'cache'))
    pymel.workspace(fr=('fileCache', 'cache'))
    pymel.workspace(fr=('shaders', 'renderData'))
    pymel.workspace(fr=('3dPaintTextures', 'renderData'))
    pymel.workspace(fr=('mel', 'scripts'))
    pymel.workspace(fr=('furFiles', 'renderData'))
    pymel.workspace(fr=('OBJ', 'data'))
    pymel.workspace(fr=('scene', 'scene'))
    pymel.workspace(fr=('alembicCache', 'cache'))
    pymel.workspace(fr=('sourceImages', 'sourceImages'))
    pymel.workspace(fr=('furImages', 'renderData'))
    pymel.workspace(fr=('mentalRay', 'renderData'))
    pymel.workspace(fr=('movie', 'movie'))
    pymel.workspace(fr=('audio', 'sound'))
    pymel.workspace(fr=('sound', 'sound'))
    pymel.workspace(fr=('mayaAscii', 'scenes'))
    pymel.workspace(fr=('autoSave', 'autoSave'))
    pymel.workspace(fr=('diskCache', 'cache'))
    pymel.workspace(fr=('mayaBinary', 'scenes'))     
     
    #Units
    pymel.mel.eval('setUpAxis \"y\" ;')
    pymel.currentUnit(  linear='centimeter', 
                        time='pal', 
                        angle='degree')
    
    pymel.playbackOptions(min=1, max=25, ast=1, aet=25)   
    #playbackOptions -min 1 -max 120 -ast 1 -aet 200
    pymel.currentTime(1)  
    
    pymel.playbackOptions(v='all')
    pymel.playbackOptions(l='continuous')
    pymel.playbackOptions(ps=0)      
      
    #settings
    pymel.mel.eval('setAttributeEditorVisible 0 ;')
    pymel.mel.eval('setChannelsLayersVisible 1 ;')
    pymel.optionVar(fv=('defaultCameraNearClipValue', 1))
    pymel.optionVar(fv=('defaultCameraFarClipValue', 1000000))
    pymel.undoInfo(state=True, infinity=True)
       
    #load plugins
    plugins = { 'vray': 'C:/Program Files/Autodesk/Maya2016/vray/plug-ins/vrayformaya.mll',
                'xgenVRay': 'C:/Program Files/Autodesk/Maya2016/vray/plug-ins/xgenVRay.py',            
                'AbcExport': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/AbcExport.mll',
                'AbcImport': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/AbcImport.mll',
                'animImportExport': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/animImportExport.mll',
                'gpuCache': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/gpuCache.mll',
                #'ik2Bsolver': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/ik2Bsolver.mll',
                #'ikSpringSolver': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/ikSpringSolver.mll',
                #'MayaMuscle': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/MayaMuscle.mll',
                'objExport': 'C:/Program Files/Autodesk/Maya2016/bin/plug-ins/objExport.mll',
                'fbxmaya': 'C:/Program Files/Autodesk/Maya2016/plug-ins/fbx/plug-ins/fbxmaya.mll',
                }
        
    for eachPlugin, pluginPath in plugins.iteritems():
        try:
            pymel.loadPlugin(pluginPath, qt=True)
        except Exception as result:
            print result            
    
    #pymel.mel.eval('unifiedRenderGlobalsWindow;') 
    #pymel.mel.eval('updateRendererUI;')    
         
    #===========================================================================
    # #render global settings    
    # defaultRenderGlobals = pymel.PyNode('defaultRenderGlobals')    
    # defaultRenderGlobals.setAttr('currentRenderer', 'vray')
    # pymel.mel.eval('updateRendererUI;')
    # 
    # try :        
    #     pymel.setAttr('vraySettings.width', 1920)
    #     pymel.setAttr('vraySettings.height', 1080)
    #     pymel.setAttr('vraySettings.aspectLock', True)
    #     pymel.setAttr('defaultResolution.lockDeviceAspectRatio', True)
    #     pymel.setAttr('vraySettings.aspectRatio',  1.778)
    #     pymel.setAttr('vraySettings.pixelAspect',  1.00)
    # except :
    #     pass
    #===========================================================================
       
    #pymel.window('unifiedRenderGlobalsWindow', e=1, vis=0)
    
    #call scripts
    from menu import mayaMenu
    reload(mayaMenu)
    window = mayaMenu.Menu()

    print('\n---------------------------------------------------------------------------------------------') ;
    print('Successful loaded custom settings for the project called \"%s\"'% PROJECT_FULL_NAME) ;
    print('Copyright c2018 Subin Gopi reserch and development - All Rights Reserved. subing85@gmail.com') ;
    print('---------------------------------------------------------------------------------------------\n\n') ;

#End#############################################################################