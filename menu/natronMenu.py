'''
Blender Menu v0.1
Date : March 15, 2018
Last modified: March 15, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface 
 
example   
from menu import gimpMenu
reload(gimpMenu)
window = gimpMenu.Menu()
window.show ()      

'''


import sys
import os
import datetime
import getpass
import warnings
import pprint

from functools import partial

from module import collectToolKit
from module import jsonManager

PROJECT_NICE_NAME = os.environ['PROJECT_NICE_NAME']
PLUGINS_PATH = os.environ['PLUGINS_PATH']


class Menu (object):
    
    def __init__(self):
        pass
    
    
        path = '{}/natron/initGui.py'.format (PLUGINS_PATH)        
        command, definitions = self.getMenuCommand()     
           
        self.createMenuFile (path, command, definitions)  
        
    
    def createMenuFile (self, path, command, definitions):
        
        menuDefinitions, menuCommands = self.getMenuCommand()   
        
        if os.path.isfile(path) :
            
            try :
                os.chmod (path, 0777)
                os.remove (path)
            except Exception, result :
                warnings.warn (result)
        
        
        comment = ['#Natron Menu v0.1',
                   '#Form implementation generated from natronMenu module',
                   '#Created: {}'.format(datetime.datetime.now().strftime('%d:%m:%Y - %I:%M:%S:%p')),
                   '#    by: {}'.format(getpass.getuser()),
                   '#WARNING! All changes made in this file will be lost!\n\n'
                   ]       
        
        try :        
            menuData = open(path, 'w')        
            menuData.write('\n'.join (comment + menuDefinitions + ['\n'] + menuCommands))        
            menuData.close ()
        except Exception, result :
            warnings.warn (result)       
                     
                     
    def getMenuCommand (self):
        
        menuCommands = []        
        menuDefinitions = []        
   
        toolKit = collectToolKit.Toolkits(toolKitType='Narton')        
        
        for eachFolder, bundles in toolKit.bundle.iteritems():            
            for eachModule, bundleData in bundles.iteritems():                
                grouping = '{}/{}/{}s'.format(PROJECT_NICE_NAME, eachFolder, bundleData['__name__'])
                function = bundleData['__name__']
                key = 'QtCore.Qt.Key.Key_L'
                modifiers = 'QtCore.Qt.KeyboardModifier.ShiftModifier'              
                               
                menuLine = 'NatronGui.natron.addMenuCommand (\'{}\', \'{}\', {}, {})'.format (grouping, function, key, modifiers)                
                menuCommands.append (menuLine)
                
                currentModule = 'def {}():\n\tfrom toolKit.Narton.{} import {}\n\tresult = {}.trailRun()\n'.format (function, eachFolder, bundleData['__name__'],  bundleData['__name__'])    
                menuDefinitions.append (currentModule)
                                
        return menuDefinitions, menuCommands   

#End######################################################################################    


