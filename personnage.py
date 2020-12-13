
class Personnage (object):
    def __init__(self):
        self.nom = ""
        self.monde = ""
        self.XP = 0
        self.niveau_general = 0

    def addXP(self, valeur):
        self.XP = self.XP + valeur
        self.defineTotalLevel()

    def deleteXP(self, valeur):
        self.XP = self.XP - valeur
        if self.XP < 0:
            self.XP = 0
        self.defineTotalLevel()

    def defineTotalLevel(self):
        if self.XP > 100:
            self.niveau_general = 1
        if self.XP > 200:
            self.niveau_general = 2

    def display_niveaux(self):
        print("---> XP :", self.XP, "<---")
        print("---> niveau :", self.niveau_general, "<---")
    
