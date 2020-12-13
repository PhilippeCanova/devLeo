#! coding: utf8
# <>
'''
pseudo = input("Quelle est votre nom ? ")
age = input("quelle age a tu ? ")
sport = input("Quelle sport fait tu ? ")

text = "vous vous appeler {} vous avez {}ans et vous faite du {}"
print(text.format(pseudo,age,sport))

validation = input("Es bien cela ? ")
if validation == 'oui' or 'Oui' or 'OUI' or 'OUi' or 'oUI' or 'OuI' or 'oUi' or 'ouI':
    print("Super vous pouvait à present entrer dans notre site ")
elif validation == 'non' or 'Non' or 'NON':
    print("Un problème est survenue relançer le logiciel d'autentification")
else:
    print("relancer le programme")


start=""
while start.upper() != 'OUI': 
    start = input("Voulez vous vous inscrire ? ")
    if start.upper() == 'OUI':
            print("Allons y ! ")
    elif start.lower() == 'non':
            print("bon ben casse toi")
    else:
            print("Je n'ai pas compris")

identifiant = input("Quelle est votre identifiant (prénom) ? ")
modepasse = input("Quelle sera votre mot de passe ? ")
age = input("Quelle est votre age ? ")
sport = input("quelle sport ou activité faitre vous ? ")
date = input("Quelle est votre date de naissance ? ")
ville = input("dans quelle ville êtes vous né ? ")

MenuConfig = "Votre identifiant sera {}, et votre mot de passe ***."
print(MenuConfig.format(identifiant, ))

AficherMdp = input("Pour afficher votre mot de passe faite /mpd")
if AficherMdp.lower() == '/mdp':
    print(AficherMdp.format(modepasse))

MenuPerso = "A propos de vos info : Vous avez {}ans, vous faite de {}, vous êtes né le {} à {} ! "
print(MenuPerso.format(age, sport, date, ville))

correction = print("es bien cela ? ")
if correction == 'oui' or 'Oui' or 'OUI' or 'OUi' or 'oUI' or 'OuI' or 'oUi' or 'ouI':
    print(" nice ")
else:
    print(" bah va te faire foutre ")
    

print("super vous êtes aprésent connecter !! ")

print("vous accèder a l'interface de connexion ! ")

user_id = input("rentrée votre identifiant : ")
user_passworld = input("rentrée votre mot de passe : ")

if user_passworld == modepasse:
    print("Bienvenue a toi", user_id)
else:
    print("mauvais mot de passe")

print("vous êtes rentréé dans notre logiciel ! ")

print("voila vos info : ")
'''

lette = input("Choisissez une lettre : ")

if lette in "aeiouy":
    print("c'est une voyelle")
else:
    print("c'est une consonne")