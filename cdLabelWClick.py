# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##          Label as option selector           ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##              GPL (c)2008-2012               ##
  ##                                            ##
    ##############################################

"""
Adds attributes:
    showFocus   default = False

"""

from __future__ import unicode_literals

__version__ = "0.2"             ## Go to end for change log


from PyQt4 import QtCore
from PyQt4 import QtGui


class CDLabelWClick(QtGui.QLabel):

    __showFocus = False
    def showHover_get(self):
        return self.__showFocus
    def showHover_set(self, value):
        self.__showFocus = value
    showFocus = property(showHover_get, showHover_set)

    @property
    def data(self):
        return self._data

    def __init__(self, *args, **kwds):
        QtGui.QLabel.__init__(self, *args)

        self._initialIndex = -1
        self._initialText = u""
        self._data = [[],[]]
        self._pixmap = []
        self._currentIndex = -1
        ## Default roles -2:Text, -3:Default data
        self._roles = [-2, -3]
        
        self.flags = QtCore.Qt.ItemIsEditable


    def enterEvent(self, event):
        self.emit(QtCore.SIGNAL('entered()'))
        
    def flags_get(self):
        return self._flags
    def flags_set(self, value):
        self._flags = value
    flags = property(flags_get, flags_set)

    def initialText(self):
        return self._initialText

    def isModified(self):
        """cdLabelWClick.isModified()"""
        return self._initialIndex != self._currentIndex

    def leaveEvent(self, event):
        self.emit(QtCore.SIGNAL('leaved()'))

    def mouseDoubleClickEvent(self, event):
        # print("""CDLabelWClick.mouseDoubleClickEvent()""")
        
        # print(self.flags, QtCore.Qt.ItemIsEditable)
        if self.flags & QtCore.Qt.ItemIsEditable:
            # print('passed')
            self.emit(QtCore.SIGNAL('doubleClicked()'))

        # print("""CDLabelWClick.mouseDoubleClickEvent() - END""")

    def mouseReleaseEvent(self, event):
        # print("""CDLabelWClick.mouseReleaseEvent()""")
        # print(self.flags)
        if self.flags & QtCore.Qt.ItemIsEditable:
            # print('passed')
            if self.count():
                self.roll()
            self.emit(QtCore.SIGNAL('clicked()'))

        # print("""CDLabelWClick.mouseReleaseEvent() - END""")

    def clear(self):
        self._data = [[], []]
        self._pixmap = []
        self._text = []
        self._currentIndex = -1

    def count(self):
        return len(self._data[0])

    def load(self, values, textKey=None):
        for index, value in enumerate(values):
            if textKey:
                self.setItemText(index, value[textKey])
            self.setItemData(index, value)

    def currentData(self, role=-3):
        if self._currentIndex < 0:
            return None
        else:
            try:
                roleIndex = self._roles.index(role)      # Must check validity
                return self._data[roleIndex][self._currentIndex]
            except:
                print (self._data)
                print (roleIndex)
                print (self._currentIndex)
                raise

    def currentIndex(self):
        return self._currentIndex

    def currentText(self):
        return self._data[0][self._currentIndex]

    def currentPixmap(self):
        if self.currentIndex() < 0:
            return None
        else:
            return self._pixmap[self._currentIndex]


    def roll(self):
        """CDLabelWClick.roll()"""
        # print(self._data)
        if self._currentIndex + 1 == self.count():
            self.setCurrentIndex(0)
        else:
            self.setCurrentIndex(self._currentIndex+1)


    def current_setByData(self, data, role=-3, initialToo=False):
        """CDLabelWClick.current_setByData()"""
        # print("CDLabelWClick.current_setByData()", self._roles)
        roleIndex = self._roles.index(role)      # Must check validity
        index = self._data[roleIndex].index([x for x in self._data[roleIndex] if x == data][0])
        self.setCurrentIndex(index, initialToo)
        

    def setCurrentIndex(self, index, initialToo=False):
        if index < 0:
            self.setText('')
            self.setPixmap(QtGui.QPixmap())
        else:
            self.setText("{}".format(self._data[0][index]))
            if self._pixmap[index]:
                self.setPixmap(self._pixmap[index])
        if initialToo:
            self._initialIndex = index
            self._initialText = self.text()
            self._initialData = self.currentData()
        self._currentIndex = index
        # self.update()
        self.emit(QtCore.SIGNAL('changed()'))

    def setCurrentText(self, text, initialToo=False):
        # print("CDLabelWClick.setCurrentText()", self._data)
        index = self._data[0].index(text.capitalize())
        self.setCurrentIndex(index, initialToo)


    def setItemData(self, index, data, role=-3):
        if role not in self._roles:
            self._roles.append(role)
            self._data.extend([[None]])

        roleIndex = self._roles.index(role)      # Must check validity

        try:    # v0.4.15.2
            self._data[roleIndex].extend((index - len(self._data[roleIndex]) + 1) * [None])
        except:
            print ("""cdLabelWClick.setItemData()""")
            print ('    ', role)
            print ('    ', self._roles)
            print ('    ', self._data)
        
        self._data[roleIndex][index] = data


    def setItemPixmap(self, index, pixmap):
        self._pixmap.extend(( index - len(self._pixmap)+1)*[None])
        self._pixmap[index] = pixmap

    def setItemText(self, index, text):
        self._pixmap.extend(( index - len(self._pixmap) + 1) * [None])
        self._data[0].extend(( index - len(self._data[0]) + 1) * [None])
        self._data[0][index] = u"{}".format(text)

    def setText(self, text, initialToo=False):
        QtGui.QLabel.setText(self, text)
        if initialToo:
            self._initialText = self.text()



