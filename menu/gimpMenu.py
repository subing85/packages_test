'''
Studio Publi-SH v0.1
Date : February 14, 2018
Last modified: February 14, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface 
 
example   
from menu import gimpMenu
reload(gimpMenu)
window = gimpMenu.Menu()
window.show ()      

'''


import sys
import os
import subprocess
import warnings
import pprint

from functools import partial

from module import openStyleSheet


CURRENT_PATH = os.path.dirname (__file__) # CURRENT_PATH = os.getcwd()
UI_FILE = '{}/gimpMenu_ui.ui'.format (CURRENT_PATH)

try :
    from PyQt4 import QtCore 
    from PyQt4 import QtGui
    from PyQt4 import uic
    
    FROM, BASE = uic.loadUiType (UI_FILE)
    
except :
    from PySide import QtCore 
    from PySide import QtGui   
    from module import openPySide
    
    FROM, BASE = openPySide.loadUi (UI_FILE)    


class Menu (FROM, BASE):
     
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent=None) #QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
    
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]            
            
        openStyleSheet.StyleSheet (self)
        
        self.setWindowTitle ('Studio Publi-SH v0.1')
        self.resize (200, 450)


if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    window = Menu ()
    window.show ()
    sys.exit (app.exec_())     

