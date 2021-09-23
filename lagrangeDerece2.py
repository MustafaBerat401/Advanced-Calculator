

from PyQt5 import QtWidgets
import math as mt
from PyQt5 import QtGui

from lagrangeDrc2Tasarim import Ui_MainWindow

class LangranceDrc2Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(LangranceDrc2Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))

        
        self.ui.ikiDereceHesapButton.clicked.connect(self.ikinciLagrange)

    def ikinciLagrange(self):
        x = float(self.ui.xDegeriLine_2.text())
        x0 = float(self.ui.x0Line_2.text())
        x1 = float(self.ui.x1Line_2.text())
        x2 = float(self.ui.x2Line.text())
        fx0 = float(self.ui.fxoLine_2.text())
        fx1 = float(self.ui.fx1Line_2.text())
        fx2 = float(self.ui.fx2Line.text())
        
        result2 = ((((x - x1) / (x0 - x1)) * ((x - x2) / (x0 - x2))) * fx0) + ((((x - x0) / (x1 - x0)) * ((x - x2) / (x1 - x2))) * fx1) + ((((x - x0) / (x2 - x0)) * ((x - x1) / (x2 - x1))) * fx2) 

        self.ui.sonucLabel_2.setText(format(str(result2),'.5'))
