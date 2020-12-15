import os, time
from utils import separation, vague
from random import randint
from personnage import Personnage

choix_niveau = {
    'noob': ['2 et 5', 2, 5, 1, '1xp', 1, '1xp'],
    'debutant': ['3 et 10', 3, 10, 2, '2xp', 1, '1xp'],
    'normal':['5 et 15', 5, 15, 3, '3xp', 2, '2xp'],
    'avance':['10 et 20',
        10,
        20,
        4,
        '4xp',
        2,
        '2xp'],
    'expert':['15 et 25',
        15,
        25,
        5,
        '5xp',
        2,
        '2xp'],
    'pro':['20 et 30',
        20,
        30,
        6,
        '6xp',
        3,
        '2xp'],
    'maitre':['25 et 35',
        25,
        35,
        7,
        '7xp',
        3,
        '3xp'],
    'grandmaitre':['30 et 40',
        30,
        40,
        8,
        '8xp',
        4,
        '4xp'],
    'master':['35 et 45',
        35,
        45,
        9,
        '9xp',
        4,
        '4xp'],
    'champion':['40 et 50',
        40,
        50,
        10,
        '10xp',
        5,
        '5xp'],
    'insane':['50 et 60',
        50,
        60,
        11,
        '11xp',
        5,
        '5xp'],
    'legendaire':['60 et 90',
        60,
        90,
        12,
        '12xp',
        6,
        '6xp'],
}

def ChoixNiveau(personnage):  
    choixNiv = True
    while choixNiv != False:
        for cle in choix_niveau.keys():
            print(f"--> {cle}")

        nivChoix = input("Choisissez un niveau de difficulté >>> ")

        if nivChoix in choix_niveau.keys():
            p1, p2, p3, p4, p5, p6, p7 = choix_niveau[nivChoix]
            jeuTempsExemple( personnage, p1, p2, p3, p4, p5, p6, p7)
            choixNiv = False
        else:
            print("Je n'ai pas compris... choisissez un niveau de difficulter... ")

"""--------------------------------------------------------------"""

def jeuTempsExemple(
    personnage,
    nbSeconde,
    nbRandintMin,
    nbRandintMax,
    nbXpadd,
    messXpAdd,
    nbXpDelete,
    messXpDelete):
    autreDemandeRegle = True
    os.system('cls')
    print("Bienvenue ! ")
    vague()
    while autreDemandeRegle != False:
        DemandeRegle = input("Voulez vous que je vous rapelle les règles ? >>>  ")
        if DemandeRegle.upper() == 'OUI':
            os.system('cls')
            separation()
            print("Ok, les voici : ")
            vague()
            print("Le but de ce jeu sera d'essayer en comptant le nombre de seconde dans sa tête de donner le nombre exact de seconde après le 'go' ")
            print("Le nombre de seconde que vous devriez trouver sera entre", nbSeconde, "seconde ")
            separation()

            ComprisRegleChrono = True
            while ComprisRegleChrono != False:
                ComprisRegleChrono = input("Avez vous compris les règles ? >>> ")
                if ComprisRegleChrono.upper() == 'OUI':
                    print("Très bien c'est partie ! ")
                    autreDemandeRegle = False
                    ComprisRegleChrono = False
                elif ComprisRegleChrono.upper() == 'NON':
                    print("Ok je vous laisse encore un peu de temps pour les relire... ")
                    vague()
                else:
                    print("Je n'ai pas compris répondez par oui ou non ")
                    vague()
        
        elif DemandeRegle.upper() == 'NON':
            print("Parfais ! ")
            time.sleep(1)
            os.system('cls')
            autreDemandeRegle = False
        else:
            print("Je n'ai pas compris répondez par oui pou non ")
            separation()
            time.sleep(2)
            os.system('cls')

    AlorsRejouerChrono = True
    while AlorsRejouerChrono != 'NON':
        os.system('cls')
        NombreSeconde = randint(nbRandintMin, nbRandintMax)
        separation()
        print("C'est parti ! ")
        vague()
        print("Recherche d'un nombre aléatoire entre", nbSeconde,"...")
        time.sleep(2)
        print("Trouvé ! préparer vous...")
        time.sleep(5)
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
        vague()
        
        if resultat_seconde == NombreSeconde:
            personnage.addXP(nbXpadd)
            print("Super, vous gagner", messXpAdd)
            separation()
        else:
            personnage.deleteXP(nbXpDelete)
            print("Malheuresement vous perdez", messXpDelete)
            separation()
        
        RejouerChrono = True
        while RejouerChrono != False:

            AlorsRejouerChrono = input("Voulez vous rejouer ? >>> ")
            if AlorsRejouerChrono.upper() == 'OUI':
                RejouerChrono = False
            elif AlorsRejouerChrono.upper() == 'NON':
                RejouerChrono = False
                AlorsRejouerChrono = False
                return
            else:
                print("Je n'ai pas compris, répondez par oui ou non... ")

