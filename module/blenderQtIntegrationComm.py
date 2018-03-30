bl_info = { 'name': 'Qt Integration',
            'author': 'Vincent Gires',
            'description': 'Qt Integration',
            'version': (0, 0, 0),
            'blender': (2, 7, 9),
            'location': '',
            'warning': '',
            'wiki_url': '',
            'tracker_url': '',
            'category': 'Qt'
            }

import bpy
import sys
import os
import logging

logger = logging.getLogger(__name__)

class QtWindowEventLoop(bpy.types.Operator):
    bl_idname = 'screen.qt_event_loop'
    bl_label = 'PyQt Event Loop'
    _timer = None
    _close = None
    
    def __init__(self, widget):
        self._widget = widget
    
    def close(self):
        self._close = True
    
    def modal(self, context, event):
        wm = context.window_manager
        
        if self._close:
            logger.debug('cancel modal operator')
            wm.event_timer_remove(self._timer)
            return {'CANCELLED'}
        else:
            logger.debug('process the events for Qt window')
            self.event_loop.processEvents()
            self.app.sendPostedEvents(None, 0)
        
        return {'PASS_THROUGH'}
    
    def execute(self, context):
        logger.debug('execute operator')
        
        self.app = QtWidgets.QApplication.instance()
        # instance() gives the possibility to have multiple windows
        # and close it one by one
        
        if not self.app:
            self.app = QtWidgets.QApplication(['blender'])
        self.event_loop = QtCore.QEventLoop()
        
        self.widget = self._widget()
        self.widget.context = context
        self.widget.destroyed.connect(self.close)
        
        logger.debug(self.app)
        logger.debug(self.widget)
        
        # run modal
        wm = context.window_manager
        self._timer = wm.event_timer_add(1/120, context.window)
        context.window_manager.modal_handler_add(self)
        
        return {'RUNNING_MODAL'}


def register():
    bpy.utils.register_module(__name__)
    
    from qt_integration import example
    bpy.utils.register_class(example.CustomWindowOperator)
    bpy.utils.register_class(example.QtPanelExample)
    
def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == '__main__':
    register()
