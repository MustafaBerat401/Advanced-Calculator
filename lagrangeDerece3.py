

from PyQt5 import QtWidgets
import math as mt
from PyQt5 import QtGui

from lagrangeDrc3Tasarim import Ui_MainWindow

class LangranceDrc3Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(LangranceDrc3Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))

        self.ui.ucDereceHesapButton.clicked.connect(self.ucLagrangeHesap)

    def ucLagrangeHesap(self):
        x = float(self.ui.xDegeriLine.text())
        x0 = float(self.ui.x0Line.text())
        x1 = float(self.ui.x1Line.text())
        x2 = float(self.ui.x2Line.text())
        x3 = float(self.ui.x3Line.text())
        fx0 = float(self.ui.fxoLine.text())
        fx1 = float(self.ui.fx1Line.text())
        fx2 = float(self.ui.fx2Line.text())
        fx3 = float(self.ui.fx3Line.text())


        result = ((((x-x1) * (x-x2) * (x-x3)) / ((x0-x1) * (x0-x2) * (x0-x3))) * fx0) + ((((x-x0) * (x-x2) * (x-x3)) / ((x1-x0) * (x1-x2) * (x1-x3))) * fx1) + ((((x-x0) * (x-x1) * (x-x3)) / ((x2-x0) * (x2-x1) * (x2-x3))) * fx2) + ((((x-x0) * (x-x1) * (x-x2)) / ((x3-x0) * (x3-x1) * (x3-x2))) * fx3)

        self.ui.sonucLabel.setText(format(str(result),'.5'))

