# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from rashdrivingcode import rush
from speed_check import trackMultipleObjects
from parking import Ui_Dialog
#from pothole import r
#import socket
class Ui_potholeno(object):
    def parkingclick(self):
        trackMultipleObjects()
    def driveclick(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.respond()
    def setupUi(self, potholeno):
        potholeno.setObjectName("potholeno")
        potholeno.resize(892, 744)
        self.widget = QtWidgets.QWidget(potholeno)
        self.widget.setGeometry(QtCore.QRect(50, 20, 831, 531))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.visionsafety = QtWidgets.QLabel(self.widget)
        self.visionsafety.setObjectName("visionsafety")
        self.gridLayout.addWidget(self.visionsafety, 0, 0, 1, 3)
        self.pothole_2 = QtWidgets.QLabel(self.widget)
        self.pothole_2.setObjectName("pothole_2")
        self.gridLayout.addWidget(self.pothole_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.potholebutton = QtWidgets.QPushButton(self.widget)
        self.potholebutton.setObjectName("potholebutton")
        self.gridLayout.addWidget(self.potholebutton, 1, 2, 1, 1)
        self.drive = QtWidgets.QLabel(self.widget)
        self.drive.setObjectName("drive")
        self.gridLayout.addWidget(self.drive, 2, 0, 1, 1)
        self.driveno = QtWidgets.QLabel(self.widget)
        self.driveno.setObjectName("driveno")
        self.gridLayout.addWidget(self.driveno, 2, 1, 1, 1)
        self.drivebutton = QtWidgets.QPushButton(self.widget)
        self.drivebutton.setObjectName("drivebutton")
        self.gridLayout.addWidget(self.drivebutton, 2, 2, 1, 1)
        self.drive_2 = QtWidgets.QLabel(self.widget)
        self.drive_2.setObjectName("drive_2")
        self.gridLayout.addWidget(self.drive_2, 3, 0, 1, 1)
        self.drivebutton_2 = QtWidgets.QPushButton(self.widget)
        self.drivebutton_2.setObjectName("drivebutton_2")
        self.gridLayout.addWidget(self.drivebutton_2, 3, 1, 1, 2)
        #keys
        #self.potholebutton.clicked.connect(self.startclick)
        self.drivebutton.clicked.connect(self.parkingclick)
        self.drivebutton_2.clicked.connect(self.driveclick)
        #keys
        self.retranslateUi(potholeno)
        QtCore.QMetaObject.connectSlotsByName(potholeno)

    def retranslateUi(self, potholeno):
        _translate = QtCore.QCoreApplication.translate
        potholeno.setWindowTitle(_translate("potholeno", "Dialog"))
        self.visionsafety.setText(_translate("potholeno", "                                                                                           VISION SAFETY"))
        self.pothole_2.setText(_translate("potholeno", "POTHOLE"))
        self.label_2.setText(_translate("potholeno", "0"))
        self.potholebutton.setText(_translate("potholeno", "PRESS TO SEE"))
        self.drive.setText(_translate("potholeno", "DRIVE"))
        self.driveno.setText(_translate("potholeno", "0"))
        self.drivebutton.setText(_translate("potholeno", "PRESS TO SEE"))
        self.drive_2.setText(_translate("potholeno", "PARKING"))
        self.drivebutton_2.setText(_translate("potholeno", "PRESS TO SEE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    potholeno = QtWidgets.QDialog()
    ui = Ui_potholeno()
    ui.setupUi(potholeno)
    potholeno.show()
    sys.exit(app.exec_())

