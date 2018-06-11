'''
Studio Launc-HER v0.1 
Date : February 07, 2018
Last modified: March 28, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module is the basic core (back bone) of this pipeline configuration. Primary inputs for project settings.
    set the environment variables to Linux   
'''

import sys
import os
import imp
import py_compile
import warnings
import subprocess
import pprint
import threading
from functools import partial

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic

from module import studioProjects
from module import studioConsole
from module import jsonManager
from module import studioStyleSheet
from module import studioVersioning
   
CURRENT_PATH = os.path.dirname (__file__)

if 'PACKAGE_PATH' not in os.environ:
    os.environ['PACKAGE_PATH'] = 'Z:/packages'

PACKAGE_PATH = os.environ['PACKAGE_PATH']
#CURRENT_PATH = os.getcwd()
UI_FILE = '{}/studioLauncher_ui.ui'.format (CURRENT_PATH)
FROM, BASE = uic.loadUiType (UI_FILE)

class Launcher (FROM, BASE):
    
    def __init__(self, *args):
        super(Launcher, self).__init__(*args)
  
        uic.loadUi(UI_FILE, self)    

        console = studioConsole.Console ()    
        console.stdout().messageWritten.connect (self.textEdit_output.insertPlainText)         

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0] 
            
        try :
            styleSheet = studioStyleSheet.StyleSheet (self)
            styleSheet.setStyleSheet ()            
        except :
            pass

        self.setWindowTitle ('Studio Launc-HER v0.1')
        self.resize (750, 500)
        self.standalonePackages = [ 'resources',
                                    'plugins',
                                    'bin',
                                    'icons']
        
        self.loadProject()                              

        for eachWidget in self.findChildren(QtGui.QPushButton) :            
            studioStyleSheet.setIcon(eachWidget, '{}/icons'.format (os.path.dirname(CURRENT_PATH)), [50, 50], False)             
        
        self.button_gimp.clicked.connect (partial (self.launchApplication, 'gimp'))
        self.button_blender.clicked.connect (partial (self.launchApplication, 'blender'))
        self.button_maya2016.clicked.connect (partial (self.launchApplication, 'maya2016'))
        
        self.button_natron.clicked.connect (partial (self.launchApplication, 'natron')) 
        self.button_studioPipe.clicked.connect (partial (self.launchApplication, 'studioPipe'))
        
        self.button_patch.clicked.connect (partial (self.makeVersion, 'patch'))
        self.button_minor.clicked.connect (partial (self.makeVersion, 'minor'))
        self.button_major.clicked.connect (partial (self.makeVersion, 'major'))        
        
        self.button_removeThumbs.clicked.connect (partial (self.removeFiles, 'Thumbs.db'))        
        #self.button_removePyc.clicked.connect (partial (self.removeFiles, '.pyc'))  
        
    
    def loadProject(self):
        
        #hide exists application launcher buttons
        for eachButton in self.groupBox_applications.findChildren(QtGui.QPushButton):
            eachButton.hide()            
        
        self.sp = studioProjects.StudioProjects()
        
        for eachProject in self.sp.projects:            
            button = QtGui.QPushButton(self)   
            button.setText(eachProject)    
            button.setObjectName('button_{}'.format(eachProject))
            self.verticalLayout_projects.addWidget(button)            
            button.clicked.connect (partial (self.setMyProject, eachProject))
            
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_projects.addItem(spacerItem)

        
    def setMyProject(self, currentProject):
        
        #hide exists application launcher buttons
        for eachButton in self.groupBox_applications.findChildren(QtGui.QPushButton):        
            eachButton.hide()    
        
        for ecahApplication in self.sp.projects[currentProject]['applications']:             
            for eachButton in self.groupBox_applications.findChildren(QtGui.QPushButton):                    
                if not str(eachButton.objectName()).endswith(ecahApplication):
                    continue
                eachButton.show()
                
        #set global variables
        os.environ['PROJECT_PATH'] = self.sp.projects[currentProject]['path']
        os.environ['PROJECT_NICE_NAME'] = self.sp.projects[currentProject]['niceName'] 
        os.environ['PROJECT_FULL_NAME'] = self.sp.projects[currentProject]['fullName'] 
        
        os.environ['ASSET_PATH'] = '{}/asset'.format (self.sp.projects[currentProject]['path']) 
        os.environ['ANIMATION_PATH'] = '{}/animation'.format (self.sp.projects[currentProject]['path']) 
        os.environ['RENDERING_PATH'] = '{}/rendering'.format (self.sp.projects[currentProject]['path']) 
        os.environ['COMPOSITING_PATH'] = '{}/composting'.format (self.sp.projects[currentProject]['path']) 
        os.environ['DATABASE_PATH'] = '{}/dataBase'.format (self.sp.projects[currentProject]['path']) 
        os.environ['PIPEINPUT_FILE'] = os.path.abspath(os.path.join (PACKAGE_PATH, 'pipe', 'pipeInput_%s.json'% self.sp.projects[currentProject]['niceName'])).replace('\\', '/')
        os.environ['DATABASE_SOURCE'] = os.path.abspath(os.path.join (PACKAGE_PATH,  'pipe', 'pipeInput_%s.json'% self.sp.projects[currentProject]['niceName'])).replace('\\', '/')

        self.annotation ()   
        print '\nCurrent Project\t- ', currentProject


    def launchApplication (self, application):     
            
        self.executeDependency (application)         
        
        command = 'start "" {}/{}.bat'.format (CURRENT_PATH, application)
        print command
        subprocess.call (command, stdout=None, shell=True, stderr=None) 

        
    def annotation (self):
        
        try :
            print 'PROJECT_PATH\t', os.environ['PROJECT_PATH']      
            print 'PROJECT_NICE_NAME\t', os.environ['PROJECT_NICE_NAME'] 
            #print 'DATA_PATH\t', os.environ['DATA_PATH'] 
            #print 'PYTHONPATH\t', os.environ['PYTHONPATH'] 
        except Exception as result :
            print result
            
            
    def executeDependency (self, launcher) : 
        
        dependencyPath = '{}/launchDependency.json'.format (os.environ['DATA_PATH'])
        jm = jsonManager.JManager (file=dependencyPath)        
        jm.getJsonData()
        
        if launcher not in jm._pythonObject :
            return None
        
        dependencies = jm._pythonObject[launcher]
        
        print dependencies
        
        for eachKey, eachDependency in dependencies.iteritems():            
            if eachKey=='pythonModule':                
                for eachValue in eachDependency :            
                    try :        
                        exec (eachValue) #print eachValue
                    except Exception as exceptResult:   
                        print ('executeError\t', exceptResult, eachValue)
                        
            if eachKey=='linuxCode':
                pass
            
            if eachKey=='pythonCode':
                pass  
                             
        
    def makeVersion (self, versionType):
        
        source = os.environ['PACKAGE_PATH']
        target = os.environ['PACKAGE_BACKUP_PATH']        
        excludeFolders = [  'resources',
                            'plugins',
                            'bin',
                            'icons']
        
        progressBar = self.progressBar 
        
        version = studioVersioning.Versioning ( source=source, 
                                                target=target, 
                                                excludeFolders=excludeFolders, 
                                                versionType=versionType, 
                                                progressBar=progressBar
                                                )
        #version.createVersion () 
        
        thread = threading.Thread(target=version.createVersion (), args = ())
        thread.start()
        thread.join()        
        print '\nDone'

    
    def removeFiles (self, fileType):
        
        packagePath = os.environ['PACKAGE_PATH']
        
        if not os.path.isdir(packagePath):
            QtGui.QMessageBox.warning (self, 'Warning', '{}\nNo such directory'.format(packagePath), QtGui.QMessageBox.Ok)
            return False
        
        removedList = []
        ing  = 0
        for root, dir, files in os.walk(packagePath):                  
            for eachFile in files :
                if fileType not in eachFile:
                    continue                
                
                self.progressBar.setValue (ing)
                self.progressBar.setMaximum ((ing+100))
                    
                try :
                    os.chmod (os.path.join(root, eachFile), 0777)
                    os.remove (os.path.join(root, eachFile))
                    removedList.append('removed\t{}'.format (os.path.join(root, eachFile)))
                except Exception, result :
                    print result
              
                ing+=1
                
        self.progressBar.setMaximum (100)
        self.progressBar.setValue (100)
                        
        print '\n'.join (removedList)                    

                
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())  
    
#End################################################################################################