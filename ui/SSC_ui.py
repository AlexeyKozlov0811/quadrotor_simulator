# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SSC.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 766)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 746))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 766))
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.MainGL = QtWidgets.QOpenGLWidget(self.CentralWidget)
        self.MainGL.setEnabled(True)
        self.MainGL.setGeometry(QtCore.QRect(0, 0, 815, 747))
        self.MainGL.setObjectName("MainGL")
        self.MinimapGL = QtWidgets.QOpenGLWidget(self.CentralWidget)
        self.MinimapGL.setGeometry(QtCore.QRect(820, 30, 199, 200))
        self.MinimapGL.setObjectName("MinimapGL")
        self.InfoBox = QtWidgets.QGroupBox(self.CentralWidget)
        self.InfoBox.setGeometry(QtCore.QRect(820, 240, 199, 261))
        self.InfoBox.setStyleSheet("QGroupBox{\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"}")
        self.InfoBox.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoBox.setObjectName("InfoBox")
        self.label_3 = QtWidgets.QLabel(self.InfoBox)
        self.label_3.setGeometry(QtCore.QRect(5, 210, 188, 21))
        self.label_3.setStyleSheet("QLabel {\n"
"  color:#ff0000;;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.InfoBox)
        self.label_6.setGeometry(QtCore.QRect(5, 110, 20, 20))
        self.label_6.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.ZLabel = QtWidgets.QLabel(self.InfoBox)
        self.ZLabel.setGeometry(QtCore.QRect(30, 110, 164, 20))
        self.ZLabel.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.ZLabel.setObjectName("ZLabel")
        self.XLabel = QtWidgets.QLabel(self.InfoBox)
        self.XLabel.setGeometry(QtCore.QRect(30, 50, 164, 20))
        self.XLabel.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.XLabel.setObjectName("XLabel")
        self.label_4 = QtWidgets.QLabel(self.InfoBox)
        self.label_4.setGeometry(QtCore.QRect(5, 50, 20, 20))
        self.label_4.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.InfoBox)
        self.label_5.setGeometry(QtCore.QRect(5, 80, 20, 20))
        self.label_5.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.InfoBox)
        self.label_2.setGeometry(QtCore.QRect(5, 20, 188, 30))
        self.label_2.setObjectName("label_2")
        self.MaxDistanceLabel = QtWidgets.QLabel(self.InfoBox)
        self.MaxDistanceLabel.setGeometry(QtCore.QRect(5, 230, 188, 20))
        self.MaxDistanceLabel.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"   color:#ff0000;;\n"
