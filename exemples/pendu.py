mots = [ # Lsite parmi laquelle on va choisir un mot 
    'ordinateur', 'maison', 'ecole', 'minecraft', 'lait', 'orange']

steps = [ # Figures représentant le pendu 
"""
    
          
          
         
          

""",

"""
    
          
          
         
          
___ __
""",
"""
    
          
          
   |       
   |       
___|__
""",
"""
    
   /        
   |        
   |       
   |       
___|__
""",
"""
    ________
   /        
   |        
   |       
   |       
___|__
""",

    """
    ________
   /        |
   |        
   |       
   |       
___|__
""",
"""
    ________
   /        |
   |        O
   |       
   |       
___|__
""",
"""
    ________
   /        |
   |        O
   |       /|\\
   |       
___|__
""",
"""
    ________
   /        |
   |        O
   |       /|\\
   |       /\\
___|__
"""
]

# Imports
from random import randint
import sys, os

def lance_manche():
    """ Boucle correspondant à une manche 
        Ne retourne rien
    """
    step = 0
    mot_choisi = mots[randint(0, len(mots))] # Choisi un mot dans la liste dispo
    pattern = "_"*len(mot_choisi)            # Créé la chaîne vide à affichée
    list_pattern = list(pattern)             # Liste des lettres déjà trouvées et leur emplacement

    while True:
        os.system('cls')
        print ("Mot à trouver : ", pattern)
        print("Encore {} essais.".format(len(steps)-step))
        print (steps[step])
        lettre = input('Propose une lettre : ') # Demande la lettre
        bonne_lettre = False
        for index, l in enumerate(mot_choisi):  # Parcourt la liste des lettres du mots
            if l == lettre:             # La lettre est valable
                bonne_lettre = True
                list_pattern[index] = lettre # Indique que la lettre est trouvée (remplçant ainsi le _ à cet endroit)  
                pattern = "".join(list_pattern) # Reconstitue le pattern à partir de la liste des lettres trouvées
                
        if not bonne_lettre: # La lettre proposée n'est pas bonne
            step = step + 1
        
        if step == len(steps): # Si on est au bout de la liste des figures, on a perdu
            print('Vous avez perdu. Le bon mot était : ', mot_choisi)
            break

        if pattern.find('_') == -1: # Il ne reste plus de _, le jeu est gagné. 
            print("C'est gagné !! Bravo. ")
            break

if __name__ == "__main__":
    print ("Bienvenue dans le jeu du pendu.")
    while True: # Toujours vrai. On se sert de break pour sortir

        lance_manche() # Lance une partie

        rejoue = input("Veux-tu rejouer ? Entre Q pour quitter ou autre chose pour rejouer... ")
        if rejoue.upper() == 'Q': # Termine le jeu.
            print ("Au revoir")
            break 


