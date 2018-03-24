NAME = 'Studio Publish'
ORDER = 1
TYPE = 'wrapper'
SHOTCUT = 'Ctrl+P'

DATE = 'March 08, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Check Image Extenstion'
VERSION = 1.0
CLASS = 'Validate_Image'

class Validate_Image (object):       
    
    def __init__(self):
        
        print ('To Check Image Extenstion')
        
        self.bundleResult = {   'faild': 'red',
                                'error': 'magenta',
                                'success': 'green' }
        

        
    
def trailRun ():
    from publish import studioPublish
    reload(studioPublish)
    window = studioPublish.Publish(application='natron', types='illustration')
    #window = studioPublish.Publish(application='natron', types='composing')    
    window.show ()    
