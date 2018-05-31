NAME = 'Maya Setup'
ORDER = 1
TYPE = 'wrapper'
DATE = 'May 31, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Configure Maya (startup script)'
VERSION = 1.0
CLASS = 'CreateAssetHierarchy'

class MayaSetup ():       
    
    def __init__(self):
        
        from setup.maya import mayaSetup
        reload(mayaSetup)
        mayaSetup.customSetup()

        
    
def trailRun ():
    
    MayaSetup()
    
