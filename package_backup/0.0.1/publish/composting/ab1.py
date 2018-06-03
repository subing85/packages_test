NAME = 'Image Check'
ORDER = 1
TYPE = 'validate'
DATE = 'February 07, 2018'
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
        
        return None
        
    
def trailRun ():
    Validate_Image ()
    
