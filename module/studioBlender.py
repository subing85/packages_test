'''
Open Blender v1.0.0
Date : March 30, 2018
Last modified: March 30, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage the Blender Object API
 
'''

import bpy
import warnings
import pprint

class OpenBlender(object):
    
    '''
    Description
        This Class access to blender data and utility functions.
        :param    None
                
        :example to execute  
            from module import studioBlender
            reload(studioBlender)  
            ob = studioBlender.OpenBlender()
    '''
    
    def __init__(self):        
        
        pass
    
    
    def getObjects(self):
        
        '''
        Description
            Function set for get the objects from scene.
                        
            :Type - class function (method)            
            :param    None
            :return   attributes _objects, _typeObjects            
            :example to execute        
                from module import studioBlender
                reload(studioBlender)  
                ob = studioBlender.OpenBlender()
                ob.getObjects()            
                print ob._objects
                print ob._typeObjects    
        '''    
        
        result = objectList()        
        self._objects = result[0]        
        self._typeObjects = result[1]
        
        
    def getSpecifyObjects(self, objectType=None):

        '''
        Description
            Function set for get the objects based on the argument from scene, argument should object type.
                        
            :Type - class function (method)            
            :param    objectType    <str>    example 'MESH'
            :return   attributes _specifyObjects            
            :example to execute        
                from module import studioBlender
                reload(studioBlender)  
                ob = studioBlender.OpenBlender()  
                ob.getSpecifyObjects(objectType='MESH')              
                print ob._specifyObjects
        '''
        
        self._specifyObjects = None 
                
        if not objectType:
            warnings.warn('Please specify the object type argument called \"objectType\"')     
            return None            
        
        result = objectList() 

        if objectType not in result[1]:
            warnings.warn('\"%s\" does not exist in your scene'% objectType)     
            return None
               
        self._specifyObjects = result[1][objectType]
        
    
    def objExists(self, node=None):
        
        if not node:
            warnings.warn('FUnction set \"node\" argument empty')     
            return None               
        
        result = objectList()        
        
        if node not in result[0]:            
            return False
        
        return True
    

         
        
        
    def getAllObjects(self):
        
        '''
        Description
            Function set for get all objects from scene.
                        
            :Type - class function (method)            
            :param    None
            :return   result[0]    <list>
            :example to execute        
                from module import studioBlender
                reload(studioBlender)  
                ob = studioBlender.OpenBlender()  
                allObjects = ob.getAllObjects()              
                print allObjects
        ''' 
        
        result = objectList()        
        return result[0]
    
    
    def getAllTypeObjects(self):
        
        '''
        Description
            Function set for get all objects  based object type from scene.
                        
            :Type - class function (method)            
            :param    None
            :return   result[1]    <dict>
            :example to execute        
                from module import studioBlender
                reload(studioBlender)  
                ob = studioBlender.OpenBlender()  
                allTypeObjects = ob.getAllTypeObjects()              
                print allTypeObjects
        '''         
        
        result = objectList()        
        return result[1]   
        

def objectList ():
    
    allObects = bpy.context.scene.objects                
    nameObject = {}
    typeObject = {}

    for eachObject in allObects: 
        nameObject.setdefault(eachObject.name, eachObject.type)
        typeObject.setdefault(eachObject.type, []).append(eachObject.name)
        
    return nameObject, typeObject


def createEmptyObject (type, align, location, radius, name):  
    
    '''
    Description
        Standalone Function for create Empty blender Object based on inputs                        
        :Type - class function (method)            
        :param   type    <str>  example 'SPHERE'
        :param   align    <bool>   False
        :param   location   <tuple>    (0, 0, 0)
        :param   name    <str>    example 'Puppet_Joint'
        :param   radius    <float>    example 0.22
        :return currentJoint    <<class 'bpy_types.Object'>> 
    '''  
    
         
    if bpy.data.objects.get(name) :
        try :
            bpy.data.objects[name].select = True
            #bpy.ops.object.delete(use_global=False)
            bpy.data.objects.remove(bpy.data.objects[name], True)   
        except Exception as result:
            warnings.warn ('node remove error', result)       
     
    bpy.ops.object.empty_add(type=type, view_align=align, location=location)    
    bpy.context.object.name = name
    bpy.context.object.empty_draw_size = radius 
    #bpy.context.object.show_name = True
    
    contextObject = bpy.context.object
    dataObject = bpy.data.objects[bpy.context.object.name]    
    
    return contextObject


