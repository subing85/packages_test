'''
Biped Skeleton for Blender Puppet CS v1.0.0
Date : March 29, 2018
Last modified: March 29, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module for generate Biped Skeleton for Puppet Creative Suite
 
'''

NAME = 'Biped'
ORDER = 1
MODULE_TYPE = 'Fit Skeleton'
TYPE = 'validate'
DATE = 'March 29, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Generate Biped Skeleton'
VERSION = 1.0
CLASS = 'Biped'

import imp
import warnings
import bpy

from module.blender import inputNames
imp.reload(inputNames)

from module.blender import openBlender
imp.reload(openBlender)


class Biped (object):
    
    def __init__(self):
        
        self.input = inputNames.Names()
        
        self.nameStyle = self.input._nameStyle
        self.jointRadius = self.input._jointRadius
        
    
    
    def createSkeleton(self):
        
        '''
        Description
            Function for create the skleton for Bipe puppet, only in left side                     
            :Type - class function (method)            
            :param     None
            :return    None
        ''' 
                
        #create leg fit skeleton  
        pelvis_contextObject = createEmptyObject ('SPHERE', False, (1, 0, 5.5), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._pelvis))        
        knee_contextObject = createEmptyObject ('SPHERE', False, (1, 0, 3.25), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._knee))
        ankle_contextObject = createEmptyObject ('SPHERE', False, (1, 0, 1.0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._ankle))
        legPole_contextObject = createEmptyObject ('SPHERE', False, (1, -2.5, 3.25), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._legPoleVector))

        ball_contextObject = createEmptyObject ('SPHERE', False, (1, -0.75, 0.5), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._ball))
        toe_contextObject = createEmptyObject ('SPHERE', False, (1, -1.5, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._toe))
        heel_contextObject  = createEmptyObject ('SPHERE', False, (1, 0.75, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._heel))
        
        bigToe_contextObject = createEmptyObject ('SPHERE', False, (0.3, -0.75, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._bigToe))
        pinkyToe_contextObject = createEmptyObject ('SPHERE', False, (1.7, -0.75, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._pinkyToe))
           
        openBlender.setParent(knee_contextObject.name, pelvis_contextObject.name)
        openBlender.setParent(ankle_contextObject.name, knee_contextObject.name)
        openBlender.setParent(legPole_contextObject.name, knee_contextObject.name)     
        
        openBlender.setParent(ball_contextObject.name, ankle_contextObject.name)
        openBlender.setParent(toe_contextObject.name, ball_contextObject.name)
        openBlender.setParent(heel_contextObject.name, ankle_contextObject.name)
        openBlender.setParent(bigToe_contextObject.name, ball_contextObject.name)
        openBlender.setParent(pinkyToe_contextObject.name, ball_contextObject.name)
        
        #create spine fit skeleton
        hip_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 5.5), radius=self.jointRadius, name=self.input._hip)
        hipTail_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 5), radius=self.jointRadius, name=self.input._hipTail)        
        cog_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 6), radius=self.jointRadius, name=self.input._cog)    
        spineA_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 7), radius=self.jointRadius, name=self.input._spineA)   
        spineB_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 8), radius=self.jointRadius, name=self.input._spineB)    
        chest_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 9), radius=self.jointRadius, name=self.input._chest) 
        
        tailA_contextObject = createEmptyObject ('SPHERE', False, (0, 1, 5.5), radius=self.jointRadius/2, name=self.input._tailA)
        tailB_contextObject = createEmptyObject ('SPHERE', False, (0, 2, 5.5), radius=self.jointRadius/2, name=self.input._tailB)
        tailC_contextObject = createEmptyObject ('SPHERE', False, (0, 3, 5.5), radius=self.jointRadius/2, name=self.input._tailC)
        tailD_contextObject = createEmptyObject ('SPHERE', False, (0, 4, 5.5), radius=self.jointRadius/2, name=self.input._tailD)
        tailE_contextObject = createEmptyObject ('SPHERE', False, (0, 5, 5.5), radius=self.jointRadius/2, name=self.input._tailE)
        tailF_contextObject = createEmptyObject ('SPHERE', False, (0, 6, 5.5), radius=self.jointRadius/2, name=self.input._tailF)
        
        openBlender.setParent(hipTail_contextObject.name, hip_contextObject.name)
        openBlender.setParent(hip_contextObject.name, cog_contextObject.name)        
        openBlender.setParent(chest_contextObject.name, spineB_contextObject.name)
        openBlender.setParent(spineB_contextObject.name, spineA_contextObject.name)
        openBlender.setParent(spineA_contextObject.name, cog_contextObject.name)
        
        openBlender.setParent(pelvis_contextObject.name, hip_contextObject.name)
        
        openBlender.setParent(tailF_contextObject.name, tailE_contextObject.name)
        openBlender.setParent(tailE_contextObject.name, tailD_contextObject.name)
        openBlender.setParent(tailD_contextObject.name, tailC_contextObject.name)
        openBlender.setParent(tailC_contextObject.name, tailB_contextObject.name)
        openBlender.setParent(tailB_contextObject.name, tailA_contextObject.name)
        openBlender.setParent(tailA_contextObject.name, hip_contextObject.name)        
          
        #create neck to head fit skeleton
        neckA_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 10), radius=self.jointRadius, name=self.input._neckA)
        neckB_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 11), radius=self.jointRadius, name=self.input._neckB) 
        head_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 11.5), radius=self.jointRadius, name=self.input._head)
        headTail_contextObject = createEmptyObject ('SPHERE', False, (0, 0, 12.25), radius=self.jointRadius, name=self.input._headTail)
        
        upperJaw_contextObject = createEmptyObject ('SPHERE', False, (0, -0.5, 11.75), radius=self.jointRadius/2, name=self.input._upperJaw)
        upperJawTail_contextObject = createEmptyObject ('SPHERE', False, (0, -1, 11.75), radius=self.jointRadius/2, name=self.input._upperJawTail)
        
        lowerJaw_contextObject = createEmptyObject ('SPHERE', False, (0, -0.5, 11.25), radius=self.jointRadius/2, name=self.input._lowerJaw)
        lowerJawTail_contextObject = createEmptyObject ('SPHERE', False, (0, -1, 11.25), radius=self.jointRadius/2, name=self.input._lowerJawTail) 
        
        tongueA_contextObject = createEmptyObject ('SPHERE', False, (0, -0.5, 11.5), radius=self.jointRadius/2, name=self.input._tongueA)
        tongueB_contextObject = createEmptyObject ('SPHERE', False, (0, -0.65, 11.5), radius=self.jointRadius/2, name=self.input._tongueB)
        tongueC_contextObject = createEmptyObject ('SPHERE', False, (0, -0.8, 11.5), radius=self.jointRadius/2, name=self.input._tongueC)
        tongueD_contextObject = createEmptyObject ('SPHERE', False, (0, -0.95, 11.5), radius=self.jointRadius/2, name=self.input._tongueD)
        tongueE_contextObject = createEmptyObject ('SPHERE', False, (0, -1.1, 11.5), radius=self.jointRadius/2, name=self.input._tongueE)

        uvulaA_contextObject = createEmptyObject ('SPHERE', False, (0, -0.25, 11.7), radius=self.jointRadius/2, name=self.input._uvulaA)
        uvulaB_contextObject = createEmptyObject ('SPHERE', False, (0, -0.25, 11.55), radius=self.jointRadius/2, name=self.input._uvulaB)
        uvulaC_contextObject = createEmptyObject ('SPHERE', False, (0, -0.25, 11.4), radius=self.jointRadius/2, name=self.input._uvulaC)
        uvulaD_contextObject = createEmptyObject ('SPHERE', False, (0, -0.25, 11.25), radius=self.jointRadius/2, name=self.input._uvulaD)
        
        earA_contextObject = createEmptyObject ('SPHERE', False, (0.5, 0, 11.5), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._earA))
        earB_contextObject = createEmptyObject ('SPHERE', False, (0.75, 0, 11.5), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._earB))     
                
        openBlender.setParent(headTail_contextObject.name, head_contextObject.name)
        openBlender.setParent(head_contextObject.name, neckB_contextObject.name)
        openBlender.setParent(neckB_contextObject.name, neckA_contextObject.name)
        openBlender.setParent(neckA_contextObject.name, chest_contextObject.name)
        
        openBlender.setParent(upperJawTail_contextObject.name, upperJaw_contextObject.name)
        openBlender.setParent(upperJaw_contextObject.name, head_contextObject.name)
        
        openBlender.setParent(lowerJawTail_contextObject.name, lowerJaw_contextObject.name)
        openBlender.setParent(lowerJaw_contextObject.name, head_contextObject.name)
        
        openBlender.setParent(tongueE_contextObject.name, tongueD_contextObject.name)
        openBlender.setParent(tongueD_contextObject.name, tongueC_contextObject.name)
        openBlender.setParent(tongueC_contextObject.name, tongueB_contextObject.name)
        openBlender.setParent(tongueB_contextObject.name, tongueA_contextObject.name)
        openBlender.setParent(tongueA_contextObject.name, head_contextObject.name)
        
        openBlender.setParent(uvulaD_contextObject.name, uvulaC_contextObject.name)
        openBlender.setParent(uvulaC_contextObject.name, uvulaB_contextObject.name)
        openBlender.setParent(uvulaB_contextObject.name, uvulaA_contextObject.name)
        openBlender.setParent(uvulaA_contextObject.name, head_contextObject.name)    
        
        openBlender.setParent(earB_contextObject.name, earA_contextObject.name)    
        openBlender.setParent(earA_contextObject.name, head_contextObject.name)                
        
        #create eye fit skeleton
        eyeA_contextObject = createEmptyObject ('SPHERE', False, (0.25, -0.75, 12), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._eyeA))
        eyeB_contextObject = createEmptyObject ('SPHERE', False, (0.25, -1, 12), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._eyeB))

        openBlender.setParent(eyeB_contextObject.name, eyeA_contextObject.name)
        openBlender.setParent(eyeA_contextObject.name, head_contextObject.name)
        
        #create arm fit skeleton        
        clavicle_contextObject = createEmptyObject ('SPHERE', False, (0.5, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._clavicle))
        shoulder_contextObject = createEmptyObject ('SPHERE', False, (1, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._shoulder))        
        elbow_contextObject = createEmptyObject ('SPHERE', False, (2.5, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._elbow))        
        wrist_contextObject = createEmptyObject ('SPHERE', False, (4, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._wrist))    
        armPole_contextObject = createEmptyObject ('SPHERE', False, (2.5, 1.5, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._armPoleVector))        
        
        openBlender.setParent(wrist_contextObject.name, elbow_contextObject.name)        
        openBlender.setParent(armPole_contextObject.name, elbow_contextObject.name)
        openBlender.setParent(elbow_contextObject.name, shoulder_contextObject.name)
        openBlender.setParent(shoulder_contextObject.name, clavicle_contextObject.name)
        openBlender.setParent(clavicle_contextObject.name, chest_contextObject.name)        
        
        #create arm finger fit skeleton        
        thumbA_contextObject = createEmptyObject ('SPHERE', False, (4.25, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbA))    
        thumbB_contextObject = createEmptyObject ('SPHERE', False, (4.5, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbB))    
        thumbC_contextObject = createEmptyObject ('SPHERE', False, (4.7, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbC))    
        thumbD_contextObject = createEmptyObject ('SPHERE', False, (4.9, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbD))    
        thumbE_contextObject = createEmptyObject ('SPHERE', False, (5.1, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbE))    
        
        indexA_contextObject = createEmptyObject ('SPHERE', False, (4.25, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexA))    
        indexB_contextObject = createEmptyObject ('SPHERE', False, (4.5, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexB))    
        indexC_contextObject = createEmptyObject ('SPHERE', False, (4.7, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexC))    
        indexD_contextObject = createEmptyObject ('SPHERE', False, (4.9, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexD))    
        indexE_contextObject = createEmptyObject ('SPHERE', False, (5.1, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexE))            
            
        middleA_contextObject = createEmptyObject ('SPHERE', False, (4.25, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleA))    
        middleB_contextObject = createEmptyObject ('SPHERE', False, (4.5, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleB))    
        middleC_contextObject = createEmptyObject ('SPHERE', False, (4.7, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleC))    
        middleD_contextObject = createEmptyObject ('SPHERE', False, (4.9, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleD))    
        middleE_contextObject = createEmptyObject ('SPHERE', False, (5.1, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleE)) 

        ringA_contextObject = createEmptyObject ('SPHERE', False, (4.25, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringA))    
        ringB_contextObject = createEmptyObject ('SPHERE', False, (4.5, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringB))    
        ringC_contextObject = createEmptyObject ('SPHERE', False, (4.7, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringC))    
        ringD_contextObject = createEmptyObject ('SPHERE', False, (4.9, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringD))    
        ringE_contextObject = createEmptyObject ('SPHERE', False, (5.1, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringE))    
        
        pinkyA_contextObject = createEmptyObject ('SPHERE', False, (4.25, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyA))    
        pinkyB_contextObject = createEmptyObject ('SPHERE', False, (4.5, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyB))    
        pinkyC_contextObject = createEmptyObject ('SPHERE', False, (4.7, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyC))    
        pinkyD_contextObject = createEmptyObject ('SPHERE', False, (4.9, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyD))    
        pinkyE_contextObject = createEmptyObject ('SPHERE', False, (5.1, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyE))        
        
        openBlender.setParent(thumbA_contextObject.name, wrist_contextObject.name)        
        openBlender.setParent(indexA_contextObject.name, wrist_contextObject.name)        
        openBlender.setParent(middleA_contextObject.name, wrist_contextObject.name)        
        openBlender.setParent(ringA_contextObject.name, wrist_contextObject.name)        
        openBlender.setParent(pinkyA_contextObject.name, wrist_contextObject.name)        
        
        openBlender.setParent(thumbE_contextObject.name, thumbD_contextObject.name)        
        openBlender.setParent(thumbD_contextObject.name, thumbC_contextObject.name)        
        openBlender.setParent(thumbC_contextObject.name, thumbB_contextObject.name)        
        openBlender.setParent(thumbB_contextObject.name, thumbA_contextObject.name)       
         
        openBlender.setParent(indexE_contextObject.name, indexD_contextObject.name)        
        openBlender.setParent(indexD_contextObject.name, indexC_contextObject.name)        
        openBlender.setParent(indexC_contextObject.name, indexB_contextObject.name)        
        openBlender.setParent(indexB_contextObject.name, indexA_contextObject.name)        
        
        openBlender.setParent(middleE_contextObject.name, middleD_contextObject.name)        
        openBlender.setParent(middleD_contextObject.name, middleC_contextObject.name)        
        openBlender.setParent(middleC_contextObject.name, middleB_contextObject.name)        
        openBlender.setParent(middleB_contextObject.name, middleA_contextObject.name)       
        
        openBlender.setParent(ringE_contextObject.name, ringD_contextObject.name)        
        openBlender.setParent(ringD_contextObject.name, ringC_contextObject.name)        
        openBlender.setParent(ringC_contextObject.name, ringB_contextObject.name)        
        openBlender.setParent(ringB_contextObject.name, ringA_contextObject.name)               
                    
        openBlender.setParent(pinkyE_contextObject.name, pinkyD_contextObject.name)        
        openBlender.setParent(pinkyD_contextObject.name, pinkyC_contextObject.name)        
        openBlender.setParent(pinkyC_contextObject.name, pinkyB_contextObject.name)        
        openBlender.setParent(pinkyB_contextObject.name, pinkyA_contextObject.name)                   
            
                    
    
    def removeSkeleton(self):
        pass
    
    
    def resetSkeleton(self):
        pass
    
    
    def hasExists (self):
        pass


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


#End##################################################################################################