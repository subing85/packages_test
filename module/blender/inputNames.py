'''
Name Inputs v0.1
Date : March 26, 2018
Last modified: March 26, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module can provide the name attributes for Rig 
 
example   
    from module.blender import nameInputs            
    input = nameInputs.Inputs()
'''


class Names (object) :
    def __init__(self) :        

        #Global variables
        self._configure = 'Configure'
        self._globalScale = 'GlobalScale'
        self._globals = 'Global'
        
        self._jointRadius = 0.1
        self._nameStyle = (0, 1, 2)
        #self._nameStyle = (1, 0, 2)
        #self._nameStyle = (2, 1, 0)
        
        self._leg = 'Leg'
        self._legFinger = 'LegFinger'  
                      
        self._pelvis = 'Pelvis'
        self._knee = 'Knee'
        self._ankle = 'Ankle'
        self._legPoleVector = 'LegPoleVector'
        
        self._foot = 'Foot'         
        self._ball = 'Ball'
        self._toe = 'Toe'
        self._heel = 'Heel'
        self._pinkyToe = 'PinkyToe'
        self._bigToe = 'BigToe'
                
        self._hip = 'Hip' 
        self._hipTail = 'HipTail'                       
        self._cog = 'Cog'
        self._spineA = 'SpineA'
        self._spineB = 'SpineB'        
        self._chest = 'Chest'        
        self._neckA = 'NeckA'
        self._neckB = 'NeckB'        
        self._head = 'Head'        
        self._headTail = 'HeadTail'        
        
        self._upperJaw = 'UpperJaw'
        self._upperJawTail = 'UpperJawTail'        
        self._lowerJaw = 'LowerJaw'     
        self._lowerJawTail = 'LowerJawTail' 
           
        self._tongueA = 'TongueA'
        self._tongueB = 'TongueB'
        self._tongueC = 'TongueC'
        self._tongueD = 'TongueD' 
        self._tongueE = 'TongueE' 
        
        self._uvulaA = 'UvulaA'
        self._uvulaB = 'UvulaB'
        self._uvulaC = 'UvulaC'
        self._uvulaD = 'UvulaD'  
        
        self._eyeA = 'EyeA'
        self._eyeB = 'EyeB'        
        self._eyeAim = 'EyeAim'
        
        self._earA = 'EarA' 
        self._earB = 'EarB'
        
        self._clavicle = 'Clavicle'
        self._shoulder = 'Shoulder'
        self._elbow = 'Elbow'
        self._wrist = 'Wrist'
        self._armPoleVector = 'ArmPoleVector'         
        
        self._thumbA = 'ThumbA'
        self._thumbB = 'ThumbB'
        self._thumbC = 'ThumbC'
        self._thumbD = 'ThumbD'
        self._thumbE = 'ThumbE'        
        
        self._indexA = 'IndexA'
        self._indexB = 'IndexB'
        self._indexC = 'IndexC'
        self._indexD = 'IndexD'
        self._indexE = 'IndexE'
                
        self._middleA = 'MiddleA'
        self._middleB = 'MiddleB'
        self._middleC = 'MiddleC'
        self._middleD = 'MiddleD'
        self._middleE = 'MiddleE'        
        
        self._ringA = 'RingA'    
        self._ringB = 'RingB'    
        self._ringC = 'RingC'    
        self._ringD = 'RingD'    
        self._ringE = 'RingE'            
            
        self._pinkyA = 'PinkyA'         
        self._pinkyB = 'PinkyB'         
        self._pinkyC = 'PinkyC'         
        self._pinkyD = 'PinkyD'         
        self._pinkyE = 'PinkyE'          
        
        self._tailA = 'TailA'   
        self._tailB = 'TailB'   
        self._tailC = 'TailC'   
        self._tailD = 'TailD'   
        self._tailE = 'TailE'
        self._tailF = 'TailF'        
        
        self._legList = [   self._pelvis, 
                            self._knee, 
                            self._ankle,
                            self._legPoleVector,
                            self._ball,
                            self._toe,
                            self._heel,
                            self._pinkyToe,
                            self._bigToe
                            ]
        
        self._armList = [   self._clavicle,
                            self._shoulder,
                            self._elbow,
                            self._wrist,
                            self._armPoleVector,
                            self._thumbA,
                            self._thumbB,
                            self._thumbC,
                            self._thumbD,
                            self._thumbE,  
                            
                            self._indexA,
                            self._indexB,
                            self._indexC,
                            self._indexD,
                            self._indexE,
                                
                            self._middleA,
                            self._middleB,
                            self._middleC,
                            self._middleD,
                            self._middleE,
                            
                            self._ringA,
                            self._ringB, 
                            self._ringC, 
                            self._ringD,
                            self._ringE,        
                            
                            self._pinkyA,   
                            self._pinkyB,      
                            self._pinkyC,       
                            self._pinkyD,       
                            self._pinkyE, 
                            ]        
        
        

        self._characterName = 'Generic'        
        self._joint = 'Jnt'
        self._fitJoint = 'FJnt'
        self._twist = 'Twist'
        self._leftSide = 'L'
        self._rightSide = 'R'
        self._centerSide = 'C'
        self._frontSide = 'F'
        self._backSide = 'B' 

        self._ik = 'IK'
        self._fk = 'FK'
        self._bind = 'Bind'
        self._blend = 'Blend'       

        self._configureJoint = 'ConfigureJoint'       

        #General Utilities
        self._blendColor = 'BC'
        self._reverse = 'RV'
        self._multiplyDivide = 'MD'
        self._plusMinusAverage = 'PM'
        self._clamp = 'CP'
        self._distanceBetween = 'DB'
        self._pointOnCurveInfo = 'PC'       

        self._group = 'Group'
        self._offset = 'Offset'
        self._null = 'Null'
        self._control = 'Ctrl'
        self._sdk = 'SDK'
        self._locator = 'Loc'
        self._curve = 'Crv'   
        self._deform = 'Deform'  

        self._pointConstraint = 'PointConstraint' 
        self._orientConstraint = 'OrientConstraint'
        self._aimConstraint = 'AimConstraint' 
        self._parentConstraint = 'ParentConstraint'
        self._scaleConstraint = 'ScaleConstraint'
        self._poleVectorConstraint = 'PoleVectorConstraint'      

        self._ikHandle = 'IKHandle'
        self._effector = 'IKEffector'             

        self._hierarchyAppend = {'World': { '1_Control': ['Offset', 'Controls'], 
                                            '2_Geometry': ['Layout', 'Animation', 'Render'],
                                            '3_Skeleton': ['FitSkeleton'],
                                            '4_Deformer': [],
                                            '5_Global': [],                                            
                                            }
                                 }
        
#End########################################################################################################        