def setParent (source, target):
    
    bpy.ops.object.select_all(action='DESELECT')
    
    sourceNode = bpy.data.objects[source]
    targetNode = bpy.data.objects[target] 
    
    #b.parent = a    
    targetNode.select = True     #select the object for the 'parenting'
    sourceNode.select = True
    bpy.context.scene.objects.active = targetNode    #the active object will be the parent of all selected object    
    #bpy.ops.object.parent_set()
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    
    
def setMirror(nodes, axis, search, replace):
    
    '''
    Description
        Function for duplicat the input object place to like a mirror                      
        :Type     standalone function            
        :param    nodes   <list>     example ['L_Pelvis', 'L_Knee', 'L_Ankle']
        :param    axis    <tuple>    example (-1, 1, 1)
        :param    search  <str>      example 'L_'
        :param    replace <str>      example 'R_'
        
        :retun    duplicats <dict>    example ('L_Pelvis': 'R_Pelvis', 'L_Knee',: 'R_Knee', 'L_Ankle': 'R_Ankle')
        
    ''' 
    
    if not nodes:
        warnings.warn('nodes are none or empty')
        return None    
    
    for eachNode in nodes:
        if not bpy.data.objects.get(eachNode) :
            print ('no such object in the scene\t', eachNode)
            continue
        
        nodeName = eachNode.replace(search, replace)        
        
        if bpy.data.objects.get(nodeName) :
            try :
                bpy.data.objects[nodeName].select = True
                bpy.data.objects.remove(bpy.data.objects[nodeName], True)   
            except Exception as result:
                warnings.warn ('node remove error', result)           
      
        #mirror value
        bpy.ops.object.select_all(action='DESELECT')             
        sourceNode = bpy.data.objects[eachNode]
        sourceNode.select = True
        bpy.context.scene.objects.active = sourceNode
            
        value = sourceNode.location        
        x, y, z = value.x*axis[0], value.y*axis[1], value.z*axis[2]        
        #duplicate the object
        bpy.ops.object.duplicate()
        duplicates =  bpy.context.object        
              
        duplicates.location = (x, y, z) # set duplicate value        
        duplicates.name = nodeName
         
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')


def getObjectContext(node):    
    pass


def getObjectData(node):
    objects = bpy.data.objects[node]
    return objects    


def getObjectOpp(node):
    pass


def extrudeBone(size=None):
    
    #extrude bones(create bones)  
    bpy.ops.object.mode_set(mode='EDIT')
     
    for index in range (size):
        bpy.ops.armature.extrude()
        bpy.ops.transform.translate(value=(0,0,1))
        
def createBones(armature=True, fitJoints=None, parent=True):
    
    pass
        

def createBones_(armature=True, fitJoints=None, parent=True):
    
    '''
    Description
        Function for create Armature Bones based on the input arguments                      
        :Type     standalone function            
        :param    fitJoints   <[str]>     example  ['L_Pelvis', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
        :param    parent    <bool>      example True or False        
        :retun    bones <[str]>    example ['L_Pelvis': 'R_Pelvis', 'L_Knee',: 'R_Knee', 'L_Ankle': 'R_Ankle']
        
    ''' 
    
    #create armature
    if armature:
        bpy.ops.object.armature_add(location=(0, 0, 0))   
        object = bpy.context.scene.objects.active   
        object.name = 'FitSkeleton'
        armature = object.data
        armature.name = 'Armature'
        
    object = bpy.context.scene.objects.active   
     
    #extrude bones(create bones)  
    bpy.ops.object.mode_set(mode='EDIT')
     
    for index in range (3):
        bpy.ops.armature.extrude()
        bpy.ops.transform.translate(value=(0,0,1))
     
    bpy.ops.object.mode_set(mode='OBJECT')
    object = bpy.context.scene.objects.active    
         
    #fitJoints = ['L_Pelvis', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
     
    #rename the bones
    boneList = object.data.bones.values()    
    for index in range(len(boneList)):
        poseBone = object.pose.bones.get(boneList[index].name)    
        poseBone.name = fitJoints[index]
     
    bpy.ops.object.mode_set(mode='EDIT')
    object = bpy.context.scene.objects.active    
    armatureBoneList = object.data.edit_bones
     
    for index in range (len(armatureBoneList)):        
        skeletonObject = bpy.data.objects[fitJoints[index]]        
        location = skeletonObject.location
        #rotation = skeletonObject.rotation_euler       
        armatureBoneList[index].head = location
         
    toeSkeletonObject = bpy.data.objects[fitJoints[-1]]        
    toeLocation = toeSkeletonObject.location
    armatureBoneList[-1].tail = toeLocation
    
    return armatureBoneList


   
    
#End##########################################################################################