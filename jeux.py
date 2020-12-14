from random import randint
import os, sys
import time
from winsound import Beep

from personnage import Personnage
from utils import vague, separation

from cmd_combat import CombatExemple, CombatPro
from cmd_chrono import jeuTempsNormal



def Lance_jeu_bienvenue():
    separation()
    print(" Bienvenue dans mon jeu ! ")
    separation()

    Lance_jeu = True
    while Lance_jeu == True:
        FirstInterface = input(" Veux tu commencer à jouer ? >>> ")

        if FirstInterface.upper() == "OUI":
            print("Bien commençons... ")
            time.sleep(1)
            Lance_jeu = False
        elif FirstInterface.upper() == 'NON':
            print("Bon, ok, à plus tard peut être... ")
            separation()
        else:
            print("Je n'ai pas compris... veuillez répondre par oui ou non ")
            separation()
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
    personnage.addXP(50)
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
        personnage.display_niveaux()
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
    personnage.display_niveaux()
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

def WaitCommand(personnage):
    EnterCommand = False
    while EnterCommand != True:
        os.system('cls')
        CommandEnter = input(">>> ")

        if CommandEnter.lower() == "/combat exercice":
            CombatExemple(personnage)
            print("Stats du Combat : ")
            personnage.display_niveaux()
        elif CommandEnter.lower() == "/combat":
            CombatPro(personnage)
            print("Stats du Combat : ")
            personnage.display_niveaux()
        elif CommandEnter.lower() == "/commandes":
            règleCommandes()
        elif CommandEnter.lower() == "/niveau":
            AffichageSatsNiveau(personnage)
        elif CommandEnter.lower() in ["/questions credit", "/qc"]:
            questionaireCredit()
        elif CommandEnter.lower() in ["/jeu seconde", "/js"]:
            jeuTempsNormal(personnage)
        else:
            print("Cette Command n'existe pas")
# Permet de lancer le lanceur de command en boucle


"""---------------------------------------------------------------------------"""

personnage = Personnage()

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
