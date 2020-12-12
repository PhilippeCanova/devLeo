
def definitNomDuMonde():
    return "Mon monde"

def definitNomDuJoueur():
    return "Léo"

def displayConsigne():
    print ("Voilà ce que tu as faire")

def definitCommande():
    Lance_partie2 = False
    while not Lance_partie2:
        NewPartie = input(" Quelle commande voulez-vous lancer ? >>>")
        if (NewPartie[0] != "/"):
            print("Votre commande doit commencer par un /")
        else:
            Lance_partie2=True    
    return NewPartie.upper()



if __name__ == "__main__":
    nomDuMonde = ""
    nomDuJoueur = ""

    # Choix du monde
    nomDuMonde = definitNomDuMonde()

    # Choix Pseudo
    nomDuJoueur = definitNomDuJoueur()

    # Affichage consigne 
    displayConsigne()

    # Boucle commande do until Quit 
    commande = None

    while commande != "/QUIT":

        # # Entrer commande
        commande = definitCommande()
        
        # # Réalisation du jeu
        if commande == '/JEU':
            # Execute le jeu
            print ("Lancement de JEU")

print ("Au revoir !")