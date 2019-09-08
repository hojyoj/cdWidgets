# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##         Text edit with validation           ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##                GPL (c)2011                  ##
  ##                                            ##
    ##############################################

"""
Adds attributes:
    message         Error messages
    isValid
    isModified      default = False
"""

__version__ = "0.1"             ## Go to end for change log


from PyQt4 import QtGui



class CDTextEdit(QtGui.QTextEdit):

    def __init__(self, *args, **kwds):

        self._message = u""
        self._initialHtml = u""
        self._initialText = u""

        QtGui.QTextEdit.__init__(self, *args, **kwds)


    def initialHtml(self):
        return self._initialHtml

    def initialText(self):
        return self._initialText


    def isModified(self):
        if self.toPlainText() != self.initialText():
            return True
        else:
            return False

    def isValid(self):
        """CDTextEdit.isValid()"""
        if not self.isHidden():
            valid = True
            self._message = ""
            return valid
        else:
            return True

    def message(self):
        ## mensaje = u"Válido" if self.isValid() else "Se requieren de %d a %d caracteres" % (self.longitudMinima, self.longitudMaxima)
        return self._message


    def setHtml(self, html, initialToo=True):
        result = QtGui.QTextEdit.setHtml(self, html)
        if initialToo:
            self._initialHtml = html
            self._initialText = self.toPlainText()
        return result


    def setInitialHtml(self, html, currentToo=False):
        self._initialHtml = html
        if currentToo:
            self.setHtml(html)
            self._initialText = self.toPlainText()
        else:
            initialHtml = self.toHtml()
            self.setHtml(html)
            self._initialText = self.toPlainText()
            self.setHtml(initialHtml)


    def setInitialText(self, text, currentToo=False):
        self._initialText = text
        if currentToo:
            self.setPlainText(text)


    def setMessage(self, message):
        self._message = message




if __name__ == "__main__":
    print ("Test routine not implemented")



"""
~~~~~~  Change log  ~~~~~~


2012.11.06  v0.1    Added   initialToo argument to setHtml

"""


