'''
QT StyleSheet v0.1 
Date : March 14, 2018
Last modified: March 14, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module to set the style sheet to Qt ui
    
'''

import os

try:
    from PyQt4 import QtCore 
    from PyQt4 import QtGui
    from PyQt4 import uic
    
except:
    from PySide import QtCore 
    from PySide import QtGui   

class StyleSheet ():
    
    def __init__(self, window):            
        self.window = window  
    
    def setStyleSheet (self):
        setStyleSheets (self.window)        
    
    def getStyleSheet (self):        
        self._style = getStyleSheets ()


def setStyleSheets (window) :
        
    style = getStyleSheets()    
    window.setStyleSheet(style)
    

def getStyleSheets () :
    
    groupBox = 'QGroupBox {font: 14pt \"MS Shell Dlg 2\"; border: 1px solid #FFAA00;}'        
    generic = 'QWidget {font: 12pt \"MS Shell Dlg 2\";}'   
    
    styleList = [groupBox, generic]    
    style = ''    
    
    for eachStyle in styleList :        
        style+='{} '.format (eachStyle)

    return style


def setIcon (widget, iconPath, size, sizeLock): # import QIcon
    
    '''
        Description    :- This function set set the icons(images) to QtGui.
            
            :param    widget <QtWidget>    example QtGui.QPushButton
            :param    iconPath <syr>    example '/home/usr/icons/test.png'
            :param    size <list>    example [512, 512]
            :param    sizeLock <bool>    example True or False
            
            :return   None    
    '''
    
    iconFile = iconPath      
 
    if os.path.isdir(iconPath) :        
        if not widget.objectName() :
            return False        
        iconFile = '{}/{}.png'.format(iconPath, str(widget.objectName()).split('_')[-1])
        
    if not os.path.isfile(iconFile) :
        iconFile = '{}/unknown.png'.format(iconPath) 
       
    icon = QtGui.QIcon ()
    icon.addPixmap (QtGui.QPixmap (iconFile), QtGui.QIcon.Normal, QtGui.QIcon.Off)                   
    widget.setIcon (icon)
    
    try :
        widget.setIconSize (QtCore.QSize(size[0], size[1]))
    except Exception as result :
        #print (result)
        pass
    
    #===========================================================================
    # if sizeLock : 
    #     widget.setMinimumSize (QtCore.QSize(size[0], size[1]))
    #     widget.setMaximumSize (QtCore.QSize(size[0], size[1]))
    #     #widget.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    #===========================================================================
   

def setToolBar (toolBar, widgets, layout, separator):
    
    '''
        Description    :- This function set create and add the widgets to QToolBar.
            
            :param    toolBar <QtWidget>    example QtGui.QToolBar
            :param    widgets <QtWidget list>    example [QtGui.QActions]
            :param    layout <QtWidget>    example QtGui.HorizontalLayout
            :param    separator <bool>    example True or False
            
            :return   None    
    '''       
    
    if not toolBar :
        toolBar = QtGui.QToolBar()
        layout.addWidget (toolBar)   
         
    for eachWidget in widgets :
        toolBar.addAction (eachWidget)        
        if separator :
            toolBar.addSeparator ()      
    
#End########################################################################