
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from standardHesapMakinesiDesign import Ui_MainWindow

class WindowStandard(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowStandard, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))


        # Rakamlar Buton Etkileşimi
        self.ui.nineButton.clicked.connect(self.clickRakam)
        self.ui.eightButton.clicked.connect(self.clickRakam)
        self.ui.sevenButton.clicked.connect(self.clickRakam)
        self.ui.sixButton.clicked.connect(self.clickRakam)
        self.ui.fiveButton.clicked.connect(self.clickRakam)
        self.ui.fourButton.clicked.connect(self.clickRakam)
        self.ui.threeButton.clicked.connect(self.clickRakam)
        self.ui.twoButton.clicked.connect(self.clickRakam)
        self.ui.oneButton.clicked.connect(self.clickRakam)
        self.ui.zeroButton.clicked.connect(self.clickRakam)

        # Diğer Buton Etkileşimleri
        self.ui.multiplyButton.clicked.connect(self.clickIslemler)
        self.ui.plusButton.clicked.connect(self.clickIslemler)
        self.ui.minusButton.clicked.connect(self.clickIslemler)
        self.ui.divideButton.clicked.connect(self.clickIslemler)

        self.ui.equalButton.clicked.connect(self.clickEqual)
        self.ui.percentButton.clicked.connect(self.clickIsaretYuzde)
        self.ui.plusMinusButton.clicked.connect(self.clickIsaretYuzde)
        self.ui.cButton.clicked.connect(self.clickDelete)
        self.ui.ceButton.clicked.connect(self.clickClear)
        self.ui.decimalButton.clicked.connect(self.clickRakam)


    def clickRakam(self):
        btn_text = self.sender().text()
        if self.ui.outputLabel.text() == "0":
            self.ui.outputLabel.setText("")
            self.ui.outputLabel.setText(self.ui.outputLabel.text() + btn_text) 
        else:
            self.ui.outputLabel.setText(self.ui.outputLabel.text() + btn_text)


    def clickIsaretYuzde(self):
        buton = self.sender()

        deger = float(self.ui.outputLabel.text())

        if buton.text() == "+/-":
            deger = deger * -1

        else:
            deger = deger * 0.01
        
        self.ui.outputLabel.setText(format(deger,'.15g'))

    def clickIslemler(self):
        btn_text = self.sender().text()
        if self.ui.outputLabel.text() != "0":
            self.ui.outputLabel.setText(self.ui.outputLabel.text()+btn_text)

    def clickClear(self):
        self.ui.outputLabel.setText("0")
    
    def clickDelete(self):
        x = self.ui.outputLabel.text()
        x=x[:-1]
        self.ui.outputLabel.setText(x)
        if len(x)==0:
            self.ui.outputLabel.setText("0")

    def clickEqual(self):
        content = self.ui.outputLabel.text()
        result = eval(content)
        self.ui.outputLabel.setText(format(str(result),'.10'))
        


