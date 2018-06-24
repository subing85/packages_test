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


from module import inputNames 
from module import studioBlender
from assets.blender import skeletonBiped




class Build(object):
    
    def __init__(self):
    
        
        self.input = inputNames.Names()
        
        
    
    def create(self):
        
        #studioBlender.createBones (armature, fitJoints, parent)
        
        
        legSkeletons = ['L_Pelvis', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
        spineSkeletons = ['Cog', 'SpineA', 'SpineB', 'Chest', 'NeckA', 'NeckB', 'Head', 'HeadTail']
        lowerJawSkeletons = ['LowerJaw', 'LowerJawTail']
        upperJawSkeletons = ['UpperJaw', 'UpperJawTail']
        tongueSkeletons = ['TongueA', 'TongueB', 'TongueC', 'TongueD','TongueE']        
        uvulaSkeletons = ['UvulaA', 'UvulaB', 'UvulaC', 'UvulaD']       
        eyeSkeletons = ['L_Eye', 'L_EyeTail']        
        armSkeletons = ['L_Clavicle', 'L_Shoulder', 'L_Elbow', 'L_Wrist']
        
        thumbSkeletons = ['L_ThumbA', 'L_ThumbB', 'L_ThumbC', 'L_ThumbD', 'L_ThumbE']
        indexSkeletons = ['L_IndexA', 'L_IndexB', 'L_IndexC', 'L_IndexD', 'L_IndexE']
        middleSkeletons = ['L_MiddleA', 'L_MiddleB', 'L_MiddleC', 'L_MiddleD', 'L_MiddleE']
        ringSkeletons = ['L_RingA', 'L_RingB', 'L_RingC', 'L_RingD', 'L_RingE']
        pinkySkeletons = ['L_PinkyA', 'L_PinkyB', 'L_PinkyC', 'L_PinkyD', 'L_PinkyE']
        hipSkeletons = ['Hip', 'HipTail']
        
        puppetBones = {1: {'extrude': 3, 'position': legSkeletons},
                       2: {'extrude': 6, 'position': spineSkeletons},
                       3: {'extrude': 0, 'position': lowerJawSkeletons},
                       4: {'extrude': 0, 'position': upperJawSkeletons},
                       5: {'extrude': 3, 'position': tongueSkeletons},
                       6: {'extrude': 2, 'position': uvulaSkeletons},
                       7: {'extrude': 0, 'position': eyeSkeletons},
                       8: {'extrude': 2, 'position': armSkeletons},
                       
                       9: {'extrude': 3, 'position': thumbSkeletons},
                       10:{'extrude': 3, 'position': indexSkeletons},
                       11:{'extrude': 3, 'position': middleSkeletons},
                       12:{'extrude': 3, 'position': ringSkeletons},
                       13:{'extrude': 3, 'position': pinkySkeletons},
                                           
                       14:{'extrude': 0, 'position': hipSkeletons}   
                       }
        
        skeletonList = ['Root']
        
        skeletonList.extend(legSkeletons[0:4])
        skeletonList.extend(spineSkeletons[0:7])
        skeletonList.extend(lowerJawSkeletons[0:1])
        skeletonList.extend(upperJawSkeletons[0:1])
        skeletonList.extend(tongueSkeletons[0:4])
        skeletonList.extend(uvulaSkeletons[0:3])
        skeletonList.extend(eyeSkeletons[0:1])
        skeletonList.extend(armSkeletons[0:3])        
        skeletonList.extend(thumbSkeletons[0:4])
        skeletonList.extend(indexSkeletons[0:4])
        skeletonList.extend(middleSkeletons[0:4])
        skeletonList.extend(ringSkeletons[0:4])
        skeletonList.extend(pinkySkeletons[0:4])           
        skeletonList.extend(hipSkeletons[0:1])           
        
        tailSkeletonList = {'L_Ball_Bone': 'L_Toe',
                            'Head_Bone': 'HeadTail',
                            'LowerJaw_Bone': 'LowerJawTail',
                            'UpperJaw_Bone': 'UpperJawTail',
                            'TongueD_Bone': 'TongueE',
                            'UvulaC_Bone': 'UvulaD',
                            'L_Eye_Bone': 'L_EyeTail',                            
                            'L_Elbow_Bone': 'L_Wrist',                            
                            'L_ThumbD_Bone': 'L_ThumbE',
                            'L_IndexD_Bone': 'L_IndexE',
                            'L_MiddleD_Bone': 'L_MiddleE',
                            'L_RingD_Bone': 'L_RingE',
                            'L_PinkyD_Bone': 'L_PinkyE',
                            'Hip_Bone': 'HipTail'
                            }   
        
        
        #unparent fit skeletons        
        biped = skeletonBiped.Biped()
        biped.brakeHierarchy(root='Cog')       
                       
        #create base armature
        bpy.ops.object.armature_add(location=(0, 0, 0))   
        armatureObject = bpy.context.scene.objects.active   
        armatureObject.name = 'FitSkeleton'
        armature = armatureObject.data
        armature.name = 'Armature' 
        
        bpy.ops.object.mode_set(mode='EDIT') 
        
        #create bones (extrude bones)     
        for index, propertys in puppetBones.items():          
            bpy.ops.armature.bone_primitive_add()
                        
            for boneIndex in range (propertys['extrude']):            
                bpy.ops.armature.extrude()
                bpy.ops.transform.translate(value=(0,0,1))             
            
        #store the new bone to variable
        #armatureObject = bpy.context.scene.objects.active       
        boneList = armatureObject.data.edit_bones
        baseBoneList = []      
        
        #set name and head bone position
        for index in range(len(boneList)):  
            boneList[index].name = '%s_%s'%(skeletonList[index], self.input._bone)
            baseBoneList.append(boneList[index].name) 
            
            if index>0:                
                
                headObject = bpy.data.objects[skeletonList[index]]                   
                #parentObject = headObject.parent
                headRotation = headObject.rotation_euler

                #headPostion = headObject.location
                headPostion = headObject.matrix_world.translation
                boneList[index].head = headPostion
                boneList[index].roll = headRotation.x

        
        #set tail bone position
        for eachBone in boneList:
            
            if eachBone.name not in tailSkeletonList.keys(): 
                continue
            
            print (eachBone.name, tailSkeletonList[eachBone.name])
            tailObject = bpy.data.objects[tailSkeletonList[eachBone.name]]
            tailPostion = tailObject.matrix_world.translation
            eachBone.tail = tailPostion 



        #bpy.ops.armature.duplicate()
        #create mirror
        rightLegSkeletons = ['L_Pelvis', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
        rightArmSkeletons = ['L_Clavicle', 'L_Shoulder', 'L_Elbow', 'L_Wrist']  
        
        rightThumbSkeletons = ['L_ThumbA', 'L_ThumbB', 'L_ThumbC', 'L_ThumbD', 'L_ThumbE']
        rightIndexSkeletons = ['L_IndexA', 'L_IndexB', 'L_IndexC', 'L_IndexD', 'L_IndexE']
        rightMiddleSkeletons = ['L_MiddleA', 'L_MiddleB', 'L_MiddleC', 'L_MiddleD', 'L_MiddleE']
        rightRingSkeletons = ['L_RingA', 'L_RingB', 'L_RingC', 'L_RingD', 'L_RingE']
        rightPinkySkeletons = ['L_PinkyA', 'L_PinkyB', 'L_PinkyC', 'L_PinkyD', 'L_PinkyE']        
              
        
        rightPuppetBones = {1: {'extrude': 3, 'position': rightLegSkeletons},                            
                            2: {'extrude': 2, 'position': rightArmSkeletons},
                            
                            2: {'extrude': 3, 'position': rightThumbSkeletons},
                            2: {'extrude': 3, 'position': rightIndexSkeletons},
                            2: {'extrude': 3, 'position': rightMiddleSkeletons},
                            2: {'extrude': 3, 'position': rightRingSkeletons},
                            2: {'extrude': 3, 'position': rightPinkySkeletons},
                            
                            }
         
        rightTailSkeletonList = {   'R_Ball_Bone': 'L_Toe',                           
                                    'R_Elbow_Bone': 'L_Wrist',
                                    
                                    'R_ThumbD_Bone': 'L_ThumbE',
                                    'R_IndexD_Bone': 'L_IndexE',
                                    'R_MiddleD_Bone': 'L_MiddleE',
                                    'R_RingD_Bone': 'L_RingE',
                                    'R_PinkyD_Bone': 'L_PinkyE',                                    
                                    }  
        
        rightSkeletonList = []
        rightSkeletonList.extend(rightLegSkeletons[0:4])
        rightSkeletonList.extend(rightArmSkeletons[0:3])         
        
       
        #create mirror bones (extrude bones)
        sb = studioBlender.OpenBlender()
                                    
        for index, propertys in rightPuppetBones.items():             
            currentName = propertys['position'][0].replace('%s_'% self.input._leftSide, '%s_'%self.input._rightSide)
            bpy.ops.armature.bone_primitive_add(name=currentName)
            
            for boneIndex in range (propertys['extrude']):
                bpy.ops.armature.extrude()
                bpy.ops.transform.translate(value=(0,0,1))

           
        armatureObject = bpy.context.scene.objects.active       
        rightBoneList = armatureObject.data.edit_bones 

        #set mirror name and head bone position
        ing = 0
        for eachRightBone in rightBoneList:  

            if eachRightBone.name in baseBoneList:
                continue
            
            prefixName = rightSkeletonList[ing].replace('%s_'% self.input._leftSide, '%s_'%self.input._rightSide)            
            eachRightBone.name = '%s_%s'%(prefixName, self.input._bone)
             
            rightHeadObject = bpy.data.objects[rightSkeletonList[ing]]                   
            #parentObject = rightHeadObject.parent
            rightHeadRotation = rightHeadObject.rotation_euler            
            
            rightHeadPostion = rightHeadObject.matrix_world.translation
            eachRightBone.head = (rightHeadPostion.x*-1, rightHeadPostion.y, rightHeadPostion.z)
            eachRightBone.roll = rightHeadRotation.x*-1      
            
            ing+=1
            

        #set mirror tail bone position
        for eachRightBone in rightBoneList:
            if eachRightBone.name in baseBoneList:
                continue 
            
            if eachRightBone.name not in rightTailSkeletonList.keys():
                continue
            
            rightTailObject = bpy.data.objects[rightTailSkeletonList[eachRightBone.name]] 
            rightTailPostion = rightTailObject.matrix_world.translation
            eachRightBone.tail = (rightTailPostion.x*-1,  rightTailPostion.y, rightTailPostion.z)            

           
        #bpy.ops.object.select_all(action='DESELECT')
        
        bpy.ops.object.mode_set(mode='OBJECT')    
        #bpy.context.object.data.draw_type = 'STICK'

        #re-parent  
        biped.setHierarchy()
        

             
        #bpy.ops.armature.duplicate()
        

        #mirror
        
        
        
        
        
