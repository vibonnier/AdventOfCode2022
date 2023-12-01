# Rappel: A, X rock - B, Y paper - C, Z scissors.
# liste = open('PSR_list_test').read()
liste = open('PSR_list').read()
liste = liste.splitlines(False)
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Calculer si c'est win 6pts, lose 0pt ou draw 3pts à chaque fois.
score = 0
for i in range(len(liste)):
    if liste[i] == "A X" or liste[i] == "B Y" or liste[i] == "C Z":
        score += 3
    elif liste[i] == "A Z" or liste[i] == "B X" or liste[i] == "C Y":
        score += 0
    else:
        score += 6


# Ajouter le score du choix : 1pt for X, 2pts for Y and 3pts for Z.
for i in range(len(liste)):
    if liste[i][2] == "X":
        score += 1
    elif liste[i][2] == "Y":
        score += 2
    else:
        score += 3
print("Notre score est", score)


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# X lose, Y draw and Z win.
# Calculer le score du choix : 1pt for Rock, 2pts for Paper and 3pts for Scissors.
score = 0
for i in range(len(liste)):
    if liste[i] == "A Y" or liste[i] == "B X" or liste[i] == "C Z":
        score += 1
    elif liste[i] == "A Z" or liste[i] == "B Y" or liste[i] == "C X":
        score += 2
    else:
        score += 3


# Ajouter le score de la gagne : 0pt for X, 3pts for Y and 6pts for Z.
for i in range(len(liste)):
    if liste[i][2] == "X":
        score += 0
    elif liste[i][2] == "Y":
        score += 3
    else:
        score += 6

print("Notre nouveau score est", score)
