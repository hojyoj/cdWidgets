# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##          Combo Box with validation          ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##              GPL (c)2008-2013               ##
  ##                                            ##
    ##############################################

"""
Incorporates cdStatusLabel
Adds attributes:
    emptyAllowed    default = False     capitalized     default = False
    onlyNumbers     default = False     hasStatusLabel  default = True
    minimo          (minimum length)    maximo          (maximum length)
    message         Error messages      trimmed
    isValid                             isModified      default = False
    externalValidation                  externalMessage
"""

from __future__ import print_function

__version__ = "2.2"             ## Go to end for change log

import sys
from PyQt4 import QtCore, QtGui

from cdWidgets import cdStatusLabel



class CDComboBox(QtGui.QComboBox):

    def __init__(self, *args, **kwds):
        """CDComboBox.__init__()"""
        self._baseStyle = ""
        self._style = ""
        self._trimmed = True
        self._message = u""
        self._prefix = u""
        self._emptyAllowed = False
        self._externalValidation = True
        self._externalMessage = u""
        self._capitalized = False
        if 'minimo' in kwds:
            self._minimo = kwds['minimo']
        else:
            self._minimo = None

        self._statusLabel = None

        QtGui.QComboBox.__init__(self, *args)

        self._flags = 0

        self._data = [[]]
        self._initialData = [None]
        self._initialText = u""
        self._initialIndex = -1
        self._roles = [999]

        if 'hasStatusLabel' in kwds:
            self.hasStatusLabel(kwds['hasStatusLabel'])
        else:
            self.hasStatusLabel(False)
            
        self.style = []
        self.style.append({'background-color':"#FFFFFF"})
        self.style.append({'background-color':"#F8FFC0"})
        self.style.append({'background-color':"#FF0000"})
        
        self.styleMode = 0

        self.update()

        self.connect(self, QtCore.SIGNAL("currentIndexChanged(int)"), self.currentIndexChanged)

    
    def addItem(self, text, data=None, role_=999):
        # print("""cdComboBox.addItem()[{}]""".format(self.objectName()))
        
        if role_ not in self._roles:
            self._roles.append(role_)
            self._data.append([None for x in self._data[0]])
        
        for index, role in enumerate(self._roles):
            if role == role_:
                self._data[index].append(data)
            else:
                self._data[index].append(None)

        # index = len(self._data) - 1
        
        QtGui.QComboBox.addItem(self, text)
    
    
    def clear(self):
        # print("""cdComboBox.clear()[{}]""".format(self.objectName()))
        self._initialData = [None]
        self._roles = [999]
        self._data = [[]]
        
        QtGui.QComboBox.clear(self)
        

    def currentData(self, role_=None):
        ## Must not return QVariant, receiver must not try to convert because
        ## None can't be converted, resulting in attribute exception
        # print('CDComboBox.currentData()')

        if self.currentIndex() < 0:
            return None
        elif role_:
            # return self.itemData(self.currentIndex(), role)
            # print(self._roles)
            # print(self._data)
            return self._data[self._roles.index(role_)][self.currentIndex()]
        else:
            # print("CDComboBox.currentData()", self._data)
            # print("CDComboBox.currentData()", self._roles)
            # print("CDComboBox.currentData()", self.currentIndex())
            return self._data[self._roles.index(999)][self.currentIndex()]


    def currentIndexChanged(self, index):
        self.update()
       # self.emit(QtCore.SIGNAL("currentIndexChanged(int)"), index)


    def emptyAllowed(self):
        return self._emptyAllowed

    def setEmptyAllowed(self, value=True):
        self._emptyAllowed = value
        self.update()


    # def findData(self, data):
        # return 


    def flags_get(self):
        return self._flags
    def flags_set(self, value):
        self._flags = value
        if value & QtCore.Qt.ItemIsEditable:
            self.setEnabled(True)
        else:
            self.setEnabled(False)
    flags = property(flags_get, flags_set)


    def focusInEvent(self, event):
        QtGui.QComboBox.focusInEvent(self, event)
        self.emit(QtCore.SIGNAL("gotFocus()"))

    def focusOutEvent(self, event):
        QtGui.QComboBox.focusOutEvent(self, event)
        self.emit(QtCore.SIGNAL("lostFocus()"))

    def hasStatusLabel(self, value=None):
        """cdComboBox.CDComboBox.hasStatusLabel()"""
        if value is None:
            return self._hasStatusLabel
        else:
            # self._hasStatusLabel = None
            self._hasStatusLabel = value
            if self._hasStatusLabel:
                if self._statusLabel is None:
                    self._statusLabel = cdStatusLabel.CDStatusLabel(self)
                    self._statusLabel.setBuddy(self)
                    margin = self._statusLabel.size().width()
                    self._baseStyle = """QComboBox::drop-down{subcontrol-origin:margin;} QComboBox{margin-right:%dpx; padding:1px;}""" % (margin+1)
                    self.setStyleSheet()
                    self.update()
            else:
                if self._statusLabel:
                    self._statusLabel.destroy()
                    self._baseStyle = """
                        QComboBox::drop-down{subcontrol-origin:margin;}
                        QComboBox{
                        margin-right:0px;
                        padding:1px
##                    }
                    """
                    self.setStyleSheet()
                    self.update()

    def initialData(self, role=999):
        return self._initialData[self._roles.index(role)]

    def initialIndex(self):
        return self._initialIndex

    def initialText(self):
        return self._initialText


    def insertItem(self, index, text):
        # print("""cdComboBox.insertItem()""")
        # self._data[len(self._roles)-1] = [ None for x in self._data[0] ]
        
        for roleIndex, role in enumerate(self._roles):
            self._data[roleIndex].insert(index, None)
        
        QtGui.QComboBox.insertItem(self, index, text)
        

    def itemData(self, *args):
        QtGui.QComboBox.itemData(self, *args)
        print ("This message is generated by cleaning process")
        print ("Replacing itemData use for currentData")
        
        
    def isModified(self):
        """cdComboBox.isModified()"""
        # print(type(self.initialText()), type(self.currentText()))
        try:
            if self.initialText() == self.currentText():
                return False
            else:
                return True
        except:
            print (" ==== ERROR @ cdComboBox.CDComboBox.isValid()", self.initialText(), self.currentText())


    def isValid(self):
        """cdComboBox.CDComboBox.isValid()"""
        valid = None
        if not self.isHidden():
            valid = True
            self._message = ""

            if not self._emptyAllowed and not self.currentText() and self._minimo is None:
                # print(not self._emptyAllowed, not self.currentText(), self._minimo)
                valid = False
                self._message += u"{} no debe estar vacío\n".format(self._prefix).lstrip(' ').capitalize()

            self._message = self._message.rstrip("\n")

            return valid
        else:
            return True


    def message(self):
        ## mensaje = u"Válido" if self.isValid else "Se requieren de %d a %d caracteres" % (self.longitudMinima, self.longitudMaxima)
        return self._message


    def resizeEvent(self, event):
        if self.hasStatusLabel():
            self.statusLabel.setFixedHeight(self.size().height())
            sz = self.statusLabel.size()
            ## frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
            self.statusLabel.move(self.rect().right()-sz.width(),(self.rect().bottom()+1-sz.height())/2)

            if self.lineEdit():
                self.lineEdit().resize(self.size().width()-18-sz.width(), self.size().height()-2)
                self.lineEdit().move(1, 1)
        else:
            if self.lineEdit():
                self.lineEdit().resize(self.size().width()-18, self.size().height()-2)
                self.lineEdit().move(1, 1)


    def setCurrentData(self, data, role_=999, initialToo=False):        
        try:
            if data is None:
                self.setCurrentIndex(-1, initialToo)
            else:
                index = self._data[self._roles.index(role_)].index(data)
                self.setCurrentIndex(index, initialToo)
        except:
            print (sys.exc_info()[1])
            print (self._data)
            raise
            
        # if index > -1:
        # else:
            # if initialToo:
                # self._intialIndex = index
                # self._initialText = QtCore.QString()
                # self._initialData = QtCore.QVariant()


    def setCurrentIndex(self, index, initialToo=False):
        QtGui.QComboBox.setCurrentIndex(self, index)
        if initialToo:
            self._initialIndex = index
            self._initialText = self.currentText()
            # print(u"cdComboBox.setCurrentIndex() {},{}".format(self._initialText, self.currentText()).encode('utf8'))
            # print(type(self.initialText()), type(self.currentText()))
            if index < 0:
                self._initialData[self._roles.index(999)] = None
            else:
                # self._initialData = self.itemData(index)
                self._initialData[self._roles.index(999)] = self._data[self._roles.index(999)][index]
        self.update()


    def setCurrentText(self, text, initialToo=False):
        index = QtGui.QComboBox.findText(self, text)
        if index > -1:
            self.setCurrentIndex(index, initialToo)
        else:
            self.setEditText(text)
            if initialToo:
                self._initialIndex = index
                self._initialText = QtCore.QString(text)
                self._initialData[self._roles.index(999)] = None


    def setItemData(self, index, data, role_):
        # print("""cdComboBox.setItemData()[{}]""".format(self.objectName()))
        
        if index >= len(self._data[self._roles.index(999)]):
            print ("""Error: index out of range""")
            f=g
        else:
            if role_ not in self._roles:
                self._roles.append(role_)
                self._data.append([None for x in self._data[0]])
            
            roleIndex = self._roles.index(role_)
            self._data[roleIndex][index] = data


    def setStyleSheet(self, text=None):
        # print("CDComboBox.setStyleSheet()")
        
        # print(text)
        
        if text is None:
            if self._style:
                text = self._baseStyle.replace(";", "; {};".format(self._style), 1)
            else:
                text = self._baseStyle
        elif type(text) is dict:
                # print(3336)
                if self.styleMode is 1:
                    # print(3337, self.statusLabel.status())
                    style = self.style[self.statusLabel.status()]
                    
                    # print(444555, self._style)
                    
                    for key in style.keys():
                        index = self._style.find(key)
                        if index+1:
                            index += len(key) + 1
                            
                            self._style = self._style[:index] + style[key] + self._style[index+len(style[key]):]
                            
                    # print(444556, self._style)
                    
                text = self._baseStyle + self._style
                            
            
        else:
            if text:
                # print(3333)
                if '{' in text:
                    # print(3334)
                    self._style = text
                    #~ text = self._baseStyle.replace(";", "; {};".format(text), 1)
                else:
                    # print(3335)
                    self._style = 'QWidget{{{}}}'.format(text)

                # print(3338)
                
                text = self._baseStyle + self._style
            else:
                text = self._baseStyle
                
        # print(99888, text)
        
        QtGui.QComboBox.setStyleSheet(self, text)

        # print("CDComboBox.setStyleSheet() - END")


    @property
    def statusLabel(self):
        return self._statusLabel


    def update(self):
        if self.hasStatusLabel():
            old = self.statusLabel.status
            
            # print(33000, self.styleSheet())
            
            if self.isValid():
                self.statusLabel.setStatus(0)
                # print(33001, self.styleMode, self.styleMode is 1)
                if self.styleMode is 1:
                    # print(33002, self.style[0])
                    self.setStyleSheet(self.style[0])
            else:
                self.statusLabel.setStatus(1)
                if self.styleMode is 1:
                    self.setStyleSheet(self.style[1])
            self.statusLabel.setMessage(self.message())
            if self.statusLabel.status != old:
                # Se emite un evento de statusChanged
                self.emit(QtCore.SIGNAL("statusChanged(int)"), self.currentIndex())



