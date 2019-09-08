

from PyQt4 import QtCore, QtGui


class CDGrowFrame(QtGui.QFrame):

    def __init__(self, *args, **kwds):
        if kwds.has_key('orientation'):
            self.orientation = kwds['orientation']
        else:
            self.orientation = "vertical"

        if kwds.has_key('buddy'):
            self.buddy = kwds['buddy']
        else:
            self.buddy = None

        QtGui.QFrame.__init__(self, *args)


        if kwds.has_key('position'):
            self.basePos = kwds['position']
        else:
            print "default position"
            self.basePos = QtCore.QPoint(250, 250)

        self.timeLine = QtCore.QTimeLine(300)

        self.status = None

        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("frameChanged(int)"), self.frameChanged)
        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("finished()"), self.finished)



    def initialize(self):
        self.timeLine.setFrameRange(0, self.size().height());
        size = self.size()
        size.setHeight(0)
        self.resize(size)


    def start(self):
        print "start()"
        print self.parent().size()
        x = self.basePos.x() + self.buddy.size().width()/2 - self.size().width()/2
        if x < 0:
            x = 0
        elif x + self.size().width() > self.parent().size().width():
            x = self.parent().size().width() - self.size().width()
        y = self.basePos.y() + self.buddy.size().height()/2

        self.move(QtCore.QPoint(x, y))
        if self.status is None:
            self.timeLine.setDirection(QtCore.QTimeLine.Forward)
        else:
            self.timeLine.setDirection(QtCore.QTimeLine.Backward)

        self.timeLine.start()


    def frameChanged(self, index):
        pos = self.pos()
        size = self.size()
        if self.orientation == "vertical":
            y = self.basePos.y() - index / 2
            if y < 0:
                y = 0
            pos.setY(y)
            size.setHeight(index)
        else:
            self.setMaximumSize(QtCore.QSize(self.parameter - index, 16777215))
        self.move(pos)
        self.resize(size)


    def finished(self):
        if self.status is None:
            self.status = 0
        else:
            self.status = None


    # def paintEvent(self, event):
        # print "paintEvent()"
        # pos = self.basePos
        # size = self.size()
        # if self.orientation == "vertical":
            # pos.setY(pos.y - index / 2)
            # size.setHeight(index)
        # else:
            # self.setMaximumSize(QtCore.QSize(self.parameter - index, 16777215))

        # self.move(pos)
        # self.resize(size)


