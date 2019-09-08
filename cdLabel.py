# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   cdLabel                                    ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   (c)2008                                    ##
  ##                                             ##
    ###############################################

from PyQt4 import QtCore, QtGui




class CDLabel(QtGui.QLabel):

    _initialText = ''

    def __init__(self, *args, **kwds):

        # self._initialText = args[0]

        self._rotation = kwds.pop('rotation', 0)

        QtGui.QLabel.__init__(self, *args)

        self._origin = QtCore.QPoint(0,0)
        self._orientation = 'right'



    def event(self, evt):
        #Double click causes QTouchEvent to be sent
        if evt.type() == QtCore.QEvent.MouseButtonDblClick:
            self.emit(QtCore.SIGNAL('doubleClicked()'))
        return QtGui.QLabel.event(self, evt)


    def enterEvent(self, event):
        self.emit(QtCore.SIGNAL('entered()'))

    @property
    def initialText(self):
        return self._initialText


    def isModified(self):
        return self.text() != self.initialText


    def leaveEvent(self, event):
        self.emit(QtCore.SIGNAL('leaved()'))

    def mouseReleaseEvent(self, event):
        self.emit(QtCore.SIGNAL('clicked()'))

    def paintEvent(self, event):    # print "CDLabel.paintEvent()"
        if self._rotation:
            # self.setMaximumWidth(QtGui.QFontMetrics(self.font()).height()+6)

            painter = QtGui.QPainter(self)
            painter.translate((self.width()+QtGui.QFontMetrics(self.font()).height())/2-QtGui.QFontMetrics(self.font()).descent()-1, (self.height()+QtGui.QFontMetrics(self.font()).width(self.text()))/2)

            painter.rotate(self._rotation)
            painter.drawText(self._origin, self.text())

        elif self._orientation == 'up':
            # self.setMaximumWidth(QtGui.QFontMetrics(self.font()).height()+6)

            if not self.minimumWidth():
                self.setMinimumWidth(10)

            painter = QtGui.QPainter(self)

            painter.translate(
            ( self.width() - QtGui.QFontMetrics(self.font()).height() - QtGui.QFontMetrics(self.font()).descent() ) / 2 + 1,
            ( self.height() + QtGui.QFontMetrics(self.font()).width(self.text())) / 2
            )
            # painter.translate(
            # self.width() / 2 - QtGui.QFontMetrics(self.font()).descent() - 1,
            # ( self.height() + QtGui.QFontMetrics(self.font()).width( self.text() ) ) / 2
            # )

            painter.rotate(270)
            painter.drawText(QtCore.QRect(0, 0, self.height(), self.width()), 0, self.text())
            painter.end()

            #~ self.setMaximumWidth(QtGui.QFontMetrics(self.font()).height())

            #~ self.updateGeometry()
            #~ self.setAlignment(QtCore.Qt.AlignHCenter)

            #~ print 'xxx', self.width()
            #~ print self.sizeHint()

        elif self._orientation == 'down':
            # self.setMaximumWidth(QtGui.QFontMetrics(self.font()).height()+6)
            self.setMinimumWidth(10)

            painter = QtGui.QPainter(self)
            painter.translate((self.width()-QtGui.QFontMetrics(self.font()).height())/2+QtGui.QFontMetrics(self.font()).descent()+1, 0)

            painter.rotate(90)
            painter.drawText(0, 0, self.text())
        else:
            painter = QtGui.QPainter(self)

            # print (789), self.alignment() and QtCore.Qt.Left

            # self.setAlignment(QtCore.Qt.AlignHCenter)

            painter.translate((self.width()-QtGui.QFontMetrics(self.font()).width(self.text()))/2, (self.height()+QtGui.QFontMetrics(self.font()).height())/2-QtGui.QFontMetrics(self.font()).descent()-1)
            painter.drawText(0, 0, self.text())


    def orientation(self):
        return self._orientation
    def setOrientation(self, value):
        self._orientation = value


    def origin(self):
        return self._origin
    def setOrigin(self, value):
        self._origin = value


    def rotation(self):
        return self._rotation
    def setRotation(self, value):
        self._rotation = value


    # def sizeHint(self):
        # return QtCore.QSize(0,0)


    def setText(self, value, initialToo=False):
        QtGui.QLabel.setText(self, value)
        if initialToo:
            self._initialText = self.text()