if __name__ == "__main__":
    print ("""====  Testing cdLabelWClick  ======""")

    import sys

    app = QtGui.QApplication(sys.argv)

    fondo = QtGui.QWidget()

    label = CDLabelWClick(fondo)

    layout = QtGui.QVBoxLayout(fondo)

    # fondo.setLayout(layout)fondo
    fondo.show()


    print ("""~~~~  Set Data  ~~~~~~""")

    label.setItemText(0, u'Name1 ñ')
    label.setItemData(0, u'Data1 ñ')

    label.setItemText(1, u'Name2 ñ')
    label.setItemData(1, u'Data2 ñ')
    label.setItemData(1, {'a':u'dat1 ñ', 'b':u'dat2ñ'}, role=1001)


    print ("""~~~~  Test  ~~~~~~""")

    # print("""Test 1     No preset""")

    # print("""Test 2     Preset by Index""")
    # label.setCurrentIndex(1)

    # print("""Test 3     Preset by Text""")
    # label.setCurrentText('Name2')

    # print("""Test 4     Preset by Data""")
    # label.current_setByData('Data2')

    print ("""Test 5     Retrieve data""")

    label.setCurrentIndex(0)
    print ("    Data of item 0")
    # print("        ", label.currentData().toString())
    # print("        ", "{}".format(label.currentData().toString()))
    # print("        ", u"{}".format(label.currentData().toString()))
    # print"        ", eval("{}".format(label.currentData().toString())))
    print ("        ", eval("{}".format(label.currentData())) == u'Data1 ñ')

    label.setCurrentIndex(1)
    print ("    Data of item 1 role 0")
    print ("        ", label.currentData())
    print ("        ", label.currentData() == u'Data2 ñ')
    print ("        ", u'{}'.format(label.currentData()) == u'Data2 ñ')

    print ("    Data of item 1 role 1")
    tmp1 = label.currentData(role=1001)
    print ("        ", tmp1, type(tmp1))
    tmp2 = eval("{}".format(label.currentData(role=1001)))
    print ("        ", tmp2, type(tmp2))
    print ("        ", tmp2 == {'a':u'dat1 ñ', 'b':u'dat2ñ'})

    ## ~~~~  ~~~~~~


    app.exec_()




"""
~~~~~~  Change log  ~~~~~~

2012.10.16  v0.2    Added   Function currentText()

2012.08.25  v1.0            Se implementa comportamiento de selector de opciones

"""


