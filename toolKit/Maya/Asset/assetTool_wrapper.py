NAME = 'Asset Tool'
ORDER = 2
TYPE = 'wrapper'
DATE = 'May 31, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To create asset attributes on asset node'
VERSION = 1.0
ICON = 'assetTool.png'
CLASS = 'AssetTool_Wrapper'

class AssetTool_Wrapper ():       
    
    def __init__(self):
        
		from assets import assetTool
		reload(assetTool)
		assetTool.runMayaUiDemo()   
    
def trailRun ():
    
    AssetTool_Wrapper ()
