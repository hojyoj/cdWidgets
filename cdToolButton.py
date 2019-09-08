# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Tool Button with Criptidos vision          ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   por Críptidos Digitales                    ##
 ##   GPL (c)2008                                ##
  ##                                             ##
    ###############################################

"""
Adds attributes:
    mouseOver         event
"""

import sys
from PyQt4 import QtCore, QtGui


version = 0.1
## Vea al final por change log



class CDToolButton(QtGui.QToolButton):

    def __init__(self, *args, **kwds):

        QtGui.QToolButton.__init__(self, *args)


    def enterEvent(self, event):
        self.emit(QtCore.SIGNAL("enter()"))

    def leaveEvent(self, event):
        self.emit(QtCore.SIGNAL("leave()"))



if __name__=='__main__':
    aplicacion=QtGui.QApplication(sys.argv)
    fondo=QtGui.QWidget(None)

    etiquetaSinLimites=QtGui.QLabel('0  a 65535')
    linea = QtGui.CDLineEdit(fondo, hasStatusLabel=True)
    linea.setStatusLabelStyle(0)

    etiqueta2=QtGui.QLabel('ninguno hasta 5')
    linea2 = QtGui.CDLineEdit(fondo, hasStatusLabel=True)
    linea2.setAllowedLengths(0,5)

    etiqueta3 = QtGui.QLabel('de 2 a 5 caracteres con tip de ayuda')
    linea3 = QtGui.CDLineEdit(fondo, minimo=2, maximo=5, hasStatusLabel=True)


    layout=QtGui.QVBoxLayout()
    layout.addWidget(etiquetaSinLimites)

    layout.addWidget(linea)

    layout.addWidget(etiqueta2)
    layout.addWidget(linea2)

    layout.addWidget(etiqueta3)
    layout.addWidget(linea3)

    fondo.setLayout(layout)
    fondo.show()
    aplicacion.exec_()


""" Bitácora de cambios
2009-Ene-24 11:15 v0.1  Creación, emision de evento enter
"""