"}")
        self.MaxDistanceLabel.setObjectName("MaxDistanceLabel")
        self.YLabel = QtWidgets.QLabel(self.InfoBox)
        self.YLabel.setGeometry(QtCore.QRect(30, 80, 164, 20))
        self.YLabel.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.YLabel.setObjectName("YLabel")
        self.label_9 = QtWidgets.QLabel(self.InfoBox)
        self.label_9.setGeometry(QtCore.QRect(5, 130, 188, 16))
        self.label_9.setObjectName("label_9")
        self.DivitationXLabel = QtWidgets.QLabel(self.InfoBox)
        self.DivitationXLabel.setEnabled(True)
        self.DivitationXLabel.setGeometry(QtCore.QRect(5, 150, 188, 20))
        self.DivitationXLabel.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.DivitationXLabel.setObjectName("DivitationXLabel")
        self.CurrDistanceLabel = QtWidgets.QLabel(self.InfoBox)
        self.CurrDistanceLabel.setEnabled(True)
        self.CurrDistanceLabel.setGeometry(QtCore.QRect(5, 190, 188, 20))
        self.CurrDistanceLabel.setStyleSheet("QLabel {\n"
"   border: 1px solid gray;\n"
"}")
        self.CurrDistanceLabel.setObjectName("CurrDistanceLabel")
        self.label_10 = QtWidgets.QLabel(self.InfoBox)
        self.label_10.setGeometry(QtCore.QRect(5, 170, 188, 21))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.CentralWidget)
        self.label_8.setGeometry(QtCore.QRect(820, 10, 199, 20))
        self.label_8.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("QLabel {\n"
"   background-color: rgb(215, 215, 215);\n"
"   border: 1px solid gray;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.ControlButton = QtWidgets.QPushButton(self.CentralWidget)
        self.ControlButton.setEnabled(True)
        self.ControlButton.setGeometry(QtCore.QRect(820, 690, 199, 50))
        self.ControlButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.ControlButton.setAutoDefault(False)
        self.ControlButton.setDefault(False)
        self.ControlButton.setFlat(False)
        self.ControlButton.setObjectName("ControlButton")
        self.ControlBox = QtWidgets.QGroupBox(self.CentralWidget)
        self.ControlBox.setGeometry(QtCore.QRect(820, 510, 199, 171))
        self.ControlBox.setStyleSheet("QGroupBox{\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"}")
        self.ControlBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ControlBox.setObjectName("ControlBox")
        self.FileFileMod = QtWidgets.QRadioButton(self.ControlBox)
        self.FileFileMod.setGeometry(QtCore.QRect(5, 40, 199, 50))
        self.FileFileMod.setObjectName("FileFileMod")
        self.KeybordDisplayMod = QtWidgets.QRadioButton(self.ControlBox)
        self.KeybordDisplayMod.setGeometry(QtCore.QRect(5, 10, 199, 50))
        self.KeybordDisplayMod.setObjectName("KeybordDisplayMod")
        self.InputFilePath = QtWidgets.QLineEdit(self.ControlBox)
        self.InputFilePath.setGeometry(QtCore.QRect(5, 100, 189, 20))
        self.InputFilePath.setObjectName("InputFilePath")
        self.label = QtWidgets.QLabel(self.ControlBox)
        self.label.setGeometry(QtCore.QRect(5, 80, 189, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.ControlBox)
        self.label_7.setGeometry(QtCore.QRect(5, 123, 189, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.OutputFilePath = QtWidgets.QLineEdit(self.ControlBox)
        self.OutputFilePath.setGeometry(QtCore.QRect(5, 143, 189, 20))
        self.OutputFilePath.setObjectName("OutputFilePath")
        MainWindow.setCentralWidget(self.CentralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.ControlsInfo = QtWidgets.QAction(MainWindow)
        self.ControlsInfo.setObjectName("ControlsInfo")
        self.Restart = QtWidgets.QAction(MainWindow)
        self.Restart.setObjectName("Restart")
        self.AboutInfo = QtWidgets.QAction(MainWindow)
        self.AboutInfo.setObjectName("AboutInfo")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.ResumeAction = QtWidgets.QAction(MainWindow)
        self.ResumeAction.setEnabled(True)
        self.ResumeAction.setObjectName("ResumeAction")
        self.ComputeAction = QtWidgets.QAction(MainWindow)
        self.ComputeAction.setObjectName("ComputeAction")
        self.RestartAction = QtWidgets.QAction(MainWindow)
        self.RestartAction.setObjectName("RestartAction")
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setObjectName("About")
        self.Controls = QtWidgets.QAction(MainWindow)
        self.Controls.setObjectName("Controls")
        self.menu.addAction(self.ResumeAction)
        self.menu.addAction(self.RestartAction)
        self.menu.addSeparator()
        self.menu.addAction(self.ComputeAction)
        self.menu_2.addAction(self.About)
        self.menu_2.addAction(self.Controls)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Симулятор квадрокоптера"))
        self.InfoBox.setTitle(_translate("MainWindow", "Інформація про положення"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Максимальна відстань від оператора</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Z:"))
        self.ZLabel.setText(_translate("MainWindow", "0"))
        self.XLabel.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Х:"))
        self.label_5.setText(_translate("MainWindow", "У:"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Поточні координати</p></body></html>"))
        self.MaxDistanceLabel.setText(_translate("MainWindow", "0"))
        self.YLabel.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Відхилення від Х</p></body></html>"))
        self.DivitationXLabel.setText(_translate("MainWindow", "0"))
        self.CurrDistanceLabel.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Відстань від оператора</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Міні-мапа"))
        self.ControlButton.setText(_translate("MainWindow", "Пауза"))
        self.ControlBox.setTitle(_translate("MainWindow", "Режим роботи симулятору"))
        self.FileFileMod.setText(_translate("MainWindow", "Файл-Файл"))
        self.KeybordDisplayMod.setText(_translate("MainWindow", "Клавіатура-Дисплей"))
        self.label.setText(_translate("MainWindow", "Вхідний файл"))
        self.label_7.setText(_translate("MainWindow", "Файл виходу"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Інформація"))
        self.ControlsInfo.setText(_translate("MainWindow", "Управління"))
        self.Restart.setText(_translate("MainWindow", "Почати заново"))
        self.AboutInfo.setText(_translate("MainWindow", "Про програму"))
        self.Exit.setText(_translate("MainWindow", "Вихід"))
        self.ResumeAction.setText(_translate("MainWindow", "Продовжити"))
        self.ComputeAction.setText(_translate("MainWindow", "Обрахувати"))
        self.RestartAction.setText(_translate("MainWindow", "Почати спочатку"))
        self.About.setText(_translate("MainWindow", "Про програму "))
        self.Controls.setText(_translate("MainWindow", "Управління"))
