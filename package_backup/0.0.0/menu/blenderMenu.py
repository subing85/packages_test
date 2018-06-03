'''
Natron Menu v0.1
Date : March 10, 2018
Last modified: March 11, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module will generate dynamic menu for natron.
    
    https://wiki.blender.org/index.php/Dev:2.5/Source/Installation/EnvironmentVariables#BLENDER_VERSION_.28and_BLENDER_VERSION_PREV.29   

 BLENDER_USER_BASE=${HOME}/.blender/${BLENDER_VERSION}
 BLENDER_SYSTEM_BASE=${BLENDER_SHARE}/${BLENDER_VERSION}
 BLENDER_USER_DATAFILES=${HOME}/.blender/${BLENDER_VERSION}/datafiles
 BLENDER_SYSTEM_DATAFILES=${BLENDER_SHARE}/${BLENDER_VERSION}/datafiles
 BLENDER_USER_PY=${HOME}/.blender/${BLENDER_VERSION}/py
 BLENDER_SYSTEM_PY=${BLENDER_SHARE}/${BLENDER_VERSION}/py
 BLENDER_USER_PLUGINS=${HOME}/.blender/${BLENDER_VERSION}/plugins
 BLENDER_SYSTEM_PLUGINS=${BLENDER_SHARE}/${BLENDER_VERSION}/plugins:${MOVIE_PROJECT}/plugins

'''



import os
import pprint
import datetime
import getpass 

from functools import partial

from module import collectToolKit

#PROJECT_NICENAME = os.environ['PROJECT_NICENAME']
PROJECT_NICENAME ='TPS'
#PLUGINS_PATH = os.environ['PLUGINS_PATH']


class Menu (object):

    def __init__(self):
        
        #path = '{}/natron/initGui.py'.format (PLUGINS_PATH)        
        command, definitions = self.getMenuCommand()     
           
        #self.createMenuFile (path, command, definitions)  
        
    
    def createMenuFile (self, path, command, definitions):    
        
        pass   


                 
                     
    def getMenuCommand (self):
        
        menuCommands = []        
        menuDefinitions = []        
   
        toolKit = collectToolKit.Toolkits(toolKitType='Blender')      
        
        for eachFolder, bundles in toolKit.bundle.items():            
            for eachModule, bundleData in bundles.items(): 
                
                print (eachFolder, eachModule, bundleData['__name__'])
                               
                #===============================================================
                # grouping = '{}/{}/{}s'.format(PROJECT_NICENAME, eachFolder, bundleData['__name__'])
                # function = bundleData['__name__']
                # key = 'QtCore.Qt.Key.Key_L'
                # modifiers = 'QtCore.Qt.KeyboardModifier.ShiftModifier'              
                #                 
                # menuLine = 'NatronGui.natron.addMenuCommand (\'{}\', \'{}\', {}, {})'.format (grouping, function, key, modifiers)                
                # menuCommands.append (menuLine)
                #  
                # currentModule = 'def {}():\n\tfrom toolKit.Narton.{} import {}\n\tresult = {}.trailRun()\n'.format (function, eachFolder, bundleData['__name__'],  bundleData['__name__'])    
                # menuDefinitions.append (currentModule)
                #===============================================================
                                
        return menuCommands, menuDefinitions    
    
Menu ()   

      
#===============================================================================
# import bpy
# 
# 
# def menu_draw(self, context):
#     self.layout.operator("wm.save_homefile")
# 
# bpy.types.INFO_HT_header.append(menu_draw)       
#     
#===============================================================================
#End######################################################################################