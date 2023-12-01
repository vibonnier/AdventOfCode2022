# liste = open('TreeHouse_test').read()
liste = open('TreeHouse').read()
liste = liste.split("\n")
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Nombre de colonnes et de lignes.
nb_colonne = int(len(liste[0]))
nb_ligne = len(liste)


# Check la visibility par la droite.
def check_right(id_ligne, id_colonne):
    visibility = True
    for i in range(id_colonne + 1, nb_colonne):
        if liste[id_ligne][i] < liste[id_ligne][id_colonne]:
            visibility = True
        else:
            visibility = False
            break
    return visibility


# Check la visibility par la gauche.
def check_left(id_ligne, id_colonne):
    visibility = True
    for i in range(0, id_colonne):
        if liste[id_ligne][i] < liste[id_ligne][id_colonne]:
            visibility = True
        else:
            visibility = False
            break
    return visibility


# Check la visibility par le bas.
def check_bottom(id_ligne, id_colonne):
    visibility = True
    for i in range(id_ligne + 1, nb_ligne):
        if liste[i][id_colonne] < liste[id_ligne][id_colonne]:
            visibility = True
        else:
            visibility = False
            break
    return visibility


# Check la visibility par le haut.
def check_head(id_ligne, id_colonne):
    visibility = True
    for i in range(0, id_ligne):
        if liste[i][id_colonne] < liste[id_ligne][id_colonne]:
            visibility = True
        else:
            visibility = False
            break
    return visibility


def check_de_tous_les_cotes(id_ligne, id_colonne):
    if check_right(id_ligne, id_colonne) or check_left(id_ligne, id_colonne) \
    or check_head(id_ligne, id_colonne) or check_bottom(id_ligne, id_colonne):
        visibility = True
    else:
        visibility = False
    return visibility


def sum_visible():
    sum = 0
    for i in range(nb_ligne):
        for j in range(nb_colonne):
            if check_de_tous_les_cotes(i, j):
                sum += 1
    return sum


print("Le nombre d'arbres visibles est", sum_visible())


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Compter le nb d'éléments vus à droite.
def see_right(id_ligne, id_colonne):
    sum_vu = 0
    i = id_colonne + 1
    try:
        while liste[id_ligne][i] < liste[id_ligne][id_colonne]:
            sum_vu += 1
            i += 1
        sum_vu += 1
        i += 1
    except IndexError:
        pass
    return sum_vu


# Compter le nb d'éléments vus à gauche.
def see_left(id_ligne, id_colonne):
    sum_vu = 0
    i = id_colonne - 1
    if i != -1:
        while liste[id_ligne][i] < liste[id_ligne][id_colonne]:
            if i < 1:
                break
            else:
                sum_vu += 1
                i += - 1
        sum_vu += 1
        i += - 1
    return sum_vu


# Compter le nb d'éléments vus en bas.
def see_bottom(id_ligne, id_colonne):
    sum_vu = 0
    i = id_ligne + 1
    try:
        while liste[i][id_colonne] < liste[id_ligne][id_colonne]:
            sum_vu += 1
            i += 1
        sum_vu += 1
        i += 1
    except IndexError:
        pass
    return sum_vu


# Compter le nb d'éléments vus en haut.
def see_head(id_ligne, id_colonne):
    sum_vu = 0
    i = id_ligne - 1
    if i != -1:
        while liste[i][id_colonne] < liste[id_ligne][id_colonne]:
            if i < 1:
                break
            else:
                sum_vu += 1
                i += - 1
        sum_vu += 1
        i += - 1
    return sum_vu


def see_de_tous_les_cotes(id_ligne, id_colonne):
    scenic_score = see_right(id_ligne, id_colonne) * see_left(id_ligne, id_colonne) \
                 * see_head(id_ligne, id_colonne) * see_bottom(id_ligne, id_colonne)
    return scenic_score


def find_highest_scenic_score():
    scenic_score_max = 0
    for i in range(nb_ligne):
        for j in range(nb_colonne):
            scenic_score_current = see_de_tous_les_cotes(i, j)
            if scenic_score_current > scenic_score_max:
                scenic_score_max = scenic_score_current
    return scenic_score_max


print("The highest scenic score is", find_highest_scenic_score())
