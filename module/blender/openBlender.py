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



def getObjectContext(node):    
    pass


def getObjectData(node):
    objects = bpy.data.objects[node]
    return objects    


def getObjectOpp(node):
    pass



