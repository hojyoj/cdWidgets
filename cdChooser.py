# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Slide Selector with validation             ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2008-2012                           ##
  ##                                             ##
    ###############################################

"""
"""

__version__ = '0.1'

import sys
from PyQt4 import QtCore, QtGui


# Resource object code
#
# Created: mar 7. may 18:08:42 2013
#      by: The Resource Compiler for PyQt (Qt v4.7.2)
#
# WARNING! All changes made in this file will be lost!


qt_resource_data = b"\
\x00\x00\x02\x68\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x22\x00\x00\x00\x40\x08\x06\x00\x00\x00\x7f\x7b\xa5\x93\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\x00\x00\x00\x00\x00\xf9\x43\
\xbb\x7f\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xdd\x05\x07\x14\x15\x33\xa4\x09\x9e\x36\x00\x00\x00\x1d\x69\x54\
\x58\x74\x43\x6f\x6d\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x43\x72\
\x65\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x47\x49\x4d\x50\x64\
\x2e\x65\x07\x00\x00\x01\xcc\x49\x44\x41\x54\x68\xde\xdd\x99\x4d\
\x6e\x83\x30\x10\x85\xdf\x90\x0b\x54\x8a\x7a\x90\x6c\x7a\x82\xdc\
\xa7\x87\x81\x43\x24\x67\x08\xca\x01\xba\xc9\x11\xba\x2f\x42\xe2\
\x02\xe8\x75\x43\x23\x42\xc1\x78\xfc\x83\x2d\x46\xf2\xce\x32\x1f\
\x33\xcf\xc3\xc3\x06\x12\x05\xc9\x92\xa3\x48\xfa\xf0\xcd\x41\x48\
\x7e\x72\x25\x92\x65\x60\x1a\x12\x11\x42\xf5\x96\x92\x03\x44\x14\
\x10\xd7\x7a\x4b\x0e\x10\x41\x41\x7c\x95\x2f\x39\x40\x04\x01\x09\
\xd5\x03\x24\x07\x08\x00\x28\x36\xdd\xa2\x22\x7f\xa3\x0a\x26\x4c\
\x4d\x00\x98\x1b\xa5\x57\x67\x55\x64\xa2\x15\x91\x07\x80\xb3\x61\
\x2d\x37\x8d\x68\xca\x21\x22\x3d\x80\x0e\xc0\x31\x28\x88\x12\xc2\
\x76\x4d\x9d\x58\x23\x40\x34\x00\xaa\x68\xc2\x5c\x10\xe5\xdc\xb8\
\xa8\x6c\x40\xec\x72\x58\x35\xb4\x2d\x21\x16\x41\xb6\x86\x98\x05\
\x49\x01\xf1\x0f\x24\x15\xc4\xcb\xf6\x25\x79\x49\x05\xf1\x92\x11\
\x92\x3f\x00\xde\x53\x40\x3c\x33\x42\xb2\x4c\x09\xf1\xcc\x88\x8d\
\x36\x44\xa4\x06\x70\x32\x7d\x3b\x5c\x21\xb4\x7e\xe4\x04\xe0\xcd\
\xd4\xb6\x7d\x7c\x52\x61\x21\xd2\x76\xc8\xc6\x11\xc0\xc1\x30\xef\
\xee\x65\x15\x2d\x44\xda\x8b\x48\x17\xab\x24\x63\x10\x86\x10\xa9\
\x2f\x48\x81\x4c\x22\x14\x48\x0f\xa0\xf5\x05\xb9\x5a\x98\x98\xb5\
\x39\xdd\xe0\x4f\xfd\xfe\x6b\x72\xd0\x89\xa6\x34\xf5\x5a\xfa\x6d\
\x3b\xaf\x09\xa4\xb2\x78\xdb\xb5\x86\xe6\x05\x23\x5a\x0b\x10\xf5\
\xa3\x37\xc4\x35\xe4\x03\xb4\x99\xc9\xc6\x18\xe5\x69\x15\xb3\x32\
\xcf\xa9\x60\x0a\xc3\xe2\x9a\xff\x62\x5b\xe0\x46\x44\xae\x4e\x27\
\x46\x11\x32\xd3\x02\x78\x90\x3c\xab\x8f\xae\x02\xc3\xf4\x00\x3a\
\x92\x47\x75\x8b\x77\x2c\x53\xb3\x30\xe5\x30\x67\xb2\x0a\xc5\x9b\
\x6a\x61\x4c\xd6\xf1\x4b\xad\x11\x9f\x32\x2d\x94\xaa\x01\xf0\x4d\
\xf2\xc3\xcb\x18\x89\xb2\x77\x93\x9c\xee\xaa\xfb\x14\xc2\x29\x23\
\xae\x99\x71\xea\xac\x29\x60\xf6\x71\x04\x1e\x12\x66\x5f\xd7\x24\
\x21\x60\xf6\x79\x95\xe6\x03\x93\xcd\x75\x6b\xb4\x7f\xdf\xa1\x03\
\xd7\xc8\x29\x48\x5e\x92\x5e\xc9\xcf\x00\x95\x59\x80\x4c\xa0\x6e\
\x63\x90\x5f\x86\xea\x7c\x73\x9a\x04\x06\xc3\x00\x00\x00\x00\x49\
\x45\x4e\x44\xae\x42\x60\x82\
\x00\x00\x02\x77\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x22\x00\x00\x00\x40\x08\x06\x00\x00\x00\x7f\x7b\xa5\x93\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\x00\x00\x00\x00\x00\xf9\x43\
\xbb\x7f\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xdd\x05\x07\x14\x15\x1e\xe1\xd6\xc2\x43\x00\x00\x00\x1d\x69\x54\
\x58\x74\x43\x6f\x6d\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x43\x72\
\x65\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x47\x49\x4d\x50\x64\
\x2e\x65\x07\x00\x00\x01\xdb\x49\x44\x41\x54\x68\xde\xcd\x9a\xc1\
\x6d\xc3\x30\x0c\x45\x3f\xe9\x05\x0c\x04\xed\x1e\xb9\x74\x82\xee\
\xd0\x31\x3a\x4c\x32\x44\x32\x43\x8d\x0e\xd0\x4b\x06\x31\x0c\x74\
\x81\x82\xbd\x28\x85\x1b\xc8\xb6\x24\x52\x32\x09\xe4\x94\x38\x7e\
\x11\xbf\xc9\x2f\x2a\x90\xff\x71\xc2\x5e\x21\xcb\x71\xf2\x02\x72\
\x8f\x77\x2f\x20\x4d\x56\x88\x44\x44\xb2\x2e\x20\xa2\x1a\x20\x5c\
\xb2\x82\x2e\x40\x6a\xc1\xb0\x46\x5b\x2e\x40\xac\x61\xd8\xe2\xa9\
\x73\x01\x62\x05\xc3\x56\x4b\xab\x85\xe1\x48\x9d\x38\x13\x11\x4a\
\xca\x85\x0a\x66\x5e\x3a\x01\x9c\x00\xc8\xe3\x2b\x37\xd4\x95\x75\
\x63\x15\x06\x11\x39\x02\x38\xd4\xa8\xc0\x39\x20\x13\x80\x5e\x44\
\xba\x1a\xed\x20\x07\x64\x9e\x4e\xf3\xde\xf4\x28\xd6\x33\x80\x31\
\xe1\xcb\xed\x05\x1c\x11\xda\x25\x26\x58\xad\x88\x8b\x6d\x40\xeb\
\x34\xb1\xf6\x06\x56\x69\x62\x8b\x5f\x6b\x01\xc3\x56\x4b\xaf\x85\
\x61\x4b\x1d\x68\x60\x38\xe3\xc2\x1a\x30\x17\x8d\x79\xb6\x04\x1f\
\x89\xe8\xb9\xd4\x3c\x5b\x02\x3f\xdd\xb7\x29\x54\xdc\x2d\xb7\x6f\
\x34\x01\xb8\x89\xc8\x6b\x4a\x7d\xd1\x98\x67\x6c\xb4\x83\x1e\xc0\
\xb1\x95\x43\xfb\x5c\x79\xaf\x03\x70\x20\xa2\x21\xac\xce\xaa\x68\
\x49\x6b\xf1\x52\x52\x24\x22\x7d\x00\x5b\x16\x6d\x03\x90\x24\x81\
\x9b\x99\xe7\xbd\x5d\xfc\x04\xe0\x67\x77\x10\x22\xba\x01\xf8\xde\
\xf8\xd8\x35\xc1\x6c\x5d\x55\x1a\xb1\xd2\x87\xaa\x8e\x24\x16\xb4\
\xa1\x6a\x6a\x12\xcb\x77\x1f\xb6\x1f\x5b\x71\xf6\xd0\xf4\xfe\xec\
\x23\xef\x09\x11\x84\x9c\x67\x03\x6a\x9b\x69\xf6\x00\x91\x04\xd2\
\x6a\x5b\xc1\x1e\x20\x16\x41\x88\xe8\x4a\x44\x63\x2b\x88\xa8\x58\
\x83\x7f\x48\x1a\x3f\x58\x6e\xc6\x63\x20\x53\x70\x57\x5d\xcb\x89\
\x40\x2c\x35\x87\x15\x88\xb1\xd5\x58\x02\x00\xbe\xd6\xac\x61\x0d\
\x88\xb5\xa7\x66\x8c\xa5\x42\x44\xde\x6a\x40\x44\x41\x44\xe4\x65\
\x6e\x8a\x03\x40\x6e\x53\xcc\x1e\x49\x92\xf5\x4c\xbd\xf4\x18\x85\
\x3d\x40\x98\x82\x68\x0f\x94\xd8\x03\x84\x09\x88\xd5\xd1\x1a\x7b\
\x80\x50\x81\x58\x1f\x32\xb2\x07\x88\x22\x10\x0f\xc7\xad\x43\x2d\
\x88\x7b\x09\xdf\x8a\x4b\x93\x5d\xb8\xd7\x3f\x29\x7c\xec\x35\x96\
\xf8\x05\xfb\x9e\x4d\x45\xe0\x2c\x6a\x70\x00\x00\x00\x00\x49\x45\
\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x0b\
\x02\x99\x2c\x07\
\x00\x4c\
\x00\x65\x00\x66\x00\x74\x00\x5f\x00\x30\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x0c\
\x09\x2f\xe8\x07\
\x00\x52\
\x00\x69\x00\x67\x00\x68\x00\x74\x00\x5f\x00\x30\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x01\x00\x00\x02\x6c\
"




