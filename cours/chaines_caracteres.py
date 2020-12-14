# Pour créer une chaîne de caractère :
variable = "Je crée une variable"
variable = 'Je crée une autre variable'
variable = """Et une troisième
incluant deux lignes"""

# Et avec du cast :
variable = str(10)
variable = str(3.2)
variable = str(False)

# Mais erreur sur 
# variable = 'J'en est créé trois' car apastrophe au milieu
variable = "J'en est créé trois" # mettre ""
variable = 'J\'en est créé trois' # mettre \ pour l'échappement
print(type(variable))

# Changer la case
chaine = "voici une chaine quelconque"
print (chaine.upper())
print (chaine.lower())
print (chaine.capitalize())

# Formater
chaine = "deux un"
chaine = chaine.center(10) # => remplit de vide des deux côtés et retourne un string
print(chaine) 
chaine = chaine.strip() # => retire les espaces en bout
print(chaine) 

chaine2 = "Mon age est de " + " 45 " + "ans"
chaine2 = "Mon age est de " + str(45) + "ans"
# Mais erreur si chaine2 = "Mon age est de " + 45 + "ans"

age = 45
chaine2 = "Je suis {} et mon age est de {} ans".format("Philippe", age) # insère age
print (chaine2)

mot = "test"
chaine = f"Voici un {mot}" # Insère la valeur de la variable dans la chaine
print (chaine)

print (chaine.replace('i', 'x')) # Remplace des lettres ou groupe de lettres

# Information sur la chaîne 
chaine = "abcdefghijklm"
print (len(chaine)) # Longueur de la chaîne
print(chaine[0]) # Premier caractère
print(chaine[-1]) # Dernier caractère
print(chaine[-2]) # Avant dernier caractère
print(chaine[1:3]) # plusieurs caractères
print(chaine[2:]) # enlève les 2 premiers caractères
print(chaine[-5:]) # 5 derniers caractères
print(chaine[1:6:2]) # Saute des lettres
print(chaine[::2]) # Saute des lettres

i = 0 # On appelle l'indice 'i' par convention
while i < len(chaine):
    print(chaine[i]) # On affiche le caractère à chaque tour de boucle
    i += 1

