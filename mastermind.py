from random import *

def generercode(level):
    if level == "Facile":
        code = []
        for _ in range(4):
            code.append(randrange(10))
        return code
    elif level == "Moyen":
        code = []
        for _ in range(6):
            code.append(randrange(16))
        return code
    elif level == "Difficile":
        code = []
        for _ in range(7):
            code.append(randrange(21))
        code.append(code[1])
        return code
    elif level == "Extreme":
        code = []   
        for _ in range(20):
            code.append(randrange(50))
        code.append(code[7])
        code.append(code[5])
        return code

def verification(code,proposition):
    nombre_mal_placer=0
    nombre_bien_placer=0
    if proposition == code:
        print("Gagner")
        stop = "True"
        return stop
    if len(proposition) != len(code):
        print("Pas la meme longeur pour rappel : Facile = 4 chiffres ; Moyen = 6 chiffres ; Difficile = 8 chiffres ; Extreme = 20 chiffres")
    else:
        for chiffre in (proposition):
            if chiffre in (code):
                print(chiffre,"Présent dans le code secret")
            else:
                print(chiffre," pas présent dans le code secret")
        for indicep,valeur in enumerate(proposition):
            if proposition[indicep] == code[indicep]:
                nombre_bien_placer +=1
            else:
                nombre_mal_placer += 1 
        print("Il y a ",nombre_mal_placer," chiffre mal placer")
        print("Il y a ",nombre_bien_placer," chiffre bien placer")
    

def jeux():
    print("Bienvenue dans le jeux mastermind\n\n"
    "Les pions de 4 à 8 chiffres différentes + éventuellement une absence de pion\n\n"
    "Niveau : Facile (entier de 0 à 9), Moyen (entier de 0 à 15), Difficile (entier de 0 à 20 + doublon possible), Extrême (entier de 0 à 50 + triplon) \n\n"
    "Longueur du code à trouver : Facile = 4 chiffres ; Moyen = 6 chiffres ; Difficile = 8 chiffres\n\n"
    "Tu as le droit a 12 propositions pour déchiffrer le code\n"
    )
    level = input("Merci de choisir un niveau de difficulté : Facile, Moyen, Difficile :")
    if level == "Facile" or level == "Moyen" or level == "Difficile" or level == "Extreme":
        code = generercode(level)
        for _ in range(12):
            proposition_joueur = input("Entrez une proposition de code pour deviner (separer avec virgule) : ")
            output=proposition_joueur.split(',')
            proposition = []
            for i in output:
                proposition.append(int(i))
            print(proposition)
            stop = verification(code,proposition)
            if stop == "True":
                break
        print("Fin du Jeu")
    else:
        print("NOP ENTRE UN BON LEVEL DE DIFFICULTE ! Relance le jeu ")
    
print(jeux())
