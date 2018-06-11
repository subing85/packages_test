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
from publish import studioPublish
reload(studioPublish)
window = studioPublish.Publish(types='compositing')
window.show ()      

'''


import sys
import os
import subprocess
import warnings
import pprint
import inspect
import pkgutil

from functools import partial

from module import collectBundels
from pipe import pipeLayout
from module import studioStyleSheet
#reload(collectBundels)
#reload(pipeLayout)

#PIPEINPUT_FILE = os.environ['PIPEINPUT_FILE']
PIPEINPUT_FILE = 'os'

CURRENT_PATH = os.path.dirname (__file__) # CURRENT_PATH = os.getcwd()
UI_FILE = '{}/studioPublish_ui.ui'.format (CURRENT_PATH)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

FROM, BASE = uic.loadUiType (UI_FILE)

class Publish (FROM, BASE):
    
    def __init__(self, *args):
        super(Publish, self).__init__(*args)
  
        uic.loadUi(UI_FILE, self)    
    
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]            

        self.setWindowTitle ('Studio Launc-HER v0.1')
        
print ('\n__name__', __name__)
  
if __name__ == 'publish.studioBlenderPublish':   
    app = QtWidgets.QApplication(sys.argv) 
    window = Publish()
    window.show()   







