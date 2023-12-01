# Une façon d'ouvrir un fichier dans Python.
# Ici "read" considère chaque caractère distinct ou des nombres.
# Une autre façon (celle que tout le monde utilise sur internet)
# with open('Elf_list','r') as f :
# Cette formulation demande une suite par ex dans une boucle, etc.
# liste = open('Elf_list_test').read()
liste = open('Elf_list').read()


# Créé un nouvel élément de la liste après chaque espace, mais du coup, les supprime tous sans distinction.
# liste = liste.split()
# Sinon fait comme "split" mais garde en mémoire les espaces.
liste = liste.splitlines(True)
print(liste)


# "int" transforme en nombre et append ajout à une liste.
# Créer une liste de nombre et parfois du vide.
futur_liste = []
for i in range(len(liste)):
    if len(liste[i]) > 1:
        futur_liste.append(int(liste[i]))
    else:
        futur_liste.append([])
liste = futur_liste
print(liste)


# Sommer et Arrêter quand on tombe sur du vide.
futur_liste = [0]
id_futur_liste = 0
for i in range(len(liste)):
    if not liste[i]:
        futur_liste.append(0)
        id_futur_liste += 1
    else:
        futur_liste[id_futur_liste] += liste[i]
liste = futur_liste
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Trouver le plus grand élément de la liste.
nb_calories_max = 0
id_elf = 0
for i in range(len(liste)):
    if liste[i] > nb_calories_max:
        nb_calories_max = liste[i]
        id_elf = i
    else:
        nb_calories_max = nb_calories_max
        id_elf = id_elf
print("L'elfe numéro", id_elf + 1, "transporte le plus de nourriture avec", nb_calories_max, "calories")


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Sommer les 3 plus grand élément de la liste.
sum_max_calories = 0
compteur = 0
while compteur < 3:
    compteur += 1
    sum_max_calories += max(liste)
    liste.remove(max(liste))
print("Les 3 elfes avec le plus de nourriture transportent à eux trois", sum_max_calories, "calories")
