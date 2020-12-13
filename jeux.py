from random import randint
import os
import time
from winsound import Beep

#from jeux.trouvenote import leJeu

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
# Permet de copier coller l'affichage du niveau et xp (fonction ne marche pas!)


def vague():
    print("------------")
# Permet de faire une ligne de vague ~~


def separation():
    print("------------------------------------------------")
# permet de faire une ligne de tirer --


def XP_add(xp, gain):
    nouveauNiveau = xp + gain
    return nouveauNiveau
# Ajoute des points d'XP / personnage.XP = XP_add(personnage.XP, 50)


def XP_delete(xp, gain):
    # retire des points de vie à niveauXP et retourne un entier représentant le nouveau niveau d'XP"""
    PerdreNiveau = xp - gain
    return PerdreNiveau
# Supprime de l'xp / personnage.XP = XP_delete(personnage.XP, 20)


def XP_display(ChiffreDeXP):
    print("---> XP :", ChiffreDeXP, "<---")
# Permet d'afficher l'xp du joueur / XP_display(personnage.XP)


def niveau_display(niveauAcumulé):
    print("---> niveau :", niveauAcumulé, "<---")
# permet d'afficher le niveau / niveau_display(personnage.niveau_general)


def XP_getTotalLevel(toto):
    level = 0
    if toto >= 100:
        level = 1
    if toto >= 200:
        level = 2
    return level
# Permet de savoir le nb d'xp requis pour passer un niveau


def CombatExemple(personnage):
    os.system('cls')
    print("Vous vous lancer dans un combat !")
    print("Vous allez être mis à l'épreuve ! ")
    print("recherche d'un adversaire... ")
    vague()
    #Adversaire = True
    Adversaire = True
    RemiseANiveau = True
    CombatEgal = True
    while Adversaire != False:
        premier_num = randint(0, 10)
        print("Trouvé ! votre adversaire et de niveau :", premier_num)
        vague()
        if premier_num >= personnage.niveau_general:
            print("Aïe l'adversaire est meilleur que vous mais vous avez peut être encore une chance de vous en sortir !")
            NonAbandon = input("Voulez vous poursuivre le combat ? ")
            separation()
            if NonAbandon.upper() == "OUI":
                print("Très bien un bonne aventurier n'abandonne jamais ! ")
                vague()
                while RemiseANiveau != 'OUI':
                    RemiseANiveau = input(
                        "Vous aller tirer un numéro au hasard, si il est plus grand que celui de votre adversaire, vous ménerai un combat à égalité, si l'adverser gagne vous avez définitivement perdu ! Prêt ? >>> ")
                    separation()
                    if RemiseANiveau.upper() == "OUI":
                        Numéro_joueur_5 = randint(1, 10)
                        print("Vous avez tirer le numéro", Numéro_joueur_5)
                        Numéro_adversaire_5 = randint(1, 10)
                        print("l'adversaire à tirer le numéro",
                              Numéro_adversaire_5)
                        if Numéro_joueur_5 >= Numéro_adversaire_5:
                            print("Super ! le combat est à egalité maintenant ! ")
                            while CombatEgal != "OUI":
                                CombatEgal = input(
                                    "Maintenant si vous remprorter le duel de hasard vous gagner ! Prêt ?! >>> ")
                                if CombatEgal.upper() == "OUI":
                                    vague()
                                    Numéro_joueur_2 = randint(1, 10)
                                    print("Vous avez tirer le numéro",
                                          Numéro_joueur_2)
                                    Numéro_adversaire_2 = randint(1, 10)
                                    print("l'adversaire à tirer le numéro",
                                          Numéro_adversaire_2)
                                    if Numéro_joueur_2 >= Numéro_adversaire_2:
                                        print("Super !!! vous avez gagner !!!")
                                        print(
                                            "grâce a votre super performance vous gagner 50XP")
                                        personnage.niveauXP = XP_add(
                                            personnage.XP, 50)
                                        return
                                    elif Numéro_joueur_2 < Numéro_adversaire_2:
                                        print(
                                            "Snif, Malheureusement c'est fini... fini si prêt du but... ")
                                        print("Pour le coup vous perdez 20XP ")
                                        personnage.deleteXP(20)
                                        return
                                    else:
                                        print("Problèmes !!!")
                                elif RemiseANiveau.upper() == "NON":
                                    print(
                                        "Bien revener dès que vous êtes prêt ! ")
                                else:
                                    print(
                                        "Je n'ai pas compris... répondez par oui ou non...")
                        elif Numéro_adversaire_5 > Numéro_joueur_5:
                            print(
                                "Snif... Malheuresement c'est fini. Le combat est terminé")
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
            print(
                "Super votre niveau est supérieur que celui de votre adversaire ! Cela vous donne un avantage !")
            print("maintenant vous allez mener un combat avec un avantage désisif")
            print("vous allez tirez un nombre au hasard entre 1 et 10 et votre adversaire entre 0 et 5. et le plus grad des chiffre l'emporte.")
            DerWhile = True
            while DerWhile != "OUI":
                PrêtNumPlusGrand = input(
                    "Par conséquence vous aurez plus de chance que votre adversaire de gagner ! Prêt ? >>> ")
                if PrêtNumPlusGrand.upper() == "OUI":
                    vague()
                    numéro_joueur_8 = randint(1, 10)
                    numéro_adversaire_8 = randint(1, 5)
                    print("Votre numéro est :", numéro_joueur_8)
                    print("Numéro de l'adversaire est :", numéro_adversaire_8)
                    if numéro_joueur_8 >= numéro_adversaire_8:
                        print("Super !!! vous avez gagner !!!")
                        print("grâce a votre super performance vous gagner 40XP")
                        personnage.addXP(40)
                        return
                    elif numéro_joueur_8 < numéro_adversaire_8:
                        print(
                            "Snif, Malheureusement c'est fini... fini si prêt du but... ")
                        print("Pour le coup vous perdez 20XP ")
                        personnage.XP = XP_delete(personnage.XP, 20)
                        return
                    else:
                        print("Problèmes !!!")
                elif PrêtNumPlusGrand.upper() == "NON":
                    print("Ok revenez quand vous êtes prêt... ")
                else:
                    print("Problèmes !!! ")
