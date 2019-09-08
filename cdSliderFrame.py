# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##                 Slide Frame                 ##
 ##                   module                    ##
 ##                                             ##
 ##              from Basiq Series              ##
 ##           by Críptidos Digitales            ##
 ##                 GPL (c)2008                 ##
  ##                                            ##
    ##############################################

"""
"""

from PyQt4 import QtCore, QtGui

from cdWidgets import cdFrame





class Form(cdFrame.CDFrame):
    
    def __init__(self, *args, **kwds):
        
        cdFrame.CDFrame.__init__(self, *args, **kwds)

        self.body = cdFrame.CDFrame(self)
        self.body.setObjectName("body")
        self.body.setStyleSheet("#body{color:#600AFF; background-color:QLinearGradient(x1:1, y1:0, x2:0, y2:0, stop:0 #ECE0D0, stop:.09 #C6A78B, stop:1 #C6A78B ); border:0px;}")

        if self.orientation in ['left', 'right']:
            self.body.orientation = 'horizontal'

        self.bodyLY = QtGui.QVBoxLayout(self.body)
        self.bodyLY.setSpacing(0)
        self.bodyLY.setContentsMargins(0, 6, 6, 6)

        self.spacerTop = QtGui.QFrame(self.body)
        self.spacerTop.setStyleSheet("background-color:rgba(255,0,0,0);")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacerTop.sizePolicy().hasHeightForWidth())
        self.spacerTop.setSizePolicy(sizePolicy)

        self.bodyLY.addWidget(self.spacerTop)

        self.spacerBottom = QtGui.QFrame(self.body)
        self.spacerBottom.setStyleSheet("background-color:rgba(255,0,0,0);")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacerBottom.sizePolicy().hasHeightForWidth())
        self.spacerBottom.setSizePolicy(sizePolicy)

        self.bodyLY.addWidget(self.spacerBottom)


        self.lockFR = QtGui.QFrame(self.body)
        self.lockLY = QtGui.QVBoxLayout(self.lockFR)
        self.lockLY.setContentsMargins(0, 0, 6, 0)

        self.lockRB = QtGui.QRadioButton(u'Bloquear', self.lockFR)
        self.lockLY.addWidget(self.lockRB)

        self.bodyLY.addWidget(self.lockFR)

        self.connect(self.lockRB, QtCore.SIGNAL('toggled(bool)'), self.lock_toggled)

        self.handle = QtGui.QFrame(self)

        self.handle.setMinimumSize(QtCore.QSize(10, 0))
        self.handle.setMaximumSize(QtCore.QSize(10, 16777215))
        self.handle.setStyleSheet("background-color:QLinearGradient(x1:1, y1:0, x2:0, y2:0, stop:0 #C6A78B, stop:1 #A78260); border:0px; border-top-left-radius:6px; border-bottom-left-radius:6px;")
        self.handle.setFrameShape(QtGui.QFrame.StyledPanel)
        self.handle.setFrameShadow(QtGui.QFrame.Raised)
        
        if self.orientation is 'right':
            layout = QtGui.QHBoxLayout(self)
            layout.addWidget(self.body)
            layout.addWidget(self.handle)
        elif self.orientation is 'left':
            layout = QtGui.QHBoxLayout(self)
            layout.addWidget(self.handle)
            layout.addWidget(self.body)
        elif self.orientation is 'up':
            layout = QtGui.QVBoxLayout(self)
            layout.addWidget(self.body)
            layout.addWidget(self.handle)
        elif self.orientation is 'down':
            layout = QtGui.QVBoxLayout(self)
            layout.addWidget(self.handle)
            layout.addWidget(self.body)

        layout.setSpacing(0)
        layout.setMargin(0)

        self.connect(self, QtCore.SIGNAL('entered()'), self.stretch)
        self.connect(self, QtCore.SIGNAL('leaved()'), self.shrink)
        # self.connect(self.ui.controlLockRB, QtCore.SIGNAL('toggled(bool)'), self.controlMenu_toggledLock)

        # self.parent().layout().addWidget(self)


    def init(self):
        pass


    def widget_add(self, widget, style=''):
        """        slideMenu.widget_add()"""

        no = " border-top-left-radius:0;"
        ne = " border-top-right-radius:0;"
        se = " border-bottom-right-radius:0;"
        so = " border-bottom-left-radius:0;"

        if self.orientation == 'right':
            ne = " border-top-right-radius:6;"
            se = " border-bottom-right-radius:6;"

        style = "{}{}{}{}{}".format(style, no, ne, se, so)

        # item.setStyleSheet(style)

        self.bodyLY.insertWidget(self.bodyLY.count()-1, widget)

        # self.ui.buttonsFR.layout().itemAt(self.ui.buttonsFR.layout().count()-1).widget().setStyleSheet(style)

        # self.setStyleSheet(self.style)


    def addSpacing(self, *args):
        self.bodyLY.addSpacing(*args)
        
        
    def addWidget(self, widget):
        self.body.layout().insertWidget(self.body.layout().count()-2, widget)
        
    def contents_clear(self):
        pass

    def lock_hide(self, hide=True):
        if hide:
            self.lockRB.hide()
        else:
            self.lockRB.show()

    def lock_toggled(self, value):

        # self.app.optionsMenu_isLocked = value
        if value:
            self.lockRB.setText('Bloqueado')
        else:
            self.lockRB.setText('Bloquear')
        # self.app.mainMenu_isLocked = value


    def lock_set(self, value=True):
        self.lockRB.setChecked(value)
        # if value:
            # self.lockRB.setText('Bloqueado')
        # else:
            # self.lockRB.setText('Bloquear')


    def stretch(self):
        # print("    cdSliderFrame.show()")
        if self.body.isHidden():
            self.body.showGradual()
            # self.ui.mainMenuLYFR.showGradual(40)
        # print("    cdSliderFrame.show() - END")


    def shrink(self):
        # print("    cdSliderFrame.hide()")
        if not self.lockRB.isChecked():
            if not self.body.isHidden():
                self.body.hideGradual()
                # self.ui.mainMenuLYFR.hideGradual(40)
        # print("    cdSliderFrame.hide() - END")
        

