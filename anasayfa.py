from PyQt5 import QtWidgets
from PyQt5 import QtGui
from mainPage import Ui_MainWindow
from standardHesapMakinesi import WindowStandard
from bilimselHesapMakinesi import WindowBilimsel
from integral import IntegralWindow
from turev import TurevWindow
from dogrusalInterpolasyon import DogrusalInterpolasyonWindow
from kaymaliYatakHesabi import KaymaliYatakWindow
from lagrangeDerece1 import LangranceDrc1Window
from lagrangeDerece2 import LangranceDrc2Window
from lagrangeDerece3 import LangranceDrc3Window
from lagrangeDerece4 import LangranceDrc4Window
from lagrangeDerece5 import LangranceDrc5Window

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))
        
        self.ui.standardButton.clicked.connect(self.standard)
        self.ui.bilimselButton.clicked.connect(self.bilimsel)
        self.ui.integralButton.clicked.connect(self.integral)
        self.ui.turevButton.clicked.connect(self.turev)
        self.ui.kaymaliButton.clicked.connect(self.kaymaliYatak)
        self.ui.dogrusalButton.clicked.connect(self.dogrusalInterp)
        self.ui.lagrangeDrc1.clicked.connect(self.lagrangeDerece1)
        self.ui.lagrangeDrc2.clicked.connect(self.lagrangeDerece2)
        self.ui.lagrangeDrc3.clicked.connect(self.lagrangeDerece3)
        self.ui.lagrangeDrc4.clicked.connect(self.lagrangeDerece4)
        self.ui.lagrangeDrc5.clicked.connect(self.lagrangeDerece5)

        
        self.standard = WindowStandard()
        self.bilimsel = WindowBilimsel()
        self.integral = IntegralWindow()
        self.turev = TurevWindow()
        self.dogrusal = DogrusalInterpolasyonWindow()
        self.kaymali = KaymaliYatakWindow()
        
        self.lagrangeDerece1 = LangranceDrc1Window()
        self.lagrangeDerece2 = LangranceDrc2Window()
        self.lagrangeDerece3 = LangranceDrc3Window()
        self.lagrangeDerece4 = LangranceDrc4Window()
        self.lagrangeDerece5 = LangranceDrc5Window()

    def standard(self):
        self.standard.show()

    def bilimsel(self):
        self.bilimsel.show()

    def integral(self):
        self.integral.show()

    def turev(self):
        self.turev.show()

    def dogrusalInterp(self):
        self.dogrusal.show()

    def kaymaliYatak(self):
        self.kaymali.show()

    def lagrangeDerece1(self):
        self.lagrangeDerece1.show()
    def lagrangeDerece2(self):
        self.lagrangeDerece2.show()
    def lagrangeDerece3(self):
        self.lagrangeDerece3.show()
    def lagrangeDerece4(self):
        self.lagrangeDerece4.show()
    def lagrangeDerece5(self):
        self.lagrangeDerece5.show()



