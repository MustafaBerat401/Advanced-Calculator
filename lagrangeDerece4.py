
from PyQt5 import QtWidgets
import math as mt
from PyQt5 import QtGui

from lagrangeDrc4Tasarim import Ui_MainWindow

class LangranceDrc4Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(LangranceDrc4Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))

        self.ui.dortDereceHesapButton.clicked.connect(self.dortLagrangeHesap)

    def dortLagrangeHesap(self):
        x = float(self.ui.xDegeriLine.text())
        x0 = float(self.ui.x0Line.text())
        x1 = float(self.ui.x1Line.text())
        x2 = float(self.ui.x2Line.text())
        x3 = float(self.ui.x3Line.text())
        x4 = float(self.ui.x4Line.text())
        fx0 = float(self.ui.fxoLine.text())
        fx1 = float(self.ui.fx1Line.text())
        fx2 = float(self.ui.fx2Line.text())
        fx3 = float(self.ui.fx3Line.text())
        fx4 = float(self.ui.fx4Line.text())

        result = ((((x-x1) * (x-x2) * (x-x3) * (x-x4)) / ((x0-x1) * (x0-x2) * (x0-x3) * (x0-x4))) * fx0) + + ((((x-x0) * (x-x2) * (x-x3) * (x-x4)) / ((x1-x0) * (x1-x2) * (x1-x3) * (x1-x4))) * fx1) + ((((x-x0) * (x-x1) * (x-x3) * (x-x4)) / ((x2-x0) * (x2-x1) * (x2-x3) * (x2-x4))) * fx2) + ((((x-x0) * (x-x1) * (x-x2) * (x-x4)) / ((x3-x0) * (x3-x1) * (x3-x2) * (x3-x4))) * fx3) + ((((x-x0) * (x-x1) * (x-x2) * (x-x3)) / ((x4-x0) * (x4-x1) * (x4-x2) * (x4-x3))) * fx4) 

        self.ui.sonucLabel.setText(format(str(result),'.5'))





