'''
Studio Asset v0.1
Date : June 01, 2018
Last modified: June 01, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module create and modify the asset attributes creations
 
example 
node = 'null1'
from assets import studioAsset
reload(studioAsset)  
sa = studioAsset.StudioAsset(node=node)
sa.create()
'''

import sys
import os
import datetime
import warnings
import pprint

from pipe import pipeLayout
from module import studioDatabase

from pymel import core as pymel
from maya import OpenMaya as openMaya

PRJECT_PATH = os.environ['PROJECT_PATH']
PROJECT_NICE_NAME = os.environ['PROJECT_NICE_NAME']
PROJECT_FULL_NAME = os.environ['PROJECT_FULL_NAME']
PRJECT_PATH = os.environ['PROJECT_PATH']
DATABASE_PATH = os.environ['DATABASE_PATH']
PACKAGE_PATH = os.environ['PACKAGE_PATH']
DATABASE_SOURCE = os.environ['DATABASE_SOURCE']


class StudioAsset(object):
    
    '''
    Description
        This Class can manage Asset Node and its validation.
        :param    node <str>     example 'null'
        
        :example to execute  
            node = 'null1'
            from assets import studioAsset
            reload(studioAsset)  
            sa = studioAsset.StudioAsset(node=node)
            sa.create()  
    '''  
   
    def __init__(self, node=None):

        if node:     
            self.node = pymel.PyNode(node)            
        else:
            self.node = self.getAssetNode()
            
        if not self.node:
            self.node = None
        
        self.attributes = { 'assetName': {'order': 1, 'type': 'string', 'value': ''}, 
                            'assetType': {'order': 2, 'type': 'string', 'value': ''},  
                            'modelVersion': {'order': 3, 'type': 'string', 'value': ''}, 
                            'modelLastModified': {'order': 4, 'type': 'string', 'value': ''}, 
                            'puppetVersion': {'order': 5, 'type': 'string', 'value': ''}, 
                            'puppetLastModified': {'order': 6, 'type': 'string', 'value': ''}, 
                            'renderLastModified': {'order': 7, 'type': 'string', 'value': ''}, 
                            'renderVersion': {'order': 8, 'type': 'string', 'value': ''}, 
                            'assetPath': {'order': 9, 'type': 'string', 'value': ''}, 
                            'LastModified': {'order': 10, 'type': 'string', 'value': ''}, 
                            'workStatus': {'order': 11, 'type': 'string', 'value': ''}
                           }    
    
    def create(self): 
        
        '''
            Description
                This function set will create custom asset attribute on asset node.    
                :Type - class function (method)       
                :param    None           
                :return   None
        '''  
        
        self.remove()       
        
        attributeList = setReorder(self.attributes)
        
        for eachOrder, eachAttribute in attributeList.iteritems():
            self.node.addAttr(eachAttribute, dt='string', k=True)      
            value = self.attributes[eachAttribute]['value']                  
            self.node.setAttr(eachAttribute, value)
            self.node.setAttr(eachAttribute, l=True)
        
    
    def remove(self):
        
        '''
            Description
                This function set will remove custom asset attribute on asset node.    
                :Type - class function (method)       
                :param    None           
                :return   None
        '''          
        
        for eachAttribute in self.attributes:            
            if not pymel.objExists('{}.{}'.format(self.node.name(), eachAttribute)):
                continue
            
            self.node.setAttr(eachAttribute, l=False)
            self.node.deleteAttr(eachAttribute)
            
            print 'attribute \"{}\" deleted from \"{}\"'.format(eachAttribute, self.node.name())

    
    def exists(self):
        
        '''
            Description
                This function set will check all custom asset attributes exists in asset node.    
                :Type - class function (method)       
                :param    None           
                :return   result <dict>
        '''  
        
        result = {False: [],
                  True: []}
        
        attributeList = setReorder(self.attributes)        
        for eachOrder, eachAttribute in attributeList.iteritems(): 
            if not pymel.objExists('{}.{}'.format(self.node.name(), eachAttribute)):                
                result.setdefault(False, []).append(eachAttribute)
            else:
                result.setdefault(True, []).append(eachAttribute)
                
        if result[False]:
            openMaya.MGlobal.displayWarning ('%s attributes are does not exists in %s.'% (', '.join(result[False]), self.node.name()))         
            return False
        else:
            return True

    
    def getValues(self):
        
        '''
            Description
                This function set will get custom asset attributes value on asset node attributes.    
                :Type - class function (method)       
                :param    None           
                :return   attributeValues <dict>
        '''  
        
        attributeValues = {}        
        attributeList = setReorder(self.attributes)
        for eachOrder, eachAttribute in attributeList.iteritems():
            
            if not pymel.objExists('{}.{}'.format(self.node.name(), eachAttribute)):
                continue
                
            currentValue = self.node.getAttr(eachAttribute)
            attributeValues.setdefault(eachAttribute, currentValue)  
        return attributeValues   
              
    
    def setValues(self, values):
        
        '''
            Description
                This function set will set custom asset attributes value on asset node attributes.    
                :Type - class function (method)       
                :param    None           
                :return   None
        '''  
                
        attributeList = setReorder(self.attributes)
        for eachOrder, eachAttribute in attributeList.iteritems():
            
            if not pymel.objExists('{}.{}'.format(self.node.name(), eachAttribute)):
                continue            
            
            if eachOrder not in values :
                continue
            
            self.node.setAttr(eachAttribute, l=False)
            self.node.setAttr(eachAttribute, values[eachOrder])       
            self.node.setAttr(eachAttribute, l=True)
            
            
    def getAssetNode(self):  
        
        '''
            Description
                This function set collect custom asset node in the scene.    
                :Type - class function (method)       
                :param    None           
                :return   None
        '''        
  
        #transforms = pymel.ls(type='transform')  
        transforms = pymel.ls(assemblies=1)
        nulls = []      
        for eachTransform in transforms :
            if eachTransform.getShapes():
                continue
            nulls.append(eachTransform)
            
        if not nulls:
            return None           
            
        if len(nulls)>1:
            return None
        
        self.node = nulls[0]
        
        #return nulls[0]
        
        
    def getAssets(self, assetType=None, dataType=None):
        
        '''
            Description
                This function set collect the specific assets from database or scene.    
                :Type - class function (method)       
                :param    assetType   <str>    example 'Props'
                :param    dataType    <str>     example 'database' or 'scenes'                
                :return   result      <list>    example ['Bat', 'Ball']
        '''            
        
        if not assetType:
            warnings.warn ('function getAssets argument \"assetType\" None') 
            return None         
        
        if not dataType:
            warnings.warn ('function getAssets argument \"dataType\" None') 
            return None 
        
        assets = self.getAllAssets(dataType=dataType)
        
        if not assets:
            warnings.warn ('function getAssets empty database') 
            return None

        
        if assetType not in assets:
            warnings.warn ('{} does not exists in the database'.format(assetType))  
            
        result = assets[assetType]          
        return result
    
            
    def getAllAssets(self, dataType=None):
        
        '''
            Description
                This function set collect the all assets from database or scene.    
                :Type - class function (method)       
                :param    dataType    <str>     example 'database' or 'scenes'                
                :return   result      <dict>    example  {'Props': ['Bed']} 
        '''            
                
        if not dataType:
            warnings.warn ('function getAssets argument \"dataType\" None') 
            return None         
                 
        assetTypeList = self.getAssetTypeList()        
        result = {}
        
        if dataType=='database':
            
            db = studioDatabase.Database (dataType='assets')
            db.getValue()
            databaseValue = db.value            
            
            for eachOrder,  eachValue in databaseValue.iteritems():
                currentAsset = eachValue['primary']['title']['label']['value']
                currentIndex = int(eachValue['primary']['catagory']['types']['value'])
                currentAssetType = assetTypeList[currentIndex-1]         
                result.setdefault(currentAssetType, []).append(currentAsset)
                
        if dataType=='scenes':            
            print '\nWork in progress'

        return result        
        
        
    def getAssetTypeList(self):
        
        pipe = pipeLayout.Layout (DATABASE_SOURCE)
        assetList = pipe._pipeAssetTypeList
        return assetList       


def setReorder (data) :   

    '''
    Description
        This method will sort the order of dictionary variable.
        
        :Type - standalone function (method)
        :param    data <dict>     example {'assetName': {'order': 1}, 'assetType': {'order': 2}
        :return   result <dict> 
        
        :example to execute  
            node = 'null1'
            from assets import studioAsset
            reload(studioAsset)  
            myData = {'assetName': {'order': 1}, 'assetType': {'order': 2}
            sa = studioAsset.setReorder(datd=myData)            
    '''       

    result = {}
    
    for eachKey, eachValue in data.iteritems():
        result.setdefault(eachValue['order'], eachKey)
    
    return result
        
#End####################################################################################################