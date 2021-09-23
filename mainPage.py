# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 585)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.standardButton = QtWidgets.QPushButton(self.centralwidget)
        self.standardButton.setGeometry(QtCore.QRect(20, 20, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.standardButton.setFont(font)
        self.standardButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 238, 47);")
        self.standardButton.setObjectName("standardButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 340, 231, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lagrangeDrc1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lagrangeDrc1.setFont(font)
        self.lagrangeDrc1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lagrangeDrc1.setObjectName("lagrangeDrc1")
        self.verticalLayout.addWidget(self.lagrangeDrc1)
        self.lagrangeDrc2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lagrangeDrc2.setFont(font)
        self.lagrangeDrc2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lagrangeDrc2.setObjectName("lagrangeDrc2")
        self.verticalLayout.addWidget(self.lagrangeDrc2)
        self.lagrangeDrc3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lagrangeDrc3.setFont(font)
        self.lagrangeDrc3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lagrangeDrc3.setObjectName("lagrangeDrc3")
        self.verticalLayout.addWidget(self.lagrangeDrc3)
        self.lagrangeDrc4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lagrangeDrc4.setFont(font)
        self.lagrangeDrc4.setStyleSheet("background-color: rgb(255, 110, 26);\n"
"background-color: rgb(255, 255, 255);")
        self.lagrangeDrc4.setObjectName("lagrangeDrc4")
        self.verticalLayout.addWidget(self.lagrangeDrc4)
        self.lagrangeDrc5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lagrangeDrc5.setFont(font)
        self.lagrangeDrc5.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lagrangeDrc5.setObjectName("lagrangeDrc5")
        self.verticalLayout.addWidget(self.lagrangeDrc5)
        self.bilimselButton = QtWidgets.QPushButton(self.centralwidget)
        self.bilimselButton.setGeometry(QtCore.QRect(20, 110, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bilimselButton.setFont(font)
        self.bilimselButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bilimselButton.setObjectName("bilimselButton")
        self.dogrusalButton = QtWidgets.QPushButton(self.centralwidget)
        self.dogrusalButton.setGeometry(QtCore.QRect(20, 200, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dogrusalButton.setFont(font)
        self.dogrusalButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 238, 47);")
        self.dogrusalButton.setObjectName("dogrusalButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 290, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.kaymaliButton = QtWidgets.QPushButton(self.centralwidget)
        self.kaymaliButton.setGeometry(QtCore.QRect(300, 200, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kaymaliButton.setFont(font)
        self.kaymaliButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kaymaliButton.setObjectName("kaymaliButton")
        self.integralButton = QtWidgets.QPushButton(self.centralwidget)
        self.integralButton.setGeometry(QtCore.QRect(300, 20, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.integralButton.setFont(font)
        self.integralButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.integralButton.setObjectName("integralButton")
        self.turevButton = QtWidgets.QPushButton(self.centralwidget)
        self.turevButton.setGeometry(QtCore.QRect(300, 110, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.turevButton.setFont(font)
        self.turevButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 238, 47);")
        self.turevButton.setObjectName("turevButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Advanced Calculator"))
        self.standardButton.setText(_translate("MainWindow", "Standard Hesap Makinesi"))
        self.lagrangeDrc1.setText(_translate("MainWindow", "1.Dereceden Lagrange"))
        self.lagrangeDrc2.setText(_translate("MainWindow", "2.Dereceden Lagrange"))
        self.lagrangeDrc3.setText(_translate("MainWindow", "3.Dereceden Lagrange"))
        self.lagrangeDrc4.setText(_translate("MainWindow", "4.Dereceden Lagrange"))
        self.lagrangeDrc5.setText(_translate("MainWindow", "5.Dereceden Lagrange"))
        self.bilimselButton.setText(_translate("MainWindow", "Bilimsel Hesap Makinesi"))
        self.dogrusalButton.setText(_translate("MainWindow", "Doğrusal İnterpolasyon"))
        self.label.setText(_translate("MainWindow", "Lagrange İnterpolasyon"))
        self.kaymaliButton.setText(_translate("MainWindow", "Kaymalı Yatak Hesabı"))
        self.integralButton.setText(_translate("MainWindow", "İntegral"))
        self.turevButton.setText(_translate("MainWindow", "Türev"))