# Permet de lancer un combat avec les consigne


def CombatPro(personnage):
    os.system('cls')
    Adversaire = True
    RemiseANiveau = True
    CombatEgal = True
    separation()
    while Adversaire != False:
        premier_num = randint(0, 10)
        print("votre adversaire et de niveau :", premier_num)
        vague()
        if premier_num >= personnage.niveau_general:
            print("Votre adversaire est meilleur que vous...")
            NonAbandon = input("Voulez vous poursuivre le combat ? ")
            separation()
            if NonAbandon.upper() == "OUI":
                while RemiseANiveau != 'OUI':
                    RemiseANiveau = input("Prêt ? >>> ")
                    separation()
                    if RemiseANiveau.upper() == "OUI":
                        Numéro_joueur_5 = randint(1, 10)
                        print("Vous avez tirer le numéro", Numéro_joueur_5)
                        Numéro_adversaire_5 = randint(1, 10)
                        print("l'adversaire à tirer le numéro",
                              Numéro_adversaire_5)
                        if Numéro_joueur_5 >= Numéro_adversaire_5:
                            print("Super ! le combat est à egalité maintenant ! ")
                            while CombatEgal != "OUI":
                                CombatEgal = input(
                                    "Maintenant si vous remprorter le duel de hasard vous gagner ! Prêt ?! >>> ")
                                if CombatEgal.upper() == "OUI":
                                    vague()
                                    Numéro_joueur_2 = randint(1, 10)
                                    print("Vous avez tirer le numéro",
                                          Numéro_joueur_2)
                                    Numéro_adversaire_2 = randint(1, 10)
                                    print("l'adversaire à tirer le numéro",
                                          Numéro_adversaire_2)
                                    if Numéro_joueur_2 >= Numéro_adversaire_2:
                                        print("Super !!! vous avez gagner !!!")
                                        print(
                                            "grâce a votre super performance vous gagner 50XP")
                                        personnage.XP = XP_add(
                                            personnage.XP, 50)
                                        return
                                    elif Numéro_joueur_2 < Numéro_adversaire_2:
                                        print(
                                            "Snif, Malheureusement c'est fini... fini si prêt du but... ")
                                        print("Pour le coup vous perdez 20XP ")
                                        personnage.XP = XP_delete(
                                            personnage.XP, 20)
                                        return
                                    else:
                                        print("Problèmes !!!")
                                elif RemiseANiveau.upper() == "NON":
                                    print(
                                        "Bien revener dès que vous êtes prêt ! ")
                                else:
                                    print(
                                        "Je n'ai pas compris... répondez par oui ou non...")
                        elif Numéro_adversaire_5 > Numéro_joueur_5:
                            print(
                                "Snif... Malheuresement c'est fini. Le combat est terminé")
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
                    numéro_joueur_8 = randint(1, 10)
                    numéro_adversaire_8 = randint(1, 5)
                    print("Votre numéro est :", numéro_joueur_8)
                    print("Numéro de l'adversaire est :", numéro_adversaire_8)
                    if numéro_joueur_8 >= numéro_adversaire_8:
                        print("Super !!! vous avez gagner !!!")
                        print("grâce a votre super performance vous gagner 40XP")
                        personnage.XP = XP_add(personnage.XP, 40)
                        return
                    elif numéro_joueur_8 < numéro_adversaire_8:
                        print(
                            "Snif, Malheureusement c'est fini... fini si prêt du but... ")
                        print("Pour le coup vous perdez 20XP ")
                        personnage.XP = XP_delete(personnage.XP, 20)
                        return
                    else:
                        print("Problèmes !!!")
                elif PrêtNumPlusGrand.upper() == "NON":
                    print("Ok revenez quand vous êtes prêt... ")
                else:
                    print("Je n'ai pas compris... répondez par oui ou non... ")