def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)



class CDChooser(QtGui.QFrame):
    """ Widget that allows selection of one or more options from a list,
        displaying all options selected, horizontally or vertically.
    """

    def __init__(self, *args, **kwds):

        QtGui.QFrame.__init__(self, *args)

        self.setObjectName('Form')
        self.setStyleSheet('background-color:#FFFFFF;')
        
        LY = QtGui.QHBoxLayout(self)
        
        LY.setSpacing(0)
        LY.setMargin(0)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.frame = QtGui.QFrame(self)
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setStyleSheet('background-color:#FFFFFF;')

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        
        self.frame.setSizePolicy(sizePolicy)
        # self.frame.setFrameShape(QtGui.QFrame.Panel)
        # self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        # self.frame.setStyleSheet('background-color:#FF00FF;')

        self.frameLY = QtGui.QHBoxLayout(self.frame)
        self.frameLY.setSpacing(0)
        self.frameLY.setMargin(0)

        LY.addWidget(self.frame)
        

        self.BU = QtGui.QPushButton(self)
        self.BU.setFlat(True)
        self.BU.setStyleSheet('background-color:#FFFFFF;')
        self.BU.setBaseSize(32, 32)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BU.sizePolicy().hasHeightForWidth())
        self.BU.setSizePolicy(sizePolicy)
        
        self.BU.setText('')
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/Plus.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BU.setIconSize(QtCore.QSize(36, 36))
        self.BU.setIcon(icon)
        
        LY.addWidget(self.BU)

        self.connect(self.BU, QtCore.SIGNAL('clicked()'), self.add)


        self.list = ListWidget()
        self.list.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.connect(self.list, QtCore.SIGNAL('currentRowChanged(int)'), self.listCurrentRowChanged)

        

    def add(self, data=None, initialToo=False):
        # print("""CDChooser.add()""")
        # print(data, initialToo)
        
        label = HoverLabel(master=self)
        label.master = self
        
        label.dataCurrent_set(data, initialToo)
        
        self.frame.layout().addWidget(label)

        # print("""CDChooser.add() - END""")


    def clear(self):
        # print("""CDChooser.clear()""")
        # print(self.frame.layout().count())
        
        index = 1
        while index:
            if self.frame.layout().count() > index:
                label = self.frame.layout().itemAt(index).widget()
                self.frame.layout().removeWidget(label)
                label.setParent(None)
                del label
            elif self.frame.layout().count() == index:
                self.frame.layout().itemAt(0).widget().clear()                
                index -= 1
            elif self.frame.layout().count() < index:
                self.add()
                index = 0
        
        # print("""CDChooser.clear() - END""")
    
    
    _initialIndex = -1
    _currentIndex = -1
    def currentIndex(self):
        return self._currentIndex
    def setCurrentIndex(self, value, initialToo=False):
        if initialToo:
            self._initialIndex = self._currentIndex
        while self._currentIndex < value:
            self.moveLeft()


    def listCurrentRowChanged(self, row):
        # print("""CDChooser.listCurrentRowChanged()""")
        
        self.current.update()
        
        self.emit(QtCore.SIGNAL("changed()"))
        # print("""CDChooser.listCurrentRowChanged() - END""")
    
    
    def close(self):
        self.list.close()
        

    def text(self, index=None):
        
        if index is None:
            if self._currentIndex + 1:
                return self._names[self._currentIndex]
            else:
                return None
        else:            
            return self._names[index]
        

    def count(self):
        return len(self._names)

    _data = []
    _names = []
    def data(self):
        self._data = []
        for index in range(self.frame.layout().count()):
            label = self.frame.layout().itemAt(index).widget()
            if label.index_current > -1:
                self._data.append(self.list.item(label.index_current).dat)
        return self._data
    def setData(self, names, data = []):
        self.clear()
        self._names = names
        self._data = data
        self.emit(QtCore.SIGNAL('changed()'))

    current = None


    def modifiedData(self):
        # print("modifiedData")
        data = []
        for index in range(self.frame.layout().count()):
            label = self.frame.layout().itemAt(index).widget()
            if label.isModified:
                if label.index_current + 1:
                    data.append(self.list.item(label.index_current).dat)
                else:
                    data.append(None)
        # print("modifiedData - END")
        return data
        

    _default = None
    def default_get(self):
        return self._default
    def default_set(self, value):
        self._default = value
    defaultData = property(default_get, default_set)
        
        
    def isModified(self):
        # print "CDChooser.isModified()"
        isModified = False
        for index in range(self.frame.layout().count()):
            if self.frame.layout().itemAt(index).widget().isModified():
                
                isModified = True
        # print "CDChooser.isModified() - END"
        return isModified


    def list_set(self, data):
        
        self.list.set_data(data)        
        return
        
        
    def setFont(self, font):

        QtGui.QFrame.setFont(self, font)

        # self.leftLI.setFont(font)
        # self.rightLI.setFont(font)



