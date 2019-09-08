# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Status Label to add to other widgets       ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2008                                ##
  ##                                             ##
    ###############################################


"""Widget que se adhiere a otros widgets y que sirve para indicar mediante colores y tips un estado particular debido a la informacion que contiene.

    message
    style
    setStatus()
    setStyle()
    visibleIfValid()
"""


import sys

from PyQt4 import QtCore, QtGui



class CDStatusLabel(QtGui.QLabel):
    """This is the class that implements the whole thing"""

    def message(self):
        return self._message.rstrip("\n")

    def setMessage(self, value):
        self._message = value
        self.setToolTip(value)


    def shape(self):
        return self._shape

    def setShape(self, value):
        # print 'setShape', self.text()
        self._shape = value
        if self._shape == 0:
            self.setFixedWidth(7)
            self._radius =  """
                border-left-width: 0px;
                border-top-right-radius: 3px;
                border-top-left-radius: 3px;
                border-bottom-right-radius: 3px;
                border-bottom-left-radius: 3px;
                """
        else:
            self.setFixedSize(16, 16)
            self._radius = """
                border-radius: 8px;
                """

        self.setStyleSheet("""
            QLabel {
            border-style: solid;
            border-width: 1px;
            border-color: #A0A0A0;
            %s
            %s
            }
            """ % (self.background, self._radius))


    def status(self):
        return self._status


    def setStatus(self, value, messageKwd=None):
        # print 'setStatus', self.text()
        self._status = value
        if value == 0:              # Transparente
            self.color = """
                background-color: rgba(0,0,0,0);
                selection-background-color: rgba(0,0,0,0);
                """
            self.color2 = """
                background-color: rgba(0,0,0,0);
                selection-background-color: rgba(0,0,0,0);
                """

        elif value == 1:            # Rojo
            self.color = """
                background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #FF8080);
                selection-background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #FF8080);
            """
            self.color2 = """
                background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #808080);
                selection-background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #808080);
            """

        elif value == 2:            # Verde
            if self._visibleIfValid:
                self.color = """
                    background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5,stop:0 white, stop:1 #80FF80);
                    selection-background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #80FF80);
                """
                self.color2 = """
                    background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5,stop:0 white, stop:1 #808080);
                    selection-background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #808080);
                """
            else:
                self.color = """
                    background-color: rgba(0,0,0,0);
                    selection-background-color: rgba(0,0,0,0);
                    """
                self.color2 = """
                    background-color: rgba(0,0,0,0);
                    selection-background-color: rgba(0,0,0,0);
                    """

        elif value == 3:            # Amarillo
            self.color = """
                background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #FFFF80);
                selection-background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #80FFFF);
            """
            self.color2 = """
                background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #808080);
                selection-background-color:QLinearGradient(x1:0, y1:0, x2:.5, y2:.5, stop:0 white, stop:1 #808080);
            """

        self.setStyleSheet("""
            QLabel:Enabled {
            border:1px solid #C0C0C0;
            %s
            %s
            }
            QLabel:Disabled {
            border:1px solid #C0C0C0;
            %s
            %s
            }
            """ % (self.color, self.radius, self.color2, self.radius))

        if messageKwd is not None:
            self.message = messageKwd


    def visibleIfValid(self):
        return self._visibleIfValid


    def setVisibleIfValid(self, value=True):
        self._visibleIfValid = value
        self.update()



    def __init__(self, *args, **kwds):

        QtGui.QLabel.__init__(self, *args, **kwds)

        self.background = ''
        self.radius = ''
        self._message = ''
        self._visibleIfValid = False
        self.setText('')

        if 'style' in kwds:
            self.setShape(kwds['style'])
        else:
            self.setShape(0)

        if 'status' in kwds:
            self.setStatus(kwds['status'])
        else:
            self.setStatus(0)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)

        self.setFocusPolicy(QtCore.Qt.NoFocus)

        self.setCursor(QtCore.Qt.WhatsThisCursor)




"""
Ejemplo de uso
"""

if __name__=='__main__':

    index = 0

    def change():
        global index

        if index == 0:
            statusLabel.setShape(0)
            statusLabel.setStatus(0)
            statusLabel.message = "Status: --"
        elif index == 1:
            statusLabel.setShape(1)
            statusLabel.setStatus(2)
            statusLabel.message = "Status: Ok"
        elif index == 2:
            statusLabel.setShape(0)
            statusLabel.setStatus(3)
            statusLabel.message = "Status: Warning"
        elif index == 3:
            statusLabel.setShape(0)
            statusLabel.setStatus(1)
            statusLabel.message = "Status: Error"
            index = -1

        index += 1



    aplicacion = QtGui.QApplication(sys.argv)


    forma = QtGui.QWidget()

    layout = QtGui.QHBoxLayout()
    layout.setSpacing(0)

    button = QtGui.QPushButton(forma)
    button.setText("Click me")

    forma.connect(button, QtCore.SIGNAL('clicked()'), change)


    statusLabel = CDStatusLabel(forma)

    change()

    statusLabel.setVisibleIfValid(True)         # True/False

    layout.addWidget(button)
    layout.addWidget(statusLabel)

    forma.setLayout(layout)
    forma.show()
    aplicacion.exec_()

