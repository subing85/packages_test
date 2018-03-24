'''
Studio Pipe Details v0.1
Date : February 21, 2018
Last modified: February 21, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface    
'''

import sys
import os
import pprint
import warnings
from functools import partial

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic

from module import studioDatabase
from pipe import pipeLayout
from module import qtWidgets

reload (studioDatabase)

PRJECT_PATH = '/media/meera/FE5868105867C5CD/Project/MiniMovie'
DATABASE_PATH = '/media/meera/FE5868105867C5CD/Project/MiniMovie/database'

ICON_PATH = '/media/meera/FE5868105867C5CD/Project/MiniMovie/packages/icons'



class Details (object):
    
    #def __init__(self, *args):
    def __init__(self, **kwargs):
        
        self.parents = kwargs['parent']        
        self.database = kwargs['database']  
        self.pipeDatabase = kwargs['pipeDatabase']         
        self.currentItem = kwargs['item']     
        self.currentOrder = kwargs['order']
        
        self.departmentLayout = None
        self.currentOpen = None
        
           
        
        
        self.ing = 1
        
        
        
        
        
        #pprint.pprint (self.database)
        
        self.setupUi ()
        
        
    def setupUi (self) :
        
        #pprint.pprint (self.database)
        
        self.currentItem = self.database[self.currentOrder]['primary']['title']['label']['value']
        #self.departments = self.database.values()[0]['primary'].keys()
        #self.currentItem = self.database[self.currentOrder]['secondary']['title']['label']['value']        
        self.departments = self.database.values()[0]['secondary']

          
        self.groupBox_name = QtGui.QGroupBox()
        self.groupBox_name.setObjectName('groupBox_name')          
        self.parents.addWidget(self.groupBox_name)        
        
        self.horizontalLayout_name = QtGui.QHBoxLayout (self.groupBox_name)
        self.horizontalLayout_name.setSpacing (10)
        self.horizontalLayout_name.setObjectName ('horizontalLayout_name')
                                                  
        self.label_poseLabel = QtGui.QLabel()
        self.label_poseLabel.setObjectName ('label_poseLabel')     
        self.label_poseLabel.setText ('Name')
        self.label_poseLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_name.addWidget (self.label_poseLabel)        
        
        self.lineEdit_poseLabel = QtGui.QLineEdit ()
        self.lineEdit_poseLabel.setObjectName ('lineEdit_poseLabel')
        self.lineEdit_poseLabel.setReadOnly (True)        
        self.lineEdit_poseLabel.setText (self.currentItem)
        self.horizontalLayout_name.addWidget (self.lineEdit_poseLabel) 

        self.groupBox_mode = QtGui.QGroupBox ()
        self.groupBox_mode.setTitle ('')
        self.groupBox_mode.setObjectName ('groupBox_mode')
        self.parents.addWidget(self.groupBox_mode)        
        
        self.verticalLayout_mode = QtGui.QVBoxLayout (self.groupBox_mode)
        self.verticalLayout_mode.setSpacing (1)
        self.verticalLayout_mode.setObjectName ('verticalLayout_mode')    

        #self.setCentralWidget()

        self.setDepartments (self.verticalLayout_mode)
        #self.setCurrentDepartment ()


        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.parents.addItem(spacerItem)

           
            
    def setDepartments (self, layout) :
        
        #self.deleteExistsWidgets_ (self.verticalLayout_main)
        
        for index in range (len(self.departments.keys())) :        
            self.setCurrentDepartment (self.departments.keys()[index], layout)
            
            
    def setCurrentDepartment (self, department, layout):          
        
        horizontalLayout_display = QtGui.QHBoxLayout ()
        horizontalLayout_display.setSpacing (1)
        horizontalLayout_display.setObjectName ('horizontalLayout_display')
        layout.addLayout(horizontalLayout_display)

        horizontalLayout_mode = QtGui.QHBoxLayout()
        horizontalLayout_mode.setObjectName ('horizontalLayout_mode')
        layout.addLayout(horizontalLayout_mode)  
        
        gridLayout_details = QtGui.QGridLayout()
        gridLayout_details.setObjectName('gridLayout_details')
        horizontalLayout_mode.addLayout(gridLayout_details)      
        
        verticalLayout_comments = QtGui.QVBoxLayout()
        verticalLayout_comments.setObjectName('verticalLayout_comments')
        horizontalLayout_mode.addLayout(verticalLayout_comments)                        
            
        button_number = QtGui.QPushButton()       
        button_number.setObjectName('button_number_{}'.format(department))
        self.decorateWidget (button_number, str(self.ing), [22, 22], [22, 22], 'Fixed')       
        horizontalLayout_display.addWidget(button_number)
           
        button_name = QtGui.QPushButton()
        button_name.setObjectName('button_name_{}'.format(department))  
        button_name.setStyleSheet ('Text-align:left;')                        
        self.decorateWidget (button_name, '  {}' .format(department), [22, 22], [16777215, 22], 'Preferred')       
        horizontalLayout_display.addWidget(button_name)
        
        button_open = QtGui.QPushButton()
        button_open.setObjectName('button_open_{}'.format(department))
        button_open.clicked.connect (partial(self.departmentOpen, department, button_open, gridLayout_details))
        self.decorateWidget (button_open, '+', [22, 22], [22, 22], 'Fixed')
        horizontalLayout_display.addWidget(button_open)  
        
        self.ing+=1 
    
        
    def departmentOpen (self, department, button, gridLayout):
        
        
        if self.departmentLayout :        
            self.deleteWidgets (self.departmentLayout)
            
        if self.currentOpen==button :
            self.currentOpen=None
            return None

        self.currentOpen = button

        layoutList = pipeLayout.setReorder(self.departments[department]) 
        
        for index in range (len(layoutList)) :
            
            types = self.departments[department][layoutList[index]]['type']
            value = self.departments[department][layoutList[index]]['value']                          
            colors = self.departments[department][layoutList[index]]['color']  
            
            niceName = self.departments[department][layoutList[index]]['niceName']  
            
            label = QtGui.QLabel()
            label.setObjectName ('label_{}'.format(layoutList[index]))     
            label.setText (niceName)
            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            gridLayout.addWidget(label, index, 0, 1, 1)            
            
            if types=='string':                
                lineEdit = QtGui.QLineEdit ()
                lineEdit.setObjectName ('lineEdit_{}'.format(layoutList[index])) 
                lineEdit.setReadOnly (True)        
                lineEdit.setText (str(value))
                
                gridLayout.addWidget(lineEdit, index, 1, 1, 1)
                
            if types=='listItem':          
                treeWidget = QtGui.QTreeWidget()
                treeWidget.setObjectName('treeWidget_{}'.format(layoutList[index]))                
                treeWidget.setAlternatingRowColors(True)
                treeWidget.setHeaderHidden(True)
                gridLayout.addWidget(treeWidget, index, 1, 1, 1)

                item = QtGui.QTreeWidgetItem (treeWidget)                
                item.setText (0, str(index+1))             
                item.setText (1, str(value))
                
                #===============================================================
                # icon        = QtGui.QIcon ()
                # icon.addPixmap(QtGui.QPixmap('%s/icons/mesh.png'% (self.currentDirectory)), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
                # item.setIcon (1, icon)   
                #===============================================================
                
            if types=='image':
                button = QtGui.QPushButton()
                button.setObjectName('button_{}'.format(layoutList[index]))
                button.setMinimumSize(QtCore.QSize(341, 240))
                button.setMaximumSize(QtCore.QSize(341, 240))                
                gridLayout.addWidget(button, index, 1, 1, 1)
                
            if types=='movie':                
                horizontalLayout_movie = QtGui.QHBoxLayout()
                horizontalLayout_movie.setObjectName('verticalLayout_movie')
                horizontalLayout_movie.setContentsMargins(1, 1, 1, 1)        
                horizontalLayout_movie.setSpacing(10)                
                gridLayout.addLayout(horizontalLayout_movie, index, 1, 1, 1)  
                                  
                button_backward = QtGui.QPushButton()
                button_backward.setObjectName('button_backward')
                button_backward.setFlat(True)
                #button_backward.setStyleSheet('border: 1px solid #ff007f;border-radius: 15px;')
                button_backward.setStyleSheet('border-radius: 15px;')              
                button_backward.setMinimumSize(QtCore.QSize(30, 30))
                button_backward.setMaximumSize(QtCore.QSize(30, 30))
                horizontalLayout_movie.addWidget (button_backward) 
                                  
                qtWidgets.setIcon(button_backward, ICON_PATH, [30, 30], False)              
                                           
                button_play = QtGui.QPushButton()
                button_play.setObjectName('button_play')
                button_play.setFlat(True)   
                button_play.setStyleSheet('border-radius: 15px;')                             
                button_play.setMinimumSize(QtCore.QSize(30, 30))
                button_play.setMaximumSize(QtCore.QSize(30, 30))  
                horizontalLayout_movie.addWidget (button_play)  
                             
                qtWidgets.setIcon(button_play, ICON_PATH, [30, 30], False)              
                   
                button_forward = QtGui.QPushButton()
                button_forward.setObjectName('button_forward')
                button_forward.setFlat(True)
                button_forward.setStyleSheet('border-radius: 15px;')                             
                button_forward.setMinimumSize(QtCore.QSize(30, 30))
                button_forward.setMaximumSize(QtCore.QSize(30, 30))
                horizontalLayout_movie.addWidget (button_forward) 
                              
                qtWidgets.setIcon(button_forward, ICON_PATH, [30, 30], False)            
                
                spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                horizontalLayout_movie.addItem(spacerItem)
                
            if types=='stringItem':                
                textEdit_comment = QtGui.QTextEdit()
                textEdit_comment.setObjectName('textEdit_comment')
                textEdit_comment.setText (str(value))
                gridLayout.addWidget(textEdit_comment, index, 1, 1, 1)  
                                            
        self.departmentLayout = gridLayout
                         
          
    def decorateWidget (self, widget, lable, min, max, policy) :
        widget.setText(lable)      
        widget.setMinimumSize(QtCore.QSize(min[0], min[1]))
        widget.setMaximumSize(QtCore.QSize(max[0], max[1]))       
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)       
        if policy=='Fixed' :                            
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)           
        widget.setSizePolicy(sizePolicy)        
        
    
    def deleteWidgets (self, layout):
                            
        for index in range (layout.count()): 
            
            item = layout.itemAt(index)
            
            if isinstance(item, QtGui.QWidgetItem):            
                item.widget().deleteLater() 
                
            if isinstance(item, QtGui.QSpacerItem):                 
                #item.widget().deleteLater() 
                layout.removeItem(item)  
                
            if isinstance(item, QtGui.QHBoxLayout):
                self.deleteWidgets (item)
                
            if isinstance(item, QtGui.QVBoxLayout):
                self.deleteWidgets (item)               
                            
            index+=1
            
            


    def deleteExistsWidgets (self, layout):   
        for index in range (layout.count ()):            
            child = layout.itemAt(index)            
            for cindex in range (child.count ()):            
                child.itemAt(cindex).widget().deleteLater()  



    def clearLayout_ (self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())               
                     
    
    def clearLayouts (self, layout):
        
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
    
            if isinstance(item, QtGui.QWidgetItem):
                print "widget" + str(item)
                item.widget().close()
                # or
                # item.widget().setParent(None)
            elif isinstance(item, QtGui.QSpacerItem):
                print "spacer " + str(item)
                # no need to do extra stuff
            else:
                print "layout " + str(item)
                self.clearLayout(item.layout())
    
            # remove the item from layout
            layout.removeItem(item)    


#===============================================================================
# if __name__ == '__main__':
#              
#     app = QtGui.QApplication(sys.argv)
#     ex = Details()
#     ex.show()
#     sys.exit(app.exec_())                
#===============================================================================
             
             
             
             
             
             
             
             
             
             
             
             