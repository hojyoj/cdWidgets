# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Line edit with validation                  ##
 ##   for Registro Federal de Causantes (RFC)    ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2008-2012                           ##
  ##                                             ##
    ###############################################

"""
Inherits cdLineEdit
Adds attributes:
    MORAL           0
    FISICA          1
    personality     default FISICA
    requiredLength  int
"""

__version__ = "0.4"             ## Go to end for change log


import sys

from PyQt4 import QtCore, QtGui

from cdWidgets.cdLineEdit import CDLineEdit


class CDRfcEdit(CDLineEdit):

    MORAL = 0
    FISICA = 1

    LETTERS = u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = u"0123456789"
    SEPARATORS = u" -"


    def personality(self):
        return self._personality

    def setPersonality(self, value=-1):
        if value == self.MORAL:
            self._personality = self.MORAL
            self._requiredLength = 12
        else:
            """Si value es FISICA o cualquier otro valor"""
            self._personality = self.FISICA
            self._requiredLength = 13
        self.update()



    def __init__(self, *args, **kwds):
        # print "cdrfcedit.__init__()", args, kwds

        self._requiredLength = 0

        if 'personality' in kwds.keys():
            tmpPersonality = kwds.pop('personality')
        else:
            tmpPersonality = self.FISICA

        CDLineEdit.__init__(self, *args, **kwds)

        self.setPersonality(tmpPersonality)

        self.connect(self, QtCore.SIGNAL('textEdited(QString)'), self.textEdited)

        self.currentDate = QtCore.QDate().currentDate()


    def isValid(self):
        # print "cdWidgets.cdRfcEdit.isValid()"
        """ En lugar de analizar las ocurrencias de separadores, se analiza la
        validez de los bloques, ya que de cualquier forma se guarda el rfc sin
        separadores """

        valid = True
        message = u""
        text = u"{}".format(self.text())

        if text==u"" and self._emptyAllowed:
            message += u"%s es dato opcional\n" % self._messagePrefix.capitalize()
        elif text==u"":
            valid = False
            message += u"    No debe estar vacío\n"
        else:
            initials = [None, None]
            datePos = [None, None]
            homo = [None, None]
            separators = [None, None]
            zone = 0

            for index, ch in enumerate(text):

                if zone == 0:
                    if ch in self.LETTERS:
                        if initials[0] is None:
                            initials = [index, index]
                        else:
                            initials[1] = index
                    else:
                        zone = 1

                if zone == 1:
                    if ch in self.NUMBERS:
                        if datePos[0] is None:
                            datePos = [index, index]
                        elif index - datePos[0] < 6:
                            datePos[1] = index
                        else:
                            zone = 2
                    elif ch in self.SEPARATORS:
                        if separators[0] is None:
                            separators[0] = index
                        else:
                            zone = 2
                    else:
                        zone = 2

                if zone == 2:
                    if ch in self.SEPARATORS:
                        if separators[1] is None:
                            separators[1] = index
                        else:
                            zone = 3
                    elif homo[0] is None:
                        homo = [index, index]
                    elif index - homo[0] < 3:
                        homo[1] = index
                    else:
                        zone = 3

                if zone == 3:
                    pass

            if initials[0] is None or initials[1]-initials[0] != self._requiredLength - 10:
                valid = False
                message += u"    Debe iniciar con %s letras\n" % (self._requiredLength - 9)

            if datePos[0] is None or datePos[1]-datePos[0] < 5:
                valid = False
                message += u"    Debe contener una fecha en formato AAMMDD\n"
            elif datePos[1]-datePos[0] == 5:
                # Podría checar que los primeros caracteres coincidan con el nombre
                tmpMessage = u""
                fecha = text[datePos[0]:datePos[1]+1]

                # if not ( 1950 < 1900+int(fecha[0:2]) <= self.currentDate.year() ):
                    # tmpMessage += u"año, "
                if not ( 0 < int(fecha[2:4]) <= 12 ):
                    tmpMessage += u"mes, "
                if tmpMessage:
                    if not ( 0 < int(fecha[4:6]) <= 30 ):
                        tmpMessage += u"dias"
                else:
                    if not ( 0 < int(fecha[4:6]) <= QtCore.QDate(1900+int(fecha[0:2]), int(fecha[2:4]), 1 ).daysInMonth()):
                        tmpMessage += u"días"
                if tmpMessage:
                    valid = False
                    message += u"    Error en los dígitos de %s\n" % tmpMessage.rstrip(', ')

            if homo[0] is None or homo[1]-homo[0] != 2:
                valid = False
                message += u"    La homoclave (combinación final de letras o números) debe ser de 3 caracteres\n"


            if len(text.replace(" ", "").replace("-", "")) - self._requiredLength > 0:
                valid = False
                message += u"    Debe tener %s caracteres en total\n" % (self._requiredLength)


        # Validación externa
        if not self._externalValidation:
            valid = False
            message += self.externalMessage

        if valid and message == u"":
            message += u"Formato válido"

        self._validationMessage = message.rstrip("\n")
        return valid


    def textEdited(self, text):
        cursorPosition = self.cursorPosition()
        self.setText(u"{}".format(self.text()).upper())
        self.setCursorPosition(cursorPosition)
        self.update()




def main():
    app = QtGui.QApplication(sys.argv)

    fondo = QtGui.QWidget()

    rfcEdit = CDRfcEdit(fondo, personality=CDRfcEdit.MORAL)

    widget2 = QtGui.QLineEdit('solo para que veas que pasa cuando cambias de foco')

    layout = QtGui.QVBoxLayout()
    layout.addWidget(rfcEdit)
    layout.addWidget(widget2)

    fondo.setLayout(layout)
    fondo.show()

    app.exec_()


if __name__=='__main__':
    main()



"""
~~~~~~  Change log  ~~~~~~

2012.10.25  v0.4    Fixed   Validación de separadores, se permite uno por zona.

"""
