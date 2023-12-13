# https://www.redblobgames.com/pathfinding/a-star/introduction.html
import timeit
from queue import PriorityQueue


# liste = open('Puzzles/Heightmap_test').read()
liste = open('Puzzles/Heightmap').read()
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


def comparer_hauteur(position_current, neighbor):
    if position_current.hauteur == neighbor.hauteur - 1 or position_current.hauteur >= neighbor.hauteur:
        return True
    else:
        return False


def check_if_we_can_move(position_current, neighbor_current):
    if comparer_hauteur(position_current, neighbor_current):
        return True
    else:
        return False


def set_neighborhood(position_current, deplacement_x, deplacement_y, liste_neighbors_available):
    try:
        neighbor_current = position(position_current.abscisse + deplacement_x, position_current.ordonnee + deplacement_y)
        if check_if_we_can_move(position_current, neighbor_current):
            liste_neighbors_available.append(neighbor_current)
    except KeyError:
        pass
    return


def find_neighbors_available(position_current):
    liste_neighbors_available = []
    set_neighborhood(position_current, 1, 0, liste_neighbors_available)
    set_neighborhood(position_current, -1, 0, liste_neighbors_available)
    set_neighborhood(position_current, 0, 1, liste_neighbors_available)
    set_neighborhood(position_current, 0, -1, liste_neighbors_available)
    return liste_neighbors_available


def distance(position1, position2):
    return abs(position1.abscisse - position2.abscisse) + abs(position1.ordonnee - position2.ordonnee)


def tous_les_chemins_A_star_algorithm():
    which_direction = PriorityQueue()
    which_direction.put((0, start))
    came_from = dict()
    came_from[start.nom] = None
    cost_so_far = dict()
    cost_so_far[start] = 0
    cost_neighbor_current = 0

    while not which_direction.empty():
        position_current = which_direction.get()
        position_current = position_current[1]
        liste_neighbors_available = find_neighbors_available(position_current)

        if position_current.nom == end.nom:
            break

        for neighbor_current in liste_neighbors_available:
            cost_neighbor_current += cost_so_far[position_current] + 1
            if neighbor_current not in cost_so_far or cost_neighbor_current < cost_so_far[neighbor_current]:
                cost_so_far[neighbor_current] = cost_neighbor_current
                priority = cost_neighbor_current + distance(position_current, neighbor_current)
                which_direction.put((priority, neighbor_current))
                came_from[neighbor_current.nom] = position_current.nom
    return came_from


def chemin_plus_court():
    nb_step = 0
    position_current = end.nom
    came_from = dict()
    came_from = tous_les_chemins_A_star_algorithm()
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


def tous_les_chemins_A_star_algorithm_bis():
    which_direction = PriorityQueue()
    came_from = dict()
    cost_so_far = dict()

    liste_start_possible = trouver_hauteur_min()
    for i in range(len(liste_start_possible)):
        which_direction.put((0, liste_start_possible[i]))
        came_from[liste_start_possible[i].nom] = None
        cost_so_far[liste_start_possible[i]] = 0

    cost_neighbor_current = 0

    while not which_direction.empty():
        position_current = which_direction.get()
        position_current = position_current[1]
        liste_neighbors_available = find_neighbors_available(position_current)
        if position_current.nom == end.nom:
            break

        for neighbor_current in liste_neighbors_available:
            cost_neighbor_current += cost_so_far[position_current] + 1
            if neighbor_current not in cost_so_far or cost_neighbor_current < cost_so_far[neighbor_current]:
                cost_so_far[neighbor_current] = cost_neighbor_current
                priority = cost_neighbor_current + distance(position_current, neighbor_current)
                which_direction.put((priority, neighbor_current))
                came_from[neighbor_current.nom] = position_current.nom

    return came_from


def chemin_plus_court_bis():
    nb_step = 0
    position_current = end.nom
    came_from = dict()
    came_from = tous_les_chemins_A_star_algorithm_bis()
    while globals()[position_current].hauteur != ord('a'):
        position_current = came_from[position_current]
        nb_step += 1
    return [nb_step, globals()[position_current]]


print('The fewest steps starting from an elevation a is', chemin_plus_court_bis()[0], 'and starts at', chemin_plus_court_bis()[1])


####################################################################################################################
# REMARQUES ######################################################################################################
####################################################################################################################

# Speed test for the different algorithms.

def tous_les_chemins_greedy_best_first_search():
    which_direction = PriorityQueue()
    which_direction.put((0, start))
    came_from = dict()
    came_from[start.nom] = None
    cost_so_far = dict()
    cost_so_far[start] = 0
    cost_neighbor_current = 0

    while not which_direction.empty():
        position_current = which_direction.get()
        position_current = position_current[1]
        liste_neighbors_available = find_neighbors_available(position_current)

        if position_current.nom == end.nom:
            break

        for neighbor_current in liste_neighbors_available:
            cost_neighbor_current += cost_so_far[position_current] + 1
            if neighbor_current not in cost_so_far or cost_neighbor_current < cost_so_far[neighbor_current]:
                cost_so_far[neighbor_current] = cost_neighbor_current
                priority = distance(position_current, neighbor_current)
                which_direction.put((priority, neighbor_current))
                came_from[neighbor_current.nom] = position_current.nom
    return came_from


def tous_les_chemins_Dijkstra_s_algorithm():
    which_direction = PriorityQueue()
    which_direction.put((0, start))
    came_from = dict()
    came_from[start.nom] = None
    cost_so_far = dict()
    cost_so_far[start] = 0
    cost_neighbor_current = 0

    while not which_direction.empty():
        position_current = which_direction.get()
        position_current = position_current[1]
        liste_neighbors_available = find_neighbors_available(position_current)

        if position_current.nom == end.nom:
            break

        for neighbor_current in liste_neighbors_available:
            cost_neighbor_current += cost_so_far[position_current] + 1
            if neighbor_current not in cost_so_far or cost_neighbor_current < cost_so_far[neighbor_current]:
                cost_so_far[neighbor_current] = cost_neighbor_current
                priority = cost_neighbor_current
                which_direction.put((priority, neighbor_current))
                came_from[neighbor_current.nom] = position_current.nom
    return came_from


print('For the Greed Best Find Search ie only the distance as priority')
print(timeit.timeit(lambda: tous_les_chemins_greedy_best_first_search(), number=1000))

print('For the Dijkstra s algorithm ie only the cost as priority')
print(timeit.timeit(lambda: tous_les_chemins_Dijkstra_s_algorithm(), number=1000))

print('For the A* algorithm ie use both')
print(timeit.timeit(lambda: tous_les_chemins_A_star_algorithm(), number=1000))
