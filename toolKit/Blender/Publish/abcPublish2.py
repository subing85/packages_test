NAME = 'Studio Publish111'
ORDER = 1
TYPE = 'wrapper'
DATE = 'March 08, 2018'
AUTHOR = 'Subin Gopi'
COMMENTS = 'To Check Image Extenstion1111'
VERSION = 1.0
CLASS = 'Validate_Imag1e'

class Validate_Image1 (object):       
    
    def __init__(self):
        
        print ('To Check Image Extenstion')
        
        self.bundleResult = {   'faild': 'red',
                                'error': 'magenta',
                                'success': 'green' }
        
        return None
        
    
def trailRun ():

    from publish import studioPublish
    reload(studioPublish)
    window = studioPublish.Publish(types='compositing')
    window.show ()
