# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'turevTasarimi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1100, 880)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sonucLabel = QtWidgets.QLabel(self.centralwidget)
        self.sonucLabel.setGeometry(QtCore.QRect(160, 520, 861, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sonucLabel.setFont(font)
        self.sonucLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sonucLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sonucLabel.setObjectName("sonucLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 420, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 91, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-3, -5, 1111, 301))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.VLine)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(105, 563, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.denklemLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.denklemLineEdit.setGeometry(QtCore.QRect(170, 380, 821, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.denklemLineEdit.setFont(font)
        self.denklemLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.denklemLineEdit.setObjectName("denklemLineEdit")
        self.hesaplaButton = QtWidgets.QPushButton(self.centralwidget)
        self.hesaplaButton.setGeometry(QtCore.QRect(20, 550, 91, 41))
        self.hesaplaButton.setObjectName("hesaplaButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(95, 663, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(365, 677, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.xDegerLine = QtWidgets.QLineEdit(self.centralwidget)
        self.xDegerLine.setGeometry(QtCore.QRect(410, 670, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xDegerLine.setFont(font)
        self.xDegerLine.setAlignment(QtCore.Qt.AlignCenter)
        self.xDegerLine.setObjectName("xDegerLine")
        self.sonucButton = QtWidgets.QPushButton(self.centralwidget)
        self.sonucButton.setGeometry(QtCore.QRect(220, 740, 91, 41))
        self.sonucButton.setObjectName("sonucButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 752, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.degerSonucuLabel = QtWidgets.QLabel(self.centralwidget)
        self.degerSonucuLabel.setGeometry(QtCore.QRect(350, 740, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.degerSonucuLabel.setFont(font)
        self.degerSonucuLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.degerSonucuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.degerSonucuLabel.setObjectName("degerSonucuLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Türev"))
        self.sonucLabel.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "="))
        self.label_2.setText(_translate("MainWindow", "f(x)"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      Türevini almak istediğiniz denklemi aşağıdaki açıklamaya göre ve örnekte gösterildiği gibi giriniz.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">     Açıklama:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">      ** = İki tane yanyana yıldız ifadesi üs ifadesi girmek için kullanılır.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">      Örnek: </span><span style=\" font-size:10pt; color:#000000;\">f(x)</span><span style=\" font-family:\'arial,sans-serif\'; font-size:11pt; color:#202124; background-color:#ffffff;\"> = x**3+2*x**2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; color:#202124; background-color:#ffffff;\">       </span><span style=\" font-family:\'arial,sans-serif\'; font-size:10pt; color:#202124; background-color:#ffffff;\">Örnekte gösterilen denklem x üzeri küp artı 2 çarpı x kare şeklinde okunabilir. Tüm denklemler bu formatta girilebilir. Trigonometrik ifadeler için </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:10pt; color:#202124; background-color:#ffffff;\">     de geçerlidir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'arial,sans-serif\'; font-size:8pt; color:#202124;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">      Örnek: </span><span style=\" font-size:10pt; color:#000000;\">f(x)</span><span style=\" font-size:10pt; color:#ff5500;\"> </span><span style=\" font-family:\'arial,sans-serif\'; font-size:11pt; color:#202124; background-color:#ffffff;\">= sin(x)**2+2*cos(x)**3 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'arial,sans-serif\'; font-size:11pt; color:#202124;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:10pt; color:#202124; background-color:#ffffff;\">      şeklinde denklemler girilmelidir.</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "="))
        self.denklemLineEdit.setText(_translate("MainWindow", "x**2+2*x**3"))
        self.hesaplaButton.setText(_translate("MainWindow", "Hesapla"))
        self.label.setText(_translate("MainWindow", "Hesaplamak istediğiniz x değeri"))
        self.label_5.setText(_translate("MainWindow", "="))
        self.sonucButton.setText(_translate("MainWindow", "Sonuç"))
        self.label_6.setText(_translate("MainWindow", "="))
        self.degerSonucuLabel.setText(_translate("MainWindow", "0"))
