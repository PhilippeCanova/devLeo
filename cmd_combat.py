import os, time
from utils import separation, vague
from random import randint
from personnage import Personnage


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
                                        personnage.addXP(50)
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
                        personnage.deleteXP(20)
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
                                        personnage.addXP(50)
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
                        personnage.addXP(40)
                        return
                    elif numéro_joueur_8 < numéro_adversaire_8:
                        print(
                            "Snif, Malheureusement c'est fini... fini si prêt du but... ")
                        print("Pour le coup vous perdez 20XP ")
                        personnage.deleteXP(20)
                        return
                    else:
                        print("Problèmes !!!")
                elif PrêtNumPlusGrand.upper() == "NON":
                    print("Ok revenez quand vous êtes prêt... ")
                else:
                    print("Je n'ai pas compris... répondez par oui ou non... ")
# Per met de lancer un combat sans consigne
