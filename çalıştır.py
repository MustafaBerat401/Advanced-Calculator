from PyQt5 import QtWidgets
from anasayfa import MainPage

app = QtWidgets.QApplication([])
win = MainPage()
win.show()
app.exec_()