# Per met de lancer un combat sans consigne


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
# Permet de Lancer le jeu


def créationMonde():
    Lance_partie = True
    while Lance_partie:
        NewPartie = input(" Voulez-vous créer un nouveau monde ? >>> ")

        if NewPartie.upper() == 'OUI':
            print("Très bien... Création du monde... ")
            time.sleep(2)
            Lance_partie = False
        elif NewPartie.upper() == 'NON':
            print("très bien... ")
            time.sleep(1)
            os.system('cls')
        else:
            print("Je n'ai pas compris... veuillez répondre pas oui ou non ")
            time.sleep(2)
            os.system('cls')
    separation()
# permet de créé un monde (un seul possible pour le moment)


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
    print("Bien à présent vous avez un pseudo ! Bonne chose de faite", pseudo, "!")
    print("Vous Avez fait votre première action, donc je vous offre 50 XP")
    personnage.XP = XP_add(personnage.XP, 50)
# Permet de gérer les option du pseudo


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

        ChoixComprisConsigne = input(
            "Avez vous compris les consigne en rapport avec le niveau ? >>> ")

        if ChoixComprisConsigne.upper() == 'OUI':
            print("Parfais ! ")
            time.sleep(2)
            ComprisConsigne = False
        elif ChoixComprisConsigne.upper() == 'NON':
            os.system('cls')
            print("bien je vous réexplique : ")
        else:
            os.system('cls')
            print("Je n'ai pas compris... répondez par oui ou non... ")
# Permet de donne les consigne sur le niveau

def règleCommandes():
    os.system('cls')
    vague()
    print("1. Afficher les commandes : /commandes")
    print("2. Démarer un combat en mode entrainement (pour expliquer les règle) : /combat exercice")
    print("3. Lancer un combat en mode pro (Une fois règles compris) /combat")
    print("4. afficher les crédit de façon ludique : /questions credit OU /qc")
    print("5. pour lancer le mini jeu seconde : /jeu seconde OU /js")
    vague()
# Permet d'afficher les commandes

def optionConsigneCommand():
    ComprisConsigneCommand = True
    while ComprisConsigneCommand:
        separation()
        print("Bien maintenant voici les règle concernant les commandes : ")
        vague()
        print("1. Afficher les commandes : /commandes")
        print("2. Démarer un combat en mode entrainement (pour expliquer les règle) : /combat exercice")
        print("3. Lancer un combat en mode pro (Une fois règles compris) /combat")
        print("4. afficher les crédit de façon ludique : /questions credit OU /qc")
        print("5. pour lancer le mini jeu seconde : /jeu seconde OU /js")
        separation()

        ChoixComprisConsigneCommand = input(
            "Avez vous compris les consigne en rapport avec les commandes ? >>> ")

        if ChoixComprisConsigneCommand.upper() == 'OUI':
            print("Parfais... encore une fois ! ")
            time.sleep(2)
            os.system('cls')
            ComprisConsigneCommand = False
            separation()
        elif ChoixComprisConsigneCommand.upper() == 'NON':
            print("bien je vous réexplique : ")
            time.sleep(2)
            os.system('cls')
        else:
            print("Je n'ai pas compris... répondez par oui ou non... ")
            time.sleep(2)
            os.system('cls')
# Donne les consigne pour les commandes

def MiseEnAutonomie(personnage):
    separation()
    print("Bien maintenant vous voici en autonomie : ")
    WaitCommand(personnage)
# Permet d'avertir la mise en autonomie

def AffichageSatsNiveau(personnage):
    vague()
    XP_display(personnage.niveauXP)
    niveau_display(personnage.niveau_general)
    vague()
# Afficher les stas du niveau du joueur

