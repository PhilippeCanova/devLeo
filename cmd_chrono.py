import os, time
from utils import separation, vague
from random import randint
from personnage import Personnage

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
        DemandeRegle = input("Voulez vous que je vous rapelle les règles ? >>> ")
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








if __name__ == "__main__":
    personnage = Personnage()
    
    
    jeuTempsExemple(
        personnage,
        '3 et 10',
         3, 
         10,
        2,
        '2xp',
        1,
        '1xp')
    