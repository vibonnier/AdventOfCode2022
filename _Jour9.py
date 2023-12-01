# liste = open('Deplacements_test').read()
liste = open('Deplacements').read()
liste = liste.split()
print(liste)


# Création de la grille. Chaque élément est un point sur la grille.
class grille:

        def __init__(self, abscisse, ordonnee):
            self.abscisse = int(abscisse)
            self.ordonnee = int(ordonnee)
            self.etat = '.'


# Encoder la taille de la grille en longueur.
def longueur_grille():
    long_current = 0
    long_max_right = 0
    long_max_left = 0
    for i in range(len(liste)):
        if liste[i] == 'R':
            long_current += int(liste[i + 1])
            if long_current > long_max_right and long_current > 0:
                long_max_right = long_current
        elif liste[i] == 'L':
            long_current -= int(liste[i + 1])
            if long_current < long_max_left and long_current < 0:
                long_max_left = long_current
    return [long_max_right, long_max_left]


# Encoder la taille de la grille en hauteur.
def hauteur_grille():
    haut_current = 0
    haut_max_head = 0
    haut_max_bottom = 0
    for i in range(len(liste)):
        if liste[i] == 'U':
            haut_current += int(liste[i + 1])
            if haut_current > haut_max_head and haut_current > 0:
                haut_max_head = haut_current
        elif liste[i] == 'D':
            haut_current -= int(liste[i + 1])
            if haut_current < haut_max_bottom and haut_current < 0:
                haut_max_bottom = haut_current
    return [haut_max_head,  haut_max_bottom]


def position(i, j):
    position_i_j = globals()['position_' + str(i) + '_' + str(j)]
    return position_i_j


# Créer la grille via les éléments position_ij.
def creation():
    longueur_right = longueur_grille()[0]
    longueur_left = longueur_grille()[1]
    hauteur_head = hauteur_grille()[0]
    hauteur_bottom = hauteur_grille()[1]
    for i in range(longueur_left, longueur_right + 1):
        for j in range(hauteur_bottom, hauteur_head + 1):
            globals()['position_' + str(i) + '_' + str(j)] = grille(i, j)


def afficher_grille():
    longueur_right = longueur_grille()[0]
    longueur_left = longueur_grille()[1]
    hauteur_head = hauteur_grille()[0]
    hauteur_bottom = hauteur_grille()[1]
    for i in reversed(range(hauteur_bottom, hauteur_head + 1)):
        for j in range(longueur_left, longueur_right + 1):
            print(position(j, i).etat, end='')
        print(i)
    return


creation()


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def deplacer_H(i):
    if liste[i] == 'R':
        H.abscisse += 1
    elif liste[i] == 'L':
        H.abscisse -= 1
    elif liste[i] == 'U':
        H.ordonnee += 1
    elif liste[i] == 'D':
        H.ordonnee -= 1


def deplacer_T():
    # mouvements de gauche - droite
    if T.abscisse - H.abscisse == 2 and T.ordonnee == H.ordonnee:
        T.abscisse = H.abscisse + 1
    elif T.abscisse - H.abscisse == -2 and T.ordonnee == H.ordonnee:
        T.abscisse = H.abscisse - 1
    # mouvements de haut - bas
    elif T.ordonnee - H.ordonnee == 2 and T.abscisse == H.abscisse:
        T.ordonnee = H.ordonnee + 1
    elif T.ordonnee - H.ordonnee == -2 and T.abscisse == H.abscisse:
        T.ordonnee = H.ordonnee - 1
    # mouvements diagonale via abscisse
    elif T.abscisse - H.abscisse == -1 and T.ordonnee - H.ordonnee == -2:
        T.ordonnee = H.ordonnee - 1
        T.abscisse = H.abscisse
    elif T.abscisse - H.abscisse == 1 and T.ordonnee - H.ordonnee == -2:
        T.ordonnee = H.ordonnee - 1
        T.abscisse = H.abscisse
    elif T.abscisse - H.abscisse == 1 and T.ordonnee - H.ordonnee == 2:
        T.ordonnee = H.ordonnee + 1
        T.abscisse = H.abscisse
    elif T.abscisse - H.abscisse == -1 and T.ordonnee - H.ordonnee == 2:
        T.ordonnee = H.ordonnee + 1
        T.abscisse = H.abscisse
    # mouvements diagonale via ordonnée
    elif T.abscisse - H.abscisse == -2 and T.ordonnee - H.ordonnee == 1:
        T.ordonnee = H.ordonnee
        T.abscisse = H.abscisse - 1
    elif T.abscisse - H.abscisse == -2 and T.ordonnee - H.ordonnee == -1:
        T.ordonnee = H.ordonnee
        T.abscisse = H.abscisse - 1
    elif T.abscisse - H.abscisse == 2 and T.ordonnee - H.ordonnee == -1:
        T.ordonnee = H.ordonnee
        T.abscisse = H.abscisse + 1
    elif T.abscisse - H.abscisse == 2 and T.ordonnee - H.ordonnee == 1:
        T.ordonnee = H.ordonnee
        T.abscisse = H.abscisse + 1
    else:
        pass


