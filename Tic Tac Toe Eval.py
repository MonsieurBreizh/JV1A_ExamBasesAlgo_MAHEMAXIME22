#Partie 2 : Tic Tac Toe ou Morpion

#Exercice 1:

#Ecrire la fonctionnalité permettant d'afficher la grille du jeu

def afficheGrille(tableau):
    for i in range(0,9,3):
        print(tableau[i], tableau[i+1], tableau[i+2])
        grille = [" "," "," "," "," "," "," "," "," "]
tour = 0

#Exercice 2:

#Ecrire la fonctionnalité permettant de jouer un O ou un X.

def ajouteSymbole(tableau,numeroDeTour):
    caseValable = False
    while(not caseValable):
        numeroCase = int(input("Quelle case ?"))
        if(numeroCase <9) and (tableau[numeroCase]!="O") and (tableau[numeroCase]!="X"):
            caseValable = True
    symbole = "O"
    if(numeroDeTour%2==1):
        symbole = "X"
    tableau[numeroCase] = symbole

#Exercice 3:

#Ecrire la fonctionnalité vérifiant si oui ou non l'un des joueurs a réussi à aligner 3 symboles sur une ligne verticale, horizontale, diagonale.

#Dans cette partie de code je vais montrer la fonctionnalité si le joueur à réussi à aligner 3 symboles identiques sur une ligen verticale, horizontale, ou diagonale

def testeVictoireHorizontale(tableau):
    for i in range(0,9,3):
        if((tableau[i] == tableau[i+1] == tableau[i+2]) and (tableau[i]=="O" or tableau[i]=="X")):
            return True
    return False
   
def testeVictoireVerticale(tableau):   
    for i in range(3):
        if((tableau[i] == tableau[i+3] == tableau[i+6]) and (tableau[i]=="O" or tableau[i]=="X")):
            return True
    return False

def testeVictoireDiagonale(tableau):
    if(tableau[4]=="O" or tableau[4]=="X"):
        if((tableau[0] == tableau[4] == tableau[8]) or (tableau[2] == tableau[4] == tableau[6])):
            return True    
    return False


#Exercice 4 :

#Ecrire la fonctionnalité vérifiant si la grille est complète.

#Ensuite je vais voir si quand je complète ma grille la console s'arrête.

tour+=1
def afficheGrille(grille):
    ajouteSymbole(grille,tour)
victoire = testeVictoireHorizontale(grille) or testeVictoireVerticale(grille) or testeVictoireDiagonale(grille)
if(victoire):
    print("Bravo vous êtes le grand champion !")
else:
    print("Vous avez fait match nul !")

#Exercice 5 :

#Ecrire un programme permettant de jouer à deux au Tic Tac Toe.

def afficheGrille(tableau):
    for i in range(0,9,3):
        print(tableau[i], tableau[i+1], tableau[i+2])

def ajouteSymbole(tableau,numeroDeTour):
    caseValable = False
    while(not caseValable):
        numeroCase = int(input("Quelle case ?"))
        if(numeroCase <9) and (tableau[numeroCase]!="O") and (tableau[numeroCase]!="X"):
            caseValable = True
    symbole = "O"
    if(numeroDeTour%2==1):
        symbole = "X"
    tableau[numeroCase] = symbole

def testeVictoireHorizontale(tableau):
    for i in range(0,9,3):
        if((tableau[i] == tableau[i+1] == tableau[i+2]) and (tableau[i]=="O" or tableau[i]=="X")):
            return True
    return False
   
def testeVictoireVerticale(tableau):   
    for i in range(3):
        if((tableau[i] == tableau[i+3] == tableau[i+6]) and (tableau[i]=="O" or tableau[i]=="X")):
            return True
    return False

def testeVictoireDiagonale(tableau):
    if(tableau[4]=="O" or tableau[4]=="X"):
        if((tableau[0] == tableau[4] == tableau[8]) or (tableau[2] == tableau[4] == tableau[6])):
            return True    
    return False


#ici débute le programme principal
grille = [" "," "," "," "," "," "," "," "," "]
tour = 0
victoire = False 
while(not victoire and tour < 9):
    tour+=1
    afficheGrille(grille)
    ajouteSymbole(grille,tour)
    victoire = testeVictoireHorizontale(grille) or testeVictoireVerticale(grille) or testeVictoireDiagonale(grille)
if(victoire):
    print("Bravo vous êtes le grand champion !")
else:
    print("Vous avez fait match nul !")


#Exerice 6 : 

#Qu'aura t-on besoin de faire, si on souhaite désormais programmer un jeu de puissance 4 ?

#Pour jouer à un puissance 4 il faudra désormais jouer avec des rond mais qui ont une couleur différente (rouge et jaune) et pour cela on peut utiliser colorama.
#De plus, il faudra rajouter d'avantages de cases que ce soit en hauteur qu'en longueur. Il faudra bien évidemment comme le nom l'indique, indiquer que si l'on met 4 jetons de même couleur que ce soit en verticale, en diagonale ou en horizontale.