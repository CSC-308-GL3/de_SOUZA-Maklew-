from Employe import Employe
class Intervention:

    def __init__(self, numero, date, duree, tarifkm,technicien:Employe):
        self._numero = numero,
        self._date = date,
        self._duree = duree,
        self._tarifkm = tarifkm
        self._technicien = technicien

    ##Procédure affiche
    def affiche(self):
       print("numero:"+self._numero,"date:"+self._date, "durée:"+self._duree,"tarif:"+self._tarifkm,"technicien:"+self._technicien.getNom)

    ##Fonction fraisKm
    def fraisKm(self, dist):
        frais=self._tarifkm * dist
        return frais 

    ##Fonction fraisMo
    def fraisMo(self):
        return self._tarifkm


   
        