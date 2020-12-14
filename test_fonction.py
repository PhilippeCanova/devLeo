def calcule(nombre1, nombre2):
    print("les nombre sont {} et :"   )

def faitTonChoix(
    message1,
    messagePrompt,
    reponseSort,
    messageSort,
    reponseNegatif,
    messageNegatif,
    messageAbsurbe ):
    boucle = True
    while boucle:
        print(message1)
        entree = input(messagePrompt)
        if entree.upper() == reponseSort:
            boucle = False
            print(messageSort)
        elif entree.upper() == reponseNegatif:
            print (messageNegatif)
        else:
            print (messageAbsurbe)

def faitTonDoubleChoix(
    message1,
    messagePrompt,
    reponseSort,
    messageSort,
    reponseNegatif,
    messageNegatif,
    messageAbsurbe ):
    boucle = True
    while boucle:
        print(message1)
        entree = input(messagePrompt)
        if entree.upper() == reponseSort:
            print(messageSort)
            return reponseSort
        elif entree.upper() == reponseNegatif:
            print (messageNegatif)
            return reponseNegatif
        else:
            print (messageAbsurbe)

retour = faitTonDoubleChoix(
    "Salut mon poulet, veux-tu jouer ?",
    "Tappe OUI si tu veux jouer >>>",
    "OUI",
    "OK, nous allons jouer.",
    "NON",
    "Bon, ben j'attends alors que tu te décides.",
    "Euh, pas comprendre"
)
if retour == "OUI":
    print ("J'ajoute des points")
else:
    print ("Je retranche des points")
    

faitTonChoix(
    "On va tester ton QI.",
    "Es-tu idiot ? >>> ",
    "NON",
    "Bon, alors tu es intellignet.",
    "OUI",
    "Bon, ben tu trop couillon.",
    "Euh, pas comprendre"
)
