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



