# Les variables permettent de stocker des valeurs
ma_variable = 12

""" Les noms de variable :
    - ne doivent pas commencer par un chiffre
    - éviter les caractères accuentués
    - commencer par une majuscule pour nommer les classes
    - utiliserLeCamelCase ou utiliser_les_underscores
"""

# Quand une variable est sur la gauche d'un =, on affecte une valeur
ma_variable = 2

# Affectation multiple 
variable1, test, facteur, message = 10, False, 3.2, "ok test"

# Quand une variable est sur la froite, on l'utilise.
ma_variable = ma_variable * 2

""" Les types de données principaux sont :
    - les entiers (integer)
    - les décimaux (float)
    - les chaînes de caractères (string)
    - les bouléens (bool)
    - None => absence de valeurs
    - les objets propres à Python ou créés par toi
"""

# Pour convertir un type, il existe des fonctions
chaine = str(variable1)
entier = int(chaine)
test = bool('')
print(test)

# On ne peut pas mélanger les types
# print(message + variable1) => entraine une erreur
# mais :
print(message + str(variable1) )

# Pour conntaîre la valeur d'une variable, on l'afficher avec print
print(chaine)
print(chaine, entier) # Affiche plusieurs valeurs
# Mais cela ne donne pas le type

# Pour connaître le type d'une variable, utiliser la fonction type()
type(entier) # retourne <class 'int'>
print(type(test)) # retourne <class 'bool'> sur la console 

# Exemple d'objet
import decimal
pi = decimal.Decimal('3.0') #Pi est un objet <class 'decimal.Decimal'>
print(type(pi))

# Certaines fonctions retournent des valeurs pouvant être récupérées
# dans des variables
une_variable = input('Entrer un mot')
# d'autre s'exécute sans rien retourner (donc en retournant None par défaut)
une_autre_variable = print("Je retourne None: ")
print(une_autre_variable) 