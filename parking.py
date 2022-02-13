# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parking.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import socket
import socket
from boltcode import datasent
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1040, 893)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(110, 80, 831, 581))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.first = QtWidgets.QLabel(self.widget)
        self.first.setTextFormat(QtCore.Qt.RichText)
        self.first.setScaledContents(False)
        self.first.setObjectName("first")
        self.gridLayout.addWidget(self.first, 1, 0, 1, 1)
        self.second = QtWidgets.QLabel(self.widget)
        self.second.setObjectName("second")
        self.gridLayout.addWidget(self.second, 1, 1, 1, 1)
        self.third = QtWidgets.QLabel(self.widget)
        self.third.setObjectName("third")
        self.gridLayout.addWidget(self.third, 2, 0, 1, 1)
        self.fourth = QtWidgets.QLabel(self.widget)
        self.fourth.setObjectName("fourth")
        self.gridLayout.addWidget(self.fourth, 2, 1, 1, 1)
        self.parking = QtWidgets.QLabel(self.widget)
        self.parking.setObjectName("parking")
        self.gridLayout.addWidget(self.parking, 0, 0, 1, 2)
        

        self.retranslateUi(Dialog)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def respond(self):
        #data=datasent()
        data=2
        if int(data)==1:
            _translate = QtCore.QCoreApplication.translate
            self.first.setText(_translate("Dialog", "0"))
            self.second.setText(_translate("Dialog", "1"))
            self.third.setText(_translate("Dialog", "1"))
            self.fourth.setText(_translate("Dialog", "1"))
        if int(data)==5:
            _translate = QtCore.QCoreApplicaion.translate
            print("2")
            self.first.setText(_translate("Dialog", "1"))
            self.second.setText(_translate("Dialog", "1"))
            self.third.setText(_translate("Dialog", "1"))
            self.fourth.setText(_translate("Dialog", "1"))
        if int(data)==3:
            _translate = QtCore.QCoreApplication.translate
            self.first.setText(_translate("Dialog", "1"))
            self.second.setText(_translate("Dialog", "1"))
            self.third.setText(_translate("Dialog", "0"))
            self.fourth.setText(_translate("Dialog", "1"))
        if int(data)==4:
            _translate = QtCore.QCoreApplication.translate
            self.first.setText(("Dialog", "1"))
            self.second.setText(("Dialog", "1"))
            self.third.setText(("Dialog", "0"))
            self.fourth.setText(("Dialog", "0"))
        if int(data)==2:
            _translate = QtCore.QCoreApplication.translate
            self.first.setText(_translate("Dialog", "0"))
            self.second.setText(_translate("Dialog", "0"))
            self.third.setText(_translate("Dialog", "1"))
            self.fourth.setText(_translate("Dialog", "1")) 
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.first.setText(_translate("Dialog", "1"))
        self.second.setText(_translate("Dialog", "1"))
        self.third.setText(_translate("Dialog", "1"))
        self.fourth.setText(_translate("Dialog", "1"))
        self.parking.setText(_translate("Dialog", "                                                                                                            PARKING SPACE"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.respond()
    sys.exit(app.exec_())
    

