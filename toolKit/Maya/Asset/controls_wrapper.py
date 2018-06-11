NAME = 'Create Controls'
ORDER = 3
TYPE = 'wrapper'
DATE = 'May 31, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Create and manage the controls shapes'
VERSION = 1.0
ICON = 'controls.png'
CLASS = 'Controls_Wrapper'


class Controls_Wrapper ():       
    
    def __init__(self):
	
        from pymel import core as pymel
        pymel.mel.eval('source \"Z:/packages/assets/sgControlMaker.mel\"')    
        
    
def trailRun ():
    
    Controls_Wrapper ()
