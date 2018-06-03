NAME = 'Create Asset Hierarchy'
ORDER = 1
TYPE = 'wrapper'
DATE = 'May 31, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Create Asset Hierarchy'
VERSION = 1.0
ICON = 'assetHierarchy.png'
CLASS = 'CreateAssetHierarchy_Wrapper'


class CreateAssetHierarchy_Wrapper ():       
    
    def __init__(self):
	
        from assets import studioHierarchy
        reload (studioHierarchy)
        studioHi = studioHierarchy.StudioHierarchy(assetName='Asset')
        studioHi.create()        
        
    
def trailRun ():
    
    CreateAssetHierarchy_Wrapper ()
