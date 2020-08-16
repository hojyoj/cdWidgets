# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##                 Main Window                 ##
 ##                                             ##
 ##                                             ##
 ##              from Basiq Series              ##
 ##           by Críptidos Digitales            ##
 ##                 GPL (c)2008                 ##
  ##                                            ##
	##############################################

"""
"""


## Enable for testing (adds parent directory)
import os, sys
sys.path.append(os.getcwd()[:os.getcwd().rfind('\\')])



from PyQt4 import QtCore, QtGui

from basiq import menus
# from basiq import about



class CDMainWindow(QtGui.QMainWindow):

	def __init__(self, *args, **kwds):

		self.cnt = kwds.pop( 'cnt', None )
		self.app = self.cnt.app

		QtGui.QMainWindow.__init__(self, *args)

		self.ui = QtCore.QObject()


		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)

		## CENTRAL WIDGET AND LAYOUT
		centralWidget_ = QtGui.QWidget(self)
		centralWidget_.setObjectName("centralWidget")

		##    Apply layout direction here
		layout = QtGui.QHBoxLayout(centralWidget_)
		layout.setSpacing(0)
		layout.setMargin(0)
		layout.setObjectName("centralLayout")

		self.setCentralWidget(centralWidget_)

		## CONTENTS LAYOUT (apply direction here)
		self._contentsLayout = QtGui.QVBoxLayout()

		layout.addLayout(self._contentsLayout)


		## MAIN MENU
		self._mainMenu = menus.SlideMenu(centralWidget_, cnt = self.cnt, orientation='down')
		self._mainMenu.style = {'color1':'#C6A78B', 'color2':'#B79270'}

		##    Exit button
		exit_icon = QtGui.QIcon()
		exit_icon.addPixmap(QtGui.QPixmap(":/Shotdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self._mainMenu.button_add(1, '&Salir', exit_icon, self.exit)


		##    INFORMACIÓN Button and widget
		# self.ui.lock1FR.setStyleSheet("background-color:#F8F0FF; border-radius:20;")

		info_icon = QtGui.QIcon()
		info_icon.addPixmap(QtGui.QPixmap(":/Info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		infoBU = self._mainMenu.button_add(2, '&Info', info_icon, self.app.about_show)

		self.connect(infoBU, QtCore.SIGNAL('enter()'), self.info_show)
		self.connect(infoBU, QtCore.SIGNAL('leave()'), self.info_hide)
		# self.connect(self.ui.infoTO, QtCore.SIGNAL('clicked()'), self.app.showAbout)

		# self.ui.infoTO.setDefaultAction(self.infoAC)
		# self.ui.infoTO.setIconSize(QtCore.QSize(40, 40))


		self.info = QtGui.QTextEdit(self)
		self.info.hide()
		self.info.setStyleSheet("background-color:#FFFFA0;")
		self.info.setGeometry(infoBU.x()+40, infoBU.y()+100, 250, 180)

		self.info.setText(u"Basiq Series, the best!")


		layout.insertWidget(0, self._mainMenu.master)

		layout.setStretch(1, 1)


		self.connect(self._mainMenu.master, QtCore.SIGNAL('exit()'), self.exit)


		## TITLE
		self._titleWidget = TitleWidget(centralWidget_)
		self.connect(self._titleWidget, QtCore.SIGNAL('clicked()'), self.mainMenu.show)

		self._contentsLayout.addWidget(self._titleWidget)

		## ~~~  Main Title  ~~~~~~
		#! Check if maintitle_use can be checked
		# self.ui.titleFR.hide()
		self._titleWidget.hide()



	# def about_show(self):
		# form = about.Form(app=self.app)
		# result = form.exec_()


	def contentsLayout_get(self):
		return self._contentsLayout
	def contentsLayout_set(self, value):
		self._contentsLayout = value
	contentsLayout = property(contentsLayout_get, contentsLayout_set)


	def exit(self):
		# if not self.ui.mainMenuLYFR.isHidden():
			# self.close()
		self.close()


	def info_hide(self):
		self.info.hide()

	def info_show(self):
		"""mainView.info_show()"""
		# if self.info:
		# self.info.setText(self.infoText)
		self.info.show()
		self.mode = u'information'


	def keyPressEvent(self, event):
		# print "CDMainWindow.keyPressEvent()"
		# print event.key()
		if event.key()==16777273:
			self.emit(QtCore.SIGNAL('F10Pressed()'))


	def mainMenu_get(self):
		return self._mainMenu
	def mainMenu_set(self, value):
		self._mainMenu = value
	mainMenu = property(mainMenu_get, mainMenu_set)


	def resized(self, event):
		"""    CDMainWindow.resized()"""

		layoutZoom = (self.width() * 2.0) / (2000.0 - self.height())

		if layoutZoom < 1.0:
			self.layoutZoom = 0.8
		elif 1.0 <= layoutZoom < 1.2:
			self.layoutZoom = 1.0
		elif 1.2 <= layoutZoom:
			self.layoutZoom = 1.2

		font = QtGui.QFont()
		# font.setFamily("Microsoft Sans Serif")
		font.setFamily("Arial")
		font.setPointSize(12 * self.layoutZoom)
		font.setWeight(75)
		font.setBold(True)

		self._titleWidget.setFont(font)

		try:
			self.mainMenu.font_set(font)
		except:
			print (sys.exc_info()[1])
			pass

		return

	@property
	def titleWidget(self):
		return self._titleWidget


	def title_clicked(self):
		if self.ui.mainMenuLYFR.isHidden():
			self.ui.mainMenuLYFR.showGradual()



class TitleWidget(QtGui.QWidget):

	def __init__(self, *args):

		QtGui.QWidget.__init__(self, *args)

		self.setStyleSheet("background-color:rgba(0,0,0,0);")
		# self.setObjectName("titleFR")

		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

		layout = QtGui.QHBoxLayout(self)
		layout.setSpacing(0)
		layout.setContentsMargins(0, 4, 0, 0)

		self.titleSpacerLeftFR = QtGui.QFrame(self)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.titleSpacerLeftFR.sizePolicy().hasHeightForWidth())
		self.titleSpacerLeftFR.setSizePolicy(sizePolicy)
		self.titleSpacerLeftFR.setObjectName("titleSpacerLeftFR")

		layout.addWidget(self.titleSpacerLeftFR)

		self.currentLeftCapFR = QtGui.QFrame(self)
		self.currentLeftCapFR.setMinimumSize(QtCore.QSize(12, 0))
		self.currentLeftCapFR.setMaximumSize(QtCore.QSize(12, 16777215))
		self.currentLeftCapFR.setStyleSheet("""background-color:QRadialGradient(cx:.9, cy:.5, radius:.5, fx:1, fy:.5, stop:0 #D0E4FF, stop:.1 #D0E4FF, stop:1 #6090F0); border-top-left-radius:12px; border-bottom-left-radius:12px;""")
		self.currentLeftCapFR.setObjectName("currentLeftCapFR")

		layout.addWidget(self.currentLeftCapFR)

		self.currentTO = QtGui.QToolButton(self)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(3)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.currentTO.sizePolicy().hasHeightForWidth())
		self.currentTO.setSizePolicy(sizePolicy)
		self.currentTO.setMinimumSize(QtCore.QSize(0, 36))
		self.currentTO.setStyleSheet("color:#0000FF; background-color:QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6090F0, stop:.3 #D0E4FF, stop:.7 #D0E4FF, stop:1 #6090F0); padding:3;")
		self.currentTO.setText("")
		self.currentTO.setIconSize(QtCore.QSize(24, 24))
		self.currentTO.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.currentTO.setAutoRaise(True)
		self.currentTO.setObjectName("currentTO")

		self.connect(self.currentTO, QtCore.SIGNAL('clicked()'), self.clicked)

		layout.addWidget(self.currentTO)

		self.currentRightCapFR = QtGui.QFrame(self)
		self.currentRightCapFR.setMinimumSize(QtCore.QSize(12, 0))
		self.currentRightCapFR.setMaximumSize(QtCore.QSize(12, 16777215))
		self.currentRightCapFR.setStyleSheet("""background-color:QRadialGradient(cx:.1, cy:.5, radius:.5, fx:0, fy:.5, stop:0 #D0E4FF, stop:.1 #D0E4FF, stop:1 #6090F0); border-top-right-radius:12px; border-bottom-right-radius:12px;""")
		self.currentRightCapFR.setObjectName("currentRightCapFR")

		layout.addWidget(self.currentRightCapFR)

		self.titleSpacerRightFR = QtGui.QFrame(self)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.titleSpacerRightFR.sizePolicy().hasHeightForWidth())
		self.titleSpacerRightFR.setSizePolicy(sizePolicy)
		self.titleSpacerRightFR.setObjectName("titleSpacerRightFR")

		layout.addWidget(self.titleSpacerRightFR)


	def clicked(self):
		self.emit(QtCore.SIGNAL('clicked()'))


	def setColors(self, textColor, gradient1):
			self.currentTO.setStyleSheet("color:{}; background-color:qlineargradient(x1:0, y1:0, X2:1, y2:1, stop:0 {}, stop:.5 #FFFFFF, stop:1 {}); padding:3;".format(textColor, gradient1, gradient1))

			self.currentLeftCapFR.setStyleSheet("background-color:QRadialGradient(cx:.9, cy:.5, radius:.5, fx:1, fy:.5, stop:0 #E0FFB0, stop:.1 #E0FFB0, stop:1 {}); border-top-left-radius:12px; border-bottom-left-radius:12px;".format(gradient1))

			self.currentRightCapFR.setStyleSheet("background-color:QRadialGradient(cx:.1, cy:.5, radius:.5, fx:0, fy:.5, stop:0 #E0FFB0, stop:.1 #E0FFB0, stop:1 {}); border-top-right-radius:12px; border-bottom-right-radius:12px;".format(gradient1))


	def setFont(self, font):

		QtGui.QWidget.setFont(self, font)

		self.currentTO.setFont(font)


	def setText(self, text):

		self.currentTO.setText(text)



if __name__ == "__main__":

	app = QtGui.QApplication(sys.argv)

	window = CDMainWindow(app=app)
	window.show()

	window.mainMenu.button_add(None, text='puaj', slot=window.keyPressEvent)

	app.exec_()

