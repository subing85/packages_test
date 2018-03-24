import PyQt4

#print help(PyQt4)

from PyQt4.QtCore import QT_VERSION_STR
from PyQt4.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR

print("Qt version:", QT_VERSION_STR)
print("SIP version:", SIP_VERSION_STR)
print("PyQt version:", PYQT_VERSION_STR)


import platform
print(platform.python_version())

#https://www.lfd.uci.edu/%7Egohlke/pythonlibs/#pyqt4
#http://download.qt.io/official_releases/pyside/