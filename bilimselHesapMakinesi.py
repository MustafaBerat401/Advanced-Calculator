import math as m
import scipy as sc
import sympy as sp
import mpmath as mp
from numpy import log as ln
import numpy as np
from PyQt5 import QtGui

from PyQt5 import QtWidgets

from bilimselHesapMakinesiDesign import Ui_MainWindow

class WindowBilimsel(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowBilimsel, self).__init__()

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
        self.ui.decimalButton.clicked.connect(self.clickOndalik)

        self.ui.acParantezButton.clicked.connect(self.clickParantez)
        self.ui.kapaParantezButton.clicked.connect(self.clickParantez)

        self.ui.faktoriyelButton.clicked.connect(self.clickFaktoriyel)

        self.ui.karekokButton.clicked.connect(self.clickKarekok)
        
        self.ui.logButton.clicked.connect(self.clickLogaritma)
        
        self.ui.lnButton.clicked.connect(self.clickLN)

        self.ui.piButton.clicked.connect(self.clickPi)

        self.ui.eulerButton.clicked.connect(self.clickEuler)

        self.ui.expButton.clicked.connect(self.clickExp)

        self.ui.ikiPiButton.clicked.connect(self.clickIkiPi)

        self.ui.usAlmaButton.clicked.connect(self.clickUsAlma)

        self.ui.mutlakXButton.clicked.connect(self.clickMutlak)

        # Trigonometrik Fonksiyon Etkileşimleri
        self.ui.sinButton.clicked.connect(self.clickSin)
        self.ui.cosButton.clicked.connect(self.clickCos)
        self.ui.tanButton.clicked.connect(self.clickTan)
        self.ui.cotButton.clicked.connect(self.clickCot)
        self.ui.secButton.clicked.connect(self.clickSec)
        self.ui.cscButton.clicked.connect(self.clickCsc)

        self.ui.sin1Button.clicked.connect(self.clickSin1)
        self.ui.cos1Button.clicked.connect(self.clickCos1)
        self.ui.tan1Button.clicked.connect(self.clickTan1)
        self.ui.cot1Button.clicked.connect(self.clickCot1)
        self.ui.lgammaButton.clicked.connect(self.clickLgamma)
        self.ui.log1pButton.clicked.connect(self.clickLog1p)

        self.ui.sinhButton.clicked.connect(self.clickSinh)
        self.ui.coshButton.clicked.connect(self.clickCosh)
        self.ui.tanhButton.clicked.connect(self.clickTanh)
        self.ui.cothButton.clicked.connect(self.clickCoth)
        self.ui.sechButton.clicked.connect(self.clickSech)
        self.ui.cschButton.clicked.connect(self.clickCsch)

        self.ui.sinh1Button.clicked.connect(self.clickSinh1)
        self.ui.cosh1Button.clicked.connect(self.clickCosh1)
        self.ui.tanh1Button.clicked.connect(self.clickTanh1)
        self.ui.coth1Button.clicked.connect(self.clickCoth1)
        self.ui.sech1Button.clicked.connect(self.clickSech1)
        self.ui.csch1Button.clicked.connect(self.clickCsch1)




#**********************************************************************

    def clickRakam(self):
        btn_text = self.sender().text()
        if self.ui.outputLabel.text() == "0":
            self.ui.outputLabel.setText("")
            self.ui.outputLabel.setText(btn_text) 
        else:
            self.ui.outputLabel.setText(self.ui.outputLabel.text() + btn_text)

#**********************************************************************

    def clickOndalik(self):
        self.ui.outputLabel.setText(self.ui.outputLabel.text() + '.')

#**********************************************************************

    def clickIsaretYuzde(self):
        buton = self.sender()

        deger = float(self.ui.outputLabel.text())

        if buton.text() == "+/-":
            deger = deger * -1

        else:
            deger = deger * 0.01
        
        self.ui.outputLabel.setText(format(deger,'.15g'))
#**********************************************************************

    def clickIslemler(self):
        btn_text = self.sender().text()
        if self.ui.outputLabel.text() != "0":
            self.ui.outputLabel.setText(self.ui.outputLabel.text()+btn_text)

#**********************************************************************

    def clickClear(self):
        self.ui.outputLabel.setText("0")

#**********************************************************************
    
    def clickDelete(self):
        x = self.ui.outputLabel.text()
        x=x[:-1]
        self.ui.outputLabel.setText(x)
        if len(x)==0:
            self.ui.outputLabel.setText("0")
#**********************************************************************

    def clickEqual(self):
        content = self.ui.outputLabel.text()
        result = eval(content)
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   
    def clickParantez(self):
        btn_text = self.sender().text()
        if self.ui.outputLabel.text() == "0":
            self.ui.outputLabel.setText("")
            self.ui.outputLabel.setText(btn_text) 
        else:
            self.ui.outputLabel.setText(self.ui.outputLabel.text() + btn_text)

