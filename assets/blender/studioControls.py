'''
Control creation for Blender Puppet CS v1.0.0
Date : June 20, 2018
Last modified: June 20, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module for generate controls and manage the control shape for Puppet Creative Suite
 
example
    import imp
    from assets.blender import studioControls
    imp.reload(studioControls)
    biped = studioControls.Control()
    biped.create()
 
'''

import bpy
import imp
import pprint

from module import inputNames
from module import studioBlender

imp.reload(inputNames)
imp.reload(studioBlender)


class Controls(object):
    
    def __init__(self):
        
        self.input = inputNames.Names()
    
    
    def create(self, **kwargs):
        
        self.shape = 'CIRCLE'
        self.name = 'Temp_Ctrl'
        self.radius = self.input._scale
        
        if kwargs['shape']:
            self.shape = kwargs['shape']
    
        if kwargs['name']:
            self.name = kwargs['name']  
            
        if kwargs['radius']:
            self.radius = kwargs['radius']
            
        #create control shape        
        control = blenderEmptyObject(shape=self.shape, name=self.name, radius=self.radius)
        
        #create control group
        bpy.ops.object.empty_add(   type='PLAIN_AXES', 
                                    view_align=False, 
                                    location=(0,0,0)
                                    ) 
        bpy.context.object.name = '%s_%s'% (self.name, self.input._group)
        bpy.context.object.empty_draw_size = 0.0
        
        #parent the control to group
        control.parent = bpy.context.object        
        return control, bpy.context.object
        #return  control
        
    
def blenderEmptyObject (shape=None, name=None, radius=None):     
        
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.empty_add(type=shape, view_align=False, location=(0,0,0))    
    bpy.context.object.name = name
    bpy.context.object.empty_draw_size = radius 
    #bpy.context.object.show_name = True
    
    contextObject = bpy.context.object
    dataObject = bpy.data.objects[bpy.context.object.name]    
    
    return contextObject
