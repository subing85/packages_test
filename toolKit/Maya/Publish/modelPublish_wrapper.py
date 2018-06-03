NAME = 'Model Publish'
ORDER = 1
TYPE = 'wrapper'
DATE = 'June 03, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Publish the Models'
VERSION = 1.0
ICON = 'modelPublish.png'
CLASS = 'ModelPublish_Wrapper'

class ModelPublish_Wrapper():       
    
    def __init__(self):
        
        from PySide import QtGui
        from shiboken import wrapInstance
        from maya import OpenMayaUI as OpenMayaUI
        MAYA_MAIN_WINOW = wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QtGui.QWidget)

        from publish import studioPublish
        reload(studioPublish)
        window = studioPublish.Publish(application='Maya', types='model', parent=MAYA_MAIN_WINOW)
        window.show()
        
        
def trailRun ():
    
    ModelPublish_Wrapper()
