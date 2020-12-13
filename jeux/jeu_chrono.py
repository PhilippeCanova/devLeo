import os, time
from utils import separation, vague
from random import randint
from personnage import Personnage


def jeuTemps(personnage):
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


if __name__ == "__main__":
    personnage = Personnage()
    
    jeuTemps(personnage)
    