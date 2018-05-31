
'''
Collect Toolkits v0.1 
Date : March 08, 2018
Last modified: March 08, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description


'''

import sys
import os
import warnings

from module import collectBundels

TOOLKIT_PATH = os.environ['TOOLKIT_PATH']

class Toolkits (object):

    def __init__(self, toolKitType=None):        
        
        self.bundle= collectModules (os.path.join(TOOLKIT_PATH, toolKitType)) 


def collectModules (path):     

    if not path :
        warnings.warn('argument is none')
 
    if not os.path.isdir(path) :
        warnings.warn('No such directory')
 
    bundles = {}
 
    for eachFolder in os.listdir(path):
 
        bundlePath = os.path.join(path, eachFolder)         
        
        if not os.path.isdir(bundlePath):            
            continue  
          
        buldleObject = collectBundels.Bundles (path=bundlePath , bundelType='wrapper')   
        wrapperBuldle = buldleObject.getValidBundles()   
 
        bundles.setdefault(eachFolder, wrapperBuldle)        
 
    return bundles


    #bundle = collectModules (os.path.join(TOOLKIT_PATH, 'Narton'))
    #print bundle
    