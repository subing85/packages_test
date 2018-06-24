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

import imp

from module import inputNames
imp.reload(inputNames)


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
                        
            :Type     class function (method)            
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
    
    
    def getHierarchyDependent(self, root=None):
    
        '''
        Description
            Function for collect all the objects from the root.                      
            :Type     class function (method)             
            :param    root   <str>     example  ['Cog']
            :return   result <[str]>    example ['Cog', 'L_Pelvis': 'R_Pelvis', 'L_Knee',: 'R_Knee', 'L_Ankle': 'R_Ankle']
            
        ''' 
        
        self._dependent = collectHierarchy(root=root)        
        dependent_temp = self._dependent     
        self._onlyDependent = dependent_temp.remove(root)
   

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
    bpy.ops.object.track_clear(type='CLEAR_KEEP_TRANSFORM')
    

def sanpToBone (armature, bone, target, snapType, head, tail):
    
    '''
    Description
        Standalone Function for create Empty blender Object based on inputs                        
        :Type - class function (method)            
        :param   armature    <str>  example 'Armature'
        :param   bone        <str>  example 'L_Ankle_Bone'
        :param   target      <str>  example 'Empty'
        :param   snapType    <str>  example 'location' or 'rotation' or None
        :param   head        <bool> example 'True' or 'False'
        :param   tail        <bool> example 'True' or 'False'
        :return  None
    '''    
    
    bpy.ops.object.mode_set(mode='OBJECT') 
    bpy.data.objects[target].select = True
    bpy.context.scene.objects.active = bpy.data.objects[target]
    
    if snapType=='location':
        bpy.ops.object.constraint_add_with_targets(type='COPY_LOCATION')
        bpy.context.object.constraints["Copy Location"].target = bpy.data.objects[armature]
        bpy.context.object.constraints["Copy Location"].subtarget = bone             
        
    elif snapType=='rotation':
        bpy.ops.object.constraint_add_with_targets(type='COPY_ROTATION')
        bpy.context.object.constraints["Copy Rotation"].target = bpy.data.objects[armature]
        bpy.context.object.constraints["Copy Rotation"].subtarget = bone        
    
    else:
        bpy.ops.object.constraint_add(type='COPY_TRANSFORMS')        
        bpy.context.object.constraints["Copy Transforms"].target = bpy.data.objects[armature]
        bpy.context.object.constraints["Copy Transforms"].subtarget = bone
        
    position = 0
    if tail:    
        position = 1
    elif head and tail:
        position = 0.5
    
    bpy.context.object.constraints["Copy Location"].head_tail = position
        
    bpy.ops.object.track_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.ops.object.constraints_clear()
    
    
def sanpToObject (source, target, snapType):
    
    '''
    Description
        Standalone Function for create Empty blender Object based on inputs                        
        :Type - class function (method)            
        :param   armature    <str>  example 'Armature'
        :param   bone        <str>  example 'L_Ankle_Bone'
        :param   target      <str>  example 'Empty'
        :param   snapType    <str>  example 'location' or 'rotation' or None
        :param   head        <bool> example 'True' or 'False'
        :param   tail        <bool> example 'True' or 'False'
        :return  None
    '''    
    
    bpy.ops.object.mode_set(mode='OBJECT') 
    bpy.data.objects[target].select = True
    bpy.context.scene.objects.active = bpy.data.objects[target]
    
    if snapType=='location':
        bpy.ops.object.constraint_add_with_targets(type='COPY_LOCATION')
        bpy.context.object.constraints["Copy Location"].target = bpy.data.objects[source]
        
    elif snapType=='rotation':
        bpy.ops.object.constraint_add_with_targets(type='COPY_ROTATION')
        bpy.context.object.constraints["Copy Rotation"].target = bpy.data.objects[source]
    
    else:
        bpy.ops.object.constraint_add(type='COPY_TRANSFORMS')        
        bpy.context.object.constraints["Copy Transforms"].target = bpy.data.objects[source]

    bpy.ops.object.track_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.ops.object.constraints_clear()    
    
    
