# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\SSC_about.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextLabel = QtWidgets.QLabel(self.centralwidget)
        self.TextLabel.setGeometry(QtCore.QRect(10, 10, 621, 401))
        self.TextLabel.setStyleSheet("QLabel {\n"
"   background-color: rgb(215, 215, 215);\n"
"   border: 1px solid gray;\n"
"}")
        self.TextLabel.setText("")
        self.TextLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TextLabel.setObjectName("TextLabel")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setEnabled(True)
        self.BackButton.setGeometry(QtCore.QRect(430, 420, 200, 57))
        self.BackButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.BackButton.setAutoDefault(False)
        self.BackButton.setDefault(False)
        self.BackButton.setFlat(False)
        self.BackButton.setObjectName("BackButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Інформація"))
        self.BackButton.setText(_translate("MainWindow", "Назад"))
