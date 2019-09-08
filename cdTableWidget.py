# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##                TableWidget                  ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##              GPL (c)2008-2013               ##
  ##                                            ##
    ##############################################





__version__ = "0.1"             ## Go to end for change log


from PyQt4 import QtCore, QtGui




class CDTableWidget(QtGui.QTableWidget):

    def __init__(self, *args):
        """cdTableWidget.CDTableWidget.__init__()"""

        QtGui.QTableWidget.__init__(self, *args)

    def resizeEvent(self, event):
        # print "cdTableWidget.CDTableWidget.resizeEvent()"
        QtGui.QTableWidget.resizeEvent(self, event)
        self.emit(QtCore.SIGNAL("resized(QEvent)"), event)


    # def enterEvent(self, event):
        # self.emit(QtCore.SIGNAL("entered()"))

    # def focusInEvent(self, event):
        # self.emit(QtCore.SIGNAL("gotFocus()"))

    # def focusOutEvent(self, event):
        # self.emit(QtCore.SIGNAL("lostFocus()"))

    # def leaveEvent(self, event):
        # self.emit(QtCore.SIGNAL("leaved()"))

    # def mouseDoubleClickEvent(self, event):
        # self.emit(QtCore.SIGNAL("doubleClicked()"))

    # def showEvent(self, event):
        # self.emit(QtCore.SIGNAL("showed()"))