def duplicateBones(armature=None, source=None, search=None, replace=None):
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    
    fitSkeleton = bpy.data.objects[armature]
    bpy.context.scene.objects.active = fitSkeleton
    bpy.ops.object.mode_set(mode='EDIT')
    armatureObject = bpy.context.scene.objects.active     
    
    print ('source\t', source)

    #select and duplicate the bones
    existsBoneList = []
    print ('\n......................')
    
    ing = 0
    for eachBone in armatureObject.data.edit_bones:
        existsBoneList.append(eachBone.name)
        
        if eachBone.name not in source :
            continue
        
        if ing==0:
            eachBone.select_head = True
            
        eachBone.select = True
        eachBone.select_tail = True
        armatureObject.data.edit_bones.active   
             
        ing+=1
        
    bpy.ops.armature.duplicate() # duplicate the selected bones

    armatureObject = bpy.context.scene.objects.active   
    #rename the duplicate the bones
    duplicateBoneList = []
    ing = 0
    for eachBone in armatureObject.data.edit_bones:
        if eachBone.name in existsBoneList :
            continue
        
        print ('abc\t', source[ing])
        eachBone.name = source[ing].replace(search, replace) 
        duplicateBoneList.append(eachBone.name)
        ing+=1
        
    bpy.ops.armature.select_all(action='DESELECT')    
    print ('duplicate bones\t- ', duplicateBoneList)
    return duplicateBoneList
    
            
    '''
    import bpy
    arm = bpy.context.object.data
    for b in arm.edit_bones[:]:
        cb = arm.edit_bones.new(b.name)
    
        cb.head = b.head
        cb.tail = b.tail
        cb.matrix = b.matrix
        cb.parent = b 
        
    '''           

    
def getWorldRoation(source):
   pass    
    
    
