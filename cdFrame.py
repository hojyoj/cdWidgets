

from PyQt4 import QtCore, QtGui




class CDFrame(QtGui.QFrame):

    def getOrientation(self):
        return self._orientation
    def setOrientation(self, value):
        self._orientation = value
    def orientationIs(self, value):
        return value == self._orientation
    orientation = property(getOrientation, setOrientation)


    def __init__(self, *args, **kwds):
        
        self._orientation = kwds.pop('orientation', "up")

        QtGui.QFrame.__init__(self, *args)

        self.slideStatus = 0

        self.timeLine = QtCore.QTimeLine(500)
        self.timeLine.setUpdateInterval(10)

        self.oldSize = 0

        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("frameChanged(int)"), self.sizeChanged)
        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("finished()"), self.finished)


    def enterEvent(self, event):
        # print "cdFrame.enterEvent()"
        self.emit(QtCore.SIGNAL('entered()'))

    def focusInEvent(self, event):  # print "cdWidgets.cdFrame.CDFrame.focusInEvent()"
        self.emit(QtCore.SIGNAL('gotFocus()'))

    def focusOutEvent(self, event):
        # print "cdWidgets.cdFrame.CDFrame.focusOutEvent()"
        self.emit(QtCore.SIGNAL('lostFocus()'))

    def hideGradual(self, range=1000):
        if range:
            self.timeLine.setFrameRange(0, range)
        self.sizeIn()
        # self.hide()

    def leaveEvent(self, event):
        # print "cdFrame.leaveEvent()"
        self.emit(QtCore.SIGNAL('leaved()'))

    def mouseDoubleClickEvent(self, event):
        # print "cdWidgets.cdFrame.CDFrame.mouseDoubleClickEvent()"
        self.emit(QtCore.SIGNAL('doubleClicked()'))

    def showEvent(self, event):
        # print "cdFrame.showEvent()"
        self.emit(QtCore.SIGNAL('showed()'))

    def keyPressEvent(self, event):
        # print "cdFrame.keyPressEvent()"
        # print event.key()
        if event.key()==16777220:
            # print 'emitting'
            self.emit(QtCore.SIGNAL('returnPressed()'))
        else:
        # elif event.key()==16777273:
            # self.emit(QtCore.SIGNAL('F10Pressed()'))
            QtGui.QFrame.keyPressEvent(self, event)

    def showGradual(self, range=1000):
        if range:
            self.timeLine.setFrameRange(0, range)
        self.show()
        self.sizeOut()

    def sizeIn(self):
        self.slideStatus = 1
        self.start()

    def sizeOut(self):
        self.slideStatus = 0
        self.start()

    def start(self, range=0):
        # print "cdWidgets.cdFrame.CDFrame.start(%s)" % range, self.slideStatus
        # print self.timeLine.startFrame(), self.timeLine.endFrame()
        if range:
            self.timeLine.setFrameRange(0, range)
        if self.slideStatus:
            self.setMinimumHeight(0)
            if self.orientationIs("up"):
                self.oldSize = self.height()
            else:
                self.oldSize = self.width()
            self.slideStatus = 0
            self.timeLine.setDirection(QtCore.QTimeLine.Backward)
        else:
            self.slideStatus = 1
            self.timeLine.setDirection(QtCore.QTimeLine.Forward)

        # self.timeLine.setFrameRange(0, self.range)
        self.timeLine.start()

    def sizeChanged(self, index):
        # print "cdWidgets.cdFrame.CDFrame.sizeChanged()", index, self.oldSize
        # print index

        if self.slideStatus == 0:
            if self.orientationIs("up"):
                self.setMaximumHeight(self.oldSize * index / 100 )
            else:
                self.setMaximumSize(QtCore.QSize(self.oldSize * index / 100, 16777215))
        else:
            if self.orientationIs("up"):
                self.setMaximumHeight(self.oldSize * index / 100 )
            else:
                self.setMaximumSize(QtCore.QSize(self.oldSize * index / 100, 16777215))

        self.parent().repaint()

    def finished(self):
        # print "cdWidgets.cdFrame.CDFrame.finished()"
        if self.slideStatus == 0:
            self.hide()
        else:
            self.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.emit(QtCore.SIGNAL("finished()"))


