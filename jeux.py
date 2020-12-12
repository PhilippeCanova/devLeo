from random import randint
import os

niveauXP = 0 
niveau_general = 1


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
        
def CopierCollerPourDonnerNiveauEtXp():
    XP_display(niveauXP)
    niveau_general = XP_getTotalLevel(niveauXP)
    niveau_display(niveau_general)
#Permet de copier coller l'affichage du niveau et xp (fonction ne marche pas!)

def vague():
    print("------------")
#Permet de faire une ligne de vague ~~

def separation():
    print("------------------------------------------------")
#permet de faire une ligne de tirer --

def XP_add(xp, gain):
    nouveauNiveau = xp + gain
    return nouveauNiveau
#Ajoute des points d'XP / personnage.XP = XP_add(personnage.XP, 50)

def XP_delete(xp, gain):
    # retire des points de vie à niveauXP et retourne un entier représentant le nouveau niveau d'XP"""
    PerdreNiveau = xp - gain
    return PerdreNiveau
#Supprime de l'xp / personnage.XP = XP_delete(personnage.XP, 20)

def XP_display(ChiffreDeXP):
    print("---> XP :", ChiffreDeXP ,"<---")
#Permet d'afficher l'xp du joueur / XP_display(personnage.XP) 

def niveau_display(niveauAcumulé):
    print("---> niveau :", niveauAcumulé ,"<---")
#permet d'afficher le niveau / niveau_display(personnage.niveau_general)

def XP_getTotalLevel(toto):
    level = 0
    if toto >= 100:
        level = 1
    if toto >= 200:
        level = 2
    return level
#Permet de savoir le nb d'xp requis pour passer un niveau

def CombatExemple(personnage):
                    print("Vous vous lancer dans un combat !")
                    print("Vous allez être mis à l'épreuve ! ")
                    print("recherche d'un adversaire... ")
                    vague()
                    #Adversaire = True
                    Adversaire = True
                    RemiseANiveau = True
                    CombatEgal = True
                    while Adversaire != False:
                        premier_num = randint(0,10)
                        print("Trouvé ! votre adversaire et de niveau :", premier_num)
                        vague()
                        if premier_num >= personnage.niveau_general:
                            print("Aïe l'adversaire est meilleur que vous mais vous avez peut être encore une chance de vous en sortir !")
                            NonAbandon = input("Voulez vous poursuivre le combat ? ")
                            separation()
                            if NonAbandon.upper() == "OUI":
                                print("Très bien un bonne aventurier n'abandonne jamais ! ")
                                vague()
                                while RemiseANiveau != 'OUI' :
                                    RemiseANiveau = input("Vous aller tirer un numéro au hasard, si il est plus grand que celui de votre adversaire, vous ménerai un combat à égalité, si l'adverser gagne vous avez définitivement perdu ! Prêt ? >>> ")
                                    separation()
                                    if RemiseANiveau.upper() == "OUI":
                                            Numéro_joueur_5 = randint(1,10)
                                            print("Vous avez tirer le numéro",Numéro_joueur_5)
                                            Numéro_adversaire_5 = randint(1,10)
                                            print("l'adversaire à tirer le numéro",Numéro_adversaire_5)
                                            if Numéro_joueur_5 >= Numéro_adversaire_5:
                                                print("Super ! le combat est à egalité maintenant ! ")
                                                while CombatEgal != "OUI":
                                                    CombatEgal = input("Maintenant si vous remprorter le duel de hasard vous gagner ! Prêt ?! >>> ") 
                                                    if CombatEgal.upper() == "OUI":
                                                        vague()
                                                        Numéro_joueur_2 =randint(1,10)
                                                        print("Vous avez tirer le numéro",Numéro_joueur_2)
                                                        Numéro_adversaire_2 = randint(1,10)
                                                        print("l'adversaire à tirer le numéro",Numéro_adversaire_2)
                                                        if Numéro_joueur_2 >= Numéro_adversaire_2:
                                                            print("Super !!! vous avez gagner !!!")
                                                            print("grâce a votre super performance vous gagner 50XP")
                                                            personnage.niveauXP = XP_add(personnage.XP, 50)
                                                            return 
                                                        elif Numéro_joueur_2 < Numéro_adversaire_2:
                                                            print("Snif, Malheureusement c'est fini... fini si prêt du but... ")
                                                            print("Pour le coup vous perdez 20XP ")
                                                            personnage.deleteXP(20)
                                                            return 
                                                        else:
                                                            print("Problèmes !!!")
                                                    elif RemiseANiveau.upper() == "NON":
                                                        print("Bien revener dès que vous êtes prêt ! ")
                                                    else:
                                                        print("Je n'ai pas compris... répondez par oui ou non...")
                                            elif Numéro_adversaire_5 > Numéro_joueur_5:
                                                print("Snif... Malheuresement c'est fini. Le combat est terminé")
                                                print("Par conséquence vous perdez 20XP ;( ")
                                                personnage.deleteXP(20)
                                                return 
                                            else:
                                                print("Problèmes !!!")
                                    elif RemiseANiveau.upper() == "NON":
                                        print("Bien revener dès que vous êtes prêt ! ")
                                    else:
                                        print("Je n'ai pas compris... répondez par oui ou non")
                            elif NonAbandon.upper() == "NON":
                                print("Bien dommage à plus tard ;(")
                                print("Malheuresement par conséquence vous perdez 10XP")
                                personnage.deleteXP(10)
                                return 
                            else:
                                print("Je n'ai pas compris... réponder par oui ou non... ")
                            print("Bien ")
                        elif premier_num < personnage.niveau_general:
                            print("Super votre niveau est supérieur que celui de votre adversaire ! Cela vous donne un avantage !")
                            print("maintenant vous allez mener un combat avec un avantage désisif")
                            print("vous allez tirez un nombre au hasard entre 1 et 10 et votre adversaire entre 0 et 5. et le plus grad des chiffre l'emporte.")
                            DerWhile = True
                            while DerWhile != "OUI":
                                PrêtNumPlusGrand = input("Par conséquence vous aurez plus de chance que votre adversaire de gagner ! Prêt ? >>> ")
                                if PrêtNumPlusGrand.upper() == "OUI":
                                    vague()
                                    numéro_joueur_8 = randint(1,10)
                                    numéro_adversaire_8 = randint(1,5)
                                    print("Votre numéro est :", numéro_joueur_8)
                                    print("Numéro de l'adversaire est :", numéro_adversaire_8)
                                    if numéro_joueur_8 >= numéro_adversaire_8:
                                        print("Super !!! vous avez gagner !!!")
                                        print("grâce a votre super performance vous gagner 40XP")
                                        personnage.addXP(40)
                                        return 
                                    elif numéro_joueur_8 < numéro_adversaire_8:
                                        print("Snif, Malheureusement c'est fini... fini si prêt du but... ")
                                        print("Pour le coup vous perdez 20XP ")
                                        personnage.XP = XP_delete(personnage.XP, 20)
                                        return 
                                    else:
                                        print("Problèmes !!!")
                                elif PrêtNumPlusGrand.upper() == "NON":
                                    print("Ok revenez quand vous êtes prêt... ")
                                else:
                                    print("Problèmes !!! ")