"""--------------------------------------------------------------"""

def jeuTempsNoob(personnage):
    jeuTempsExemple(
        personnage,
        '2 et 5',
        2,
        5,
        1,
        '1xp',
        1,
        '1xp')

def jeuTempsDebutant(personnage):
    jeuTempsExemple(
        personnage,
        '3 et 10',
        3, 
        10,
        2,
        '2xp',
        1,
        '1xp')

def jeuTempsNormal(personnage):
    autreDemandeRegle = True
    os.system('cls')
    print("Bienvenue ! ")
    vague()
    while autreDemandeRegle != False:
        DemandeRegle = input("Voulez vous que je vous rapelle les règles ? >>> ")
        if DemandeRegle.upper() == 'OUI':
            os.system('cls')
            separation()
            print("Ok, les voici : ")
            vague()
            print("Le but de ce jeu sera d'essayer en comptant le nombre de seconde dans sa tête de donner le nombre exact de seconde après le 'go' ")
            print("Le nombre de seconde que vous devriez trouver sera entre 5 et 15 seconde ")
            separation()

            ComprisRegleChrono = True
            while ComprisRegleChrono != False:
                ComprisRegleChrono = input("Avez vous compris les règles ? >>> ")
                if ComprisRegleChrono.upper() == 'OUI':
                    print("Très bien c'est partie ! ")
                    autreDemandeRegle = False
                    ComprisRegleChrono = False
                elif ComprisRegleChrono.upper() == 'NON':
                    print("Ok je vous laisse encore un peu de temps pour les relire... ")
                    vague()
                else:
                    print("Je n'ai pas compris répondez par oui ou non ")
                    vague()
        
        elif DemandeRegle.upper() == 'NON':
            print("Parfais ! ")
            time.sleep(1)
            os.system('cls')
            autreDemandeRegle = False
        else:
            print("Je n'ai pas compris répondez par oui pou non ")
            separation()
            time.sleep(2)
            os.system('cls')

    AlorsRejouerChrono = True
    while AlorsRejouerChrono != 'NON':
        os.system('cls')
        NombreSeconde = randint(5, 15)
        separation()
        print("C'est parti ! ")
        vague()
        print("Recherche d'un nombre aléatoire entre 5 et 15...")
        time.sleep(2)
        print("Trouvé ! préparer vous...")
        time.sleep(5)
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
        vague()
        
        if resultat_seconde == NombreSeconde:
            personnage.addXP(3)
            print("Super, vous gagner 3xp ! ")
            separation()
        else:
            personnage.deleteXP(2)
            print("Malheuresement vous perdez 2xp...")
            separation()
        
        RejouerChrono = True
        while RejouerChrono != False:

            AlorsRejouerChrono = input("Voulez vous rejouer ? >>> ")
            if AlorsRejouerChrono.upper() == 'OUI':
                RejouerChrono = False
            elif AlorsRejouerChrono.upper() == 'NON':
                RejouerChrono = False
                AlorsRejouerChrono = False
                return
            else:
                print("Je n'ai pas compris, répondez par oui ou non... ")


    # fait le jeu seconde

def jeuTempsAvance(personnage):
    jeuTempsExemple(
        personnage,
        '10 et 20',
        10,
        20,
        4,
        '4xp',
        2,
        '2xp')

def jeuTempsExpert(personnage):
    jeuTempsExemple(
        personnage,
        '15 et 25',
        15,
        25,
        5,
        '5xp',
        2,
        '2xp')

def jeuTempsPro(personnage):
    jeuTempsExemple(
        personnage,
        '20 et 30',
        20,
        30,
        6,
        '6xp',
        3,
        '2xp')

def jeuTempsMaitre(personnage):
    jeuTempsExemple(
        personnage,
        '25 et 35',
        25,
        35,
        7,
        '7xp',
        3,
        '3xp')

def jeuTempsGrandMaitre(personnage):
    jeuTempsExemple(
        personnage,
        '30 et 40',
        30,
        40,
        8,
        '8xp',
        4,
        '4xp')

def jeuTempsMaster(personnage):
    jeuTempsExemple(
        personnage,
        '35 et 45',
        35,
        45,
        9,
        '9xp',
        4,
        '4xp')

def jeuTempsChampion(personnage):
    jeuTempsExemple(
        personnage,
        '40 et 50',
        40,
        50,
        10,
        '10xp',
        5,
        '5xp')

def jeuTempsInsane(personnage):
    jeuTempsExemple(
        personnage,
        '50 et 60',
        50,
        60,
        11,
        '11xp',
        5,
        '5xp')

def jeuTempsLegendaire(personnage):
    jeuTempsExemple(
        personnage,
        '60 et 90',
        60,
        90,
        12,
        '12xp',
        6,
        '6xp')







if __name__ == "__main__":
    personnage = Personnage()
