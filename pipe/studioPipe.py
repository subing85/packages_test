'''
Studio Publi-SH v0.1
Date : February 09, 2018
Last modified: February 09, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface    
'''

import sys
import os
import subprocess
import pprint
import warnings
from functools import partial

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic

from module import studioDatabase
from pipe import pipeLayout
from module import studioStyleSheet

from pipe import studioDetails
reload (studioDatabase)

#CURRENT_PATH = os.getcwd()
CURRENT_PATH = os.path.dirname (__file__)
PRJECT_PATH = os.environ['PROJECT_PATH']
PROJECT_NICE_NAME = os.environ['PROJECT_NICE_NAME']
PROJECT_FULL_NAME = os.environ['PROJECT_FULL_NAME']
PRJECT_PATH = os.environ['PROJECT_PATH']
DATABASE_PATH = os.environ['DATABASE_PATH']
PACKAGE_PATH = os.environ['PACKAGE_PATH']

DATABASE_SOURCE = os.path.abspath(os.path.join (PACKAGE_PATH, 'pipe', 'pipeInput_%s.json'% PROJECT_NICE_NAME))

print 'DATABASE_SOURCE\t', DATABASE_SOURCE
UI_FILE = '{}/studioPipe_ui.ui'.format (CURRENT_PATH)

FROM, BASE = uic.loadUiType (UI_FILE)