#**********************************************************************   
    
    def clickFaktoriyel(self):
        fak = self.ui.outputLabel.text()
        result = m.factorial(float(fak))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   
    
    def clickKarekok(self):
        btn_text = self.ui.outputLabel.text()
        result = m.sqrt(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   

    def clickLogaritma(self):
        btn_text = self.ui.outputLabel.text()
        result = m.log10(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   

    def clickLN(self):
        btn_text = self.ui.outputLabel.text()
        result = ln(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   
    def clickPi(self):
        self.ui.outputLabel.setText(str(m.pi))

#**********************************************************************   

    def clickEuler(self):
        self.ui.outputLabel.setText(str(m.e))

#**********************************************************************   

    def clickExp(self):
        btn_text = self.ui.outputLabel.text()
        result = m.exp(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   

    def clickIkiPi(self):
        self.ui.outputLabel.setText(str(2*(m.pi)))


#**********************************************************************   

    def clickUsAlma(self):
        btn_text = self.ui.outputLabel.text()
        result = float(btn_text)**2
        self.ui.outputLabel.setText(format(str(result),'.10'))
        
        
            

#**********************************************************************   

    def clickMutlak(self):
        buton = self.sender()

        deger = float(self.ui.outputLabel.text())

        if '-' in self.ui.outputLabel.text() and buton.text() == "|x|":
            deger = deger * -1
        
        self.ui.outputLabel.setText(str(deger))

#**********************************************************************   

    def clickSin(self):
        btn_text = self.ui.outputLabel.text()
        result = m.sin(m.radians(float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCos(self):
        btn_text = self.ui.outputLabel.text()
        result = m.cos(m.radians(float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickTan(self):
        btn_text = self.ui.outputLabel.text()
        result = m.tan(m.radians(float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCot(self):
        btn_text = self.ui.outputLabel.text()
        result = 1 / (m.tan(m.radians(float(btn_text))))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickSec(self):
        btn_text = self.ui.outputLabel.text()
        result = 1 / (m.cos(m.radians(float(btn_text))))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCsc(self):
        btn_text = self.ui.outputLabel.text()
        result = 1 / (m.sin(m.radians(float(btn_text))))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   

    def clickSin1(self):
        btn_text = self.ui.outputLabel.text()
        try:
            result = m.asin(float(btn_text))
            self.ui.outputLabel.setText(format(str(m.degrees(result)),'.10'))
        except ValueError:
            self.ui.outputLabel.setText(str("Error"))

    def clickCos1(self):
        btn_text = self.ui.outputLabel.text()
        try:
            result = m.acos(float(btn_text))
            self.ui.outputLabel.setText(format(str(m.degrees(result)),'.10'))
        except ValueError:
            self.ui.outputLabel.setText(str("Error"))

    def clickTan1(self):
        btn_text = self.ui.outputLabel.text()
        try:
            result = m.atan(float(btn_text))
            self.ui.outputLabel.setText(format(str(m.degrees(result)),'.10'))
        except ValueError:
            self.ui.outputLabel.setText(str("Error"))

    def clickCot1(self):
        btn_text = self.ui.outputLabel.text()
        try:
            result = (m.pi/2) - (m.atan(float(btn_text)))
            self.ui.outputLabel.setText(format(str(m.degrees(result)),'.10'))
        except ValueError:
            self.ui.outputLabel.setText(str("Error"))

    def clickLgamma(self):
        btn_text = self.ui.outputLabel.text()
        result = m.lgamma(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickLog1p(self):
        btn_text = self.ui.outputLabel.text()
        result = m.log1p(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   

    def clickSinh(self):
        btn_text = self.ui.outputLabel.text()
        result = m.sinh(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCosh(self):
        btn_text = self.ui.outputLabel.text()
        result = m.cosh(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickTanh(self):
        btn_text = self.ui.outputLabel.text()
        result = m.tanh(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCoth(self):
        btn_text = self.ui.outputLabel.text()
        result = 1 / (m.tanh(float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickSech(self):
        btn_text = self.ui.outputLabel.text()
        result = 1 / (m.cosh(float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCsch(self):
        btn_text = self.ui.outputLabel.text()
        result = 1 / (m.sinh(float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

#**********************************************************************   

    def clickSinh1(self):
        btn_text = self.ui.outputLabel.text()
        result = m.asinh(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCosh1(self):
        btn_text = self.ui.outputLabel.text()
        result = m.acosh(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickTanh1(self):
        btn_text = self.ui.outputLabel.text()
        result = m.atanh(float(btn_text))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCoth1(self):
        btn_text = self.ui.outputLabel.text()
        result = m.atanh( 1 / (float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickSech1(self):
        btn_text = self.ui.outputLabel.text()
        result = m.acosh( 1 / (float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

    def clickCsch1(self):
        btn_text = self.ui.outputLabel.text()
        result = m.asinh( 1 / (float(btn_text)))
        self.ui.outputLabel.setText(format(str(result),'.10'))

