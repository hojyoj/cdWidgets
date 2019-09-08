# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Slide Frame                                ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2011 Jun 13 19:58:19                ##
  ##  @author: - Jorge Hojyo                     ##
    ###############################################





from PyQt4 import QtCore, QtGui


class CDSlideFrame(QtGui.QFrame):

    def __init__(self, *args, **kwds):
        self.buddy = args[0]
        layout = args[1]
        if kwds.has_key('orientation'):
            self.orientation = kwds['orientation']
        else:
            self.orientation = "horizontal"
        if kwds.has_key('container'):
            self.container = kwds['container']
        else:
            self.container = None

        args = (self.buddy.parent(),)

        QtGui.QFrame.__init__(self, *args)

        layout.addWidget(self)

        if self.orientation == "vertical":
            policy = self.sizePolicy()
            policy.setVerticalStretch(0)
            self.setSizePolicy(policy)

            policy = self.buddy.sizePolicy()
            policy.setVerticalStretch(1)
            self.buddy.setSizePolicy(policy)

            self.setMaximumSize(QtCore.QSize(16777215, 0))

        elif self.orientation =="horizontal":
            self.setMaximumSize(QtCore.QSize(0, 16777215))

        self.status = None

        self.timeLine = QtCore.QTimeLine(300)
        self.timeLine.setUpdateInterval(10)

        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("frameChanged(int)"), self.frameChanged)
        QtCore.QObject.connect(self.timeLine, QtCore.SIGNAL("finished()"), self.finished)


    def finished(self):
        # print "finished()"
        if self.status == None:
            # print "status == None"
            self.buddy.setMaximumSize(QtCore.QSize(16777215, 16777215))
        else:
            # print "status != None"
            self.setMaximumSize(QtCore.QSize(16777215, 16777215))
            if self.orientation == "vertical":
                if self.buddy.size().height() != 0:
                    self.buddy.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.emit(QtCore.SIGNAL("finished()"))

    ## 1) [buddy] cubre todo y es elastico stretch(1)
    ##    [slide] esta oculto heigth(0) y esta fijo stretch(0)

    ## 2) [buddy] cubre el resto stretch(1)
    ##    [slide] cubre su minimo range=hint y esta fijo stretch(0)

    ## 3) [buddy] esta oculto heigth(0) y fijo stretch(0)
    ##    [slide] cubre todo y es elastico stretch(1)


    def start(self, range=0):
        # print "start(%s)" % range
        self.range = range
        if self.status == None:
            # print "self.status == None"
            self.status = 0
            self.timeLine.setDirection(QtCore.QTimeLine.Forward)
        else:
            # print "self.status != None"
            self.status = None
            self.timeLine.setDirection(QtCore.QTimeLine.Backward)
        self.timeLine.setFrameRange(0, range)
        self.timeLine.start()


    def frameChanged(self, index):
        if self.status == None:
            # print "self.status == None"
            if self.orientation == "vertical":
                self.setMaximumSize(QtCore.QSize(16777215, index))
                self.buddy.setMaximumSize(QtCore.QSize(16777215, self.container.size().height()-index))
            else:
                self.setMaximumSize(QtCore.QSize(index, 16777215))
        else:
            # print "self.status != None"
            if self.orientation == "vertical":
                self.setMaximumSize(QtCore.QSize(16777215, index))
                self.buddy.setMaximumSize(QtCore.QSize(16777215, self.container.size().height()-index))
            else:
                self.setMaximumSize(QtCore.QSize(index, 16777215))