class Pipes (QtGui.QMainWindow):
    
    def __init__(self, *args):
        super(Pipes, self).__init__(*args)
  
        uic.loadUi(UI_FILE, self)    
    
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]

        self.setWindowTitle ('Studio Publi-SH v0.1')

        self.splitter.setSizes ([167, 1664])
        self.splitter_properties.setSizes ([1167, 471])      
        #self.resize (988, 730)
        self.showMaximized()
        
        self.groupBox_shelf.hide ()
        self.treeWidget_properties.hide ()
        self.groupBox_details.hide () 
        
        print 'DATABASE_SOURCE\t', DATABASE_SOURCE       
                
        self.pipe = pipeLayout.Layout (DATABASE_SOURCE) #ge the database information     
        
        #pprint.pprint (self.pipe)
        
        self.scene = 'scene'              
                      
        self.currentLayout = None
        self.defaluDatabase = {} 
        
        self.uiConfigure ()        
        self.createLayout ()  
        self.uiSignals ()
              
    
    def uiConfigure (self) :
        studioStyleSheet.setIcon(self.action_addOn, '{}/icons'.format (os.path.dirname(CURRENT_PATH)), [50, 50], False)            
        studioStyleSheet.setIcon(self.action_update, '{}/icons'.format (os.path.dirname(CURRENT_PATH)), [50, 50], False)            
        studioStyleSheet.setIcon(self.action_remove, '{}/icons'.format (os.path.dirname(CURRENT_PATH)), [50, 50], False)    
        studioStyleSheet.setToolBar (None, [self.action_addOn, self.action_update, self.action_remove], self.horizontalLayout_shelf, True)        
        self.treeWidget_properties.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)   
        

    def uiSignals (self):        
        self.action_addOn.triggered.connect (partial (self.createPipeData, self.pipe._pipeAttributes, self.currentLayout, self.treeWidget_properties))    
        self.action_update.triggered.connect (partial (self.updatePipeData, self.pipe._pipeAttributes, self.treeWidget_properties)) 
        self.action_remove.triggered.connect (self.removePipeData)
           
        #self.treeWidget_properties.itemEntered.connect (partial (self.updateEachPipeData, self.treeWidget_properties))     
        self.treeWidget_properties.itemClicked.connect (partial (self.setCurrentPipeAttributes, self.treeWidget_properties))     
        #self.action_remove.triggered.connect (self.remove)    
        
        
    def removePipeData (self):
        
        print self.splitter.sizes ()
        print self.splitter_properties.sizes ()
        
        
    def updateEachPipeData (self, treeWidget):        
        treeWidget.selectedItems ()     
        
        
    def createLayout (self):

        layoutList = pipeLayout.setReorder(self.pipe._pipeLayout) 
        
        for ecahLayout in layoutList :
            label = self.pipe._pipeLayout[ecahLayout]['niceName']                           
            pushButton = QtGui.QPushButton(self)
            pushButton.setObjectName('button_{}'.format(ecahLayout))
            pushButton.setFlat(True)                                 
            pushButton.setText(label)            
            self.verticalLayout_layout.addWidget(pushButton)
             
            pushButton.clicked.connect (partial (self.setCurrentPipeLayout, ecahLayout, self.treeWidget_properties))            
            pushButton.setStyleSheet ('Text-align:left;')             
            studioStyleSheet.setIcon(pushButton, '{}/icons'.format (os.path.dirname(CURRENT_PATH)), [50, 50], False)
            
            
    def setCurrentPipeLayout (self, layout, treeWidget):
        
        self.currentLayout = layout #store the current layout value             
                                
        treeWidget.clear ()
        treeWidget.show ()
        self.groupBox_details.show ()
        self.groupBox_shelf.show ()        
        
        self.primaryPipe = self.pipe._pipeAttributes[layout]['primary']
        self.secondaryPipe = self.pipe._pipeAttributes[layout]['secondary']   
        
        primaryList, catagoryData = pipeLayout.setNestedReorder (self.primaryPipe) # sort the order the dict based on the order number        
        
        for index in range (len(primaryList)) :                
            colors = catagoryData[primaryList[index]]['color']
            niceName = catagoryData[primaryList[index]]['niceName']
            order = catagoryData[primaryList[index]]['order']  
              
            treeWidget.headerItem().setText(index+1, niceName)
            treeWidget.header ().resizeSection (index+1, 100)
               
            brush = QtGui.QBrush(QtGui.QColor (colors))
            brush.setStyle(QtCore.Qt.SolidPattern)
            treeWidget.headerItem().setForeground(order, brush)  
    
        treeWidget.header ().resizeSection (0, 50)
        
        self.setCurrentDatabase ()  
        
    
    def setCurrentDatabase (self) :
        
        db = studioDatabase.Database (dataType=self.currentLayout)
        db.getValue ()        
        self.databaseValue = db.value                 
        
        if not self.databaseValue :
            return        
       
        dbList = pipeLayout.setReorder(self.databaseValue) # sort the order the dict based on the order number  
        for eachDb in dbList :       
            db = {eachDb: self.databaseValue[eachDb]}            
            self.createPipeData (db, eachDb, self.treeWidget_properties) 

        
    def createPipeData (self, database, currentLayout, treeWidget) : 
        
        item = QtGui.QTreeWidgetItem (treeWidget) 
        item.setFlags (QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
           
        widgetItem = treeWidget.invisibleRootItem ()          
        item.setText (0, str (widgetItem.childCount ()))
        
        if not currentLayout :
            currentLayout = self.currentLayout
        
        primaryList, catagoryData = pipeLayout.setNestedReorder (database[currentLayout]['primary']) # sort the order the dict based on the order number        

        for index in range (len(primaryList)) :
                            
            types = catagoryData[primaryList[index]]['type']
            value = catagoryData[primaryList[index]]['value']                          
            colors = catagoryData[primaryList[index]]['color']           

            if types=='string' :     
                           
                layoutLabel = value                
                if database.has_key ('assets') :
                    layoutLabel = '{}_**{}'.format(value, widgetItem.childCount ())
                    
                item.setText (index+1, layoutLabel)          
                 
            if types=='enum' :  
                
                values = catagoryData[primaryList[index]]['values'] 
                                
                comboBox = QtGui.QComboBox (treeWidget)
                comboBox.setObjectName('comboBox_{}'.format(primaryList[index]))                 
                comboBox.setMinimumSize(QtCore.QSize(100, 30))                  
                comboBox.addItems (['None'] + values)                
                comboBox.setCurrentIndex (int(value))                                   
                comboBox.setStyleSheet('color: {};'.format(colors))
                treeWidget.setItemWidget (item, index+1, comboBox)
                     
            brush = QtGui.QBrush (QtGui.QColor(colors))
            brush.setStyle (QtCore.Qt.SolidPattern)
            item.setBackground (index+1, brush)


    def updatePipeData (self, database, treeWidget): 
        
        primaryList, catagoryData = pipeLayout.setNestedReorder (database[self.currentLayout]['primary']) # sort the order the dict based on the order number        
             
        data = {}        
         
        selectItemList = treeWidget.selectedItems ()                
        widgetItem = treeWidget.invisibleRootItem ()        
         
        for itLoop in range (widgetItem.childCount ()) :               
            pimaryPipeData = self.getPimaryPipeValues (widgetItem.child(itLoop), primaryList, catagoryData) 
                                       
            secondryPipeData = self.getSecondaryPipeValues (pimaryPipeData['title']['label'])
            finalData =  {'primary': pimaryPipeData, 'secondary': secondryPipeData, 'order': itLoop}
             
            #data.setdefault(pimaryPipeData['title']['label']['value'], finalData)
            data.setdefault(itLoop+1, finalData)
            
        db = studioDatabase.Database (dataType=self.currentLayout, data=data)
        db.create ()
        
        #pprint.pprint (data)    
        
        self.createPipeFolders (self.currentLayout, data)    
        

    def createPipeFolders (self, layout, data) :
        
        for eachIndex, eachValue in data.iteritems() :
            
            title = eachValue['primary']['title']['label']['value']            
            catagoryIndex = int (eachValue['primary']['catagory']['types']['value'])
            
            if not catagoryIndex :
                continue           
            
            catagory = eachValue['primary']['catagory']['types']['values'][catagoryIndex-1]            
            layoutPath = os.path.join (PRJECT_PATH, self.scene, layout, catagory, title)
            
            if not os.path.isdir(layoutPath) :
                try :
                    os.makedirs(layoutPath)
                except Exception as result :
                    print 'folder creation error\t', result
                
            departments = eachValue['secondary']
            for eachDepartment in departments :                
                departmentPath = os.path.join (layoutPath, eachDepartment)
                
                if not os.path.isdir(departmentPath) :        
                    try :
                        os.makedirs(departmentPath)
                    except Exception as result :
                        print 'folder creation error\t', result


    def getPimaryPipeValues (self, item, primaryList, catagoryData): 

        treeWidget = item.treeWidget ()                 
        primaryData = {} 
         
        for index in range (len(primaryList)) :            
            types = catagoryData[primaryList[index]]['type']

            if types=='string' :
                currentValue = str (item.text (index+1))

            if types=='enum' :
                comboBox = treeWidget.itemWidget (item, index+1)
                currentValue = str (comboBox.currentIndex ())

            finalData =  {primaryList[index].encode(): currentValue, 'order': index+1}

            values = {  'value': currentValue,
                        'order': index+1,
                        'type': types,
                        'color': catagoryData[primaryList[index]]['color'],
                        'values': catagoryData[primaryList[index]]['values'],
                        'niceName': catagoryData[primaryList[index]]['niceName'] 
                        }
            primaryData.setdefault (primaryList[index].encode(), values)            
            
        pipeData = {}    
        for eachCatagory, eachPipeList in self.primaryPipe.iteritems () : 
            
            primaryValues = {}            
                        
            for eachPipeKey,  eachPipeValue in eachPipeList.iteritems () : 
                if eachPipeKey not in primaryData :
                    continue                    
                                  
                primaryValues.setdefault(eachPipeKey, primaryData[eachPipeKey])                
               
            pipeData.setdefault(eachCatagory.encode(), primaryValues)
                   
        return pipeData   


    def getSecondaryPipeValues (self, pimaryKey):
        
        secondaryData = {}  
        for eachCatagory, eachPipeList in self.secondaryPipe.iteritems () : 
            
            secondoryValues = {}            
                        
            for eachPipeKey,  eachPipeValue in eachPipeList.iteritems () :                
                values = {  'value': eachPipeValue['value'],
                            'order': eachPipeValue['order'],
                            'type': eachPipeValue['type'],
                            'color': eachPipeValue['color'],
                            'values': eachPipeValue['values'],
                            'niceName': eachPipeValue['niceName'],                                                   
                            }                
                secondoryValues.setdefault(eachPipeKey, values)        
               
            secondaryData.setdefault(eachCatagory.encode(), secondoryValues)
                   
        return secondaryData   



    def setCurrentPipeAttributes (self, treeWidget) :
        
        if not treeWidget.selectedItems () :
            return None        
        
        currentItem = str (treeWidget.selectedItems ()[-1].text(1))
        currentOrder = str (treeWidget.selectedItems ()[-1].text(0))


        db = studioDatabase.Database (dataType=self.currentLayout)
        db.getValue ()        
        self.databaseValue = db.value
        
        if not self.databaseValue :
            return None
        
        if not self.databaseValue.has_key(currentOrder) :
            return None        
        
        self.deleteExistsWidgets (self.verticalLayout_details)
             
        studioDetails.Details (parent=self.verticalLayout_details, 
                               database=self.databaseValue,
                               pipeDatabase=self.secondaryPipe,
                               item=currentItem,
                               order=currentOrder)

        

    def deleteExistsWidgets (self, layout):        
   
        for index in range (layout.count ()) :            
            child = layout.itemAt(index)            
            for cindex in range (child.count ()) :            
                child.itemAt(cindex).widget().deleteLater()  

        
          
    def deleteWidgets_ (self, layout):  
         
        for index in range (layout.count ()) :            
            if not layout.itemAt(index).widget() :
                continue                        
            layout.itemAt(index).widget().deleteLater()        
        
        
        
        
if __name__ == '__main__':
            
    app = QtGui.QApplication(sys.argv)
    ex = Pipes()
    ex.show()
    sys.exit(app.exec_())       