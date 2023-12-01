# listm = open('Puzzles/Mouvments_test').read()
listm = open('Puzzles/Mouvments').read()
listm = listm.split("\n")

# Transformer la cale du bateau.
# listc = open('Puzzles/Crates_test').read()
listc = open('Puzzles/Crates').read()
listc = listc.split("\n")


# Transformer la liste en enlevant les espaces et les crochets,
# Cela donne une liste d'éléments et leur hauteur. Les colonnes sont préservées de gauche à droite.
# size_col est le nombre de colonne du bateau.
def transforme(liste):
    futur_liste = []
    for i in range(len(liste[-1])):
        for j in range(len(liste) - 1):
            if liste[j][i] != ' ' and liste[j][i] != ']' and liste[j][i] != '[':
                futur_liste.append([liste[j][i], j])
    return futur_liste


# Enlever les positions des elements et créer les colonnes numérotées.
def recreer(liste):
    futur_liste = []
    id_col = 0
    futur_liste.append(liste[0][0])
    for i in range(len(liste) - 1):
        if int(liste[i][-1]) < int(liste[i + 1][-1]):
            futur_liste.append(liste[i + 1][0])
        else:
            futur_liste.append(id_col + 1)
            id_col += 1
            futur_liste.append(liste[i + 1][0])
    futur_liste.append(id_col + 1)
    return futur_liste


def transforme_en_matrice(liste):
    mat = []
    id_col = 1
    while liste:
        i = 0
        while liste[i] != id_col:
            i += 1
        mat.append(liste[:i])
        liste = liste[i + 1:]
        id_col += 1
    return mat


# Mettre ensemble total et obtenir une matrice.
def transformation_total(liste):
    liste = transforme(liste)
    liste = recreer(liste)
    liste = transforme_en_matrice(liste)
    return liste


listn = transformation_total(listc)
print(listn)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Déplace un élément de d à a.
def deplacer(id_col_depart, id_col_arrivee):
    el_id_col_depart = listn[id_col_depart - 1][0]
    listn[id_col_arrivee - 1].insert(0, el_id_col_depart)
    listn[id_col_depart - 1] = listn[id_col_depart - 1][1:]


# Déplace nb_rep éléments de d à a.
def move(nb_rep, id_col_depart, id_col_arrivee):
    compteur = 0
    while compteur < nb_rep:
        deplacer(id_col_depart, id_col_arrivee)
        compteur += 1


# Déplace selon tous les mouvements de la liste listm.
def all_move():
    for i in range(len(listm)):
        id_col_arrivee = int(listm[i][-1])
        id_col_depart = int(listm[i][-6])
        nb_rep = int(listm[i][5:7])
        move(nb_rep, id_col_depart, id_col_arrivee)


# Donne la réponse.
# '$'.join(liste) redonne la liste avec des $ entre chaque élément.
def reponse():
    liste = []
    for i in range(len(listn)):
        liste.append(listn[i][0])
    liste = ''.join(liste)
    print("Le message à donner aux Elfes est", liste)


all_move()
print(listn)
reponse()


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Recréer notre bateau de départ.
listn = transformation_total(listc)
print(listn)


# d est la colonne de départ sur le bateau.
# a est la colonne d'arrivée sur le bateau.
# Déplace le nb-ème élément (comptage depuis le haut de la colonne) de d à a.
def deplacer_bis(nb, id_col_depart, id_col_arrivee):
    el_id_col_depart = listn[id_col_depart - 1][nb]
    listn[id_col_arrivee - 1].insert(0, el_id_col_depart)
    del listn[id_col_depart - 1][nb]


# Déplace nb éléments en bloc de d à a.
def move_bis(nb, id_col_depart, id_col_arrivee):
    compteur = 0
    id_reste = nb - 1
    while compteur < nb:
        deplacer_bis(id_reste, id_col_depart, id_col_arrivee)
        compteur += 1
        id_reste -= 1


# Déplace selon tous les mouvements de la liste listm.
def all_move_bis():
    for i in range(len(listm)):
        id_col_arrivee = int(listm[i][-1])
        id_col_depart = int(listm[i][-6])
        nb = int(listm[i][5:7])
        move_bis(nb, id_col_depart, id_col_arrivee)


all_move_bis()
print(listn)
reponse()