#Permet de lancer un combat avec les consigne

def CombatPro(personnage):
    Adversaire = True
    RemiseANiveau = True
    CombatEgal = True
    separation()
    while Adversaire != False:
        premier_num = randint(0,10)
        print("votre adversaire et de niveau :", premier_num)
        vague()
        if premier_num >= personnage.niveau_general:
            print("Votre adversaire est meilleur que vous...")
            NonAbandon = input("Voulez vous poursuivre le combat ? ")
            separation()
            if NonAbandon.upper() == "OUI":
                while RemiseANiveau != 'OUI' :
                    RemiseANiveau = input("Prêt ? >>> ")
                    separation()
                    if RemiseANiveau.upper() == "OUI":
                        Numéro_joueur_5 = randint(1,10)
                        print("Vous avez tirer le numéro",Numéro_joueur_5)
                        Numéro_adversaire_5 = randint(1,10)
                        print("l'adversaire à tirer le numéro",Numéro_adversaire_5)
                        if Numéro_joueur_5 >= Numéro_adversaire_5:
                            print("Super ! le combat est à egalité maintenant ! ")
                            while CombatEgal != "OUI":
                                CombatEgal = input("Maintenant si vous remprorter le duel de hasard vous gagner ! Prêt ?! >>> ") 
                                if CombatEgal.upper() == "OUI":
                                    vague()
                                    Numéro_joueur_2 =randint(1,10)
                                    print("Vous avez tirer le numéro",Numéro_joueur_2)
                                    Numéro_adversaire_2 = randint(1,10)
                                    print("l'adversaire à tirer le numéro",Numéro_adversaire_2)
                                    if Numéro_joueur_2 >= Numéro_adversaire_2:
                                        print("Super !!! vous avez gagner !!!")
                                        print("grâce a votre super performance vous gagner 50XP")
                                        personnage.XP = XP_add(personnage.XP, 50)
                                        return 
                                    elif Numéro_joueur_2 < Numéro_adversaire_2:
                                        print("Snif, Malheureusement c'est fini... fini si prêt du but... ")
                                        print("Pour le coup vous perdez 20XP ")
                                        personnage.XP = XP_delete(personnage.XP, 20)
                                        return 
                                    else:
                                        print("Problèmes !!!")
                                elif RemiseANiveau.upper() == "NON":
                                    print("Bien revener dès que vous êtes prêt ! ")
                                else:
                                    print("Je n'ai pas compris... répondez par oui ou non...")
                        elif Numéro_adversaire_5 > Numéro_joueur_5:
                            print("Snif... Malheuresement c'est fini. Le combat est terminé")
                            print("Par conséquence vous perdez 20XP ;( ")
                            personnage.XP = XP_delete(personnage.XP, 20)
                            return 
                        else:
                            print("Problèmes !!!")
                    elif RemiseANiveau.upper() == "NON":
                        print("Bien revener dès que vous êtes prêt ! ")
                    else:
                        print("Je n'ai pas compris... répondez par oui ou non")
            elif NonAbandon.upper() == "NON":
                print("Bien dommage à plus tard ;(")
                print("Malheuresement par conséquence vous perdez 10XP")
                personnage.XP = XP_delete(personnage.XP, 10)
                return 
            else:
                print("Je n'ai pas compris... réponder par oui ou non... ")
                print("Bien ")
        elif premier_num < personnage.niveau_general:
            print("Super votre niveau est supérieur que celui de votre adversaire ! ")
            DerWhile = True
            while DerWhile != "OUI":
                PrêtNumPlusGrand = input("Prêt ? >>> ")
                if PrêtNumPlusGrand.upper() == "OUI":
                    vague()
                    numéro_joueur_8 = randint(1,10)
                    numéro_adversaire_8 = randint(1,5)
                    print("Votre numéro est :", numéro_joueur_8)
                    print("Numéro de l'adversaire est :", numéro_adversaire_8)
                    if numéro_joueur_8 >= numéro_adversaire_8:
                        print("Super !!! vous avez gagner !!!")
                        print("grâce a votre super performance vous gagner 40XP")
                        personnage.XP = XP_add(personnage.XP, 40)
                        return 
                    elif numéro_joueur_8 < numéro_adversaire_8:
                        print("Snif, Malheureusement c'est fini... fini si prêt du but... ")
                        print("Pour le coup vous perdez 20XP ")
                        personnage.XP = XP_delete(personnage.XP, 20)
                        return 
                    else:
                        print("Problèmes !!!")
                elif PrêtNumPlusGrand.upper() == "NON":
                    print("Ok revenez quand vous êtes prêt... ")
                else:
                    print("Je n'ai pas compris... répondez par oui ou non... ")
