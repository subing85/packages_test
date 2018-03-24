#!/usr/bin/env python
from gimpfu import *

def toolKit(img, layer) :
    gimp.message("Hello world")
	
	#import sys
	#sys.path.append ('Z:/packages')
    #from publish import studioPublish
    #reload(studioPublish)
    window = studioPublish.Publish(types='compositing')
    window.show ()

register(	"python_fu_toolKit",
			"Gimp Toolkit",
			"Display a 'hello world' message",
			"JFM",
			"Open source (BSD 3-clause license)",
			"2013",
			"<Image>/File/StudioToolKit",
			"True"
			"*",
			[],
			[],
			toolKit
			)

main()
