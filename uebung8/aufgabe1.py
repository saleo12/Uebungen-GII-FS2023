from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Uebungen-GII-FS2023/uebung8/gui8.ui", self)
        self.show()

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.Grafik)
        self.verticalLayout.insertWidget(0,self.canvas)

        self.button.clicked.connect(self.plot)

        self.farbe.addItem("Rot")
        self.farbe.addItem("Violett")
        self.farbe.addItem("Blau")
        self.farbe.addItem("Türkis")
        self.farbe.addItem("Gelb")
        self.farbe.addItem("Grün")
        self.farbe.addItem("Schwarz")

    def plot(self):
        plt.clf()
        coeff_input = self.polynom.text()
        coeffs = coeff_input.split(",")

        anzahlPunkte = self.anzahl.value()
        obergrenze = self.obergrenze.value()
        untergrenze = self.untergrenze.value()

        colorText = self.farbe.currentText()
        if colorText == "Rot":
            color = "r"
        elif colorText == "Violett":
            color = "m"        
        elif colorText == "Blau":
            color = "b"
        elif colorText == "Türkis":
            color = "c"
        elif colorText == "Gelb":
            color = "y"
        elif colorText == "Grün":
            color = "g"
        else:
            color = "k"
    
        try:
            coeffs = [float(coeff.strip()) for coeff in coeffs]
        except ValueError:
            self.error_message.showMessage("Fehler: Bitte geben Sie Zahlen getrennt mit Kommas ein.")
            return
        
        if len(coeffs) == 0 or coeffs[0] == 0:
            self.error_message.showMessage("Fehler: Bitte geben Sie ein gültiges Polynom ein.")
            return
        
        poly_str = ""
        for i, coeff in enumerate(coeffs):
            if i == 0:
                poly_str += str(coeff)
            else:
                sign = "+" if coeff >= 0 else "-"
                poly_str += f" {sign} {abs(coeff)}x^{i}"


        f = np.poly1d(coeffs)
        x = np.linspace(untergrenze, obergrenze, anzahlPunkte)
        y = f(x)
        plt.plot(x,y,color+"o-")

        plt.axis("equal")
        self.canvas.draw()


app = QApplication([])
window = Window()
app.exec()