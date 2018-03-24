'''
JSON Manager
Date : March 11, 2018
Last modified: March 11, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module is can manage encode the python objects as JSON strings, and decode JSON strings into Python objects.
   
'''

import os
import json
import warnings
import datetime
import pprint
import getpass
import time


class JManager (object):
    
    '''
    Description
        This module can manage encode the python objects as JSON strings, and decode JSON strings into Python objects.
        
        :param    file <str>     example '/home/subin-g/pipeInput.json'
        :param    data <dict>    example {}        
        :attribute object.file    <str>  Return a copy of the string file
        :attribute object.data    <dict> Return a copy of the dict data                
        :attribute object.pythonObject    <dict> Return a copy of the dict from data       
        
    '''     
    
    def __init__(self, **kwargs): 
        
        self._file = None
        self._data = None
        
        self._comment = None
        self._description = None
        self._dataType =None        
        self._currentTime = time.time ()
       
        if 'file' in kwargs :        
            self._file = kwargs['file']
            
        if 'data' in kwargs :            
            self._data = kwargs['data']             
            
        if 'comment' in kwargs :            
            self._comment = kwargs['comment']             
            
        if 'description' in kwargs :            
            self._description = kwargs['description']   
            
        if 'dataType' in kwargs :            
            self._dataType = kwargs['dataType'] 

        if 'currentTime' in kwargs :            
            self._currentTime = kwargs['currentTime'] 
            
    
    def getJsonData (self):
        
        '''           
            Description
                Type - class function (method)
                Deserialize(decode) string or unicod instance containing a JSON document to a Python object.   

                :param    None                
                :attribute object.pythonObject    <dict> Return a copy of the dict from data            
        ''' 
        
        if not self._file :
            warnings.warn ('function getPipeLayout argument \"file\" None')        
            return None           

        self._pythonObject = readJsonData (self._file)
        

    def setJsonData (self): 
          
        '''           
            Description
                Type - class function (method)
                encode python object to Json string or unicod instance containing a JSON document to a Python object.   
                serialize(encode) string or unicod instance containing a Python object to JSON document.   

                :param    None                
                :attribute None   
        '''   
        
        print 'self._data', self._data     
             
        writeJsonData (self._file, self._comment, self._description, self._dataType, self._data, self._currentTime)
    
    

def readJsonData (file):
    
    '''           
        Description
            Type - standalone function
            Deserialize(decode) string or unicod instance containing a JSON document to a Python object.   

            :param    None                
            :attribute object.pythonObject    <dict> Return a copy of the dict from data            
    '''
     
    if not file :        
        warnings.warn ('function getPipeLayout argument \"file\" None')        
        return False
    
    if not os.path.isdir(os.path.dirname(file)):
        try :
            os.makedirs(os.path.dirname(file))
        except Exception as result :
            raise Exception (result)      
                  
    try :    
        openData = open (file, 'r')
        pythonObject = json.load (openData)
        openData.close ()
    except Exception as result :
        raise Exception (result)      
        pythonObject = None
         
    return pythonObject    


def writeJsonData (filePath, comment, description, dataType, data, currentTime):    
    
    '''           
        Description
            Type - standalone function
            encode python object to Json string or unicod instance containing a JSON document to a Python object.   
            serialize(encode) string or unicod instance containing a Python object to JSON document.   

            :param    None                
            :attribute None   
    '''  
    
    if not os.path.isdir(os.path.dirname(filePath)) :
        os.makedirs(os.path.dirname(filePath))
        
    
    if os.path.isfile(filePath) :
        os.chmod (filePath, 0777)
        os.remove(filePath)            
    
    result = 'successfully created Database {}'.format (filePath) 
    currentTime = datetime.datetime.now().strftime('%d-%m-%Y : %I-%M-%S-%p')
    
    genericData = { 'Comment': comment,
                    'Date': currentTime,
                    'Last modified': currentTime,
                    'Author': 'Subin. Gopi (subing85@gmail.com)',
                    'Created by': getpass.getuser(),
                    'WARNING': '# WARNING! All changes made in this file will be lost!',
                    'Description': description,
                    'Data type': dataType
                    }
    
    genericData.update (data)  
    
    pprint.pprint (genericData)
              
    
    try :   
        data = json.dumps (genericData, indent=4)         
        jsonData = open (filePath, 'w')
        jsonData.write (data)
        jsonData.close () 
                 
        os.utime(filePath, (currentTime, currentTime))
        
    except Exception as exceptResult :
        result = str (exceptResult)   
             
    print ('result\t- ', result)

#End#########################################################################################