# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Line edit with validation                  ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2008-2012                           ##
  ##                                             ##
    ###############################################

"""
Incorporates cdStatusLabel
Adds attributes:
    emptyAllowed    default = False
    symbolsAllowed  default = True
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
    externalStatus
    externalMessage
"""

__version__ = "2.4"             ## Go to end for change log


import sys
from PyQt4 import QtCore, QtGui


import cdWidgets.cdStatusLabel as cdStatusLabel


class CDLineEdit(QtGui.QLineEdit):

    _externalValidation = True
    _externalStatus = 0
    _externalMessage = u""
    _initialText = u""

    upperLetters = u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upperSpecials = u"ÁÉÍÓÚÑ"
    lowerLetters = u"abcdefghijklmnopqrstuvwxyz"
    lowerSpecials = u"áéíóúñ"
    numbers = u"0123456789"


    def __init__(self, *args, **kwds):
        # print "CDLineEdit.__init_()", args, kwds
        self._version = 2.4

        self._asciiOnly = False
        self._baseStyle = ""
        self._capitalized = False

        if 'minimo' in kwds:
            self._minimo = kwds.pop('minimo')
        else:
            self._minimo = None
        if 'maximo' in kwds:
            self._maximo = kwds.pop('maximo')
        else:
            self._maximo = None
        self._onlyNumbers = False
        self._statusLabel = None
        self._status = 0
        self._style = ""
        self._symbols = ""
        self._symbolsAllowed = True
        self._trimmed = True
        self._uppercased = False
        self._dataHolder = None

        if 'hasStatusLabel' in kwds.keys():
            hasStatusLabel = kwds.pop('hasStatusLabel')
        else:
            hasStatusLabel = True

        QtGui.QLineEdit.__init__(self, *args, **kwds)
        
        self.style = []
        self.style.append({'background-color':"#FFFFFF"})
        self.style.append({'background-color':"#FFFF80"})
        self.style.append({'background-color':"#FF0000"})
        
        self.styleMode = 0
        
        self.setStatusLabel(hasStatusLabel)
        
        self.update()

        self.connect(self, QtCore.SIGNAL('textChanged(QString)'), self.textEdited)


    def allowedLengths(self):
        return [self._minimo, self._maximo]
    def setAllowedLengths(self, minimo, maximo):
        self._minimo = minimo
        self._maximo = maximo
        self.update()


    def asciiOnly(self):
        return self._asciiOnly
    def setAsciiOnly(self, value):
        if value:
            self._asciiOnly = True
        else:
            self._asciiOnly = False


    def capitalized(self):
        return self._capitalized
    def setCapitalized(self, value=True):
        self._capitalized = value

    @property
    def dataHolder(self):
        return self._dataHolder
    def dataHolder_set(self, value):
        self._dataHolder = value

    _emptyAllowed = True
    def emptyAllowed(self):
        return self._emptyAllowed
    def setEmptyAllowed(self, value=True):
        self._emptyAllowed = value
        self.update()

    def externalMessage(self):
        return self._externalMessage
    def setExternalMessage(self):
        self._externalMessage = value
        self.update()
        
    def externalValidation(self):
        return self._externalValidation
    def setExternalValidation(self, value, message=''):
        # print "CDLineEdit.setExternalValidation()", type(message)
        self._externalValidation = value
        if message:
            self.setExternalMessage = message
        self.update()

    def externalStatus(self):
        return self._externalStatus
    def setExternalStatus(self, value):
        # print "CDLineEdit.setExternalValidation()", type(message)
        self._externalStatus = value
        self.update()

    def initialText(self):
        return self._initialText
    def setInitialText(self, text, currentToo=False):
        self._initialText = text
        if currentToo:
            self.setText(text)

    _message = u""
    def message(self):
        # print "CDLineEdit.message()", type(self._message)
        return self._message.rstrip("\n")
    def setMessage(self, value):
        self._message = value
    def uMessage(self):
        # print "CDLineEdit.uMessage()", type(self.message())
        return u"{}".format(self.message())


    _messagePrefix = u""
    def messagePrefix(self):
        return self._messagePrefix
    def setMessagePrefix(self, value):
        # print "CDLineEdit.setMessagePrefix()"
        self._messagePrefix = value
        self.update()


    def onlyNumbers(self):
        return self._onlyNumbers
    def setOnlyNumbers(self, value=True):
        self._onlyNumbers = value
        self.update()


    def status(self):
        if self._status > self._externalStatus:
            return self._status
        else:
            return self._externalStatus
    def setStatus(self, value, message):
        self._status = value
        if self.hasStatusLabel:
            self._statusLabel.setStatus(value, message)
        self.setStyleSheet()


    @property
    def statusLabel(self):
        return self._statusLabel
    def setStatusLabel(self, value=True):
        self._hasStatusLabel = value
        if self._hasStatusLabel:
            if self._statusLabel is None:
                self._statusLabel = cdStatusLabel.CDStatusLabel(self)
                self._statusLabel.setBuddy(self)
                margin = self._statusLabel.size().width()
                self._baseStyle = """QLineEdit{margin-right:%dpx; padding:1px;} QToolTip{color:#000000; background-color:#FFFF00;}""" % (margin+1)
                self.setStyleSheet()
                self.update()
        else:
            self._statusLabel.destroy()
            self._baseStyle = """QLineEdit{margin-right:0px; padding:1px;}"""
            self.setStyleSheet()
            self.update()
    def hasStatusLabel(self, value=None):
        return self._hasStatusLabel

    def setStatusLabelStyle(self, value):
        if self._hasStatusLabel:
            self._statusLabel.setShape(value)
            margin = self._statusLabel.size().width()
            styleSheet = """QLineEdit{margin-right:10px; padding:1px;}"""
            # styleSheet = """
                    # margin-right: 10px;
                    # padding: 1px;
                # """ % (margin+1)
            self.setStyleSheet(styleSheet)
        self._statusLabelStyle = value


    ## Symbols
    def symbols(self):
        return self._symbols
    def setSymbols(self, value):
        self._symbols = value


    ## Symbols allowed
    def symbolsAllowed(self):
        return self._symbolsAllowed
    def setSymbolsAllowed(self, value=True):
        self._symbolsAllowed = value
        self.update()


    def text(self):
        if self._trimmed:
            return u"{}".format(QtGui.QLineEdit.text(self)).strip()
        else:
            return QtGui.QLineEdit.text(self)
    def setText(self, value, initialToo=False):
        # print "CDLineEdit.setText()"
        QtGui.QLineEdit.setText(self, value)
        if initialToo:
            self._initialText = self.text()
        self.update()
    def uText(self):
        return u"{}".format(self.text())


    def trimmed(self):
        return self._trimmed
    def setTrimmed(self, value=True):
        self._trimmed = value
        self.update()


    def uppercased(self):
        return self._uppercased
    def setUppercased(self, value=True):
        self._uppercased = value


    _validationMessages = ""
    @property
    def validationMessages(self):
        return self._validationMessages



    def focusInEvent(self, event):
        QtGui.QLineEdit.focusInEvent(self, event)
        self.emit(QtCore.SIGNAL("gotFocus()"))


    def focusOutEvent(self, event):
        QtGui.QLineEdit.focusOutEvent(self, event)
        self.emit(QtCore.SIGNAL("lostFocus()"))


    def isModified(self):
        if u"{}".format(self.text()) != u"{}".format(self._initialText):
            return True
        else:
            return False


    def isEmpty(self):
        if u"{}".format(self.text()):
            return False
        else:
            return True


    def isValid(self):
        # print("CDLineEdit.isValid()")
        
        # , self._messagePrefix.encode('utf8'), QtGui.QLineEdit.isVisible(self)
        # if QtGui.QLineEdit.isVisible(self):
        if True:

            valid = True
            message = ""

            ## Chequeo de longitud
            texto = u"{}".format(self.text())
            if self._trimmed:
                texto = texto.strip()
            longitud = len(texto)

            bothLimits = self._minimo is not None and self._maximo is not None
            equalLimits = False
            if bothLimits:
                if self._minimo == self._maximo:
                    equalLimits = True

            if self._minimo is not None:
                if longitud == 0 and self._emptyAllowed:
                    message += u"%s es dato opcional\n" % self._messagePrefix.capitalize()
                elif longitud < self._minimo:
                    if (longitud != 0 and self._emptyAllowed) or not self._emptyAllowed:
                        valid = False
                        if not bothLimits:
                            message += u"La longitud mínima de {} es de {}\n".format(self._messagePrefix.lower(), self._minimo)
                        else:
                            if equalLimits:
                                message += u"%s requiere %d caracteres seguidos\n" % (self._messagePrefix.lower(), self._minimo)
                            else:
                                message += u"%s requiere de %d a %d caracteres\n" % (self._messagePrefix.lower(), self._minimo, self._maximo)

            if self._maximo is not None:
                if longitud > self._maximo:
                    valid = False
                    if not bothLimits:
                        message += u"La longitud máxima de %s es de %s\n" % (self._messagePrefix.lower(), self._maximo)
                    else:
                        if equalLimits:
                            message += u"%s requiere %d caracteres seguidos\n" % (self._messagePrefix.lower(), self._minimo)
                        else:
                            message += u"%s requiere de %d a %d caracteres\n" % (self._messagePrefix.lower(), self._minimo, self._maximo)

            if self._onlyNumbers:
                if [x for x in texto if x not in ["1","2","3","4","5","6","7","8","9","0"]]:
                    valid = False
                    message += u"{} acepta sólo números\n".format(self._messagePrefix.capitalize()).lstrip(' ').capitalize()

            if not self._emptyAllowed and not self.text() and self._minimo is None:
                valid = False
                message += u"{} no debe estar vacío\n".format(self._messagePrefix.capitalize()).lstrip(' ').capitalize()

            # print message.encode('utf8')

            if self.asciiOnly():
                if [x for x in texto if x in self.upperSpecials and x in self.lowerSpecials]:
                    valid = False
                    message += u"{} no acepta acentos o ñ\n".format(self._messagePrefix.capitalize()).lstrip(' ').capitalize()

            ## Check symbols
            if not self._symbolsAllowed:
                if len(texto) and not texto.isalnum():
                    valid = False
                    message += u"{} debe contener sólo letras o números\n".format(self._messagePrefix).lstrip(' ').capitalize()
            elif self._symbols:
                symbols = [x for x in texto if x not in self.upperLetters + self.upperSpecials + self.lowerLetters + self.lowerSpecials + self.numbers]

                # print 1171, type(symbols), symbols
                # print 1127, type(self._symbols), u">%s<" % self._symbols

                notValidSymbols = [x for x in symbols if x not in self._symbols]
                if notValidSymbols:
                    valid = False
                    if len(notValidSymbols) == 1:
                        message += u"{} no tiene permitido el símbolo  {}\n".format(self._messagePrefix, ''.join(set([x+' ' for x in notValidSymbols]))).lstrip(' ').capitalize()
                    else:
                        message += u"{} no tiene permitidos los símbolos  {}\n".format(self._messagePrefix, ''.join(set([x+' ' for x in notValidSymbols]))).lstrip(' ').capitalize()

            ## Validación externa
            if not self._externalValidation:
                valid = False
                message += self._externalMessage

            if valid and message == u"":
                if self._messagePrefix:
                    message += u"El formato de {} es válido\n".format(self._messagePrefix.lower())
                else:
                    message += u"El formato es válido\n"

            self._validationMessages = message.rstrip("\n")
            
            # print("CDLineEdit.isValid() - END")

            return valid
            
        else:
            
            # print("CDLineEdit.isValid() - END")
            
            return True


    def keyPressEvent(self, event):
        QtGui.QLineEdit.keyPressEvent(self, event)
        if event.key() == 16777237:
            # self.setText("Down arrow Pressed")
            self.emit(QtCore.SIGNAL("downArrowPressed()"))


    def resizeEvent(self, event):
        #~ print "cdLineEdit.resizeEvent()", self.isVisible()
        if self._hasStatusLabel:
            self._statusLabel.setFixedHeight(self.size().height())
            sz = self._statusLabel.size()
            ## frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
            self._statusLabel.move(self.rect().right()-sz.width(),(self.rect().bottom()+1-sz.height())/2)


    def showEvent(self, event):
        # print "CDLineEdit.showEvent()"
        self.update()

    def hideEvent(self, event):
        # print "CDLineEdit.hideEvent()"
        self.update()


    def setCompleter(self, completer):
        QtGui.QLineEdit.setCompleter(self, completer)


    def setStyleSheet(self, value=None):
        # print("CDLineEdit.setStyleSheet()")
        
        if value is None:
            if self._style:
                value = self._baseStyle.replace(";", "; %s;" % self._style, 1)
            else:
                value = self._baseStyle
            
            if self.styleMode is 1:
                
                style = self.style[self.status()]
                
                for key in style.keys():
                    index = self._style.find(key)
                    if index+1:
                        index += len(key) + 1
                        
                        self._style = self._style[:index] + style[key] + self._style[index+len(style[key]):]
                
                value = self._baseStyle + self._style
        
        else:
            if value:
                if '{' in value:
                    self._style = value
                    #~ text = self._baseStyle.replace(";", "; %s;" % text, 1)
                else:
                    self._style = 'QWidget{%s}' % value
                value = self._baseStyle + self._style
            else:
                value = self._baseStyle
                
        QtGui.QLineEdit.setStyleSheet(self, value)

        # print("CDLineEdit.setStyleSheet() - END")


    def textEdited(self, value):
        # print "CDLineEdit.textEdited()"
        position = self.cursorPosition()
        if self._uppercased:
            self.setText(value.upper())
        elif self._capitalized:
            self.setText("{}".format(value[:1]).upper() + value[1:])
        self.update()
        self.setCursorPosition(position)


    def update(self):
        # print("CDLineEdit.update()")
        
        if self._hasStatusLabel:

            old = self._statusLabel.status()

            if self.isValid():
                self._statusLabel.setStatus(0)
            else:
                self._statusLabel.setStatus(1, self.validationMessages)
                
            self._statusLabel.setMessage(self.validationMessages)   #! Must add externalMessages
            
            if self._statusLabel.status() != old:
                # Se emite un evento de statusChanged
                self.emit(QtCore.SIGNAL("statusChanged()"))
        
        if self.styleMode is 1:
            self.setStyleSheet()
        
        # print('CDLineEdit.update() - END')



