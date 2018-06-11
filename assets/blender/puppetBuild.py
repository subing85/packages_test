'''
Build Puppet for Blender Puppet CS v1.0.0
Date : June 11, 2018
Last modified: June 29, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module for generate puppet for Puppet Creative Suite
 
Example
    import imp
    from assets.blender import buildPuppet
    imp.reload(buildPuppet)
    build = buildPuppet.Build()
    build.create()  
'''
from module.studioBlender import extrudeBone


class Build(object):
    
    def __init__(self):
        pass
    
    
    def create(self):
        
        legSkeletons = ['L_Pelvis', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
        spineSkeletons = ['Cog', 'SpineA', 'SpineB', 'Chest', 'NeckA', 'NeckB', 'Head', 'HeadTail']
        
        puppetBones = {1: {'extrude': 3, 'pos'}}
        
        
        print ('Work in progress.......................')  
 