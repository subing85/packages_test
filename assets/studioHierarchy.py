'''
StudioHierarchy v0.1
Date : May 31, 2018
Last modified: May 31, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module create and modify the asset Hierarchy
 
example   
from assets import studioHierarchy
reload(studioHierarchy)
studioHierarchy = studioHierarchy.StudioHierarchy(assetName='Bat')
studioHierarchy.create()

'''

from maya import OpenMaya as openMaya
from pymel import core as pymel


class StudioHierarchy(object):    
        
    def __init__(self, **kwargs):
        
        self.assetName = 'None'
        
        if 'assetName' in kwargs:            
            if kwargs['assetName']==None:
                self.assetName = 'None'            
            else:            
                self.assetName = kwargs['assetName']
            
        self.groups = [ 'Control_Group', 
                        'Offset', 
                        'Controls', 
                        'Geometry_Group', 
                        'Layout', 
                        'Animation', 
                        'Render', 
                        'Deformer_Group', 
                        'Skeleton_Group', 
                        'Texture_Group', 
                        'Lighting_Group', 
                        'Efx_Group' 
                        ]                 
    
    def create(self):   
        
        existGroups = []
        
        allGroups = self.groups + [self.assetName, 'World', 'Transform']     
        
        for eachGroup in allGroups:
            if not pymel.objExists(eachGroup):
                continue            
            existGroups.append(eachGroup)
            
        if existGroups:
            openMaya.MGlobal.displayWarning ('%s Object is already exists.'% ', '.join(existGroups))         
            return False 
          
        assetGroup = pymel.group (em=1, n=self.assetName)  
          
        for eachGroup in self.groups :
            group = pymel.group(em=1, n=eachGroup)            
            group.setParent(assetGroup)

  
        pymel.parent('Offset', 'Control_Group')
        pymel.parent('Controls', 'Control_Group') 
        pymel.parent('Layout', 'Geometry_Group') 
        pymel.parent('Animation', 'Geometry_Group') 
        pymel.parent('Render', 'Geometry_Group')        
        
        #create nurbs curve
        world = pymel.circle(   c=(0,0,0),
                                nr=(0,1,0),
                                sw=360,
                                r=5,
                                d=3,
                                s=8,
                                ch=False,
                                n='World')[0]
        
        transform = pymel.circle(   c=(0,0,0),
                                    nr=(0,1,0),
                                    sw=360,
                                    r=4,
                                    d=3,
                                    s=8,
                                    ch=False,
                                    n='Transform')[0]    

        world.setParent('Offset')
        transform.setParent(world)
        
        #create attributes  
        transform.addAttr('asset', at='double', min=0, max=1, dv=0, k=True)              
        transform.addAttr('geoVis', at='double', min=0, max=1, dv=1, k=True)
        transform.addAttr('ctrlVis', at='double', min=0, max=1, dv=1, k=True)       
        transform.addAttr('meshType', at='enum', en='Layout:Animation:Render', k=True)        
        transform.addAttr('meshDisplay', at='enum', en='Normal:Template:Refrence', k=True)
        transform.addAttr('smooth', at='enum', en='00:01:02', k=True)
        transform.addAttr('raduis', at='double', min=0, max=1, dv=0, k=True)
        
        transform.setAttr('asset', lock=True)        
        transform.setAttr('v', lock=True, keyable=False, channelBox=False)
        transform.setAttr('v', lock=True, keyable=False, channelBox=False)   
        
        transform.setAttr('geoVis', keyable=False, channelBox=True)
        transform.setAttr('ctrlVis', keyable=False, channelBox=True)
        transform.setAttr('meshType', keyable=False, channelBox=True)
        transform.setAttr('meshDisplay', keyable=False, channelBox=True)
        transform.setAttr('smooth', keyable=False, channelBox=True)
        transform.setAttr('raduis', keyable=False, channelBox=True)       
             
        transform.connectAttr('geoVis', 'Geometry_Group.v')
        transform.connectAttr('ctrlVis', 'Controls.v')        
        pymel.setAttr('Geometry_Group.overrideEnabled', 1)
        transform.connectAttr('meshDisplay', 'Geometry_Group.overrideDisplayType')

        pymel.setDrivenKeyframe('Layout.visibility', cd='Transform.meshType', dv=0, v=1)
        pymel.setDrivenKeyframe('Animation.visibility', cd='Transform.meshType', dv=0, v=0)
        pymel.setDrivenKeyframe('Render.visibility', cd='Transform.meshType', dv=0, v=0)
          
        pymel.setDrivenKeyframe('Layout.visibility', cd='Transform.meshType', dv=1, v=0)
        pymel.setDrivenKeyframe('Animation.visibility', cd='Transform.meshType', dv=1, v=1)
        pymel.setDrivenKeyframe('Render.visibility', cd='Transform.meshType', dv=1, v=0)
        
        pymel.setDrivenKeyframe('Layout.visibility', cd='Transform.meshType', dv=2, v=0)
        pymel.setDrivenKeyframe('Animation.visibility', cd='Transform.meshType', dv=2, v=0)
        pymel.setDrivenKeyframe('Render.visibility', cd='Transform.meshType', dv=2, v=1)     
    
    def remove(self):
        pass    
    
    
#End####################################################################################################    