
'''
Studio Projects 0.0.1
Date : May 29, 2018
Last modified: May 29, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module is a input of Studio Launcher project list. 
    Add and remove the project from package (Studio Launcher).
    
'''

class StudioProjects(object):
    
    def __init__(self):
        
        self.projects = {   'TPS': {'fullName': 'A Teeth Pain Story',
                                    'niceName': 'TPS',
                                    'path': 'Z:/TPS',
                                    'applications': ['gimp', 'blender', 'natron', 'studioPipe']                                    
                                    },
                            'BAN': {'fullName': 'Boy And Nurse',
                                    'niceName': 'BAN',
                                    'path': 'Z:/BAN',
                                    'applications':  ['gimp', 'maya2016', 'natron', 'studioPipe']                                  
                                    }
                            }
        