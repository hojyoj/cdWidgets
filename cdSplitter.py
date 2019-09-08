# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Splitter with Criptidos vision             ##
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
from PyQt4 import QtGui


from cdWidgets import cdSplitterHandle

version = 0.1
## Vea al final por change log



class CDSplitter(QtGui.QSplitter):

    def __init__(self, *args, **kwds):
        #~ print "\n\nCDSplitter.__init__()", args, kwds
        QtGui.QSplitter.__init__(self, *args)
        self.setStyleSheet("QSplitter::handle{background-color:qradialgradient(cx:.5, cy:.5, radius:1,fx:.5, fy:.25, stop: 0 #C0E8FF, stop:1 #4070E0); border: 2 solid #0000FF; border-radius:4;}")

    
    def createHandle(self):
        #~ print "\n\ncdSplitter.createHandle()"
        return cdSplitterHandle.CDSplitterHandle(self.orientation(), self)



if __name__=='__main__':
    application = QtGui.QApplication(sys.argv)
    
    fondo = QtGui.QWidget(None)
    fondo.show()
    
    application.exec_()


""" Bitácora de cambios

2011-Ene-18 09:10 v0.1  Creation
"""


""" Justificación
CDLineEdit uses styleSheet to manage statusLabel layout, styleSheet may be overriden by user, so, CDLineEdit overrides setStyleSheet method to include the baseStyle of its own.
"""
