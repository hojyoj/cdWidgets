# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##           Filename Review Widget            ##
 ##                                             ##
 ##                                             ##
 ##              from Basiq Series              ##
 ##           by Críptidos Digitales            ##
 ##                 GPL (c)2008                 ##
  ##                                            ##
    ##############################################

"""
"""

from PyQt4 import QtCore, QtGui

from cdWidgets import cdComboBox
from cdWidgets import cdLineEdit
from cdWidgets import cdDateEdit



class CDFilenameReview(QtGui.QFrame):

    def title_get(self):
        return self._title
    def title_set(self, value):
        if self._title is None:
            self._title = QtGui.QLabel(self)
            self.layout().insertWidget(0)
        self._title.setText(value)
    title = property(title_get, title_set)


    def __init__(self, *args, **kwds):
        title = kwds.pop('title', '')
        
        QtGui.QFrame.__init__(self, *args, **kwds)
        
        layout = QtGui.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(4, 0, 4, 4)

        self.title = QtGui.QLabel(title, self)
        self.title.setStyleSheet("""color:#604020; background-color:rgba(0,0,0,0); border:0;""")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setMargin(3)
        self.title.setFont(font)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)

        layout.addWidget(self.title)


        
        self.cerFileLYFR = QtGui.QFrame(self.cerFileFR)
        self.cerFileLYFR.setStyleSheet(_fromUtf8("border:0;"))
        self.cerFileLYFR.setObjectName(_fromUtf8("cerFileLYFR"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.cerFileLYFR)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cerFileED = QtGui.QLineEdit(self.cerFileLYFR)
        self.cerFileED.setObjectName(_fromUtf8("cerFileED"))
        self.horizontalLayout.addWidget(self.cerFileED)
        self.cerFileBU = QtGui.QPushButton(self.cerFileLYFR)
        self.cerFileBU.setMaximumSize(QtCore.QSize(32, 16777215))
        self.cerFileBU.setObjectName(_fromUtf8("cerFileBU"))
        self.horizontalLayout.addWidget(self.cerFileBU)
        self.verticalLayout.addWidget(self.cerFileLYFR)
        self.verticalLayout_6.addWidget(self.cerFileFR)
