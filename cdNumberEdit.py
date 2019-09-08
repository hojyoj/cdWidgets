# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Line edit with Criptidos vision            ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2008                                ##
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
    externalMessage
"""

__version__ = "0.4.3"           ## Go to end for change log


import sys
from PyQt4 import QtCore, QtGui

from decimal import Decimal

from cdWidgets import cdStatusLabel


ON, OFF = [True, False]


class CDNumberEdit(QtGui.QLineEdit):
    """
        La corrección o aplicación de límite de decimales se
        aplica en dos ocasiones, en setValue y en FocusOut.
    """

    NUMBERS = [48,49,50,51,52,53,54,55,56,57]
    CONTROL = [16777219,16777223,16777232,16777233,16777234,16777236]
        # BS SUPR INICIO FIN LEFT RIGHT
    DECIMAL = [46]      # .
    separators = [46, 44]   # decimal, thousands
    #~ prefix = "$"        # 36


    _version = 2.4

    _baseStyle = ""
    _capitalized = False
    _emptyAllowed = True
    _externalValidation = True
    _externalMessage = u""
    _initialText = u""
    _message = u""
    _messagePrefix = u""
    __minimo = None
    __maximo = None
    __minValue = None
    __maxValue = None
    _onlyNumbers = False
    _statusLabel = None
    _style = ""
    _symbolsAllowed = True
    _trimmed = True
    _uppercased = False

    _decimals = [0, 2]
    _initialValue = None
    _range = [0, 999999]


    def __init__(self, *args, **kwds):
        """CDNumberEdit.__init__()"""

        self._thousandsSplitting = kwds.pop('thousandsSplitting', OFF)
        self.__minimo = kwds.pop('minimo', None)
        self.__maximo = kwds.pop('maximo', None)
        hasStatusLabel = kwds.pop('hasStatusLabel', True)
        
        self._dataHolder = None

        QtGui.QLineEdit.__init__(self, *args, **kwds)

        self.setStatusLabel(hasStatusLabel)

        self.update()

        self.connect(self, QtCore.SIGNAL('textChanged(QString)'), self.textEdited)


    def thousandsSplitting_get(self):
        return self._thousandsSplitting
    def thousandsSplitting_set(self, value):
        if value in [ON, OFF]:
            self._thousandsSplitting = value
        else:
            print ('value not valid')
            raise
    thousandsSplitting = property(thousandsSplitting_get, thousandsSplitting_set)
    

    def allowedLengths(self):
        return [self.__minimo, self.__maximo]
    def setAllowedLengths(self, minimo, maximo):
        # if not self._emptyAllowed and minimo == 0:
            # print("    CDLineEdit.setAllowedLengths()   Warning: minimo=0, changed emptyAllowed to True ", 'warning')
            # self.setEmptyAllowed(True)
        self.__minimo = minimo
        self.__maximo = maximo
        self.update()


    def allowedValues(self):
        return [self.__minValue, __maxValue]
    def setAllowedLengths(self, min, max):
        self.__minValue = min
        self.__maxValue = max
        self.update()


    def capitalized(self):
        return self._capitalized
    def setCapitalized(self, value):
        self._capitalized = value


    _context = None
    def context_get(self):
        return self._context
    def context_set(self, value):
        self._context = value
    context = property(context_get, context_set)
    
    @property
    def dataHolder(self):
        return self._dataHolder
    def dataHolder_set(self, value):
        self._dataHolder = value

    """ NUMERO DE POSICIONES DECIMALES
        Case 1 : []     Número indefinido
        Case 2 : [#]    Número fijo
        Case 3 : [#, #] Número preferido pero aumentable a un máximo fijo
        Case 4 : [#, -1] Número preferido pero aumentable indefinidamente
        
    """
    @property
    def decimals(self):
        return self._decimals
        
    def setDecimals(self, min='empty', max='empty'):
        
        # if min is 'empty':
            # Case 1 - Indefinido
            # dec = []
        # elif min < 0:
            # print ("deprecated, can't use negative values")
            # f=g
        # else:
            # dec = [min]
            # if max is not 'empty':
                # dec.append(0)
                # if max >= 0:
                    # Case 3 - Prefered, raisable to max
                    # dec.append(max)
                    
        dec = [0, 65535]
        
        if max is 'empty':
            if min is 'empty':
                pass
            else:
                dec = [min, min]
        else:
            dec = [min, max]            
            
        self._decimals = dec

    def emptyAllowed(self):
        return self._emptyAllowed
    def setEmptyAllowed(self, value):
        self._emptyAllowed = value
        self.update()


    def externalMessage(self):
        return self._externalMessage


    def externalValidation(self):
        return self._externalValidation
    def setExternalValidation(self, value, message):
        """cdWidgets.cdNumberEdit.setExternalValidation()"""
        self._externalValidation = value
        self._externalMessage = message
        self.update()


    def initialText(self):
        return self._initialText
    def setInitialText(self, text, currentToo=False):
        print ("DEPRECATED")
        f=g


    def initialValue(self):
        return self._initialValue
    def setInitialValue(self, value, currentToo=False):
        print ("CDNumberEdit.setInitialValue() DEPRECATION WARNING -- Use setValue('XX', initialToo=True)")
        self._initialValue = value
        if currentToo:
            self.setValue(value)


    def message(self):
        return self._message.rstrip(u"\n")
    def setMessage(self, value):
        self._message = value


    def messagePrefix(self):
        return self._messagePrefix
    def setMessagePrefix(self, value):
        self._messagePrefix = value
        self.update()


    def range(self):
        return self._range
    def setRange(self, min=0, max=999999):
        self._range = [Decimal(str(min)), Decimal(str(max))]


    def statusLabel(self):
        return self._statusLabel
    def setStatusLabel(self, value=True):
        self._hasStatusLabel = value
        if self._hasStatusLabel:
            if self._statusLabel is None:
                self._statusLabel = cdStatusLabel.CDStatusLabel(self)
                self._statusLabel.setBuddy(self)
                margin = self._statusLabel.size().width()
                self._baseStyle = """QLineEdit{margin-right:%dpx; padding:1px;}""" % (margin+1)
                self.setStyleSheet()
                self.update()
        else:
            self._statusLabel.destroy()
            self._baseStyle = """
                QLineEdit{
                    margin-right:0px;
                    padding:1px
                }
                """
            self.setStyleSheet()
            self.update()
    def hasStatusLabel(self, value=None):
        if value is None:
            return self._hasStatusLabel
        else:
            self.setStatusLabel(value)


    def setStatusLabelStyle(self, value):
        if self._hasStatusLabel:
            self._statusLabel.setShape(value)
            margin = self._statusLabel.size().width()
            styleSheet = """
                    margin-right:10px;
                    padding:1px;
                """
            # styleSheet = """
                    # margin-right: 10px;
                    # padding: 1px;
                # """ % (margin+1)
            self.setStyleSheet(styleSheet)
        self._statusLabelStyle = value


    def focusInEvent(self, event):
        QtGui.QLineEdit.focusInEvent(self, event)
        self.emit(QtCore.SIGNAL("gotFocus()"))

    def focusOutEvent(self, event):
        ## Fix decimals length before leaving
        self.limitDecimals()
        QtGui.QLineEdit.focusOutEvent(self, event)
        self.emit(QtCore.SIGNAL("lostFocus()"))


    def limitDecimals(self):
        # print("""    cdNumberEdit.limitDecimals()""")
        text = self.text()
        
        point = text.find(chr(self.separators[0]))
        if point + 1 == 0:
            point = len(text)
            length = 0
        else:
            length = len(text) - point - 1
        
        limit = 0
        
        if length < self.decimals[0]:

            if chr(self.separators[0]) not in text:
                text = text + chr(self.separators[0])
        
            text = "{}0000000000".format(text)
            
            limit = self.decimals[0]
            
        elif length >= self.decimals[1]:
            
            limit = self.decimals[1]
            
        text = text[:point+1 + limit]
        
        self.setText(text)

        # print("""    cdNumberEdit.limitDecimals() - END""")


    def format(self):
        # print("    CDNumberEdit.format()", self.objectName())
        """ Updates decimals number
            Updates thousands separator
        """
        
        curPos = self.cursorPosition()
        
        text = self.text()
        
        if text:
            pass
            ## Fix decimals overflow
            # print(281, max(0, -Decimal(text).as_tuple().exponent))
            # if max(0, -Decimal(text).as_tuple().exponent) > self.decimals[1]:
                
                ## Truncate
                # text = text[ : text.find('.') + self.decimals[1] + 1]

        
        if self.thousandsSplitting is ON:
            
            strippedText = text.replace(',', '')
            
            if '.' in strippedText:
                zeroPos = strippedText.find('.')
            else:
                zeroPos = len(strippedText)
            
            if zeroPos > 3:
                strippedText = strippedText[:zeroPos-3] + ',' + strippedText[zeroPos-3:]
                
            if zeroPos > 6:
                strippedText = strippedText[:zeroPos-6] + ',' + strippedText[zeroPos-6:]
                
            text = strippedText
        
        
        self.setText(text)
        
        self.setCursorPosition(curPos)
            
        
        
        
        # elif len(self._decimals) > 1:
            ## Permite desplegado de más decimales
            
            # if len("{}".format(value.normalize() % 1)[3:]) <= self._decimals[1]:
                # self.setText(str(value.quantize(Decimal('0.{}1'.format("0000"[:self._decimals[1]-1])))))
            # elif len(self._decimals) > 2:
                # self.setText(str(value.quantize(Decimal('0.{}1'.format("00000000"[:self._decimals[2]-1])))))
            # else:
                # self.setText("{}".format(value.normalize()))
        # else:
            ## if type(value)==Decimal:
                # self.setText(str(value.quantize(Decimal('0.{}1'.format("0000"[:self._decimals[1]-1])))))

        
        # print("    CDNumberEdit.format() -END")
        
        return
        
        cursorPos = self.cursorPosition()
        length = len(self.text())
        sincomas = self.text().replace(',', '')
        mark = len(sincomas)

        if sincomas.find('.') > -1:
            mark = sincomas.find('.')
            
            fraccion = sincomas[mark:].rstrip('0')
            
            if len(self._decimals) is 1:
                # if type(value)==Decimal:
                    #! this does not round
                    fraccion = (sincomas+'00000000')[mark:mark+self._decimals[0]+1]
            elif len(self._decimals) is not 0:
                if len(sincomas[mark+1:].rstrip('0')) < self._decimals[0]:
                    fraccion = (sincomas+'00000000')[mark:mark+self._decimals[0]+1]
                elif len(sincomas[mark+1:].rstrip('0')) > self._decimals[0]:
                    if len(self._decimals) is not 2:
                        fraccion = (sincomas+'00000000')[mark:mark+self._decimals[2]+1]
                else:
                    if self._decimals[0] is 0:
                        fraccion = ''
        else:
            fraccion = ''

        sincomas = sincomas[:mark]

        entero = sincomas[:]
        
        self.setText(entero + fraccion)

        if entero and self.thousandsSplitting is ON:
            if int(sincomas) >= 1000:
                entero = "{},{}".format(entero[:len(entero)-3], entero[len(entero)-3:])
                self.setText(entero + fraccion)
                
            if int(sincomas) >= 1000000:
                entero = "{},{}".format(entero[:len(entero)-7], entero[len(entero)-7:])
                self.setText(entero + fraccion)
                
            # self.setCursorPosition(cursorPos + len(self.text()) - length)
        
        self.setCursorPosition(cursorPos)

        # print("""CDNumberEdit.format() - END""", self.objectName())


    def isModified(self):
        # print("""cdNumberEdit.isModified()""")
    #~ @property
    #~ def isModified(self):
        #~ if self.text() != self.initialText:
            #~ return True
        #~ else:
            #~ return False
            
        if self.value() == self._initialValue:
            return False
        else:
            return True

    def isEmpty(self):
        if unicode(self.text()):
            return False
        else:
            return True

    def isValid(self):
        # print("""CDNumberEdit.isValid()""", self.objectName())
        valid = True
        message = ""
        if not self.isHidden():

            if not self.range()[0] <= self.value() <= self.range()[1]:
                valid = False
                message = u"Valor no permitido"
            elif self.value() == 0 and not self._emptyAllowed:
                valid = False
                message = u"Falta {}".format(self._messagePrefix)

        self.setMessage(message)
        # print("""CDNumberEdit.isValid() - END""", self.objectName())
        return valid


    def keyPressEvent(self, event):
        # print("CDNumberEdit.keyPressEvent()")
        
        ## Validate keystrokes
        ignore = False

        ## Ignore not valid entries
        if event.key() not in self.NUMBERS + self.CONTROL + self.DECIMAL:
            ignore = True
        
        ## If keystroke is the decimals separator
        elif event.key() in self.DECIMAL:
            
            ## If separator already exists
            if chr(self.DECIMAL[0]) in self.text():
                ignore = True
                
            ## If is empty, add trailing zero
            # elif not self.text():
                # self.setText('0')
        
        ## If keystroke is a number
        elif event.key() in self.NUMBERS:
            
            ## If value is 0, remove trailing zero
            # if self.text() is '0':
                # self.setText('')
        
            ## Not selection and cursor at end
            if not self.selectedText() and self.cursorPosition() == len(self.text()):
                
                #! Decimals limit not enforced
                #! Implement warning instead
                ## If decimals limit reached
                '''
                if chr(self.DECIMAL[0]) in self.text() and max(0, -Decimal(self.text()).as_tuple().exponent) >= self.decimals[1]:
                    
                    print (990011, self.DECIMAL)
                    print (990012, self.decimals)
                    print (990013, -Decimal(self.text()).as_tuple().exponent)
                    print (max(0, -Decimal(self.text()).as_tuple().exponent))
                    ignore = True
                '''
        
        if not ignore:
            result = QtGui.QLineEdit.keyPressEvent(self, event)

        if not self.text():
            self.setText('0')
            self.setSelection(0, 1)
        
        self.format()

        # print("CDNumberEdit.keyPressEvent() - END")


    def resizeEvent(self, event):
        """CDNumberEdit.resizeEvent()"""
        if self.hasStatusLabel():
            self.statusLabel().setFixedHeight(self.size().height())
            sz = self.statusLabel().size()
            ## frameWidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
            self.statusLabel().move(self.rect().right()-sz.width(),(self.rect().bottom()+1-sz.height())/2)


    def setCompleter(self, completer):
        QtGui.QLineEdit.setCompleter(self, completer)


    def setOnlyNumbers(self, value):
        f=g
        self._onlyNumbers = value
        self.update()


    def setStyleSheet(self, text=None):
        if text is None:
            if self._style:
                text = self._baseStyle.replace(";", "; {};".format(self._style), 1)
            else:
                text = self._baseStyle
        else:
            if text:
                if '{' in text:
                    self._style = text
                    #~ text = self._baseStyle.replace(";", "; {};".format(text), 1)
                else:
                    self._style = 'QWidget{{}}'.format(text)
                text = self._baseStyle + self._style
            else:
                text = self._baseStyle

        QtGui.QLineEdit.setStyleSheet(self, text)

    def setSymbolsAllowed(self, value=True):
        self._symbolsAllowed = value
        self.update()


    def text(self):
        # print("""CDNumberEdit.text()""", self.objectName())
        text = "{}".format(QtGui.QLineEdit.text(self))
        if self._trimmed:
            text = text.strip()
        # print("""CDNumberEdit.text() - END""", self.objectName())
        return text
    def setText(self, text, initialToo=False):
        # print("""CDNumberEdit.setText()""", self.objectName())
        
        QtGui.QLineEdit.setText(self, text)
        
        if initialToo:
            self._initialText = text
            self._initialValue = Decimal(text)
        
        # print("""CDNumberEdit.setText() - END""", self.objectName())


    def textEdited(self, texto):
        # print("""CDNumberEdit.textEdited()""", self.objectName())
        if self._uppercased:
            self.setText(texto.upper())
        elif self._capitalized:
            self.setText(unicode(texto[:1]).upper() + unicode(texto[1:]))

        self.update()
        # print("""CDNumberEdit.textEdited() - END""", self.objectName())


    def setTrimmed(self, value):
        self._trimmed = value
        self.update()

    def setUppercased(self, value):
        self._uppercased = value

    @property
    def symbolsAllowed(self):
        return self._symbolsAllowed

    def update(self):
        # print("""CDNumberEdit.update()""", self.objectName())
        if self._hasStatusLabel:
            old = self._statusLabel.status()

            if self.isValid():
                self._statusLabel.setStatus(0)
            else:
                self._statusLabel.setStatus(1, self._message)
            self._statusLabel.setMessage(self._message)
            if self._statusLabel.status() != old:
                # Se emite un evento de statusChanged
                self.emit(QtCore.SIGNAL("statusChanged()"))
        # print("""CDNumberEdit.update() - END""", self.objectName())


    def value(self):
        # print("""CDNumberEdit.value()""", self.objectName())
        """ Widget's value is obtained from text() attribute """
        try:
            return Decimal(str(self.text().replace(',', '')))
        except:
            return Decimal("0")
    def setValue(self, value, initialToo=False):
        # print("""CDNumberEdit.setValue()""", self.objectName())
        """ value must be Decimal, or convertible to Decimal"""
        # print(value)
        
        if value is None:
            value = Decimal(0)
        elif type(value) != Decimal:
            value = Decimal(value)

        self.setText("{}".format(value))
        
        self.limitDecimals()

        if initialToo:
            self._initialValue = value
            self._initialText = self.text()
        
        self.format()

        # print("""CDNumberEdit.setValue() - END""", self.objectName())



if __name__=='__main__':
    aplicacion=QtGui.QApplication(sys.argv)
    fondo=QtGui.QWidget(None)

    etiquetaSinLimites = QtGui.QLabel('0  a 65535')
    linea = CDNumberEdit(fondo, hasStatusLabel=True)
    linea.setStatusLabelStyle(0)

    etiqueta2 = QtGui.QLabel('ninguno hasta 5')
    linea2 = CDNumberEdit(fondo, hasStatusLabel=True)
    linea2.setAllowedLengths(0,5)

    etiqueta3 = QtGui.QLabel('de 2 a 5 caracteres con tip de ayuda')
    linea3 = CDNumberEdit(fondo, minimo=2, maximo=5, hasStatusLabel=True)


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
  ~~~~~~  Known Issues  ~~~~~~
    07.13   initialText should not exist
    
    2014.04.22  Backspace misbehaviour


  ~~~~~~  Change log  ~~~~~~

        v0.4.3
    07.13   Fixed decimal limits usage, again.

    2014.04.22  v0.4.2  Fixed decimals management

    2014.03.27          Removed isValid old code (not used here)

    2012.10.16  v0.4.1  Fixed   Bug en el manejo de número de decimales.

    2010-Feb-10 17:45 v2.4  Se implementa la función isModified()
    2009-Oct-06 12:55 v2.3  Se implementa la señal downArrowPressed()
    2009-Ene-20 17:10 v2.2  Se agrega el atributo prefijo para incluir un prefijo en los mensajes
    2008-Nov-18 21:10 v2.1  El default para el atributo hasStatusLabel ahora es True
    2008-Nov-18             La función isValid() ya contempla el atributo emptyAllowed


  ~~~~~~  Justification  ~~~~~~

    CDLineEdit uses styleSheet to manage statusLabel layout, styleSheet may be overriden by user, so, CDLineEdit overrides setStyleSheet method to include the baseStyle of its own.


    En desarrollo <<<
  ~~~~~~  Atributo Contexto  ~~~~

    Se puede tener un valor que en un contexto pueda considerarse
        igual a otro valor en diferente contexto.
    Ej: 100 == 116 cuando el primer valor tiene context cxINITIAL y
        el segundo valor está en el contexto cx2.

    por lo que si initialValue = 100 en contexto cxInitial
    >>>

"""
