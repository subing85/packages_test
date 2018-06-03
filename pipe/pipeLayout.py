'''
mdule : pipeLayout
class : Layout
Date : February 09, 2018
Last modified: February 09, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface    
'''



import os
import json
import pprint
import warnings

CURRENT_PATH = os.path.dirname (__file__)

class Layout (object):
    
    def __init__ (self, *args) :
        
        '''
            :param     <str>    pipeInput.json file path         
        '''
                       
        self._pipes = None
        self._pipeAttributes = None
        self._pipeLayout = None
        
        self._publishLayouts = []
        
        if not args :            
            warnings.warn ('#TypeError: __init__() missing 1 required positional argument: filepath') 
            return None            
            
        if not os.path.isfile(args[0]):
            warnings.warn ('{} No such file.'.format(args[0]))           
            return None  
        
        self._pipeInput = args[0]
        
        pipeData = getPipeLayout (file=self._pipeInput) 
               
        self._pipes = pipeData['pipe']
        self._pipeAttributes = pipeData['pipe']['attributes']
        self._pipeLayout = pipeData['pipe']['layout']
        
        #self.pipeDefaul = getDefaultValue (pipeData['pipe']['attributes'])        
        
        self._publishLayouts = getPublishLayouts (self._pipeAttributes)
        self._pipeAssetTypeList = self._pipeAttributes['assets']['primary']['catagory']['types']['values']



def getPipeLayout (file=None) :
     
    '''
        Description
            This function set will collect all pipe layout inputs from json file             
            :param    file <str>    example /home/subin-g/pipeInput.json             
            :return    pipeData    <dict>
    '''
     
    if not file :        
        warnings.warn ('function getPipeLayout argument \"file\" None')        
        return False
     
    try :    
        openData = open (file, 'r')
        pipeData = json.load (openData)
        openData.close ()
    except Exception as result :
        raise Exception (result)      
        pipeData = None
         
    return pipeData    


def getPublishLayouts (attributes) :
    
    '''
        only get publish layouts, collect from secondary    
    '''    
    
    layouts = []
    
    #pprint.pprint (attributes)
    for eachAttribute, ecahValue in attributes.iteritems() :        
        for eachSecondory in ecahValue['secondary'] :
            layouts.append(eachSecondory)
    
    return layouts
    

def setReorder (data) :
     
    '''
        data = getPipeLayout ('/media/meera/FE5868105867C5CD/Project/MiniMovie/packages/pipe/pipeInput.json')
        abc = setReorder (data['pipe']['layout'])
        pprint.pprint (abc)
    '''
     
    sortResult = {}
    
    for eachKeys, eachValues in data.iteritems () :
        sortResult.setdefault(eachValues['order'], []).append (eachKeys)        
             
    result = []        
    for eachKeys, eachValues in sortResult.items () :        
        for eachItem in eachValues :
            result.append (str(eachItem))         
    return result


def setNestedReorder (data):

    sortResult = {}    
    catagoryData = {}
    #pipeData = {}
    
    for eachItem in data : 
        for eachKeys, eachValues in data[eachItem].iteritems () :            
                       
            sortResult.setdefault(eachValues['order'], []).append (eachKeys)            
            catagoryData.setdefault(eachKeys, eachValues)            
        #pipeData.setdefault(eachItem, data[eachItem])
            
    result = []        
    for eachKeys, eachValues in sortResult.items () :        
        for eachItem in eachValues :
            result.append (str(eachItem))   
                  
    return result, catagoryData


def getDefaultValue (data) :
    
    defaluDatabase = {}
    
    for eachItem in data :      
        for eachkey, eachValue in data[eachItem].iteritems () : 
                  
            defaluDatabase.setdefault(eachkey.encode(), eachValue)
    
    return defaluDatabase