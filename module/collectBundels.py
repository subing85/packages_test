'''
Bundles Modules v0.1
Date : February 16, 2018
Last modified: February 14, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of Bundles for validate and extractor.    

'''

import os
import sys
import warnings
import pkgutil
import inspect
import py_compile
import pprint


class Bundles (object) :
    
    def __init__(self, path=None, bundelType=None) :
        
        if not path :
            warnings.warn ('class \"Bundles\" argument \"path\" None or emty')        
            
        if not bundelType :
            warnings.warn ('class \"Bundles\" argument \"bundelType\" None or emty')
            
        self.bundleType = bundelType            
        self.bundlePath = path         
                       

    def createBundles (self):
        
        warnings.warn ('work in progress')

    
    def getValidBundles (self) :  
                
        bundles = collectBundles (self.bundlePath, self.bundleType)        
        return bundles
    
    
    def getPythonBundles (self, exculeFolders) :
        
        bundles = collectValidBundles (self.bundlePath, exculeFolders)
        return bundles


def collectBundles (path, bundleType):
    
    if not path :
        warnings.warn ('Function \"getBundles\" argument \"path\" None or emty')
        
    if not os.path.isdir(path) :
        warnings.warn ('{} - No such directory'.format(path))
  
    bundleData = {}        
 
    for module_loader, name, ispkg in pkgutil.iter_modules([path]) :                       
        loader = module_loader.find_module(name)         
          
        module = loader.load_module (name)
        print (module_loader, name, module)
        
        if not hasattr(module, 'TYPE') :
            continue
               
        if module.TYPE!=bundleType and module.TYPE!='None':
            continue 
                    
        moduleMembers = {}                
        for moduleName, value in inspect.getmembers (module) :           
            moduleMembers.setdefault (moduleName, value)    
       
        bundleData.setdefault (module, moduleMembers)
       
    return bundleData


def reorder (data, key) :
   
    result = {}

    ing = 0
    for eachKey, eachValue in data.items () :
       
        #=======================================================================
        # if key not in eachValue :
        #     continue
        #=======================================================================
       
        if eachValue[key] :       
            ing = eachValue[key]
       
        if not eachValue[key] :           
            ing+=1
       
        if eachValue[key] in result :
            ing = eachValue[key] + 1              
               
        result.setdefault(ing, eachKey)
       
    return result  


def collectValidBundles (path, exculeFolders):
    
    '''
    Description
        Type - standalone function
        To validate the python code.   
                
        :param    path    <str>         exxample 'Z:\packages'
        :param    exculeFolders <list>  example ['resources', 'plugins', 'bin', 'icons']
        
        :return   result    <dict>      example {    'validModules', {currentFile, 'True'},
                                                     'unvalidModules', {currentFile, str(reult)}}       
    '''
    
    validResult = {  'validModules': {},
                'unvalidModules': {}}
    
    for root, dirs, files in os.walk (path): 
        for eachFile in files:
            currentFile = os.path.abspath(os.path.join(root, eachFile))            
            exists = True
            
            for eachExclude in exculeFolders:
                if currentFile.startswith (os.path.abspath(os.path.join(path, eachExclude))) :
                    exists = False
                    continue 
                            
            if not exists :
                continue                                            
            if not currentFile.endswith('.py'):                
                continue            
               
            try :                    
                #module_loader = imp.load_source('', currentFile)
                py_compile.compile(currentFile)                
                validResult.setdefault('validModules', {currentFile, 'True'})
                  
            except Exception as compailResult:                
                validResult.setdefault('unvalidModules', {currentFile, str(compailResult)})
                
            print  ('validModules', currentFile, 'True')
                
    return validResult

#End############################################################################