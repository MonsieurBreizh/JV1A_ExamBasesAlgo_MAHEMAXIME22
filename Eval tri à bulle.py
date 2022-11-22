#Exercice 1

#Ecrire un programme permettant de permuter deux valeurs du tableau myTable.

myTable = [1, 3, 2 ,4 ,5]
stock=myTable[0]

print = myTable

stock = myTable[3]
myTable=[]=myTable[2]
stock = myTable[1]

#Exercice 2

#Ecrire un programme permettant le parcours du tableau au cours d''une itération du tri à bulles.

myTable = [1, 5, 3 ,4 ,2]
stock=myTable[0]
for j in range (j+1, len(myTable)) :
            indice=j

print=(myTable)
print(stock)
myTable.pop(indice)
myTable.insert(0,stock)
print(myTable) 


#Exercice 3

print("Le tableau est en désordre je vais le ranger grâce à se dispositif.")
myTable = [2, 3, 4, 1, 5]
stock=myTable[0]
for i in range(0, len(myTable)) :
    for j in range (i+1, len(myTable)) :
        if myTable[j] < myTable[i] :
            if stock > myTable[j] :
                stock = myTable[j]
                indice = j
        else :
            i = i+1
print(myTable)
print(stock)
myTable.pop(indice)
myTable.insert(0,stock)
print(myTable) 

print("Le Tableau est en ordre désormais")

#Exercice 4

#Le tri à bulle est quelque chose de long dans son ensemble puisque le temps que la machine comprenneque le chiffre qui est à prendre en compte est (imaginons 5) elle va regarder quel chiffre n'est pas à sa place et ensuite recalculer le tableau pour la remettre dans le bonne ordre.

# Le temps estimer pour son éxecution (*le programme en entier + son éxecution) prend environ 2 secondes.
