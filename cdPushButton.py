

from PyQt4 import QtCore, QtGui




class CDPushButton(QtGui.QPushButton):

    def __init__(self, *args):
        QtGui.QPushButton.__init__(self, *args)

    def enterEvent(self, event):
        self.emit(QtCore.SIGNAL("entered()"))

    def leaveEvent(self, event):
        self.emit(QtCore.SIGNAL("leaved()"))

