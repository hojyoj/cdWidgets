# -*- coding: utf-8 -*-

 ##############################################
 ##                                            ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##                                             ##
 ##           by Críptidos Digitales            ##
 ##              GPL (c)2008-2013               ##
  ##                                            ##
    ##############################################

"""
    Makes sorting case insensitive
"""

__version__ = "0.1"             ## Go to end for change log


from decimal import Decimal
import datetime

from PyQt4 import QtGui, QtCore




class CDTableWidgetItem(QtGui.QTableWidgetItem):

    def __init__(self, *args):
        """CDTableWidgetItem.__init__()"""

        QtGui.QTableWidgetItem.__init__(self, *args)

        self._data = ["", None]
        self._roles = [0]

        args = list(args)

        if args:
            self._data[0] = args.pop(0)
        if args:
            self._data[1] = args.pop(0)
        

    def __lt__(self, item):
        if u"{}".format(self.text()).upper() < u"{}".format(item.text()).upper():
            return True
        else:
            return False


    def dataHasRole(self, role):
        return role in self._roles
        

    def data(self, role=None):
        # print("""\n        CDTableWidgetItem.data()""")
        
        if role is None:
            
            return self._roles, self._data
            
        else:
        
            data = QtGui.QTableWidgetItem.data(self, role)
            # print("        ", data.toInt(), data.toString())
            if role >= 1000:
                # print("""\n        CDTableWidgetItem.data()""")
                
                try:
                    roleIndex = self._roles.index(role)      # Must check validity
                except:
                    print (role, self._roles)
                    raise
                    
                if self._data[roleIndex+1] == int:
                    if type(data) is QtCore.QVariant:
                        data = data.toInt()[0]
                elif self._data[roleIndex+1] == Decimal:
                    if type(data) is QtCore.QVariant:
                        data = Decimal("{}".format(data.toString()))
                    else:
                        data = Decimal("{}".format(data))
                elif self._data[roleIndex+1] == str:
                    if type(data) is QtCore.QVariant:
                        data = data.toString()
                elif self._data[roleIndex+1] == dict:
                    if type(data) is QtCore.QVariant:
                        data = eval("{}".format(data.toString()))
                    else:
                        data = eval("{}".format(data))
                else:
                    data = self._data[roleIndex+1]
                    
            return data


    def setData(self, role, data):
        # print("""        CDTableWidgetItem.setData()""")
        
        skip = False
        
        if role not in self._roles:
            # print("            ", role, self._roles)
            self._roles.append(role)
            self._data.extend([[]])

        roleIndex = self._roles.index(role)      # Must check validity

        # self._data[roleIndex+1].extend((0 - len(self._data[roleIndex + 1]) + 1) * [None])
        self._data[roleIndex+1] = type(data)

        if role >= 1000:

            if type(data) == dict:
                data = repr(data)
            elif type(data) == Decimal:
                data = "{}".format(data)
            elif type(data) in [int, str]:
                pass
            else:
                self._data[roleIndex+1] = data
                skip = True
                # print ("""            Unknown data type in cdTableWidgetItem.setData() : {}""".format(type(data)))
                # print ("            ", role, data)
                # f=g

        if not skip:
            QtGui.QTableWidgetItem.setData(self, role, data)
        
        # print("            ", self._data)

        # print("""        CDTableWidgetItem.setData() - END""")

