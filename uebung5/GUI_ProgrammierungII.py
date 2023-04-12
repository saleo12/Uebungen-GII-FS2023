import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self): # Konstruktor
        super().__init__()

        self.setWindowTitle("GUI-Programmierung II") # Fenstertitel definieren
        self.show() # Fenster anzeigen

        #layout erzeugen
        layout = QFormLayout()

        # menu erzeugen
        menubar = self.menuBar()
        # menuauswahl erstellen
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

#----------------------------------------------------------------------------------------------- 

        #gui Elemente erstellen
        self.prenameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.birthdayDateEdit = QDateEdit()
        self.adressLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.placeLineEdit = QLineEdit()
        self.countries = QComboBox()
        button1 = QPushButton("Auf Karte zeigen")
        button2 = QPushButton("Laden")
        button3 = QPushButton("Speichern")

        #spezielle Eigenschaften der gui Elemente definieren
        self.birthdayDateEdit.setDisplayFormat("dd/MM/yyyy")
        self.countries.addItems(["Schweiz", "Ialien", "Deutschland", "Österreich"])

        #gui Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.prenameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.birthdayDateEdit)
        layout.addRow("Adresse:", self.adressLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.placeLineEdit)
        layout.addRow("Land:", self.countries)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

#-----------------------------------------------------------------------------------------------         

        #connects von der Menubar
        laden = QAction("Laden", self)
        laden.triggered.connect(self.menu_laden)
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
        Karte = QAction("Karte", self)
        Karte.triggered.connect(self.menu_karte)
        filemenu.addAction(laden)
        filemenu.addAction(save)
        filemenu.addAction(quit)
        viewmenu.addAction(Karte)
        #connects von den Buttons
        button1.clicked.connect(self.menu_karte)
        button2.clicked.connect(self.menu_laden)
        button3.clicked.connect(self.menu_save)

        # zentrales Widget erstellen und dem Layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

#----------------------------------------------------------------------------------------------- 
    #Funktionen definieren

    def menu_karte(self):
        Adresse = self.adressLineEdit.text()
        Postleitzahl = self.plzLineEdit.text()
        Ort = self.placeLineEdit.text()
        Land = self.countries.currentText()

        Adresse = Adresse.replace (" ","+")

        pfad = f"{Adresse}, {Postleitzahl}, {Ort}, {Land}"
      
        import urllib.parse
        link = "https://www.google.ch/maps/place/"+Adresse+"+"+Postleitzahl+"+"+Ort+"+"+Land
        a = urllib.parse.quote(link)

        QDesktopServices.openUrl(QUrl(link))

#----------------------------------------------------------------------------------------------- 

    def menu_laden(self):
        
        filename, filter = QFileDialog.getOpenFileName(self, "Datei laden", "", "Text Files (*.txt) ;; Python Files (*.py)")
        
        if (filename != ""):
            print(filename)
            print(filter)

            file = open(filename, "r", encoding = "utf-8")
            data = file.readline().strip().split(",")
            v,n,g,a,p,o,l = data

            datum_teile = g.split("/")
            datum = QDate(int(datum_teile[2]), int(datum_teile[1]), int(datum_teile[0]))

            self.prenameLineEdit.setText(v)
            self.nameLineEdit.setText(n)
            self.birthdayDateEdit.setDate(datum)
            self.adressLineEdit.setText(a)
            self.plzLineEdit.setText(p)
            self.placeLineEdit.setText(o)
            self.countries.setCurrentText(l)
       
            file.close()
            print("Daten aus "+filename+" erfolgreich geladen.")

        else:
            self.close()
            print("Laden wurde abgebrochen.")

#-----------------------------------------------------------------------------------------------        

    def menu_save(self):
                
        Vorname = self.prenameLineEdit.text()
        Name = self.nameLineEdit.text()
        Geburtstag = self.birthdayDateEdit.text()
        Adresse = self.adressLineEdit.text()
        Postleitzahl = self.plzLineEdit.text()
        Ort = self.placeLineEdit.text()
        Land = self.countries.currentText()

        txt = f"{Vorname}, {Name}, {Geburtstag}, {Adresse}, {Postleitzahl}, {Ort}, {Land}\n"
        
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")
             
        if filename:
            file = open(filename, "w", encoding = "utf-8")
            file.write(txt)
            file.close() 

            print("Daten wurden in der Datei "+filename+" gespeichert.")

        else:
            print("Daten konnten nicht gespeichert werden.")

#----------------------------------------------------------------------------------------------- 

    def menu_quit(self):
        self.close()    

#----------------------------------------------------------------------------------------------- 

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()