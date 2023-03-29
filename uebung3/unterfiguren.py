import math
from figur import *

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x},{self.y})"

class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__("Dreieck")
        self.a = a
        self.b = b
        self.c = c

    def umfang(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Dreieck (Seite a ={self.a}, Seite b ={self.b}, Seite c={self.c})"
    
class Rechteck(Figur):
    def __init__(self, h, l):
        super().__init__("Rechteck")
        self.h = h
        self.l = l

    def umfang(self):
        return 2*(abs(self.h)) + 2*(abs(self.l))
    
    def __str__(self):
        return f"Rechteck (Hoehe ={self.h}, Laenge ={self.l})"


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius
       
    def umfang(self):
        return self.radius * 2 * math.pi
    
    def __str__(self):
        return f"Kreis (Mittelpunkt = {self.mittelpunkt}, Radius={self.radius})"
    

class Polygon(Figur):
    def __init__(self, punkte_liste):
        super().__init__("Polygon")
        self.punkte_liste = punkte_liste

    # def umfang(self):             (funktioniert nicht)
    #    anzahl = 0
    #    for pkt in range(len(self.punkte_liste)):
    #        strecke = dist(self.punkte_liste [i+1] - self.punkte_liste[i]) 
    #        anzahl = anzahl + 1
    #    return sum(strecke)

    

M = Punkt(2,3)
k1 = Kreis(M, 10)
d1 = Dreieck(3,4,5)
r1 = Rechteck(5,6)

print(M)
print(k1)
print(k1.name, k1.umfang())
print(d1)
print(d1.name, d1.umfang())
print(r1)
print(r1.name, r1.umfang())