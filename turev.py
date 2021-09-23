
from PyQt5 import QtWidgets
from sympy import *
from PyQt5 import QtGui



from turevTasarimi import Ui_MainWindow

class TurevWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(TurevWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))

        self.ui.hesaplaButton.clicked.connect(self.turevHesabi)
        self.ui.sonucButton.clicked.connect(self.degerHesabi)

    def turevHesabi(self):
         
        x, y = symbols('x y') 
        func = self.ui.denklemLineEdit.text()
        turev = diff(func, x)

        self.ui.sonucLabel.setText(str(turev))

    def degerHesabi(self):
        x, y = symbols('x y') 
        func = self.ui.denklemLineEdit.text()
        turev = diff(func, x)
        deger = int(self.ui.xDegerLine.text())

        result = turev.subs(x,deger).evalf()

        self.ui.degerSonucuLabel.setText(format(str(float(result)),'.4'))







