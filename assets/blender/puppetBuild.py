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
    from assets.blender import puppetBuild
    imp.reload(puppetBuild)
    build = puppetBuild.Build()
    build.create()  
'''

import pprint
import bpy
import imp

from module import inputNames 
from module import studioBlender
from assets.blender import skeletonBiped
from assets.blender import studioControls

imp.reload(studioBlender)
imp.reload(studioControls)


class Build(object):
    
    def __init__(self):
    
        
        self.input = inputNames.Names()
        self.armature = 'Armature'
        
        
    
    def create(self):
        
        '''
        Description
            Function set for create puppet on the fit skeleton
            
            :Type - class function (method)            
            :param    None
            :return   None
            :example to execute        
                from assets.blender import puppetBuild
                reload(puppetBuild)  
                ob = puppetBuild.Build()  
                ob.create()              
        '''        
        
        self.createArmatureBones()
        self.setBoneHierarchy()
        self.createHierarchy()
        
        self.createFootSetup(side=self.input._leftSide)
        #self.createFootSetup(side=self.input._rightSide)
        
    
    def createHierarchy(self):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        
        groups = [  'AssetName',
                    'Control_Group', 'Offset', 'Controls', 
                    'Geometry_Group', 'Layout', 'Animation', 'Render', 
                    'Deformer_Group', 
                    'Skeleton_Group', 
                    'Texture_Group', 
                    'Lighting_Group'
                    ]
        
        for eachGroup in groups :
            bpy.ops.object.empty_add(   type='PLAIN_AXES', 
                                        view_align=False, 
                                        location=(0,0,0)
                                        ) 
            bpy.context.object.name = eachGroup
            bpy.context.object.empty_draw_size = 0.0  
        
        bpy.ops.curve.primitive_nurbs_circle_add(   view_align=False, 
                                                    location=(0,0,0)
                                                    )
        
        bpy.context.object.name = 'World'
        #world = studioBlender.createEmptyObject ('CIRCLE', False, (0, 0, 0), radius=4.0, name='World')
            
        bpy.data.objects['Control_Group'].parent = bpy.data.objects['AssetName']
        bpy.data.objects['Geometry_Group'].parent = bpy.data.objects['AssetName']
        bpy.data.objects['Deformer_Group'].parent = bpy.data.objects['AssetName']
        bpy.data.objects['Skeleton_Group'].parent = bpy.data.objects['AssetName']
        bpy.data.objects['Texture_Group'].parent = bpy.data.objects['AssetName']
        bpy.data.objects['Lighting_Group'].parent = bpy.data.objects['AssetName']
               
        bpy.data.objects['Offset'].parent = bpy.data.objects['Control_Group']
        bpy.data.objects['Controls'].parent = bpy.data.objects['Control_Group']
        bpy.data.objects['Layout'].parent = bpy.data.objects['Geometry_Group']
        bpy.data.objects['Animation'].parent = bpy.data.objects['Geometry_Group']
        bpy.data.objects['Render'].parent = bpy.data.objects['Geometry_Group']            
        
        bpy.data.objects[self.armature].parent = bpy.data.objects['Skeleton_Group']            
        bpy.data.objects['Root'].parent = bpy.data.objects['Skeleton_Group']            

        bpy.data.objects['World'].parent = bpy.data.objects['Offset']
  
        
    def setBoneHierarchy(self):
        
        '''
        
        
        '''
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        
        fitSkeleton = bpy.data.objects[self.armature]
        bpy.context.scene.objects.active = fitSkeleton
        bpy.ops.object.mode_set(mode='EDIT')
        armatureObject = bpy.context.scene.objects.active 
     
        armatureObject.data.edit_bones['Hip_Bone'].parent = armatureObject.data.edit_bones['Cog_Bone']
        armatureObject.data.edit_bones['L_Pelvis_Bone'].parent = armatureObject.data.edit_bones['Hip_Bone']
        armatureObject.data.edit_bones['R_Pelvis_Bone'].parent = armatureObject.data.edit_bones['Hip_Bone']
        armatureObject.data.edit_bones['L_Clavicle_Bone'].parent = armatureObject.data.edit_bones['Chest_Bone']
        armatureObject.data.edit_bones['R_Clavicle_Bone'].parent = armatureObject.data.edit_bones['Chest_Bone']
          
        armatureObject.data.edit_bones['L_ThumbA_Bone'].parent = armatureObject.data.edit_bones['L_Elbow_Bone']
        armatureObject.data.edit_bones['L_IndexA_Bone'].parent = armatureObject.data.edit_bones['L_Elbow_Bone']
        armatureObject.data.edit_bones['L_MiddleA_Bone'].parent = armatureObject.data.edit_bones['L_Elbow_Bone']
        armatureObject.data.edit_bones['L_RingA_Bone'].parent = armatureObject.data.edit_bones['L_Elbow_Bone']
        armatureObject.data.edit_bones['L_PinkyA_Bone'].parent = armatureObject.data.edit_bones['L_Elbow_Bone']
          
        armatureObject.data.edit_bones['R_ThumbA_Bone'].parent = armatureObject.data.edit_bones['R_Elbow_Bone']
        armatureObject.data.edit_bones['R_IndexA_Bone'].parent = armatureObject.data.edit_bones['R_Elbow_Bone']
        armatureObject.data.edit_bones['R_MiddleA_Bone'].parent = armatureObject.data.edit_bones['R_Elbow_Bone']
        armatureObject.data.edit_bones['R_RingA_Bone'].parent = armatureObject.data.edit_bones['R_Elbow_Bone']
        armatureObject.data.edit_bones['R_PinkyA_Bone'].parent = armatureObject.data.edit_bones['R_Elbow_Bone']      


    def createArmatureBones(self):
        
        '''
        Description
            Function set for create Armature Bones based on the fit skeleton
            
            :Type - class function (method)            
            :param    None
            :return   None
            :example to execute        
                from assets.blender import puppetBuild
                reload(puppetBuild)  
                ob = puppetBuild.Build()  
                ob.createArmatureBones()              
        ''' 
        
        #bake the fit skeleton hierarchy        
        biped = skeletonBiped.Biped()
        biped.brakeHierarchy(root='Root')  
        
        #create center and left side armature bones.        
        label = self.armature
        armatureLabel = 'Armature'
        
        rootSkeletons = ['Root', 'RootTail']
        legSkeletons = ['Pelvis', 'Knee', 'Ankle', 'Ball', 'Toe']
        spineSkeletons = ['Cog', 'SpineA', 'SpineB', 'Chest', 'NeckA', 'NeckB', 'Head', 'HeadTail']
        lowerJawSkeletons = ['LowerJaw', 'LowerJawTail']
        upperJawSkeletons = ['UpperJaw', 'UpperJawTail']
        tongueSkeletons = ['TongueA', 'TongueB', 'TongueC', 'TongueD','TongueE']        
        uvulaSkeletons = ['UvulaA', 'UvulaB', 'UvulaC', 'UvulaD']       
        eyeSkeletons = ['Eye', 'EyeTail']  
        earSkeletons = ['Ear', 'EarTail']   
        clavicleSkeletons = ['Clavicle', 'ClavicleTail']
        armSkeletons = ['Shoulder', 'Elbow', 'Wrist']
        thumbSkeletons = ['ThumbA', 'ThumbB', 'ThumbC', 'ThumbD', 'ThumbE']
        indexSkeletons = ['IndexA', 'IndexB', 'IndexC', 'IndexD', 'IndexE']
        middleSkeletons = ['MiddleA', 'MiddleB', 'MiddleC', 'MiddleD', 'MiddleE']
        ringSkeletons = ['RingA', 'RingB', 'RingC', 'RingD', 'RingE']
        pinkySkeletons = ['PinkyA', 'PinkyB', 'PinkyC', 'PinkyD', 'PinkyE']
        hipSkeletons = ['Hip', 'HipTail']        
        
        puppetSkeletons = { 0: {'extrude': 0, 'position': rootSkeletons},
                            1: {'extrude': 3, 'position': legSkeletons},
                            2: {'extrude': 6, 'position': spineSkeletons},
                            3: {'extrude': 0, 'position': lowerJawSkeletons},
                            4: {'extrude': 0, 'position': upperJawSkeletons},
                            5: {'extrude': 3, 'position': tongueSkeletons},
                            6: {'extrude': 2, 'position': uvulaSkeletons},
                            7: {'extrude': 0, 'position': eyeSkeletons},
                            8: {'extrude': 0, 'position': earSkeletons},
                            9:{'extrude': 0, 'position': clavicleSkeletons},
                            10:{'extrude': 1, 'position': armSkeletons},
                            11:{'extrude': 3, 'position': thumbSkeletons},
                            12:{'extrude': 3, 'position': indexSkeletons},
                            13:{'extrude': 3, 'position': middleSkeletons},
                            14:{'extrude': 3, 'position': ringSkeletons},
                            15:{'extrude': 3, 'position': pinkySkeletons},
                            16:{'extrude': 0, 'position': hipSkeletons}
                            }        
        
        skeletonList = []
        skeletonList.extend(rootSkeletons[0:1])       
        skeletonList.extend(legSkeletons[0:4])
        skeletonList.extend(spineSkeletons[0:7])
        skeletonList.extend(lowerJawSkeletons[0:1])
        skeletonList.extend(upperJawSkeletons[0:1])
        skeletonList.extend(tongueSkeletons[0:4])
        skeletonList.extend(uvulaSkeletons[0:3])
        skeletonList.extend(eyeSkeletons[0:1])
        skeletonList.extend(earSkeletons[0:1])
        skeletonList.extend(clavicleSkeletons[0:1])        
        skeletonList.extend(armSkeletons[0:2])        
        skeletonList.extend(thumbSkeletons[0:4])
        skeletonList.extend(indexSkeletons[0:4])
        skeletonList.extend(middleSkeletons[0:4])
        skeletonList.extend(ringSkeletons[0:4])
        skeletonList.extend(pinkySkeletons[0:4])           
        skeletonList.extend(hipSkeletons[0:1])
        
        leftSkeletons = []
        leftSkeletons.extend(legSkeletons)
        leftSkeletons.extend(eyeSkeletons)
        leftSkeletons.extend(earSkeletons)
        leftSkeletons.extend(clavicleSkeletons)
        leftSkeletons.extend(armSkeletons)
        leftSkeletons.extend(thumbSkeletons)
        leftSkeletons.extend(indexSkeletons)
        leftSkeletons.extend(middleSkeletons)
        leftSkeletons.extend(ringSkeletons)
        leftSkeletons.extend(pinkySkeletons)
        
        tailSkeletons = {   'L_Ball_Bone': 'Toe',
                            'Head_Bone': 'HeadTail',
                            'LowerJaw_Bone': 'LowerJawTail',
                            'UpperJaw_Bone': 'UpperJawTail',
                            'TongueD_Bone': 'TongueE',
                            'UvulaC_Bone': 'UvulaD',
                            'L_Eye_Bone': 'EyeTail',
                            'L_Ear_Bone': 'EarTail',                        
                            'L_Elbow_Bone': 'Wrist',  
                            
                            'L_Clavicle_Bone': 'Shoulder',  
                                                      
                            'L_ThumbD_Bone': 'ThumbE',
                            'L_IndexD_Bone': 'IndexE',
                            'L_MiddleD_Bone': 'MiddleE',
                            'L_RingD_Bone': 'RingE',
                            'L_PinkyD_Bone': 'PinkyE',
                            'Hip_Bone': 'HipTail'
                            }           
        
        baseBones = studioBlender.createBones(  armatures=True,
                                                label=label, 
                                                armatureLabel=armatureLabel,
                                                skeletons = puppetSkeletons,
                                                skeletonList = skeletonList,
                                                leftSkeletons = leftSkeletons,
                                                rightSkeletons = None,
                                                tailSkeletons = tailSkeletons,
                                                extrudeBones = None,
                                                axis = [1,1,1],
                                                roll = 1
                                                )

        #create mirror
        rightLegSkeletons = ['Pelvis', 'Knee', 'Ankle', 'Ball', 'Toe']
        rightArmSkeletons = ['Clavicle', 'Shoulder', 'Elbow', 'Wrist']  
        
        rightThumbSkeletons = ['ThumbA', 'ThumbB', 'ThumbC', 'ThumbD', 'ThumbE']
        rightIndexSkeletons = ['IndexA', 'IndexB', 'IndexC', 'IndexD', 'IndexE']
        rightMiddleSkeletons = ['MiddleA', 'MiddleB', 'MiddleC', 'MiddleD', 'MiddleE']
        rightRingSkeletons = ['RingA', 'RingB', 'RingC', 'RingD', 'RingE']
        rightPinkySkeletons = ['PinkyA', 'PinkyB', 'PinkyC', 'PinkyD', 'PinkyE']        
        
        rightPuppetSkeletons = {1: {'extrude': 3, 'position': rightLegSkeletons},                            
                                2: {'extrude': 2, 'position': rightArmSkeletons},
                                  
                                3: {'extrude': 3, 'position': rightThumbSkeletons},
                                4: {'extrude': 3, 'position': rightIndexSkeletons},
                                5: {'extrude': 3, 'position': rightMiddleSkeletons},
                                6: {'extrude': 3, 'position': rightRingSkeletons},
                                7: {'extrude': 3, 'position': rightPinkySkeletons},
                                }
        
        rightSkeletonList = []
        rightSkeletonList.extend(rightLegSkeletons[0:4])
        rightSkeletonList.extend(rightArmSkeletons[0:3]) 
            
        rightSkeletonList.extend(rightThumbSkeletons[0:4])   
        rightSkeletonList.extend(rightIndexSkeletons[0:4])   
        rightSkeletonList.extend(rightMiddleSkeletons[0:4])   
        rightSkeletonList.extend(rightRingSkeletons[0:4])   
        rightSkeletonList.extend(rightPinkySkeletons[0:4])   
        
        rightSkeletons = []
        rightSkeletons.extend(rightLegSkeletons)
        rightSkeletons.extend(rightArmSkeletons)
        rightSkeletons.extend(rightThumbSkeletons)
        rightSkeletons.extend(rightIndexSkeletons)
        rightSkeletons.extend(rightMiddleSkeletons)
        rightSkeletons.extend(rightRingSkeletons)
        rightSkeletons.extend(rightPinkySkeletons)
        
        rightTailSkeletonList = {   'R_Ball_Bone': 'Toe',                           
                                    'R_Elbow_Bone': 'Wrist',
                                    'R_ThumbD_Bone': 'ThumbE',
                                    'R_IndexD_Bone': 'IndexE',
                                    'R_MiddleD_Bone': 'MiddleE',
                                    'R_RingD_Bone': 'RingE',
                                    'R_PinkyD_Bone': 'PinkyE',                                    
                                    }           
        
        studioBlender.createBones(  armatures=False,
                                    label=label, 
                                    armatureLabel=armatureLabel,
                                    skeletons = rightPuppetSkeletons,
                                    skeletonList = rightSkeletonList,
                                    leftSkeletons = None,
                                    rightSkeletons = rightSkeletons,
                                    tailSkeletons = rightTailSkeletonList,
                                    extrudeBones = baseBones,
                                    axis = [-1,1,1],
                                    roll = -1
                                    ) 

        #armatureObject = bpy.context.scene.objects.active        
        bpy.ops.object.mode_set(mode='OBJECT')    
        #bpy.context.object.data.draw_type = 'STICK'

        #re-parent fit skeleton hierarchy      
        biped.setHierarchy()   


        print ('\nArmature creation and placement done!..........')
        
        
    def createFootSetup(self, side=None):
        
        ctrl = studioControls.Controls() # control class
        
        #create ik bones   
        sourceBone= [   '%s_Pelvis_Bone'% side, 
                        '%s_Knee_Bone'% side, 
                        '%s_Ankle_Bone'% side, 
                        '%s_Ball_Bone'% side
                        ]
        
        ikBones = studioBlender.duplicateBones(armature=self.armature, source=sourceBone, search='_Bone', replace='_IK', deformer=False)
        fkBones = studioBlender.duplicateBones(armature=self.armature, source=sourceBone, search='_Bone', replace='_FK', deformer=False)
        
        #ik setup
        #create ik handle
        bpy.ops.object.mode_set(mode='OBJECT')
        
        ankleIKHandle = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.2, name='%s_%s_IKHandle'% (side, self.input._ankle)) 
        ballIKHandle = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.2, name='%s_%s_IKHandle'% (side, self.input._ball)) 
        toeIKHandle = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.2, name='%s_%s_IKHandle'% (side, self.input._toe)) 
        
        studioBlender.sanpToBone (self.armature, '%s_Ankle_Bone'% side, ankleIKHandle.name, 'location', True, False)
        studioBlender.sanpToBone (self.armature, '%s_Ball_Bone'% side, ballIKHandle.name, 'location', True, False)
        studioBlender.sanpToBone (self.armature, '%s_Ball_Bone'% side, toeIKHandle.name, 'location', False, True)
     
        #set ik handle to knee, ankle and ball     
        ankleIKConstrain = studioBlender.setIKContrain( armature=self.armature, 
                                                        bone='%s_Knee_IK'% side, 
                                                        ikHandle='%s_Ankle_IKHandle'% side, 
                                                        chainCount=2, 
                                                        poleTarget=None)        
        
        ballIKConstrain = studioBlender.setIKContrain(  armature=self.armature, 
                                                        bone='%s_Ankle_IK'% side, 
                                                        ikHandle='%s_Ball_IKHandle'% side, 
                                                        chainCount=1, 
                                                        poleTarget=None)  
        
        toeIKConstrain = studioBlender.setIKContrain(   armature=self.armature, 
                                                        bone='%s_Ball_IK'% side, 
                                                        ikHandle='%s_Toe_IKHandle'% side, 
                                                        chainCount=1, 
                                                        poleTarget=None)
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #create foot roll hierarchy
        ankleRoll_SDK = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.5, name='%s_%s_Roll_SDK'% (side, self.input._ankle)) 
        ballRoll_SDK = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.5, name='%s_%s_Roll_SDK'% (side, self.input._ball)) 
        toeRoll_SDK = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.5, name='%s_%s_Roll_SDK'% (side, self.input._toe)) 
        hellRoll_SDK = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.5, name='%s_%s_Roll_SDK'% (side, self.input._heel)) 
        ankleIK_SDK = studioBlender.createEmptyObject ('PLAIN_AXES', False, (0, 0, 0), radius=0.5, name='%s_%s_IK_SDK'% (side, self.input._ankle)) 
        
        studioBlender.sanpToBone (self.armature, '%s_Ball_Bone'% side, ankleRoll_SDK.name, 'location', True, False)
        studioBlender.sanpToBone (self.armature, '%s_Ball_Bone'% side, ballRoll_SDK.name, 'location', True, False)
        studioBlender.sanpToBone (self.armature, '%s_Ball_Bone'% side, toeRoll_SDK.name, 'location', False, True)
        studioBlender.sanpToObject ('Heel', hellRoll_SDK.name, 'location')
        studioBlender.sanpToBone (self.armature, '%s_Ankle_Bone'% side, ankleIK_SDK.name, 'location', True, False)
        
        if side==self.input._rightSide: # Exception in the side of right only
            hellRoll_SDK.location.x = hellRoll_SDK.location.x*-1
                
        studioBlender.setParent(ankleIKHandle.name, ankleRoll_SDK.name)
        studioBlender.setParent(ballIKHandle.name, ballRoll_SDK.name)
        studioBlender.setParent(toeIKHandle.name, ballRoll_SDK.name)
        studioBlender.setParent(ankleRoll_SDK.name, toeRoll_SDK.name)
        studioBlender.setParent(ballRoll_SDK.name, toeRoll_SDK.name)
        studioBlender.setParent(toeRoll_SDK.name, hellRoll_SDK.name)
        studioBlender.setParent(hellRoll_SDK.name, ankleIK_SDK.name)
        
        #create foot controls        
        ankleIK_CtrlName = '%s_%s_%s_%s'% (side, self.input._ankle, self.input._ik, self.input._control)
        ankle_IKCTRL, ankle_IKCTRLGROUP = ctrl.create(  shape='CUBE', 
                                                        name=ankleIK_CtrlName, 
                                                        radius=self.input._scale/2)
        
        #snap the control to bone
        studioBlender.sanpToBone (self.armature, '%s_Ankle_Bone'% side, ankle_IKCTRLGROUP.name, 'location', True, False)
         
        ankle_constrain = ankleIK_SDK.constraints.new(type='COPY_TRANSFORMS')
        ankle_constrain.target = ankle_IKCTRL
        ankle_constrain.target_space = 'WORLD'
        ankle_constrain.owner_space = 'WORLD'
        ankle_constrain.influence = 1   
         
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='StretchSwitch', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='AnkleRoll', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='BallRoll', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='ToeRoll', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='HeelRoll', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
         
        #studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='BallTwist', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='ToeTwist', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='HeelTwist', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
         
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='KneeVisibility', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')
        studioBlender.addAttribute(node=ankle_IKCTRL.name, longName='KneeTwist', attributeType=float, defaultValue=0, minValue=0, maxValue=1, description='IK Leg Stretch Switch')

        #=======================================================================
        # bpy.ops.wm.properties_add(data_path="object")
        # setAttr "RT_Ankle_IK_Ctrl.switchStretch" 0;
        # setAttr "RT_Ankle_IK_Ctrl.lengthStrech" 10;
        # setAttr "RT_Ankle_IK_Ctrl.upperStretch" 0;
        # setAttr "RT_Ankle_IK_Ctrl.lowerStretch" 0;
        # setAttr "RT_Ankle_IK_Ctrl.stretch" 0;
        # setAttr "RT_Ankle_IK_Ctrl.footRoll" 0;
        # setAttr "RT_Ankle_IK_Ctrl.footRollAngle" 0;
        # setAttr "RT_Ankle_IK_Ctrl.footTwist" 0;
        # setAttr "RT_Ankle_IK_Ctrl.toeRoll" 0;
        # setAttr "RT_Ankle_IK_Ctrl.toeTwist" 0;
        # setAttr "RT_Ankle_IK_Ctrl.ballLift" 0;
        # setAttr "RT_Ankle_IK_Ctrl.heelTwist" 0;
        # setAttr "RT_Ankle_IK_Ctrl.kneeVisibility" 0;
        # setAttr "RT_Ankle_IK_Ctrl.kneeTwist" 0;
        # lockTo Global, World, COG, Pelvis
        #=======================================================================
        
        #set driven ankle roll    
        studioBlender.setDriven(node=ankleRoll_SDK.name,
                                nodeAttr=['rotation_euler', 0],
                                driver=ankle_IKCTRL.name,
                                driverType='SUM',
                                variableType='SINGLE_PROP',
                                variableName='Ankle_Roll',
                                driverAttr='AnkleRoll'
                                )
         
        #set driven ball roll    
        studioBlender.setDriven(node=ballRoll_SDK.name,
                                nodeAttr=['rotation_euler', 0],
                                driver=ankle_IKCTRL.name,
                                driverType='SUM',
                                variableType='SINGLE_PROP',
                                variableName='Ball_Roll',
                                driverAttr='BallRoll'
                                )         
         
        #set driven toe roll    
        studioBlender.setDriven(node=toeRoll_SDK.name,
                                nodeAttr=['rotation_euler', 0],
                                driver=ankle_IKCTRL.name, 
                                driverType='SUM',
                                variableType='SINGLE_PROP',
                                variableName='Toe_Roll',
                                driverAttr='ToeRoll'
                                ) 
         
        #set driven toe twist    
        studioBlender.setDriven(node=toeRoll_SDK.name,
                                nodeAttr=['rotation_euler', 2],
                                driver=ankle_IKCTRL.name, 
                                driverType='SUM',
                                variableType='SINGLE_PROP',
                                variableName='Toe_Twist',
                                driverAttr='ToeTwist'
                                )           
 
        #set driven hell roll    
        studioBlender.setDriven(node=hellRoll_SDK.name,
                                nodeAttr=['rotation_euler', 0],
                                driver=ankle_IKCTRL.name, 
                                driverType='SUM',
                                variableType='SINGLE_PROP',
                                variableName='Hell_Roll',
                                driverAttr='HellRoll'
                                ) 
         
        #set driven hell twist    
        studioBlender.setDriven(node=hellRoll_SDK.name,
                                nodeAttr=['rotation_euler', 2],
                                driver=ankle_IKCTRL.name, 
                                driverType='SUM',
                                variableType='SINGLE_PROP',
                                variableName='Hell_Twist',
                                driverAttr='HellTwist'
                                )         
                
        #ik stretch
        
        
        
        
        
        
        #fk setup
        
        #pelvis fk control
        pelvisFK_CtrlName = '%s_%s_%s_%s'% (side, self.input._pelvis, self.input._fk, self.input._control)        
        pelvis_FKCTRL, pelvis_FKCTRLGROUP = ctrl.create(shape='CIRCLE', name=pelvisFK_CtrlName, radius=self.input._scale/1.25)       
        
        #snap the control to bone
        studioBlender.sanpToBone (  self.armature, 
                                    '%s_Pelvis_Bone'% side, 
                                    pelvis_FKCTRLGROUP.name, 
                                    'all', 
                                    True, 
                                    False)
        
        studioBlender.parentContrainToBone( armature=self.armature, 
                                            bone='%s_Pelvis_FK'% side, 
                                            source=pelvis_FKCTRL, 
                                            type='WORLD')

        #knee fk control  
        kneeFK_CtrlName = '%s_%s_%s_%s'% (side, self.input._knee, self.input._fk, self.input._control)        
        knee_FKCTRL, knee_FKCTRLGROUP = ctrl.create(shape='CIRCLE', name=kneeFK_CtrlName, radius=self.input._scale/1.25)       
        
        #snap the control to bone
        studioBlender.sanpToBone (  self.armature, 
                                    '%s_Knee_Bone'% side, 
                                    knee_FKCTRLGROUP.name, 
                                    'all', 
                                    True, 
                                    False)
        
        studioBlender.parentContrainToBone( armature=self.armature, 
                                            bone='%s_Knee_FK'% side, 
                                            source=knee_FKCTRL, 
                                            type='WORLD')        
                
        #ankle fk control  
        ankleFK_CtrlName = '%s_%s_%s_%s'% (side, self.input._ankle, self.input._fk, self.input._control)        
        ankle_FKCTRL, ankle_FKCTRLGROUP = ctrl.create(shape='CIRCLE', name=ankleFK_CtrlName, radius=self.input._scale/1.25)       
        
        #snap the control to bone
        studioBlender.sanpToBone (  self.armature, 
                                    '%s_Ankle_Bone'% side, 
                                    ankle_FKCTRLGROUP.name, 
                                    'all', 
                                    True, 
                                    False)
        
        studioBlender.parentContrainToBone( armature=self.armature, 
                                            bone='%s_Ankle_FK'% side, 
                                            source=ankle_FKCTRL, 
                                            type='WORLD')               
                       
        #ball fk control  
        ballFK_CtrlName = '%s_%s_%s_%s'% (side, self.input._ball, self.input._fk, self.input._control)        
        ball_FKCTRL, ball_FKCTRLGROUP = ctrl.create(shape='CIRCLE', name=ballFK_CtrlName, radius=self.input._scale/1.25)       
        
        #snap the control to bone
        studioBlender.sanpToBone (  self.armature, 
                                    '%s_Ball_Bone'% side, 
                                    ball_FKCTRLGROUP.name, 
                                    'all', 
                                    True, 
                                    False)
        
        studioBlender.parentContrainToBone( armature=self.armature, 
                                            bone='%s_Ball_FK'% side, 
                                            source=ball_FKCTRL, 
                                            type='WORLD')           
                       
        studioBlender.setParent(ball_FKCTRLGROUP.name, ankle_FKCTRL.name)
        studioBlender.setParent(ankle_FKCTRLGROUP.name, knee_FKCTRL.name)
        studioBlender.setParent(knee_FKCTRLGROUP.name, pelvis_FKCTRL.name)
        
        #ik fk switch
        
        ikPlevis_COST = studioBlender.parentContrainBoneToBone( armature=self.armature,
                                                                target=sourceBone[0], 
                                                                source=ikBones[0]
                                                                )
        
        fkPelvis_CONST = studioBlender.parentContrainBoneToBone(armature=self.armature,
                                                                target=sourceBone[0], 
                                                                source=fkBones[0]
                                                                )
                    
        
        ikKnee_COST = studioBlender.parentContrainBoneToBone(   armature=self.armature,
                                                                target=sourceBone[1], 
                                                                source=ikBones[1])
        
        fkKnee_CONST = studioBlender.parentContrainBoneToBone(  armature=self.armature,
                                                                target=sourceBone[1], 
                                                                source=fkBones[1]
                                                                ) 
             
        ikAnkle_COST = studioBlender.parentContrainBoneToBone(  armature=self.armature,
                                                                target=sourceBone[2], 
                                                                source=ikBones[2])
        
        fkAnkle_CONST = studioBlender.parentContrainBoneToBone( armature=self.armature,
                                                                target=sourceBone[2], 
                                                                source=fkBones[2]
                                                                )      
                
        ikBall_COST = studioBlender.parentContrainBoneToBone(   armature=self.armature,
                                                                target=sourceBone[3], 
                                                                source=ikBones[3]
                                                                )
        
        fkBall_CONST = studioBlender.parentContrainBoneToBone(  armature=self.armature,
                                                                target=sourceBone[3], 
                                                                source=fkBones[3]
                                                                )      
                
            #twist streach and bendy
        
        
        #set heiarchy