if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)

    fondo = QtGui.QWidget()

    etiquetaSinLimites = QtGui.QLabel('0  a 65535')
    linea = CDLineEdit(fondo, hasStatusLabel=True)
    linea.setStatusLabelStyle(0)


    etiqueta2 = QtGui.QLabel('ninguno hasta 5')
    linea2 = CDLineEdit(fondo, hasStatusLabel=True)
    linea2.setAllowedLengths(0,5)


    etiqueta3 = QtGui.QLabel('de 2 a 5 caracteres con tip de ayuda\nEmpty allowed by default')
    linea3 = CDLineEdit(fondo, minimo=2, maximo=5, hasStatusLabel=True)


    layout=QtGui.QVBoxLayout()
    layout.addWidget(etiquetaSinLimites)

    layout.addWidget(linea)

    layout.addWidget(etiqueta2)
    layout.addWidget(linea2)

    layout.addWidget(etiqueta3)
    layout.addWidget(linea3)

    fondo.setLayout(layout)
    fondo.show()

    app.exec_()



"""
  ~~~~  Change log  ~~~~

  2012.02.09              Validación not symbolsAllowed ahora checa que el texto no esté vacío
  2010-Feb-10 17:45 v2.4  Se implementa la función isModified()
  2009-Oct-06 12:55 v2.3  Se implementa la señal downArrowPressed()
  2009-Ene-20 17:10 v2.2  Se agrega el atributo prefijo para incluir un prefijo en los mensajes
  2008-Nov-18 21:10 v2.1  El default para el atributo hasStatusLabel ahora es True
  2008-Nov-18             La función isValid() ya contempla el atributo emptyAllowed


  ~~~~  Justification  ~~~~

  CDLineEdit uses styleSheet to manage statusLabel layout, styleSheet may be overriden by user, so, CDLineEdit overrides setStyleSheet method to include the baseStyle of its own.
"""