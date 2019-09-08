# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##                Review Widget                ##
 ##                                             ##
 ##                                             ##
 ##              from Basiq Series              ##
 ##           by Criptidos Digitales            ##
 ##                 GPL (c)2008                 ##
  ##                                            ##
    ##############################################

"""
"""

from __future__ import print_function

__version__ = "0.1.1"


## Enable for testing (adds parent directory)
# import os, sys
# sys.path.append(os.getcwd()[:os.getcwd().rfind('\\')])


from PyQt4 import QtCore, QtGui


from cdWidgets import cdComboBox
from cdWidgets import cdLineEdit
from cdWidgets import cdDateEdit


class CDReviewWidget(QtGui.QFrame):

    def clear(self):
        self.editWidget.clear()
        

    _emptyAllowed = True
    def emptyAllowed_get(self):
        return self._emptyAllowed
    def emptyAllowed_set(self, value=True):
        self._emptyAllowed = value
        # self.update()
    messagePrefix = property(emptyAllowed_get, emptyAllowed_set)

    _extension = u'*.*'
    def extension_get(self):
        return self._extension
    def extension_set(self, value):
        self._extension = value
    extension = property(extension_get, extension_set)
    
    _messagePrefix = u""
    def messagePrefix_get(self):
        return self._messagePrefix
    def messagePrefix_set(self, value):
        # print "CDLineEdit.setMessagePrefix()"
        self._messagePrefix = value
        # self.update()
    messagePrefix = property(messagePrefix_get, messagePrefix_set)

    _MODES = [205, 203]
    VIEW, EDIT = _MODES
    _mode = None
    def mode_get(self):
        raise ValueError('Deprecated, must use function mode_is')
    def mode_set(self, value):
        """Adds init routines"""
        if value in self._MODES:
            self._mode = value
            if self.mode_is(self.EDIT):
                self.viewWidget.hide()
                self.editWidget.show()
            elif self.mode_is(self.VIEW):
                self.viewWidget.show()
                self.editWidget.hide()
        else:
            raise ValueError('Invalid value for mode: {}'.format(value))
    mode = property(mode_get, mode_set)

    def mode_is(self, value):
        """Adds validity check"""
        if value in self._MODES:
            return self._mode is value
        else:
            raise ValueError('Invalid value for mode')


    def initialText_get(self):
        return self.editWidget.inititalText()
    def inititalText_set(self, value):
        self.editWidget.setInitialText(value)
    initialText = property(initialText_get, inititalText_set)


    def text_get(self):
        return self.editWidget.text()
    def text_set(self, value):
        self.editWidget.setText(value)
        self.viewWidget.setText(value)
    text = property(text_get, text_set)


    def title_get(self):
        return self._title.text()
    def title_set(self, value):
        if self._title is None:
            self._title = QtGui.QLabel(self)
            self.layout().insertWidget(0)
        self._title.setText(value)
    title = property(title_get, title_set)


    # _viewWidget = QtGui.QLabel()
    @property
    def viewWidget(self):
        return self._viewWidget

    # _editWidget = QtGui.QLineEdit()
    def editWidget_get(self):
        return self._editWidget
    def editWidget_set(self, widget):
        self.layout().removeWidget(self._editWidget)
        self._editWidget = widget
        self.layout().addWidget(self._editWidget)
    editWidget = property(editWidget_get, editWidget_set)

    _editKind = 'ED'
    def editKind_get(self):
        return self._editKind
    def editKind_set(self, value):
        self._editKind = value
    editKind = property(editKind_get, editKind_set)

    def getOrientation(self):
        return self._orientation
    def setOrientation(self, value):
        self._orientation = value
    orientation = property(getOrientation, setOrientation)
    
    def orientationIs(self, value):
        return value == self._orientation


    def __init__(self, *args, **kwds):
        title = kwds.pop('title', '')
        self.editKind = kwds.pop('kind', 'ED')
        
        self._orientation = "vertical"

        QtGui.QFrame.__init__(self, *args)

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        font.setPointSize(9)

        layout = QtGui.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(4, 0, 4, 4)

        self._title = QtGui.QLabel(title, self)
        self._title.setStyleSheet("""color:#604020; background-color:rgba(0,0,0,0); border:0;""")
        self._title.setAlignment(QtCore.Qt.AlignCenter)
        self._title.setMargin(3)
        self._title.setFont(font)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._title.sizePolicy().hasHeightForWidth())
        self._title.setSizePolicy(sizePolicy)

        layout.addWidget(self._title)

        self._viewWidget = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._viewWidget.sizePolicy().hasHeightForWidth())
        self._viewWidget.setSizePolicy(sizePolicy)
        # self._viewWidget.setStyleSheet("""background-color:#F0F0F0; border-top:1 solid #A0A0A0; border-right:1 solid #F8F8F8; border-bottom:1 solid #F8F8F8; border-left:1 solid #A0A0A0;""")
        self._viewWidget.setStyleSheet("""background-color:#F0F0F0; border:1 solid #E0E0E0;""")

        layout.addWidget(self.viewWidget)

        if self.editKind == 'ED':
            self._editWidget = cdLineEdit.CDLineEdit(self)
            layout.addWidget(self.editWidget)
        elif self.editKind == 'CB':
            self._editWidget = cdComboBox.CDComboBox(self)
            layout.addWidget(self.editWidget)
        elif self.editKind == 'DA':
            self._editWidget = cdDateEdit.CDDateEdit(self)
            layout.addWidget(self.editWidget)
        elif self.editKind == 'FN':
            self.LYFR = QtGui.QFrame(self)
            self.LYFR.setStyleSheet("border:0;")
            self.LYFRLY = QtGui.QHBoxLayout(self.LYFR)
            self.LYFRLY.setSpacing(0)
            self.LYFRLY.setMargin(0)
            
            self._editWidget = cdLineEdit.CDLineEdit(self.LYFR)
            self._editWidget.setText('')
            self.LYFRLY.addWidget(self.editWidget)
            
            self.BU = QtGui.QPushButton(self.LYFR)
            self.BU.setText('...')
            self.BU.setMinimumSize(QtCore.QSize(32, 32))
            self.LYFRLY.addWidget(self.BU)

            self.connect(self.BU, QtCore.SIGNAL('clicked()'), self.selectPath)
            
            layout.addWidget(self.LYFR)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._editWidget.sizePolicy().hasHeightForWidth())
        self._editWidget.setSizePolicy(sizePolicy)
        self._editWidget.setStyleSheet("""background-color:#F0F0F0; border-top:1 solid #A0A0A0; border-right:1 solid #F8F8F8; border-bottom:1 solid #F8F8F8; border-left:1 solid #A0A0A0;""")

        self.mode = self.EDIT
        
        self.connect(self.editWidget, QtCore.SIGNAL('editingFinished()'), self.editingFinished)
        self.connect(self.editWidget, QtCore.SIGNAL('currentIndexChanged(int)'), self.currentIndexChanged)

        # self.setStyleSheet("background-color:#FF0000;")


    def currentIndexChanged(self, index):
        self.emit(QtCore.SIGNAL('currentIndexChanged(int)'), index)
        
    def editingFinished(self):
        self.emit(QtCore.SIGNAL('editingFinished()'))
        

    def selectPath(self):
        # print("CDReviewFrame.selectPath()")
        
        filename = QtGui.QFileDialog.getOpenFileName(self, u"Empresa Básica - Seleccione ", '/', self.extension)
        
        if filename:
            self.editWidget.setText(filename)
        
            self.emit(QtCore.SIGNAL('fileSelected()'))
        

    def setData(self, data):
        self.viewWidget.setText(u"{}".format(data))
        if self.editKind == 'ED':
            self.editWidget.setText(data)
        elif self.editKind == 'CB':
            if type(data) == list:
                self.editWidget.clear()
                for item in data:
                    self.editWidget.addItem(item['name'], item['code'])
            else:
                self.editWidget.setCurrentData(data)
        elif self.editKind == 'DA':
            self.editWidget.setDate(data)
        elif self.editKind == 'FN':
            self.editWidget.setText(data)
    
    @property
    def data(self):
        if self.editKind is 'DA':
            return self.editWidget.date()
        elif self.editKind == 'ED':
            return self.editWidget.text()
        elif self.editKind == 'CB':
            return self.editWidget.currentData()
        elif self.editKind == 'FN':
            return self.editWidget.text()
        else:
            return


    def setFont(self, titleFont, dataFont=None):
        self.title.setFont(titleFont)
        if dataFont:
            self.viewWidget.setFont(dataFont)
            self.editWidget.setFont(dataFont)


    def setStyleSheet(self, style, style2=None):
        QtGui.QFrame.setStyleSheet(self, style)
        if style2:
            self.viewWidget.setStyleSheet(style2)
            # self.editWidget.setStyleSheet(style2)


if __name__=='__main__':
    """ Usage Example
        and tests
    """
    
    
    aplicacion=QtGui.QApplication(sys.argv)
    
    mainView = QtGui.QWidget(None)
    layout = QtGui.QVBoxLayout(mainView)


    test = CDReviewFrame(mainView, kind='DA', title='Testing')


    layout.addWidget(test)

    mainView.show()
    
    aplicacion.exec_()





"""
  ~~~~  Change log  ~~~~
  2014.04.23        Fixed .data returning None


"""