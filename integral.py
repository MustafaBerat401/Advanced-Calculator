
from PyQt5 import QtWidgets
from sympy import *
from PyQt5 import QtGui
import math
from integralTasarim import Ui_MainWindow

class IntegralWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(IntegralWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))


        self.ui.hesaplaButton.clicked.connect(self.integralHesabi)
        self.ui.sonucButton.clicked.connect(self.degerHesabi)

    def integralHesabi(self):

        x = Symbol("x")  
        y = Symbol("y")  

        fonk = self.ui.denklemLineEdit.text()

        a = integrate(fonk,x)

        self.ui.sonucLabel.setText(str(a))

    def degerHesabi(self):
        x = Symbol("x")  
        y = Symbol("y")  

        fonk = self.ui.denklemLineEdit.text()
        deger = int(self.ui.xDegerLine.text())

        a = integrate(fonk,x)

        result = a.subs(x,deger).evalf()

        self.ui.degerSonucuLabel.setText(format(str(float(result)),'.4'))