class HoverLabel(QtGui.QLabel):

    index_initial = None
    index_current = None
    
    
    def __init__(self, *args, **kwds):
        
        self.master = kwds.pop('master', None)
        
        QtGui.QLabel.__init__(self, *args, **kwds)
        
        self.setStyleSheet('border:1 inset #A0A0A0;')
        
        # self.connect(self.master.list, QtCore.SIGNAL('itemSelectionChanged()'), self.update)


    def clear(self):
        if self.master.defaultData:
            self.dataCurrent_set(self.master.defaultData, initialToo=True)
        else:
            self.index_initial = -1
            self.index_current = -1
            self.setText('')
        

    def dataCurrent_set(self, value, initialToo=False):
        # print("""HoverLabel.dataCurrent_set()""")
        found = False
        if value is None:
            self.index_current = -1
            self.setText('')
            if initialToo:
                self.index_initial = index
            found = True
        else:
            index = 0
            while index < self.master.list.count() and not found:
                if self.master.list.item(index).dat == value:
                    found = True
                    self.index_current = index
                    self.setText(self.master.list.item(index).text())
                    if initialToo:
                        self.index_initial = index
                else:
                    index += 1
        if not found:
            print ("\nERROR @ HoverLabel.dataCurent_set()\n    - not found""")
            
        # print("""HoverLabel.dataCurrent_set() - END""")
        
        
    def enterEvent(self, event):
        # print("""HoverLabel.enterEvent()""")
        self.master.current = self
        
        self.master.list.setFixedSize(QtCore.QSize(self.width(), 100))
        # self.master.list.setCurrentRow(self.index_current)
        self.master.list.show()
    
    
    def isModified(self):
        # print("""HoverLabe.isModified()""")
        # print(self.index_initial, self.index_current)
        return self.index_initial != self.index_current
        
        
    def leaveEvent(self, event):
        # print("""HoverLabel.leaveEvent()""")
        if not self.master.list.geometry().contains(self.master.cursor().pos()):      
            self.master.list.hide()
        

    def mousePressEvent(self, event):
        # print("""HoverLabel.mousePressEvent()""")
        self.master.list.hide()


    def paintEvent(self, event):
        # print("""HoverLabel.paintEvent()""")        
        QtGui.QLabel.paintEvent(self, event)

        pos = self.mapToGlobal(self.parent().pos())
        pos += QtCore.QPoint(0, self.height())
        
        if self.master.current == self:
            self.master.list.move(pos)


    def update(self):
        # print("""HoverLabel.update()""")
        if self.master.current == self:
            if self.master.list.currentItem():
                self.setText(self.master.list.currentItem().text())
                self.index_current = self.master.list.currentRow()
                self.master.list.hide()
        # print("""HoverLabel.update() - END""")
        
            

