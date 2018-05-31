'''
Studio Blender Puppet v0.1
Date : March 25, 2018
Last modified: March 25, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface 
 
example   
    import imp
    from module.blender import buildPuppet
    imp.reload(buildPuppet)
    buildPuppet.launch()
'''


import sys
import os
import imp
import warnings
import pprint
import bpy
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore

from module.blender import jointBiped      
imp.reload(jointBiped)
      


context = None

CURRENT_PATH = os.path.dirname (__file__) # CURRENT_PATH = os.getcwd()
UI_FILE = '{}/buildPuppet_ui.ui'.format (CURRENT_PATH)
FROM, BASE = uic.loadUiType (UI_FILE)

class Puppet (FROM, BASE):
    
    def __init__(self, *args):
        super(Puppet, self).__init__(*args)
  
        uic.loadUi(UI_FILE, self)    
    
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0] 
        
        self._fitJoints = [ 'None'
                            'Biped', 
                            'Bird', 
                            'Bug', 
                            'Dinosaure', 
                            'Quadruped',
                            ]       

        self.setWindowTitle ('Studio Puppet v0.1')
        self.setupUi()
        
        
        self.button_fitJoints.clicked.connect (self.createFitJoints)  
        
        print (bpy.context)  

    
    def setupUi(self):
        self.comboBox_fitJoints.addItems (self._fitJoints)
    
    
        
    def createFitJoints(self):
        
        print (bpy.context)
        
        cont = bpy.context

        
        #global context
        bpy.ops.object.empty_add ()    
        bpy.context.object.name = 'name'    
           
        #=======================================================================
        # import imp
        # from module.blender import jointBiped
        # imp.reload(jointBiped)
        # biped = jointBiped.Biped()
        # biped.create(cont)
        #=======================================================================


        
        
def launch():
    #global context
    #context = bpy.context.copy()
    bpy.ops.wm.pyqt_event_loop()                


class PyQtEventLoop(bpy.types.Operator): # register class stuff
    bl_idname = "wm.pyqt_event_loop"
    bl_label = "PyQt Event Loop"
    _timer = None
    _window = None
 
    def execute(self, context):
        self._application = QtWidgets.QApplication.instance()
        if self._application is None:
            self._application = QtWidgets.QApplication(['blender'])
        self._eventLoop = QtCore.QEventLoop()
 
        self.window = Puppet()                
        self.window.show()
        return {'RUNNING_MODAL'} 
    
 
def register():
    bpy.utils.register_class(PyQtEventLoop)
    
def unregister():
    bpy.utils.unregister_class(PyQtEventLoop)
    
try:
    unregister()
except:
    pass

register()  
  
        
  
#===============================================================================
# if __name__ == 'module.blender.buildPuppet':   
#     app = QtWidgets.QApplication(sys.argv) 
#     window = Puppet()
#     window.show()   
#     #sys.exit (app.exec())
#===============================================================================