#Per met de lancer un combat sans consigne

def Lance_jeu_bienvenue():
    separation()
    print(" Bienvenue dans mon jeu ! ")
    separation()
    
    Lance_jeu = True
    while Lance_jeu == True:
        FirstInterface = input(" Veux tu commencer à jouer ? >>> ")
            
        if FirstInterface.upper() == "OUI":
            print("Bien commençons... ")
            Lance_jeu = False
        elif FirstInterface.upper() == 'NON':
            print("Bon, ok, à plus tard peut être... ")
        else:
            print("Je n'ai pas compris... veuillez répondre par oui ou non ")
    separation()
#Permet de Lancer le jeu

def créationMonde():
    Lance_partie = True
    while Lance_partie:
        NewPartie = input(" Voulez-vous créer un nouveau monde ? >>> ")
            
        if NewPartie.upper() == 'OUI':
            print("Très bien... Création du monde... ")
            Lance_partie = False
        elif NewPartie.upper() == 'NON':
            print("très bien... ")
        else:
            print("Je n'ai pas compris... veuillez répondre pas oui ou non ")
    separation()
#permet de créé un monde (un seul possible pour le moment)

def optionPseudo(personnage):
    pseudo = input(" Bien... Choisissez un pseudo >>> ")
    print("Bien à présent vous vous appelerai", pseudo)

    SauvegardePseudo = True
    while SauvegardePseudo:
        ConfirmationPseudo = input("votre pseudo vous convient t'il ? >>> ")
        
        if ConfirmationPseudo.upper() == 'OUI':
            SauvegardePseudo = False
        elif ConfirmationPseudo.upper() == 'NON':
            pseudo = input("Bien quelle sera votre nouveau pseudo >>> ")
        else:
            print("je n'ai pas compris ? répondez par oui ou non... ")
    
    personnage.nom = pseudo
    separation()
    print("Bien à présent vous avez un pseudo ! Bonne chose de faite", pseudo ,"!")
    print("Vous Avez fait votre première action, donc je vous offre 50 XP")
    personnage.XP = XP_add(personnage.XP, 50)
