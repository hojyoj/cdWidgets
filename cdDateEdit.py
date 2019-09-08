# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##          Date edit with validation          ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##             GPL (c)2011 Jun 13              ##
  ##                                            ##
    ##############################################


__version__ = "0.1.1"


from PyQt4 import QtCore, QtGui



class CDDateEdit(QtGui.QDateTimeEdit):

    __initialDate = None
    def initialDate(self):
        return self.__initialDate
    def setInitialDate(self, date):
        self.__initialDate = date

    __modificationMessages = ""
    def modificationMessages_get(self):
        return self.__modificationMessages
    def modificationMessages_set(self, value):
        self.__modificationMessages = value
    modificationMessages = property(modificationMessages_get, modificationMessages_set)

    __validationMessages = ""
    def validationMessages_get(self):
        return self.__validationMessages
    def validationMessages_set(self, value):
        self.__validationMessages = value
    validationMessages = property(validationMessages_get, validationMessages_set)



    def __init__(self, *args):
        QtGui.QDateTimeEdit.__init__(self, *args)
        self.setDisplayFormat('dd MMM yyyy')
        self.__initialDate = QtCore.QDateTime()

    def focusInEvent(self, event):
        self.emit(QtCore.SIGNAL("focusIn()"))
        return QtGui.QDateTimeEdit.focusInEvent(self, event)

    def focusOutEvent(self, event):
        self.emit(QtCore.SIGNAL("focusOut()"))
        return QtGui.QDateTimeEdit.focusOutEvent(self, event)

    def isModified(self):
        return self.date() != self.initialDate()

    def isValid(self):
        isValid = True
        messages = ""

        self.validationMessages_set(messages)

        return isValid


    def setDate(self, date, initialToo=False):
        if initialToo:
            self.__initialDate = date
        
        QtGui.QDateTimeEdit.setDate(self, date)


    def dateTimeFromText(self, text):
        
        value = QtGui.QDateTimeEdit.dateTimeFromText(self, text)
        
        ## Check dot presence in month short name 
        if 'MMMM' not in self.displayFormat() and 'MMM' in self.displayFormat():
            if value == QtCore.QDateTime(2000,1,1,0,0):
                displayFormat = self.displayFormat()
                self.setDisplayFormat(self.displayFormat().replace('MMM', 'MMM.'))
                
                value = QtGui.QDateTimeEdit.dateTimeFromText(self, text)
                
                self.setDisplayFormat(displayFormat)

        return value


    def textFromDateTime(self, dateTime):
        value = QtGui.QDateTimeEdit.textFromDateTime(self, dateTime)

        ## Check dot presence in month short name 
        if 'MMMM' not in self.displayFormat() and 'MMM' in self.displayFormat():
            month = dateTime.toString('MMM')
            value = value.replace(month, month.replace('.', ''))
        
        return value


"""
  ~~~~~~  KNOWN ISSUES ~~~~        
    07.13   It appears that in some computers using new locale for
            spanish, month's shortname for dates ends with a dot.
            This dot appears in edit widgets making editing error
            prone.
            
        2014


  ~~~~~~  WISHES    ~~~~~~~



  ~~~~~~  CHANGELOG  ~~~~~~
  
        v0.1.1
    07.14   Testing temporary hack for dot appearing in month's
            shortname, in spanish locale.


"""