def questionaireCredit():
    un_1 = True
    deux_1 = True
    os.system('cls')
    while un_1 != False:
        separation()
        print("Qui est le développeur de ce jeu ? ")
        vague()
        print("A. Thomas Canova")
        print("B. Leo Canova")
        print("C. Philippe Canova")
        print("D. Cécile Alcais")
        vague()
        un_1 = input(">>> ")
        if un_1.lower() == "a":
            os.system('cls')
            print(
                "Non, il a servie de testeur aux bêta mais n'est pas le développeur officiel... ")
        elif un_1.lower() == "b":
            os.system('cls')
            print(
                "Très bien ! en effet Leo Canova est le principal développeur du jeu... ")
            un_1 = False
        elif un_1.lower() == "c":
            os.system('cls')
            print(
                "Non, il a beaucoup aidé à la création du jeu mais n'ai pas le principal développeur... ")
        elif un_1.lower() == "d":
            os.system('cls')
            print(
                "Non, elle a servie de testeur aux bêta mais n'est pas le développeur officiel... ")
        else:
            os.system('cls')
            print("Je n'ai pas compris répondez par A, B, C ou D... ")

    while deux_1 != False:
        separation()
        print("Avec quelle script ce jeu est développer ? ")
        vague()
        print("A. JavaScript")
        print("B. C++")
        print("C. Python")
        print("D. Jungo")
        vague()
        deux_1 = input(">>> ")
        if deux_1.lower() == "a":
            os.system('cls')
            print("Non, c'est faux... ")
        elif deux_1.lower() == "b":
            os.system('cls')
            print("Non, c'est faux... ")
        elif deux_1.lower() == "c":
            os.system('cls')
            print("Très bien, le jeu a bien était développer en python... ")
            separation()
            deux_1 = False
        elif deux_1.lower() == "d":
            os.system('cls')
            print("Non, c'est faux... ")
        else:
            print("Je n'ai pas compris répondez par A, B, C ou D... ")

    print("--+ Crédit +--")
    print("Développeur : Léo Canova")
    print("Développeurs adjoin : Philippe Canova et Jason Champagne")
    print("Testeurs : Thomas Canova et Cécile Alcais")
    vague()
    AimeCredit = True
    while AimeCredit != False:
        NoteCredit = input("Notez mon jeu entre 0 et 10... >>> ")
        try:
            NoteCredit = int(NoteCredit)
        except:
            NoteCredit = -1
        if 7 <= NoteCredit <= 10:
            print("Merci beaucoup ! ")
            time.sleep(4)
            AimeCredit = False
        elif 5 <= NoteCredit <= 6:
            print("Super c'est pas trop mal ! merci... ")
            time.sleep(4)
            AimeCredit = False
        elif 3 <= NoteCredit <= 4:
            print("Bah... je vais essayer de m'améliorer")
            time.sleep(4)
            AimeCredit = False
        elif 0 <= NoteCredit <= 2:
            print("Ohh... bon, ok...")
            time.sleep(4)
            AimeCredit = False
        else:
            print("Euh, c'est entre 0 et 10... ")
# fait les question crédit

def jeuTemps():
    os.system('cls')
    separation()
    print("Bienvenue...")
    time.sleep(3)
    print("Le but de ce jeu sera d'essayer en comptant le nombre de seconde dans sa tête de donner le nombre exact de seconde après le 'go' ")
    time.sleep(9)
    print("Le nombre de seconde que vous devriez trouver sera entre 5 et 15 seconde ")
    vague()
    time.sleep(6)
    NombreSeconde = randint(5, 15)
    print("Recherche d'un nombre aléatoire entre 5 et 15...")
    time.sleep(3)
    print("Trouvé ! préparer vous...")
    time.sleep(7)
    print("GO !!! ")
    time.sleep(NombreSeconde)
    print("STOP !!!")
    vague()
    resultat_seconde = input("Combien de seconde il y a t'il eu à votre avis ? >>> ")
    try:
        resultat_seconde = int(resultat_seconde)
    except:
        resultat_seconde = -1
    if resultat_seconde == NombreSeconde:
        print("Wouaw ! impresionant ! vous avez trouvé !")
        time.sleep(2)
    elif resultat_seconde == NombreSeconde -1 or resultat_seconde == NombreSeconde +1:
        print("Presque dommage... à une seconde près... ")
        time.sleep(2)
    else:
        print("C'est perdu... ")
        time.sleep(2)
    
    vague()
    print("Le nombre à trouvé était : ", NombreSeconde)
    time.sleep(10)
# fait le jeu seconde

def WaitCommand(personnage):
    EnterCommand = False
    while EnterCommand != True:
        os.system('cls')
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
        elif CommandEnter.lower() == "/questions credit" or "/qc":
            questionaireCredit()
        elif CommandEnter.lower() == "/jeu seconde" or "/js":
            jeuTemps()
        else:
            print("Cette Command n'existe pas")
# Permet de lancer le lanceur de command en boucle


"""---------------------------------------------------------------------------"""

personnage = Personnage()

jeuTemps()

os.system('cls')
Lance_jeu_bienvenue()
os.system('cls')
créationMonde()
os.system('cls')
optionPseudo(personnage)
os.system('cls')
optionConsigneNiveau(personnage)
os.system('cls')
optionConsigneCommand()
os.system('cls')
MiseEnAutonomie(personnage)
