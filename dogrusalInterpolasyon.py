
from PyQt5 import QtWidgets
import math as mt
from PyQt5 import QtGui
from dogrusalInterpolasyonDesign import Ui_MainWindow

class DogrusalInterpolasyonWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DogrusalInterpolasyonWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))

        
        self.ui.hesaplaButton.clicked.connect(self.interpolasyonHesapla)

    def interpolasyonHesapla(self):

        a = self.ui.lineEdit1.text()
        b = self.ui.lineEdit2.text()
        c = self.ui.lineEdit3.text()
        d = self.ui.lineEdit4.text()
        e = self.ui.lineEdit5.text()

        result = (((float(d) - float(b)) / (float(c) - float(a))) * float(e)) + ((float(c) * float(b)) - (float(a) * float(d))) / (float(c) - float(a))

        self.ui.lineEdit6.setText(format(str(result),'.7'))




