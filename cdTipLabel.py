# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Tip Label                                  ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2011 Jun 13 19:58:19                ##
  ##  @author: - Jorge Hojyo                     ##
    ###############################################


import sys
from PyQt4 import QtCore, QtGui

class CDTipLabel(QtGui.QLabel):

    def __init__(self,texto,widget):
        QtGui.QLabel.__init__(self, QtGui.QApplication.desktop().screen(),QtCore.Qt.ToolTip)
        texto=unicode(texto)
        self.setPalette(QtGui.QPalette(QtCore.Qt.black, QtGui.QColor(255,255,220),
                                                      QtGui.QColor(96,96,96), QtCore.Qt.black, QtCore.Qt.black,
                                                      QtCore.Qt.black, QtGui.QColor(255,255,220)));
        self.ensurePolished();
        self.setMargin(1 + self.style().pixelMetric(QtGui.QStyle.PM_ToolTipLabelFrameWidth, None, self));
        self.setFrameStyle(QtGui.QFrame.NoFrame);
        self.setAlignment(QtCore.Qt.AlignLeft);
        self.setIndent(1);
        self.setWordWrap(QtCore.Qt.mightBeRichText(texto));
        self.setWindowOpacity(self.style().styleHint(QtGui.QStyle.SH_ToolTipLabel_Opacity, None,self) / 255.0);
        self.widget=widget

    def tipChanged(self, texto):
        texto=unicode(texto)
        if unicode(self.text()) != texto:
            return True
        else:
            return False

    def resizeEvent(self,evento):
        frameMask=QtGui.QStyleHintReturnMask()
        opcion=QtGui.QStyleOption()
        opcion.init(self)
        if (self.style().styleHint(QtGui.QtGui.QStyle.SH_ToolTip_Mask,opcion,self,frameMask)):
            self.setMask(frameMask.region())
        QtGui.QLabel.resizeEvent(self,evento)

    def showText(self,texto):
        if self.tipChanged(texto):
            self.reuseTip(texto)
            self.setTipRect()
            self.placeTip()


    def reuseTip(self,texto):
        self.setText(texto)
        if len(texto)==0:
            self.hide()
        else:
            self.show()
        fontMetrics=QtGui.QFontMetrics(self.font())
        extra=QtGui.QSize(1,0)
        if ( fontMetrics.descent()==2 and fontMetrics.ascent()>=11):
            extra.setHeight(extra.height()+1)
        self.resize(self.sizeHint()+extra)

    def paintEvent(self, evento):
        painterStyle=QtGui.QStylePainter(self)
        opcion=QtGui.QStyleOptionFrame()
        opcion.init(self)
        painterStyle.drawPrimitive(QtGui.QStyle.PE_PanelTipLabel,opcion)
        painterStyle.end();
        QtGui.QLabel.paintEvent(self,evento)

    def setTipRect(self):
        pass

    def placeTip(self ):
        posicion=self.widget.mapToGlobal(QtGui.QPoint(0,0))
        anchoWidget=self.widget.width()
        tamanoEtiqueta=self.sizeHint()
        posicionEnY=posicion.y()+self.widget.height()+3
        posicionEnX=anchoWidget/2-tamanoEtiqueta.width()/2
        self.setGeometry(posicion.x() +posicionEnX,posicionEnY,self.sizeHint().width(),self.sizeHint().height())


def main():
    def cambio(texto):
        e.showText(linea.text().toUpper())
    aplicacion=QtGui.QApplication(sys.argv)
    linea=QtGui.QLineEdit(None)
    e=CDTipLabel('juan',linea)
    linea.connect(linea,QtCore.SIGNAL('textChanged(const QString &)'),cambio)
    linea.show()
    aplicacion.exec_()


if __name__=='__main__':
    main()
