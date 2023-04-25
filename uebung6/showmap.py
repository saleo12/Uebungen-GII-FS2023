from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 06 Qt-Designer/showmap.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        breite = self.lineEdit_b.text()
        länge = self.lineEdit_l.text()
        linkmap = f"https://www.google.ch/maps/place/{breite},{länge}"
        QDesktopServices.openUrl(QUrl(linkmap))

app = QApplication([])
win = UIFenster()
app.exec()