if __name__=='__main__':
    print ("Test routine not implemented for cdComboBox")
    aplicacion=QtGui.QApplication(sys.argv)
    fondo=QtGui.QWidget(None)

    etiquetaSinLimites=QtGui.QLabel('0  a 65535')
    linea = CDComboBox(fondo, hasStatusLabel=True)
    # linea.setStatusLabelStyle(0)

    etiqueta2=QtGui.QLabel('ninguno hasta 5')
    linea2 = CDComboBox(fondo, hasStatusLabel=True)
    # linea2.setAllowedLengths(0,5)

    etiqueta3 = QtGui.QLabel('de 2 a 5 caracteres con tip de ayuda')
    linea3 = CDComboBox(fondo, minimo=2, maximo=5, hasStatusLabel=True)


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



"""
    ~~~~~~  Change log  ~~~~~~

    2009-Oct-06 12.55 v2.3  Se implementa la señal downArrowPressed()
    2009-Ene-20 17:10 v2.2  Se agrega el atributo prefijo para incluir un 
                            prefijo en los mensajes
    2008-Nov-18 21:10 v2.1  El default para el atributo hasStatusLabel ahora es
                            True
    2008-Nov-18             La función isValid ya contempla el atributo 
                            emptyAllowed


    ~~~~~~  Justification  ~~~~~~

    CDLineEdit uses styleSheet to manage statusLabel layout, styleSheet may be
    overriden by user, so, CDLineEdit overrides setStyleSheet method to include
    the baseStyle of its own.

"""