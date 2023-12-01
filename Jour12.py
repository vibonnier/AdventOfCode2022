# https://www.redblobgames.com/pathfinding/a-star/introduction.html

from queue import PriorityQueue


# liste = open('Heightmap_test').read()
liste = open('Heightmap').read()
liste = liste.split()


class map:

    def __init__(self, abscisse, ordonnee, hauteur):
        self.abscisse = int(abscisse)
        self.ordonnee = int(ordonnee)
        self.hauteur = ord(hauteur)
        self.nom = 'position_' + str(self.abscisse) + '_' + str(self.ordonnee)

    def __str__(self):
        return self.nom

    def __lt__(self, other):
        return self.nom < other.nom


# Créer la map et l'afficher.
def creation_map():
    for j in range(len(liste)):
        for i in range(len(liste[j])):
            if liste[j][i] == 'S':
                globals()['position_' + str(i) + '_' + str(j)] = map(i, j, 'a')
                globals()['start'] = map(i, j, 'a')
            elif liste[j][i] == 'E':
                globals()['position_' + str(i) + '_' + str(j)] = map(i, j, 'z')
                globals()['end'] = map(i, j, 'z')
            else:
                globals()['position_' + str(i) + '_' + str(j)] = map(i, j, liste[j][i])
            print(chr(globals()['position_' + str(i) + '_' + str(j)].hauteur), end='')
        print('')


def position(i, j):
    return globals()['position_' + str(i) + '_' + str(j)]


creation_map()


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def comparer_hauteur(position_current, neighborhood):
    if position_current.hauteur == neighborhood.hauteur - 1 or position_current.hauteur >= neighborhood.hauteur:
        return True
    else:
        return False


def check_if_we_can_move(position_current, neighborhood):
    if comparer_hauteur(position_current, neighborhood):
        return True
    else:
        return False


def set_neighborhood(position_current, deplacement_x, deplacement_y, liste_neighborhood_available):
    try:
        neighborhood_current = position(position_current.abscisse + deplacement_x, position_current.ordonnee + deplacement_y)
        if check_if_we_can_move(position_current, neighborhood_current):
            liste_neighborhood_available.append(neighborhood_current)
    except KeyError:
        pass
    return


def find_neighborhood_available(position_current):
    liste_neighborhood_available = []
    set_neighborhood(position_current, 1, 0, liste_neighborhood_available)
    set_neighborhood(position_current, -1, 0, liste_neighborhood_available)
    set_neighborhood(position_current, 0, 1, liste_neighborhood_available)
    set_neighborhood(position_current, 0, -1, liste_neighborhood_available)
    return liste_neighborhood_available


def distance(position1, position2):
    return abs(position1.abscisse - position2.abscisse) + abs(position1.ordonnee - position2.ordonnee)


def tous_les_chemins():
    which_direction = PriorityQueue()
    which_direction.put((0, start))
    came_from = dict()
    came_from[start.nom] = None
    cost_so_far = dict()
    cost_so_far[start] = 0
    cost_neighborhood_current = 0

    while not which_direction.empty():
        position_current = which_direction.get()
        position_current = position_current[1]
        liste_neighborhood_available = find_neighborhood_available(position_current)

        if position_current.nom == end.nom:
            break

        for neighborhood_current in liste_neighborhood_available:
            cost_neighborhood_current += cost_so_far[position_current] + 1
            if neighborhood_current not in cost_so_far or cost_neighborhood_current < cost_so_far[neighborhood_current]:
                cost_so_far[neighborhood_current] = cost_neighborhood_current
                priority = cost_neighborhood_current + distance(position_current, neighborhood_current)
                which_direction.put((priority, neighborhood_current))
                came_from[neighborhood_current.nom] = position_current.nom
    return came_from


def chemin_plus_court():
    nb_step = 0
    position_current = end.nom
    came_from = dict()
    came_from = tous_les_chemins()
    while position_current != start.nom:
        position_current = came_from[position_current]
        nb_step += 1
    return nb_step


print('The minimal number of steps is', chemin_plus_court())


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


def trouver_hauteur_min():
    liste_hauteur_min = []
    for j in range(len(liste)):
        for i in range(len(liste[j])):
            if position(i, j).hauteur == ord('a'):
                liste_hauteur_min.append(position(i, j))
    return liste_hauteur_min


def tous_les_chemins_bis():
    which_direction = PriorityQueue()
    came_from = dict()
    cost_so_far = dict()

    liste_start_possible = trouver_hauteur_min()
    for i in range(len(liste_start_possible)):
        which_direction.put((0, liste_start_possible[i]))
        came_from[liste_start_possible[i].nom] = None
        cost_so_far[liste_start_possible[i]] = 0

    cost_neighborhood_current = 0

    while not which_direction.empty():
        position_current = which_direction.get()
        position_current = position_current[1]
        liste_neighborhood_available = find_neighborhood_available(position_current)
        if position_current.nom == end.nom:
            break

        for neighborhood_current in liste_neighborhood_available:
            cost_neighborhood_current += cost_so_far[position_current] + 1
            if neighborhood_current not in cost_so_far or cost_neighborhood_current < cost_so_far[neighborhood_current]:
                cost_so_far[neighborhood_current] = cost_neighborhood_current
                priority = cost_neighborhood_current + distance(position_current, neighborhood_current)
                which_direction.put((priority, neighborhood_current))
                came_from[neighborhood_current.nom] = position_current.nom

    return came_from


def chemin_plus_court_bis():
    nb_step = 0
    position_current = end.nom
    came_from = dict()
    came_from = tous_les_chemins_bis()
    while globals()[position_current].hauteur != ord('a'):
        position_current = came_from[position_current]
        nb_step += 1
    return [nb_step, globals()[position_current]]


print('The fewest steps starting from an elevation a is', chemin_plus_court_bis()[0], 'and starts at', chemin_plus_court_bis()[1])