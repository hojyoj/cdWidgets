# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Line edit with Criptidos vision            ##
 ##   and key specialization                     ##
 ##                                              ##
 ##                                              ##
 ##   por Críptidos Digitales                    ##
 ##   GPL (c)2008                                ##
  ##                                             ##
    ###############################################

"""
Inherits cdLineEdit
Adds attributes:
    emptyAllowed    default = False
    onlyNumbers
    externalValidation
    externalMessage
"""

import sys
from PyQt4 import QtCore, QtGui
from cdWidgets.cdLineEdit import CDLineEdit

version = 0.1
## Vea al final por change log

import cdStatusLabel


class CDLineEditC(CDLineEdit):

    def __init__(self, *args, **kwds):  # print "CDLineEditC.__init__()", args, kwds
        CDLineEdit.__init__(self, *args)


    def keyPressEvent(self, event):
        CDLineEdit.keyPressEvent(self, event)
        if event.key() == 16777237:
            # self.setText("Down arrow Pressed")
            self.emit(QtCore.SIGNAL("downArrowPressed()"))





##  TEST  #########################################

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    mainWindow = QtGui.QWidget()


    tester = CDLineEditC(mainWindow)


    layout = QtGui.QVBoxLayout(mainWindow)
    layout.addWidget(tester)

    mainWindow.setLayout(layout)
    mainWindow.show()

    app.exec_()



""" Bitácora de cambios
2009-May-04 11:40 v0.1  Creación
"""


""" Justificación
CDLineEditC adds key specialization to CDLineEdit
    This is required by QCompleter to show the Completer list with empty Text on
        lineEdit, at down arrow pressing.
"""