class ListWidget(QtGui.QListWidget):


    def leaveEvent(self, event):
        # print("""ListWidget.leaveEvent()""")
        QtGui.QListWidget.leaveEvent(self, event)
        self.hide()


    def set_data(self, data):
        # print("""ListWidget.set_data()""")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        
        self.clear()
        
        index = 0
        
        for item in data:
            # print(item)
            
            if type(item) == list:
                listItem = QtGui.QListWidgetItem(item[0])
                listItem.dat = item[1]
            else:
                listItem = QtGui.QListWidgetItem(item)
            
            listItem.setFont(font)
        
            self.addItem(listItem)



if __name__ == '__main__':

    def update():
        label2.setText('{}'.format(chooser.currentData()))

        if chooser.currentData() == 5:

            chooser.clear()

            chooser.addItem(u'Unique option', 9)
            

    aplicacion = QtGui.QApplication(sys.argv)

    main = QtGui.QWidget(None)

    QtGui.QVBoxLayout(main)

    label = QtGui.QLabel('Prueba de CDChooser')
    label.setAlignment(QtCore.Qt.AlignCenter)
    main.layout().addWidget(label)

    chooser = CDChooser(main)
    chooser.list_set(['Opción1', 'Opción2'])
    
    main.layout().addWidget(chooser)

    label2 = QtGui.QLabel('')
    main.layout().addWidget(label2)


    main.show()


    aplicacion.exec_()


"""
    Item not selected:
        current_index = -1
        no Item available
"""