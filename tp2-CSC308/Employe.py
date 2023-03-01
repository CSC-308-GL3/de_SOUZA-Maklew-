from datetime import datetime
from Grade import Grade
class Employe:

    def __init__(self, numero, nom,date, qualification:Grade):
        self._numero = numero,
        self._nom = nom,
        self._qualification = qualification,
        self._dateEmbauche = date

    def getNom(self):
        return self._nom
    
    def getNumero(self):
        return self._numero
    
    def getQualification(self):
        return self._qualification
    
    def getDateEmbauche(self):
        return self._dateEmbauche
    
    def getAncienete(self,date):
        dure = date - self._dateEmbauche
        return dure
    
    def coutHoraire(self):
        if (self.getAncienete >= 5 and self.getAncienete <= 10 ): 
            return self._qualification.tauxHoraire * 5/100
        elif (self.getAncienete >=11 and self.getAncienete <= 15 ): 
            return self._qualification.tauxHoraire * 8/100
        else: 
            return self._qualification.tauxHoraire * 12/100