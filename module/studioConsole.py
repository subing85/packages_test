'''
Studio Console v0.1 
Date : March 08, 2018
Last modified: March 08, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This moule will manage the custom console. All print out relatives can connect with QtWidgets
    
example
    from module import customConsole   
    console = customConsole.Console ()       
    console.stdout().messageWritten.connect (self.textEdit_output.insertPlainText)    
    
'''


import sys
import PyQt4.QtCore as QtCore

class Console (QtCore.QObject):
    
  
    _stdout = None
    _stderr = None
   
    messageWritten = QtCore.pyqtSignal(str)    
   
    def flush (self):
        pass
   
    def fileno (self):
        return -1
   
    def write( self, msg ):
        if not self.signalsBlocked() :
            self.messageWritten.emit (unicode(msg))
           
    @staticmethod
    def stdout():
        if not Console._stdout :
            Console._stdout = Console()
            sys.stdout = Console._stdout
        return Console._stdout
   
    @staticmethod
    def stderr():
        if not Console._stderr :
            sys.stderr = Console._stderr
        return Console._stderr    
  
#End###########################################################################