def setMirror(nodes, axis, search, replace):
    
    '''
    Description
        Function for duplicat the input object place to like a mirror                      
        :Type     standalone function            
        :param    nodes   <list>     example ['L_Pelvis', 'L_Knee', 'L_Ankle']
        :param    axis    <tuple>    example (-1, 1, 1)
        :param    search  <str>      example 'L_'
        :param    replace <str>      example 'R_'
        
        :return    duplicats <dict>    example ('L_Pelvis': 'R_Pelvis', 'L_Knee',: 'R_Knee', 'L_Ankle': 'R_Ankle')
        
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


def createBones(**kwargs):
    
    '''
    Description
        Function for create armature, bones and its placement.                      
        :Type     standalone function                       
        :param    label            <str>     example 'FitSkeleton'
        :param    armatureLabel    <str>     example 'Armature'
        :param    skeletons        <dict>    example { 1: {'extrude': 3, 'position': ['LowerJaw', 'LowerJawTail']}
        :param    skeletonList     <list>    example ['Root', 'RootTail', 'Pelvis', 'Knee', 'Ankle']
        :param    leftSkeletons    <list>    example ['Pelvis', 'Knee', 'Ankle', 'Ball', 'Toe', 'Eye', 'EyeTail']
        :param    tailSkeletons    <dict>    example {'L_Ball_Bone': 'Toe', 'Head_Bone': 'HeadTail'}
        :return   True             <bool>
        :example to execute  
        
            from assets.blender import skeletonBiped      
            studioBlender.createBones(  label=label, 
                                        armatureLabel=armatureLabel,
                                        skeletons = puppetSkeletons,
                                        skeletonList = skeletonList,
                                        leftSkeletons = leftSkeletons,
                                        tailSkeletons = tailSkeletons
                                        )
    '''  
     
    armatures = kwargs['armatures']
    labelName = kwargs['label']
    armatureName = kwargs['armatureLabel']
    skeletons = kwargs['skeletons']
    skeletonList = kwargs['skeletonList']    
    leftSkeletons = kwargs['leftSkeletons']
    rightSkeletons = kwargs['rightSkeletons']
    tailSkeletons = kwargs['tailSkeletons']
    extrudeBones = kwargs['extrudeBones']
    axis = kwargs['axis']
    roll = kwargs['roll']
    
    input = inputNames.Names()
    
    #create base armature
    if armatures:
        bpy.ops.object.armature_add(location=(0, 0, 0))   
        armatureObject = bpy.context.scene.objects.active   
        armatureObject.name = labelName
        armature = armatureObject.data
        armature.name = armatureName
    #===========================================================================
    # else:
    #     bpy.ops.object.mode_set(mode='OBJECT')
    #     bpy.ops.object.select_all(action='DESELECT') 
    #     currentArmature = bpy.data.objects[labelName] 
    #     currentArmature.select = True
    #     armatureObject = bpy.context.scene.objects.active 
    #===========================================================================
    armatureObject = bpy.context.scene.objects.active      
    bpy.ops.object.mode_set(mode='EDIT') # set the edit mode 
    
    #create all bones (extrude bones)     
    for index, propertys in skeletons.items():
        
        if index==0:
            continue

        bpy.ops.armature.bone_primitive_add()        
        for boneIndex in range (propertys['extrude']):
            bpy.ops.armature.extrude()
            #bpy.ops.transform.translate(value=(0,0,1))      
    
    #store the new bone to variable
    baseBoneList = []     
    armatureObject = bpy.context.scene.objects.active   
    boneList = armatureObject.data.edit_bones


    # set name and head bone position
    ing = 0
    for eachBone in boneList: 
        
        if extrudeBones:
            if eachBone.name in extrudeBones:
                continue
        
        boneName = '%s_%s'%(skeletonList[ing], input._bone)
       
        if leftSkeletons:
            if skeletonList[ing] in leftSkeletons:
                boneName = '%s_%s_%s'%(input._leftSide, skeletonList[ing], input._bone)
                
        if rightSkeletons:
            if skeletonList[ing] in rightSkeletons:
                boneName = '%s_%s_%s'%(input._rightSide, skeletonList[ing], input._bone)
                
        eachBone.name = boneName
        baseBoneList.append(eachBone.name)        
              
        headObject = bpy.data.objects[skeletonList[ing]]                   
        headRotation = headObject.rotation_euler
         
        headPostion = headObject.matrix_world.translation
        eachBone.head = (headPostion.x*axis[0], headPostion.y*axis[1], headPostion.z*axis[2])
        eachBone.roll = headRotation.x*roll 
        
        ing+=1       
    
    
    pprint.pprint (tailSkeletons)
    
    # set tail bone position
    for eachBone in boneList:
         
        if eachBone.name not in tailSkeletons.keys(): 
            continue
        
        print ('Tail\t', eachBone.name)
        
        
        tailObject = bpy.data.objects[tailSkeletons[eachBone.name]]
        tailPostion = tailObject.matrix_world.translation
        eachBone.tail = (tailPostion.x*axis[0], tailPostion.y*axis[1], tailPostion.z*axis[2])
        
    return baseBoneList


def createBones_(armature=True, fitJoints=None, parent=True):
    
    '''
    Description
        Function for create Armature Bones based on the input arguments                      
        :Type     standalone function            
        :param    fitJoints   <[str]>     example  ['L_Pelvis', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
        :param    parent    <bool>      example True or False        
        :return    bones <[str]>    example ['L_Pelvis': 'R_Pelvis', 'L_Knee',: 'R_Knee', 'L_Ankle': 'R_Ankle']
        
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


def collectHierarchy(root=None):

    '''
    Description
        Function for collect all the objects from the root.                      
        :Type     standalone function            
        :param    root   <str>     example  ['Cog']
        :return   result <[str]>    example ['Cog', 'L_Pelvis': 'R_Pelvis', 'L_Knee',: 'R_Knee', 'L_Ankle': 'R_Ankle']
        
    ''' 
    
    index = 0           
    result = [root]
    
    while (index<len(result)):
        data = bpy.data.objects[result[index]]          
        for eachChildren in data.children:
            result.append(eachChildren.name)
        index+=1        
        
    return result



def setIKContrain(armature=None, bone=None, ikHandle=None, chainCount=None, poleTarget=None):
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    
    armatureObject = bpy.data.objects[armature]
    bpy.context.scene.objects.active = armatureObject
    bpy.ops.object.mode_set(mode='POSE')
    
    #set ankle ik handle
    ikBone = armatureObject.pose.bones[bone]
    ikConstrain = ikBone.constraints.new(type='IK')
    ikConstrain.target = bpy.data.objects[ikHandle]
    ikConstrain.name = '%s_IK'% ikHandle
    
    if chainCount:
        ikConstrain.chain_count = chainCount
    
    if poleTarget:
        ikConstrain.pole_target = poleTarget
        
    return ikConstrain


def addAttribute(node=None, longName=None, attributeType=None, defaultValue=0, minValue=0, maxValue=1, description=None): 
      
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    
    currentNode = bpy.data.objects[node] 
    currentNode.select = True
    bpy.context.scene.objects.active = currentNode    
    
    activeObject= bpy.context.active_object
    
    activeObject[longName] = defaultValue

    #bpy.ops.wm.properties_add(data_path="object")
    #===========================================================================
    # bpy.ops.wm.properties_edit( data_path="object",
    #                             property=longName, 
    #                             value=defaultValue, 
    #                             min=minValue, 
    #                             max=maxValue, 
    #                             use_soft_limits=False, 
    #                             soft_min=-1, 
    #                             soft_max=1, 
    #                             description='description')
    #===========================================================================
    
    #bpy.ops.wm.properties_edit(data_path="object", property="prop", value="1.0", min=0, max=1, use_soft_limits=False, soft_min=0, soft_max=1, description="")

    
    #return True

#End##########################################################################################