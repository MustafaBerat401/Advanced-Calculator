

from PyQt5 import QtWidgets
import math
from PyQt5 import QtGui

from kaymaliYatakDsgnr import Ui_MainWindow

class KaymaliYatakWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(KaymaliYatakWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icons/advanced.png"))


        self.ui.sMaksButton.clicked.connect(self.sMaksHesap)
        self.ui.sMinButton.clicked.connect(self.sMinHesap)
        
        self.ui.ortYatakBoslukButton.clicked.connect(self.ortYatakBoslukHesap)

        self.ui.izafiYatakBoslukButton.clicked.connect(self.izafiYatakBoslukHesap)

        self.ui.ortBasincButton.clicked.connect(self.ortBasincHesap)

        self.ui.acisalHizButton.clicked.connect(self.acisalHizHesap)
        self.ui.sommerfieldButton.clicked.connect(self.sommerfieldSayiHesapla)
        self.ui.surtunmeKatsayiButton.clicked.connect(self.surtunmeKatsayisiHesapla)

        self.ui.kayipGucButton.clicked.connect(self.kayipGucHesap)

        self.ui.sogutmaIslemiButton.clicked.connect(self.sogutmaIslemiKonveksiyonHesap)

#############################################################################################################

    def sMaksHesap(self):
        dUst = float(self.ui.delikUstSapmaLine.text())
        mAlt = float(self.ui.milAltSapmaLine.text())

        sMax = dUst - mAlt
         
        self.ui.smaxSonucLabel.setText(str(sMax))

    def sMinHesap(self):
        dAlt = float(self.ui.delikAltSapmaLine.text())
        mUst = float(self.ui.milUstSapmaLine.text())

        sMin = dAlt - mUst

        self.ui.sminSonucLabel.setText(str(sMin))

    def ortYatakBoslukHesap(self):
        sMaks = float(self.ui.smaxSonucLabel.text())
        sMin = float(self.ui.sminSonucLabel.text())

        ortSBosluk = (sMin + sMaks) / 2

        self.ui.ortYatakBoslukSonucLabel.setText(str(int(ortSBosluk)))

###############################################################################################################

    def izafiYatakBoslukHesap(self):

        s = int(self.ui.ortYatakBoslukSonucLabel.text())
        d = float(self.ui.yatakCapiLine.text())

        izafiBosluk = (s / d ) 

        self.ui.izafiYatakBoslukSonucLabel.setText(str(izafiBosluk))

###############################################################################################################

    def ortBasincHesap(self):
        
        f = float(self.ui.radyalYukLine.text())
        d = float(self.ui.yatakCapiLine.text())
        b = float(self.ui.yatakGenisligiLine.text())
        pem = float(self.ui.emniyetBasincDegerLine.text())

        ortBasinc = (f * 1000) / (b * d)

        self.ui.ortBasincSonucLabel.setText(format(str(ortBasinc),'.4'))

        if ortBasinc < pem:
            self.ui.uyariLabel.setText("Ortalama basınç değeri emniyet değerinden küçüktür. Yani emniyetlidir.")
        elif ortBasinc == pem:
            self.ui.uyariLabel.setText("Ortalama basınç değeri emniyet değerine eşittir. Emniyet sınırdadır. Dikkat etmelisiniz.")
        else:
            self.ui.uyariLabel.setText("Ortalama basınç değeri emniyet değerinden büyüktür. Emniyetsizdir. Değerleri kontrol edip tekrar giriniz")


###############################################################################################################


    def acisalHizHesap(self):

        n = int(self.ui.devirSayisiLine.text())
        pi = math.pi
        
        w = (2 * pi * n) / 60 

        self.ui.acisalHizSonucLabel.setText(format(str(w),'.5'))

    def sommerfieldSayiHesapla(self):
        
        p = float(self.ui.ortBasincSonucLabel.text())
        izf = float(self.ui.izafiYatakBoslukSonucLabel.text())
        yagViskzt = float(self.ui.yagViskoziteLine.text())
        w = float(self.ui.acisalHizSonucLabel.text())

        x = (p) * (izf*izf)
        y = yagViskzt * w


        So = (x) / (y*10**-3) 

        self.ui.sommerfieldSonucLabel.setText(format(str(So),'.4'))

    def surtunmeKatsayisiHesapla(self):
        
        So = float(self.ui.sommerfieldSonucLabel.text())
        izf = float(self.ui.izafiYatakBoslukSonucLabel.text())

        if So < 1:
            srtnmeKatsayi1 = (3*izf*10**-3) / So
            self.ui.surtunmeKatsayiSonucLabel.setText(format(str(srtnmeKatsayi1),'.6'))

        elif So > 1:
            srtnmeKatsayi2 = (3*izf*10**-3) / So**0.5 
            self.ui.surtunmeKatsayiSonucLabel.setText(format(str(srtnmeKatsayi2),'.6'))

###############################################################################################################

    def kayipGucHesap(self):
        surtunme = float(self.ui.surtunmeKatsayiSonucLabel.text())
        f = float(self.ui.radyalYukLine.text()) * 1000  # N
        w = float(self.ui.acisalHizSonucLabel.text())
        u = ((float(self.ui.yatakCapiLine.text()) / 2) / 1000) * w 

        kayipGuc = (surtunme) * (f) * (u) # W

        self.ui.kayipGucSonucLabel.setText(format(str(int(kayipGuc)),'.4'))

    def sogutmaIslemiKonveksiyonHesap(self):
        Ps = float(self.ui.kayipGucSonucLabel.text())
        alfa = int(self.ui.isilIletimKatsayiLine.text())
        A = float(self.ui.yuzeyAlaniLine.text())
        To = int(self.ui.ortamSicaklikLine.text())

        Ty = ((Ps) / (alfa * A)) + To

        self.ui.sogutmaIslemiSonucLabel.setText(format(str(Ty),'.5'))

        kontrolTy = float(self.ui.sogutmaIslemiSonucLabel.text())
        Tmax = float(self.ui.maksYuzeySicaklikLine.text())

        if kontrolTy > Tmax:
            self.ui.sonucBilgiLabel.setText(" {} °C, {} °C'dan büyük olduğu için konveksiyon ile soğutma yetersiz kalmaktadır. Cebri olarak soğutma işlemi yapılması gerekir.".format(kontrolTy,Tmax))
        
        elif kontrolTy < Tmax:
            self.ui.sonucBilgiLabel.setText(" {} °C, {} °C'dan küçük olduğu için konveksiyon ile soğutma işlemi yeterlidir.".format(kontrolTy,Tmax))

###############################################################################################################

