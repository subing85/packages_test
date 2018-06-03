'''
Studio Asset v0.1
Date : June 01, 2018
Last modified: June 01, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module create and modify the asset attributes 
 
example   
from assets import assetTool
reload(assetTool)
assetTool.runMayaUiDemo()    
'''

import sys
import os
import datetime
import warnings
import pprint
from functools import partial

from PySide import QtGui
from PySide import QtCore
from PySide import QtUiTools
import shiboken

from module import openPySide
from module import openStyleSheet
from pipe import pipeLayout
from assets import studioAsset
reload(studioAsset)  


from maya import cmds
from maya import mel
from pymel import core as pymel
from maya import OpenMayaUI as openMayaUI
from maya import OpenMaya as openMaya

CURRENT_PATH = os.path.dirname (__file__)

PRJECT_PATH = os.environ['PROJECT_PATH']
PROJECT_NICE_NAME = os.environ['PROJECT_NICE_NAME']
PROJECT_FULL_NAME = os.environ['PROJECT_FULL_NAME']
PRJECT_PATH = os.environ['PROJECT_PATH']
DATABASE_PATH = os.environ['DATABASE_PATH']
PACKAGE_PATH = os.environ['PACKAGE_PATH']
DATABASE_SOURCE = (os.path.join (PACKAGE_PATH,  'pipe', 'pipeInput_%s.json'% PROJECT_NICE_NAME))

UI_PATH = os.path.join (CURRENT_PATH, 'assetTool_ui.ui')
MAINWINDOW = shiboken.wrapInstance (long(openMayaUI.MQtUtil.mainWindow()), QtGui.QWidget)

FROM, BASE = openPySide.loadUi (UI_PATH)    

MAYA_MAIN_WINOW    = shiboken.wrapInstance(long(openMayaUI.MQtUtil.mainWindow()), QtGui.QWidget)


def runMayaUiDemo():
    
    '''
    Description            
        Function for load the class and delete the exists 'UI' in the scene.
        
        :Type - standalone function        
        :param    None        
        :return   None
        
        :example to execute        
            from assets import studioAsset
            reload(studioAsset)
            wind = studioAsset.runMayaUiDemo()   
            wind.show()     
    '''    
    
    if (cmds.window("MainWindow_asset", ex=True)):
        cmds.deleteUI ('MainWindow_asset')        
    else:
        #sys.stdout.write("tool is already open!\n")
        pass
    
    wind = StudioAsset()
    wind.show()  
        

class StudioAsset (FROM, BASE):

    def __init__(self, parent=MAYA_MAIN_WINOW):
        super(StudioAsset, self).__init__(parent) #QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
    
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]            
            
        styleSheet = openStyleSheet.StyleSheet (self)
        styleSheet.setStyleSheet()
        
        self.setWindowTitle ('Studio Asset v0.1')
        self.resize (460, 500)        
        
        self.pipe = pipeLayout.Layout (DATABASE_SOURCE)
        
        #=======================================================================
        # mainWindow = pymel.lsUI (wnd=1)[0]        
        # #self.setObjectName ('MainWindow') 
        # 
        # if pymel.dockControl ('MainWindow_asset', q=1, ex=1) :
        #     pymel.deleteUI('MainWindow_asset', ctl=1)
        # 
        # self.floatingLayout = pymel.paneLayout (cn='single', w=300, p=mainWindow)
        # 
        # cmds.dockControl ('MainWindow_asset', l='Smart Bake - v0.1', area='left', content=self.floatingLayout, allowedArea=['right', 'left'])        
        # cmds.control ('MainWindow_asset', e=1, p=self.floatingLayout)        
        #=======================================================================
        
        self.button_refresh.clicked.connect (self.loadValuesToWidgets)
        self.button_create.clicked.connect (self.create)
        self.button_close.clicked.connect (self.close)
        
        self.uiConfigure ()
        self.loadValuesToWidgets()   
        
        
    def uiConfigure (self):       
        
        assetTypes = self.pipe._pipeAttributes['assets']['primary']['catagory']['types']['values']       
        self.comboBox_assetType.addItems(assetTypes)       
        
        worksStatus = self.pipe._pipeAttributes['assets']['primary']['model']['modelStatus']['values']
        self.comboBox_workStatus.addItems(worksStatus)        
        
        assetPath = os.path.abspath(os.path.join(PRJECT_PATH, 'PreProduction', 'asset')).replace('\\', '/')        
        self.lineEdit_assetPath.setText(assetPath)        


    def loadValuesToWidgets (self):
        
        sa = studioAsset.StudioAsset(node=None)
        sa.getAssetNode()
        
        if not sa.node:
            openMaya.MGlobal.displayWarning ('Asset node does not exists')         
            return False
        
        values = sa.getValues()  
        
        #set QlineEidt value       
        lineWidgets = self.groupBox.findChildren (QtGui.QLineEdit)
        
        for eachWidget in lineWidgets:   
                     
            if '_' not in str(eachWidget.objectName()):
                continue
                      
            currentItem = str(eachWidget.objectName()).split('_')[-1]
            
            if currentItem not in values:
                continue
                        
            eachWidget.setText(values[currentItem])
            
        #set QComboBox value 
        comboBoxWidgets = self.groupBox.findChildren (QtGui.QComboBox)
        for eachWidget in comboBoxWidgets:   
                     
            if '_' not in str(eachWidget.objectName()):
                continue
                      
            currentItem = str(eachWidget.objectName()).split('_')[-1]
            
            if currentItem not in values:
                continue

            itemCount = eachWidget.count () 
            currentIndex = 0              
            for index in range(itemCount) :
                currentText = eachWidget.itemText (index)
                 
                if currentText != values[currentItem] :
                    continue  
                currentIndex = index 
             
            eachWidget.setCurrentIndex (currentIndex)         
        
    
    def create (self):  
        sa = studioAsset.StudioAsset(node=None)
        sa.getAssetNode()
        pymel.select (sa.node, r=True)      
        sa.create()
        
        assetName = str(self.lineEdit_assetName.text())
        assetType = str(self.comboBox_assetType.currentText())
        modelVersion = str(self.lineEdit_modelVersion.text())
        puppetVersion = str(self.lineEdit_puppetVersion.text())
        renderVersion = str(self.lineEdit_renderVersion.text())
        assetPath = str(self.lineEdit_assetPath.text())
        workStatus = str(self.comboBox_workStatus.currentText())
        
        values = {1: assetName,
                  2: assetType,
                  3: modelVersion,
                  5: puppetVersion,
                  8: renderVersion,
                  9: assetPath,
                  11: workStatus}
        
        sa.setValues(values=values)
        
        
    def close(self):                
        if (cmds.window("MainWindow_asset", ex=True)):
            cmds.deleteUI ('MainWindow_asset')        

#End##################################################################################