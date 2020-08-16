# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##       Line edit with Criptidos vision       ##
 ##                                             ##
 ##                                             ##
 ##              for Basiq Series               ##
 ##           by Críptidos Digitales            ##
 ##                 GPL (c)2008                 ##
  ##                                            ##
	##############################################

"""
Incorporates cdStatusLabel
Adds attributes:
	emptyAllowed    default = False
	onlyNumbers
	minimo          (minimum length)
	maximo          (maximum length)
	message         Error messages
	hasStatusLabel  default = True
	isValid
	trimmed
	externalValidation
	externalMessage
"""




from PyQt4 import QtCore, QtGui


class CDPassWidget(QtGui.QFrame):

	def __init__(self, *args, **kwds):
		QtGui.QFrame.__init__(self, *args)

		self.widgets = []

		self.currentIndex = -1

		self.timeLine = QtCore.QTimeLine(500)
		self.timeLine.setUpdateInterval(10)
		self.timeLine.setCurveShape(QtCore.QTimeLine.EaseInOutCurve)

		self.splitter = QtGui.QSplitter(self)
		self.splitter.setHandleWidth(1)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		self.splitter.setSizePolicy(sizePolicy)

		self.layout = QtGui.QVBoxLayout(self)
		self.layout.setSpacing(0)
		self.layout.setMargin(0)

		self.layout.addWidget(self.splitter)

		self.__mode = 'toggle'

		self.connect(self.timeLine, QtCore.SIGNAL("frameChanged(int)"), self.frameChanged)
		self.connect(self.timeLine, QtCore.SIGNAL("finished()"), self.finished)


	def addWidget(self, widget, pos=-1, show=False):
		# print  "passWidget.CDPassWidget.addWidget({}, pos={}, show={})".format(widget, pos, show)

		self.splitter.insertWidget(pos, widget)

		if show:
			self.currentIndex = self.splitter.indexOf(widget)
		else:
			widget.hide()


	def count(self):
		return self.splitter.count()


	def createHndle(self):
		return Handle(self)


	def finished(self):
		# print  "CDPassWidget.finished()"
		self.currentIndex = self.showingIndex
		try:
			self.splitter.widget(self.hiddingIndex).hide()
		except:
			pass


	def mode(self):
		return self.__mode


	def setMode(self, value):
		self.__mode = value


	def orientation_set(self, value):
		if value == 'horizontal':
			self.splitter.setOrientation(QtCore.Qt.Horizontal)
		elif value == 'vertical':
			self.splitter.setOrientation(QtCore.Qt.Vertical)


	def showWidget(self, widget):
		# print  "CDPassWidget.showWidget()", widget

		index = self.splitter.indexOf(widget)

		if index < self.splitter.count() and index != self.currentIndex:
			if self.__mode == 'toggle':
				if self.currentIndex != -1:
					self.splitter.widget(self.currentIndex).hide()
				self.splitter.widget(index).show()
				self.currentIndex = index
			else:
				self.timeLine.setFrameRange(0, self.width())
				if index < self.currentIndex:
					# print  "forward"
					self.timeLine.setDirection(QtCore.QTimeLine.Forward)
					self.handleIndex = index + 1
				else:
					# print  "backward"
					self.timeLine.setDirection(QtCore.QTimeLine.Backward)
					self.handleIndex = self.currentIndex + 1
				self.splitter.widget(index).show()
				self.hiddingIndex = self.currentIndex
				self.showingIndex = index
				self.timeLine.start()
				self.currentIndex = index


	def currentWidget(self):
		return self.splitter.widget(self.currentIndex)


	def frameChanged(self, index):
		# print  "CDPassWidget.frameChanged({})".format(index), self.handleIndex
		self.splitter.moveSplitter(index, self.handleIndex)


	def widget(self, index):
		return self.splitter.widget(index)



class Handle(QtGui.QSplitterHandle):

	def mouseDoubleClickEvent(self, event):
		self.emit(QtCore.SIGNAL('doubleClicked()'))

	def mouseReleaseEvent(self, event):
		if self.count():
			self.roll()
		self.emit(QtCore.SIGNAL('clicked()'))


