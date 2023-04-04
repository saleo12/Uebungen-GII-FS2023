import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI-Programmierung")

        layout = QFormLayout()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)


        filemenu.addAction(save)
        filemenu.addAction(quit)

        self.prenameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.birthdayDateEdit = QDateEdit()
        self.adressLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.placeLineEdit = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        button = QPushButton("Save")

 
        layout.addRow("Vorname:", self.prenameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.birthdayDateEdit)
        layout.addRow("Adresse:", self.adressLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.placeLineEdit)
        layout.addRow("Land:", self.countries)
        layout.addWidget(button)
        button.clicked.connect(self.menu_save)


        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def menu_quit(self):
        self.close()

    def menu_save(self):
        file = open("output.txt", "a", encoding = "utf-8")
        
        Vorname = self.prenameLineEdit.text()
        Name = self.nameLineEdit.text()
        Geburtstag = self.birthdayDateEdit.text()
        Adresse = self.adressLineEdit.text()
        Postleitzahl = self.plzLineEdit.text()
        Ort = self.placeLineEdit.text()
        Land = self.countries.currentText()

        txt = f"{Vorname}, {Name}, {Geburtstag}, {Adresse}, {Postleitzahl}, {Ort}, {Land}"

        file.write(txt + "\n")
        file.close()


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()