#Permet de gérer les option du pseudo

def optionConsigneNiveau(personnage):
    ComprisConsigne = True
    while ComprisConsigne:
        separation()
        print("Bien maintenant voici les règle concernant le niveau : ")
        vague()
        print("Tout-au long de l'aventure vous serez caractérisé par un niveau.")
        print("suivant les action que vous exécuterai vous gagnerai de l'XP.")
        print("Une fois un certain de nombre d'XP aquis vous passerai des niveau.")
        vague()
        print("A la fin d'une épreuve vous aurez les stat et votre niveau s'affichera comme ceci : ")
        XP_display(personnage.XP)
        niveau_display(personnage.niveau_general)
        separation()

        ChoixComprisConsigne = input("Avez vous compris les consigne en rapport avec le niveau ? >>> ")
            
        if ChoixComprisConsigne.upper() == 'OUI':
            print("Parfais ! ")            
            ComprisConsigne = False
        elif ChoixComprisConsigne.upper() == 'NON':
            print("bien je vous réexplique : ")         
        else:
            print("Je n'ai pas compris... répondez par oui ou non... ")
#Permet de donne les consigne sur le niveau

def règleCommandes():
    vague()
    print("1. Afficher les commandes : /commandes")
    print("2. Démarer un combat en mode entrainement (pour expliquer les règle) : /combat exercice")
    print("3. Lancer un combat en mode pro (Une fois règles compris) /combat")
    vague()
#Permet d'afficher les commandes

def optionConsigneCommand():
    ComprisConsigneCommand = True
    while ComprisConsigneCommand:
        separation()
        print("Bien maintenant voici les règle concernant les commandes : ")
        vague()
        print("1. Afficher les commandes : /commandes")
        print("2. Démarer un combat en mode entrainement (pour expliquer les règle) : /combat exercice")
        print("3. Lancer un combat en mode pro (Une fois règles compris) /combat")
        separation()

        ChoixComprisConsigneCommand = input("Avez vous compris les consigne en rapport avec les commandes ? >>> ")
            
        if ChoixComprisConsigneCommand.upper() == 'OUI':
            print("Parfais... encore une fois ! ")            
            ComprisConsigneCommand = False
            separation()
        elif ChoixComprisConsigneCommand.upper() == 'NON':
            print("bien je vous réexplique : ")         
        else:
            print("Je n'ai pas compris... répondez par oui ou non... ")
#Donne les consigne pour les commandes

def MiseEnAutonomie(personnage):
    separation()
    print("Bien maintenant vous voici en autonomie : ")
    WaitCommand(personnage)
#Permet d'avertir la mise en autonomie

def AffichageSatsNiveau(personnage):
    vague()
    XP_display(personnage.niveauXP)
    niveau_display(personnage.niveau_general)
    vague()
#Afficher les stas du niveau du joueur

def questionaireCapital():
    pass


def WaitCommand(personnage):
    EnterCommand = False
    while EnterCommand != True:
        CommandEnter = input(">>> ")

        if CommandEnter.lower() == "/combat exercice":
            CombatExemple(personnage)
            print("Stats du Combat : ")
            XP_display(personnage.niveauXP)
            niveau_display(personnage.niveau_general)
        elif CommandEnter.lower() == "/combat":
            CombatPro(personnage)
            print("Stats du Combat : ")
            XP_display(personnage.XP)
            niveau_display(personnage.niveau_general)
        elif CommandEnter.lower() == "/commandes":
            règleCommandes()
        elif CommandEnter.lower() == "/niveau":
            AffichageSatsNiveau(personnage)
        else:
            print("Cette Command n'existe pas")
#Permet de lancer le lanceur de command en boucle

"""---------------------------------------------------------------------------"""

personnage = Personnage()


Lance_jeu_bienvenue()

créationMonde()

optionPseudo(personnage)

optionConsigneNiveau(personnage)

optionConsigneCommand()

MiseEnAutonomie(personnage)
