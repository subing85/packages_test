NAME = 'Comet Rename'
ORDER = 4
TYPE = 'wrapper'
DATE = 'May 31, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'Comet Rename'
VERSION = 1.0
ICON = 'cometRename.png'
CLASS = 'CometRename_Wrapper'


class CometRename_Wrapper ():       
    
    def __init__(self):
	
        from pymel import core as pymel
        pymel.mel.eval('source \"Z:/packages/assets/cometRename.mel\";')    
        pymel.mel.eval('cometRename;')    
        
    
def trailRun ():
    
    CometRename_Wrapper ()
