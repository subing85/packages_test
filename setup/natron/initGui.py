#Natron Menu v0.1
#Form implementation generated from natronMenu module
#Created: 17:03:2018 - 04:12:40:pm
#    by: meera
#WARNING! All changes made in this file will be lost!


def abcPublish2():
	from toolKit.Narton.Publish import abcPublish2
	result = abcPublish2.trailRun()

def compostingPublish():
	from toolKit.Narton.Publish import compostingPublish
	result = compostingPublish.trailRun()

def compostingTool():
	from toolKit.Narton.Common import compostingTool
	result = compostingTool.trailRun()

def renderTool():
	from toolKit.Narton.Render import renderTool
	result = renderTool.trailRun()



NatronGui.natron.addMenuCommand ('TPS/Publish/abcPublish2s', 'abcPublish2', QtCore.Qt.Key.Key_L, QtCore.Qt.KeyboardModifier.ShiftModifier)
NatronGui.natron.addMenuCommand ('TPS/Publish/compostingPublishs', 'compostingPublish', QtCore.Qt.Key.Key_L, QtCore.Qt.KeyboardModifier.ShiftModifier)
NatronGui.natron.addMenuCommand ('TPS/Common/compostingTools', 'compostingTool', QtCore.Qt.Key.Key_L, QtCore.Qt.KeyboardModifier.ShiftModifier)
NatronGui.natron.addMenuCommand ('TPS/Render/renderTools', 'renderTool', QtCore.Qt.Key.Key_L, QtCore.Qt.KeyboardModifier.ShiftModifier)