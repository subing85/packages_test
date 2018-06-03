'''
Blender Menu v0.1
Date : May 30, 2018
Last modified: May 31, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to load custom maya menu
 
example   
from menu import mayaMenu
reload(mayaMenu)
window = mayaMenu.Menu()
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
from pymel import core as pymel

PROJECT_NICE_NAME = os.environ['PROJECT_NICE_NAME']
PLUGINS_PATH = os.environ['PLUGINS_PATH']

class Menu (object):
    
    def __init__(self):    
        
        menuList = self.getMenuItems()         
        self.createMenu(menuList)              
        
    
    def createMenuFile (self, path, command, definitions):        
        pass         

    
    def createMenu(self, menuList):
        
        mayaWindow = 'MayaWindow'
        menuName = 'myMenu'
         
        if pymel.menu(menuName, q=True, ex=True):    
            abc = pymel.menu(menuName, e=True, dai=True)
            abc.delete()   
             
        pymel.setParent(mayaWindow)
        projectMenu = pymel.menu(menuName, p=mayaWindow, l=PROJECT_NICE_NAME, to=True)

        for folderMenu, toolSubMenus,  in menuList.iteritems():            
            folderMenu = pymel.menuItem(l=folderMenu, sm=True, to=True, p=projectMenu)
            
            for eachTool in toolSubMenus:                              
                   
                pymel.menuItem( l=toolSubMenus[eachTool]['name'], 
                                sm=False, to=False, 
                                ann=toolSubMenus[eachTool]['comments'], 
                                p=folderMenu,
                                c=toolSubMenus[eachTool]['command']) 
                
                #print '\n', toolSubMenus[eachTool]['command']               
                #print toolSubMenus[eachTool]['command']
                
                                     
    def getMenuItems (self):
        
        menuList = {}
        toolKit = collectToolKit.Toolkits(toolKitType='Maya')  
                            
        for eachFolder, bundles in toolKit.bundle.iteritems():                            
            modules = {}                             
            for eachModule, bundleData in bundles.iteritems():
                modules[bundleData['ORDER']] = {'name': bundleData['NAME'], 
                                                'comments': bundleData['COMMENTS'],
                                                'folder': eachFolder,
                                                'module': bundleData['__name__'],
                                                'type': bundleData['TYPE'], 
                                                'date': bundleData['DATE'], 
                                                'author': bundleData['AUTHOR'], 
                                                'version': bundleData['VERSION'],
                                                'command': 'from toolKit.Maya.{} import {}\nresult = {}.trailRun()'.format(eachFolder, 
                                                                                                                           bundleData['__name__'],
                                                                                                                           bundleData['__name__'])                                                 
                                                }
                         
            menuList.setdefault(eachFolder, modules)             
            
        #pprint.pprint (menuList)
        return menuList

#End######################################################################################