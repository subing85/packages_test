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
 
example
    import imp
    from assets.blender import skeletonBiped
    imp.reload(skeletonBiped)
    biped = skeletonBiped.Biped()
    biped.createSkeleton()
 
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

from module import inputNames
imp.reload(inputNames)

from module import studioBlender
imp.reload(studioBlender)


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
        pelvis_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, 0, 5.5), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._pelvis))        
        knee_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, 0, 3.25), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._knee))
        ankle_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, 0, 1.0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._ankle))
        legPole_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, -2.5, 3.25), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._legPoleVector))

        ball_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, -0.75, 0.5), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._ball))
        toe_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, -1.5, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._toe))
        heel_contextObject  = studioBlender.createEmptyObject ('SPHERE', False, (1, 0.75, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._heel))
        
        bigToe_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0.3, -0.75, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._bigToe))
        pinkyToe_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1.7, -0.75, 0), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._pinkyToe))
        
        #create spine fit skeleton
        hip_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 5.5), radius=self.jointRadius, name=self.input._hip)
        hipTail_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 5), radius=self.jointRadius, name=self.input._hipTail)        
        cog_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 6), radius=self.jointRadius, name=self.input._cog)    
        spineA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 7), radius=self.jointRadius, name=self.input._spineA)   
        spineB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 8), radius=self.jointRadius, name=self.input._spineB)    
        chest_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 9), radius=self.jointRadius, name=self.input._chest) 
        
        tailA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 1, 5.5), radius=self.jointRadius/2, name=self.input._tailA)
        tailB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 2, 5.5), radius=self.jointRadius/2, name=self.input._tailB)
        tailC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 3, 5.5), radius=self.jointRadius/2, name=self.input._tailC)
        tailD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 4, 5.5), radius=self.jointRadius/2, name=self.input._tailD)
        tailE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 5, 5.5), radius=self.jointRadius/2, name=self.input._tailE)
        tailF_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 6, 5.5), radius=self.jointRadius/2, name=self.input._tailF)
          
        #create neck to head fit skeleton
        neckA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 10), radius=self.jointRadius, name=self.input._neckA)
        neckB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 11), radius=self.jointRadius, name=self.input._neckB) 
        head_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 11.5), radius=self.jointRadius, name=self.input._head)
        headTail_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 12.25), radius=self.jointRadius, name=self.input._headTail)
        
        upperJaw_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.5, 11.75), radius=self.jointRadius/2, name=self.input._upperJaw)
        upperJawTail_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -1, 11.75), radius=self.jointRadius/2, name=self.input._upperJawTail)
        
        lowerJaw_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.5, 11.25), radius=self.jointRadius/2, name=self.input._lowerJaw)
        lowerJawTail_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -1, 11.25), radius=self.jointRadius/2, name=self.input._lowerJawTail) 
        
        tongueA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.5, 11.5), radius=self.jointRadius/2, name=self.input._tongueA)
        tongueB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.65, 11.5), radius=self.jointRadius/2, name=self.input._tongueB)
        tongueC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.8, 11.5), radius=self.jointRadius/2, name=self.input._tongueC)
        tongueD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.95, 11.5), radius=self.jointRadius/2, name=self.input._tongueD)
        tongueE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -1.1, 11.5), radius=self.jointRadius/2, name=self.input._tongueE)

        uvulaA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.25, 11.7), radius=self.jointRadius/2, name=self.input._uvulaA)
        uvulaB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.25, 11.55), radius=self.jointRadius/2, name=self.input._uvulaB)
        uvulaC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.25, 11.4), radius=self.jointRadius/2, name=self.input._uvulaC)
        uvulaD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, -0.25, 11.25), radius=self.jointRadius/2, name=self.input._uvulaD)
        
        earA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0.5, 0, 11.5), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._ear))
        earTail_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0.75, 0, 11.5), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._earTail))     
        
        #create eye fit skeleton
        eye_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0.25, -0.75, 12), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._eye))
        eyeTail_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0.25, -1, 12), radius=self.jointRadius/2, name='%s_%s'% (self.input._leftSide, self.input._eyeTail))
        
        #create arm fit skeleton        
        clavicle_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0.5, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._clavicle))
        shoulder_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (1, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._shoulder))        
        elbow_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (2.5, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._elbow))        
        wrist_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4, 0, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._wrist))    
        armPole_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (2.5, 1.5, 10), radius=self.jointRadius, name='%s_%s'% (self.input._leftSide, self.input._armPoleVector))        
        
        #create arm finger fit skeleton        
        thumbA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.25, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbA))    
        thumbB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.5, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbB))    
        thumbC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.7, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbC))    
        thumbD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.9, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbD))    
        thumbE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (5.1, -0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._thumbE))    
        
        indexA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.25, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexA))    
        indexB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.5, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexB))    
        indexC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.7, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexC))    
        indexD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.9, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexD))    
        indexE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (5.1, -0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._indexE))            
            
        middleA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.25, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleA))    
        middleB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.5, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleB))    
        middleC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.7, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleC))    
        middleD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.9, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleD))    
        middleE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (5.1, 0, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._middleE)) 
        
        ringA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.25, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringA))    
        ringB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.5, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringB))    
        ringC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.7, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringC))    
        ringD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.9, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringD))    
        ringE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (5.1, 0.25, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._ringE))    
        
        pinkyA_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.25, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyA))    
        pinkyB_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.5, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyB))    
        pinkyC_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.7, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyC))    
        pinkyD_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (4.9, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyD))    
        pinkyE_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (5.1, 0.5, 10), radius=self.jointRadius/3, name='%s_%s'% (self.input._leftSide, self.input._pinkyE))        
        
        root_contextObject = studioBlender.createEmptyObject ('SPHERE', False, (0, 0, 0), radius=self.jointRadius, name=self.input._root)    
        
        
        
        #self.createMirrorSkeleton()        
        self.setLegHierarchy(types=self.input._leftSide)
        #self.setLegHierarchy(types=self.input._rightSide)
        self.setSpineHierarchy()
        self.setHeadHierarchy()
        self.setEarHierarchy(types=self.input._leftSide)
        self.setEyeHierarchy(types=self.input._leftSide)
        self.setArmHierarchy(types=self.input._leftSide)
            
        bpy.ops.object.select_all(action='DESELECT')
        
        print ('successfully created fit joints........................')
                    
    
    def removeSkeleton(self):
        
        nodes = []
        for eachNode in nodes:
            if not bpy.data.objects.get(eachNode) :
                print ('no such object in the scene\t', eachNode)
                continue
            
            if bpy.data.objects.get(eachNode) :
                try :
                    bpy.data.objects[eachNode].select = True
                    bpy.data.objects.remove(bpy.data.objects[eachNode], True)   
                except Exception as result:
                    warnings.warn ('node remove error', result)    
                       
        objects = bpy.context.selected_objects        
        for eachObject in objects:
            print (eachObject.type)   
             
            
    def resetSkeleton(self):
        pass
    
    
    def hasExists (self):
        pass
    

    def createMirrorSkeleton(self):
        
        inputList = self.input._legList + self.input._armList
        inputSkeletons = []
        
        for eachInput in inputList:
            inputSkeletons.append ('%s_%s'% (self.input._leftSide, eachInput))            
            #print ('%s_%s'% (self.input._leftSide, eachInput))
            
        axis = (-1, 1, 1)
        studioBlender.setMirror(inputSkeletons, axis, 'L_', 'R_')

    
    def setHierarchy(self):
        
        '''
        Description
            Function for set the fit skeleton Hierarchy.                    
            :Type - class function (method)            
            :param     None
            :return    None
        ''' 
        
        self.setLegHierarchy(types=self.input._leftSide)
        #self.setLegHierarchy(types=self.input._rightSide)
        self.setSpineHierarchy()
        self.setHeadHierarchy()
        self.setEarHierarchy(types=self.input._leftSide)
        self.setEyeHierarchy(types=self.input._leftSide)
        self.setArmHierarchy(types=self.input._leftSide)   
        
        
    def brakeHierarchy(self, root=None):
        
        '''
        Description
            Function for brake the fit skeleton hierarchy.                    
            :Type - class function (method)            
            :param     None
            :return    None
        ''' 
        
        sb = studioBlender.OpenBlender()        
        sb.getHierarchyDependent(root=root)        
        skeletonList = sb._dependent
        
        for index in range(1, len(skeletonList)):
            
            fitObject = bpy.data.objects[skeletonList[index]]             
            if not fitObject.parent:
                continue
            fitObject.select = True
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')        
        
        
    def setLegHierarchy(self, types=None):
                
        parents = { self.input._knee: self.input._pelvis,
                    self.input._ankle: self.input._knee,
                    self.input._legPoleVector: self.input._knee,
                    self.input._ball: self.input._ankle,
                    self.input._toe: self.input._ball,
                    self.input._heel: self.input._ankle,
                    self.input._bigToe: self.input._ball,
                    self.input._pinkyToe: self.input._ball,
                    self.input._ball: self.input._ankle,
                    self.input._ball: self.input._ankle,
                    self.input._ball: self.input._ankle,
                    self.input._ball: self.input._ankle                    
                    }
        
        for eachChild, eachParent in parents.items():            
            studioBlender.setParent('%s_%s'% (types, eachChild), '%s_%s'% (types, eachParent))
        
        #parent pelvis to hip (leg to spine)            
        studioBlender.setParent('%s_%s'% (types, self.input._pelvis), self.input._hip)
        

    def setSpineHierarchy(self):
        
        parents = { self.input._hipTail: self.input._hip,
                    self.input._hip: self.input._cog,
                    self.input._chest: self.input._spineB,
                    self.input._spineB: self.input._spineA,
                    self.input._spineA: self.input._cog,                   
                    self.input._tailF: self.input._tailE,
                    self.input._tailE: self.input._tailD,
                    self.input._tailD: self.input._tailC,
                    self.input._tailC: self.input._tailB,
                    self.input._tailB: self.input._tailA,                    
                    self.input._tailA: self.input._hip,
                    self.input._cog: self.input._root                    
                    }
        
        for eachChild, eachParent in parents.items():            
            studioBlender.setParent(eachChild, eachParent)
            
    
    def setHeadHierarchy(self):
        
        parents = { self.input._headTail: self.input._head,
                    self.input._head: self.input._neckB,
                    self.input._neckB: self.input._neckA,                    
                    self.input._neckA: self.input._chest,
                    
                    self.input._upperJawTail: self.input._upperJaw,
                    self.input._upperJaw: self.input._head,
                    self.input._lowerJawTail: self.input._lowerJaw,
                    self.input._lowerJaw: self.input._head,
                    
                    self.input._uvulaD: self.input._uvulaC,                    
                    self.input._uvulaC: self.input._uvulaB,
                    self.input._uvulaB: self.input._uvulaA,
                    self.input._uvulaA: self.input._upperJaw,                    

                    self.input._tongueE: self.input._tongueD,
                    self.input._tongueD: self.input._tongueC,
                    self.input._tongueC: self.input._tongueB,
                    self.input._tongueB: self.input._tongueA,
                    self.input._tongueA: self.input._lowerJaw
                    }            

        for eachChild, eachParent in parents.items():            
            studioBlender.setParent(eachChild, eachParent)
            
            
    def setEarHierarchy(self, types=None):
        
        parents = { self.input._earTail: self.input._ear,
                    }         
                    
        for eachChild, eachParent in parents.items():            
            studioBlender.setParent('%s_%s'% (types, eachChild), '%s_%s'% (types, eachParent))
       
        studioBlender.setParent('%s_%s'% (types, self.input._ear), self.input._upperJaw)
                            
            
    def setEyeHierarchy(self, types=None):
        
        parents = { self.input._eyeTail: self.input._eye,
                    }         
                    
        for eachChild, eachParent in parents.items():            
            studioBlender.setParent('%s_%s'% (types, eachChild), '%s_%s'% (types, eachParent))            
     
        studioBlender.setParent('%s_%s'% (types, self.input._eye), self.input._upperJaw)
        
        
    def setArmHierarchy(self, types=None):

        parents = { self.input._wrist: self.input._elbow,                   
                    self.input._armPoleVector: self.input._elbow,
                    self.input._elbow: self.input._shoulder,
                    self.input._shoulder: self.input._clavicle,
                    
                    self.input._thumbA: self.input._wrist,                    
                    self.input._thumbB: self.input._thumbA,
                    self.input._thumbC: self.input._thumbB,
                    self.input._thumbD: self.input._thumbC,
                    self.input._thumbE: self.input._thumbD,
                    
                    self.input._indexA: self.input._wrist,                    
                    self.input._indexB: self.input._indexA,
                    self.input._indexC: self.input._indexB,
                    self.input._indexD: self.input._indexC,
                    self.input._indexE: self.input._indexD,   
                    
                    self.input._middleA: self.input._wrist,                    
                    self.input._middleB: self.input._middleA,
                    self.input._middleC: self.input._middleB,
                    self.input._middleD: self.input._middleC,
                    self.input._middleE: self.input._middleD,
                    
                    self.input._ringA: self.input._wrist,                    
                    self.input._ringB: self.input._ringA,
                    self.input._ringC: self.input._ringB,
                    self.input._ringD: self.input._ringC,
                    self.input._ringE: self.input._ringD,                                       
                    
                    self.input._pinkyA: self.input._wrist,                    
                    self.input._pinkyB: self.input._pinkyA,
                    self.input._pinkyC: self.input._pinkyB,
                    self.input._pinkyD: self.input._pinkyC,
                    self.input._pinkyE: self.input._pinkyD,                                                       
                   
                    }         
                    
        for eachChild, eachParent in parents.items():            
            studioBlender.setParent('%s_%s'% (types, eachChild), '%s_%s'% (types, eachParent))            
     
        studioBlender.setParent('%s_%s'% (types, self.input._clavicle), self.input._chest)

#End##################################################################################################