def deplacer_tout():
    globals()['H'] = grille(0, 0)
    globals()['T'] = grille(0, 0)
    position_0_0.etat = '#'
    for i in range(0, len(liste), 2):
        for j in range(1, int(liste[i + 1]) + 1):
            deplacer_H(i)
            deplacer_T()
            position(T.abscisse, T.ordonnee).etat = '#'


# Compter les états #.
def comptage():
    sum = 0
    longueur_right = longueur_grille()[0]
    longueur_left = longueur_grille()[1]
    hauteur_head = hauteur_grille()[0]
    hauteur_bottom = hauteur_grille()[1]
    for i in range(longueur_left, longueur_right + 1):
        for j in range(hauteur_bottom, hauteur_head + 1):
            if position(i, j).etat == '#':
                sum += 1
    return sum


deplacer_tout()
afficher_grille()
print('The tail of the rope visited', comptage(), 'positions.')


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# liste = open('Deplacements2_test').read()
liste = open('Deplacements2').read()
liste = liste.split()
print(liste)
creation()


def T(i):
    Ti = globals()['T' + str(i)]
    return Ti


# Déplacer H = Tail_0.
def deplacer_Head(i):
    if liste[i] == 'R':
        T0.abscisse += 1
    elif liste[i] == 'L':
        T0.abscisse -= 1
    elif liste[i] == 'U':
        T0.ordonnee += 1
    elif liste[i] == 'D':
        T0.ordonnee -= 1


