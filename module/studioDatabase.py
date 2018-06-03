'''
Studio Database v0.1
Date : February 12, 2018
Last modified: February 12, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of Database fuctions    
'''

import os
import sys
import shelve
import anydbm
import json
import pprint

DATABASE_PATH = os.environ['DATABASE_PATH']

class Database (object):
    
    def __init__(self, **kwargs) :
        
        '''
            dataType    <str>    example 'asset'
            data        <dict>   example {'assetName': }        
            keys        <str>   example 'bat'          
        '''
        
        if 'dataType' in kwargs :         
            self.filePath = os.path.join(DATABASE_PATH, kwargs['dataType'], '{}.db'.format (kwargs['dataType'])) 
            
        if 'data' in kwargs :                   
            self.data = kwargs['data']
        
        if 'keyValue' in kwargs :
            self.keyValue = kwargs['keyValue']
            
        print 'self.filePath\t', self.filePath
                
    
    def create (self) :
        createDatabase (self.filePath, self.data)
    
    
    def getValue (self) :
        self.value = getDatabaseValue (self.filePath)            
    
    def hasValue (self) :
        self.hasValid = hasDatabaseValue (self.keyValue, self.filePath)        
        
    def createJson (self) :
        createJsonDatabase (self.filePath, self.data)    
    
    def getJsonValue (self) :
        self.value = getJsonDatabaseValue (self.filePath)            
    
    def hasJsonValue (self) :
        self.hasValid = hasJsonDatabaseValue (self.keyValue, self.filePath)
 
   
def createDatabase (filePath, data) :    
    
    if not os.path.isdir(os.path.dirname(filePath)) :
        os.makedirs(os.path.dirname(filePath))        

    result = 'successfully created Database {}'.format (filePath) 

    db = shelve.open(filePath)
    for eachKey, ecahValues in data.items() :
        
        #if db.has_key (str(eachKey)):
        
        #    a[5] = a.pop(3)

               
        try :
            db[str(eachKey)] = ecahValues
        except Exception as exceptResult :
            result = 'Error - {}'.format (exceptResult)
            
    db.close ()   
    
    #===========================================================================
    # db = shelve.open(filePath, flag='c')
    # db = data
    # 
    # db.close()
    #===========================================================================


def getDatabaseValue(filePath):
    
    if not os.path.isfile(filePath) :
        return None
    
    data = {}    
    db = shelve.open(filePath, flag='r')       
    for eachKey, ecahValues in db.iteritems() :        
        data.setdefault(str(eachKey), ecahValues)    
    db.close()
    
    return data
    

def hasDatabaseValue(currentKey, filePath):
    
    if not os.path.isfile(filePath) :
        return None        
    
    db = shelve.open(filePath, flag='r')
    
    result = False    
    
    if currentKey in db.keys() :           
        result = True
    
    return result

    
def createJsonDatabase (filePath, data) :    
    
    if not os.path.isdir(os.path.dirname(filePath)) :
        os.makedirs(os.path.dirname(filePath))        
    
    result = 'successfully created Database {}'.format (filePath) 
    
    try :   
        data = json.dumps (data, indent=4)         
        jsonData = open (filePath, 'w')
        jsonData.write (data)
        jsonData.close ()        
    except Exception as exceptResult :
        result = str (exceptResult)   
             
    print ('result\t- ', result)
    

def getJsonDatabaseValue(filePath):   
    
    jsonData = open (filePath, 'r')
    data = json.load (jsonData)
    jsonData.close ()    
    
    return data
    

def hasJsonDatabaseValue(currentKey, filePath):
    
    jsonData = open (filePath, 'r')
    data = json.load (jsonData)
    jsonData.close ()  
    
    result = False    
    if currentKey in data.keys() :          
        result = True
    
    return result

#End######################################################################################