# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##           Splitter with Timeline            ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##                GPL (c)2008                  ##
  ##                                            ##
    ##############################################

"""
Adds attributes:
    message         Error messages
"""




from PyQt4 import QtCore, QtGui


class CDSlider(QtGui.QSplitter):

    def __init__(self, *args, **kwds):
        QtGui.QSplitter.__init__(self, *args)

        self.currentIndex = -1

        self.timeLine = QtCore.QTimeLine(500)
        self.timeLine.setUpdateInterval(20)
        self.timeLine.setCurveShape(QtCore.QTimeLine.EaseInOutCurve)

        self.setHandleWidth(1)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(1)
        # sizePolicy.setVerticalStretch(1)
        # self.setSizePolicy(sizePolicy)

        # self.layout = QtGui.QVBoxLayout(self)
        # self.layout.addWidget(self.splitter)
        # self.layout.setMargin(0)

        self.__mode = 'toggle'

        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("frameChanged(int)"), self.frameChanged)
        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("finished()"), self.finished)


    def addWidget(self, widget, pos=-1, show=False):
        # print "cdSlider.CDSlider.addWidget()", widget, pos, show
        self.insertWidget(pos, widget)
        if show:
            self.currentIndex = self.indexOf(widget)
        else:
            widget.hide()


    def createHandle(self):
        return Handle(QtCore.Qt.Horizontal, self)


    def finished(self):
        self.currentIndex = self.showingIndex
        try:
            self.widget(self.hiddingIndex).hide()
        except:
            pass


    def mode(self):
        return self.__mode


    def setMode(self, value):
        self.__mode = value


    def showWidget(self, widget):
        index = self.indexOf(widget)
        if index < self.count() and index != self.currentIndex:
            # print 444, self.__mode
            if self.__mode == 'toggle':
                if self.currentIndex != -1:
                    self.widget(self.currentIndex).hide()
                self.widget(index).show()
                self.currentIndex = index
            else:
                # print 777, self.widget(index).baseSize().width(), self.width(), self.maximumWidth()
                self.timeLine.setFrameRange(0, self.width())
                if index < self.currentIndex:
                    # print "forward"
                    self.timeLine.setDirection(QtCore.QTimeLine.Forward)
                    self.handleIndex = index + 1
                else:
                    # print "backward"
                    self.timeLine.setDirection(QtCore.QTimeLine.Backward)
                    self.handleIndex = self.currentIndex + 1
                self.widget(index).show()
                self.hiddingIndex = self.currentIndex
                self.showingIndex = index
                self.timeLine.start()
                self.currentIndex = index


    def currentWidget(self):
        return self.widget(self.currentIndex)


    def frameChanged(self, index):
        # print "CDSlider.frameChanged({})".format(index)
        self.moveSplitter(index, self.handleIndex)




class Handle(QtGui.QSplitterHandle):

    def mouseDoubleClickEvent(self, event):
        self.splitter().emit(QtCore.SIGNAL('doubleClicked()'))

    def mouseReleaseEvent(self, event):
        self.splitter().emit(QtCore.SIGNAL('clicked()'))


