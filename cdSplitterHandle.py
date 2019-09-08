# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   SplitterHandle with Criptidos vision       ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c) 2011                               ##
  ##                                             ##
    ###############################################

"""
Adds attributes:
    emptyAllowed    default = False
    capitalized     default = False
    onlyNumbers     default = False
    minimo          (minimum length)
    maximo          (maximum length)
    message         Error messages
    hasStatusLabel  default = True
    isValid
    isModified      default = False
    trimmed
    externalValidation
    externalMessage
"""

import sys
from PyQt4 import QtCore, QtGui


version = 0.1
## Vea al final por change log



class CDSplitterHandle(QtGui.QSplitterHandle):

    def __init__(self, *args, **kwds):
#        print "\n\nCDSplitterHandle.__init__()", args, kwds
#        print args
        QtGui.QSplitterHandle.__init__(self, *args)
        
    
    def mouseDoubleClickEvent(self, event):
#        print "cdSplitterHandle.mouseDoubleClickEvent()"
        
        index = self.splitter().indexOf(self)
        if index == -1:
            return;
        self.splitter().emit(QtCore.SIGNAL('handleDoubleClick()'))
        QtGui.QSplitterHandle.mouseDoubleClickEvent(self, event)
    
    
    # def mouseReleaseEvent(self, event):
        # print "cdSplitterHandle.mouseReleaseEvent()"
        
        




if __name__=='__main__':
    application=QtGui.QApplication(sys.argv)
    
    fondo=QtGui.QWidget(None)
    fondo.show()
    
    application.exec_()


""" Bitácora de cambios

2011-Ene-18 09:10 v0.1  Creation
"""


""" Justificación
CDLineEdit uses styleSheet to manage statusLabel layout, styleSheet may be overriden by user, so, CDLineEdit overrides setStyleSheet method to include the baseStyle of its own.
"""