# Ti suit Tj.
def deplacer_Tail(i, j):

    # mouvements de gauche - droite
    if T(i).abscisse - T(j).abscisse == 2 and T(i).ordonnee == T(j).ordonnee:
        T(i).abscisse = T(j).abscisse + 1
    elif T(i).abscisse - T(j).abscisse == -2 and T(i).ordonnee == T(j).ordonnee:
        T(i).abscisse = T(j).abscisse - 1

    # mouvements de haut - bas
    elif T(i).ordonnee - T(j).ordonnee == 2 and T(i).abscisse == T(j).abscisse:
        T(i).ordonnee = T(j).ordonnee + 1
    elif T(i).ordonnee - T(j).ordonnee == -2 and T(i).abscisse == T(j).abscisse:
        T(i).ordonnee = T(j).ordonnee - 1

    # mouvements diagonales via abscisse
    elif T(i).abscisse - T(j).abscisse == -1 and T(i).ordonnee - T(j).ordonnee == -2:
        T(i).ordonnee = T(j).ordonnee - 1
        T(i).abscisse = T(j).abscisse
    elif T(i).abscisse - T(j).abscisse == 1 and T(i).ordonnee - T(j).ordonnee == -2:
        T(i).ordonnee = T(j).ordonnee - 1
        T(i).abscisse = T(j).abscisse
    elif T(i).abscisse - T(j).abscisse == -1 and T(i).ordonnee - T(j).ordonnee == 2:
        T(i).ordonnee = T(j).ordonnee + 1
        T(i).abscisse = T(j).abscisse
    elif T(i).abscisse - T(j).abscisse == 1 and T(i).ordonnee - T(j).ordonnee == 2:
        T(i).ordonnee = T(j).ordonnee + 1
        T(i).abscisse = T(j).abscisse

    # mouvements diagonales via ordonnée
    elif T(i).abscisse - T(j).abscisse == -2 and T(i).ordonnee - T(j).ordonnee == 1:
        T(i).ordonnee = T(j).ordonnee
        T(i).abscisse = T(j).abscisse - 1
    elif T(i).abscisse - T(j).abscisse == 2 and T(i).ordonnee - T(j).ordonnee == 1:
        T(i).ordonnee = T(j).ordonnee
        T(i).abscisse = T(j).abscisse + 1
    elif T(i).abscisse - T(j).abscisse == -2 and T(i).ordonnee - T(j).ordonnee == -1:
        T(i).ordonnee = T(j).ordonnee
        T(i).abscisse = T(j).abscisse - 1
    elif T(i).abscisse - T(j).abscisse == 2 and T(i).ordonnee - T(j).ordonnee == -1:
        T(i).ordonnee = T(j).ordonnee
        T(i).abscisse = T(j).abscisse + 1

    # mouvements diagonales abscisse!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif T(i).abscisse - T(j).abscisse <= -1 and T(i).ordonnee - T(j).ordonnee <= -2:
        T(i).ordonnee = T(j).ordonnee - 1
        T(i).abscisse = T(j).abscisse - 1
    elif T(i).abscisse - T(j).abscisse >= 1 and T(i).ordonnee - T(j).ordonnee <= -2:
        T(i).ordonnee = T(j).ordonnee - 1
        T(i).abscisse = T(j).abscisse + 1
    elif T(i).abscisse - T(j).abscisse >= 1 and T(i).ordonnee - T(j).ordonnee >= 2:
        T(i).ordonnee = T(j).ordonnee + 1
        T(i).abscisse = T(j).abscisse + 1
    elif T(i).abscisse - T(j).abscisse <= -1 and T(i).ordonnee - T(j).ordonnee >= 2:
        T(i).ordonnee = T(j).ordonnee + 1
        T(i).abscisse = T(j).abscisse - 1

    # mouvements diagonales ordonnée !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif T(i).abscisse - T(j).abscisse <= -2 and T(i).ordonnee - T(j).ordonnee >= 1:
        T(i).ordonnee = T(j).ordonnee + 1
        T(i).abscisse = T(j).abscisse - 1
    elif T(i).abscisse - T(j).abscisse <= -2 and T(i).ordonnee - T(j).ordonnee <= -1:
        T(i).ordonnee = T(j).ordonnee - 1
        T(i).abscisse = T(j).abscisse - 1
    elif T(i).abscisse - T(j).abscisse >= 2 and T(i).ordonnee - T(j).ordonnee <= -1:
        T(i).ordonnee = T(j).ordonnee - 1
        T(i).abscisse = T(j).abscisse + 1
    elif T(i).abscisse - T(j).abscisse >= 2 and T(i).ordonnee - T(j).ordonnee >= 1:
        T(i).ordonnee = T(j).ordonnee + 1
        T(i).abscisse = T(j).abscisse + 1
    else:
        pass


def deplacer_tout_bis():
    for i in range(0, 10):
        globals()['T' + str(i)] = grille(0, 0)
    position_0_0.etat = '#'
    for i in range(0, len(liste), 2):
        for nb_move in range(1, int(liste[i + 1]) + 1):
            deplacer_Head(i)
            for id_tail in range(1, 10):
                deplacer_Tail(id_tail, id_tail - 1)
                position(T9.abscisse, T9.ordonnee).etat = '#'


deplacer_tout_bis()
afficher_grille()
print('The tail of the rope visited', comptage(), 'positions.')
