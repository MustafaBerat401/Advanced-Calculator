
from PyQt5 import QtWidgets
import math as mt
from PyQt5 import QtGui

from lagrangeDrc1Tasarim import Ui_MainWindow

class LangranceDrc1Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(LangranceDrc1Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))

        
        self.ui.birDerecedenHesaplaButton.clicked.connect(self.birinciDereceLagrange)


    def birinciDereceLagrange(self):

        x = self.ui.xDegeriLine.text()
        x0 = self.ui.x0Line.text()
        x1 = self.ui.x1Line.text()
        fx0 = self.ui.fxoLine.text()
        fx1 = self.ui.fx1Line.text()

        result = (((float(x) - float(x1)) / (float(x0) - float(x1))) * float(fx0)) + (((float(x) - float(x0)) / (float(x1) - float(x0))) * float(fx1))

        self.ui.sonucLabel.setText(format(str(result),'.5'))

    










