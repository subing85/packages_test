NAME = 'Create Asset Hierarchy'
ORDER = 1
TYPE = 'wrapper'
DATE = 'May 31, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Create Asset Hierarchy'
VERSION = 1.0
CLASS = 'CreateAssetHierarchy'

from assets import studioHierarchy
reload (studioHierarchy)

class CreateAssetHierarchy ():       
    
    def __init__(self):
        
        studioHi = studioHierarchy.StudioHierarchy(assetName='Asset')
        studioHi.create()        
        
    
def trailRun ():
    
    CreateAssetHierarchy ()
