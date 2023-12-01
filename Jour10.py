# liste = open('Puzzles/Cycle_test').read()
liste = open('Puzzles/Cycle').read()
liste = liste.split()
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Change la strength pour les cycles 20, 60, 100, 140, 180 et 220.
def strength_during_some_cycle(id_current_cycle, current_X, current_strength):
    if (id_current_cycle + 20) % 40 == 0:
        current_strength += id_current_cycle * current_X
    return current_strength


def noop(id_current_cycle, current_X, current_strength):
    id_current_cycle += 1
    current_strength = strength_during_some_cycle(id_current_cycle, current_X, current_strength)
    return [id_current_cycle, current_strength]


def addx(to_add_at_X, id_current_cycle, current_X, current_strength):
    [id_current_cycle, current_strength] = noop(id_current_cycle, current_X, current_strength)
    [id_current_cycle, current_strength] = noop(id_current_cycle, current_X, current_strength)
    current_X += to_add_at_X
    return [id_current_cycle, current_X, current_strength]


def total():
    id_current_cycle = 0
    current_X = 1
    current_strength = 0
    for i in range(len(liste)):
        if liste[i] == "noop":
            [id_current_cycle, current_strength] = noop(id_current_cycle, current_X, current_strength)
        elif liste[i] == "addx":
            [id_current_cycle, current_X, current_strength] = addx(int(liste[i + 1]), id_current_cycle, current_X, current_strength)
    return current_strength


print('The sum of the six signal strength is', total())


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Passer à la ligne pendant l'affichage.
def change_line(id_current_position):
    if (id_current_position + 1) % 40 == 0:
        id_current_position = -1
        print('')
    return id_current_position


def noop_bis(id_current_position, current_X, screen):
    id_current_position += 1
    if id_current_position in range(current_X - 1, current_X + 2):
        print('# ', end='')
    else:
        print('. ', end='')
    id_current_position = change_line(id_current_position)
    return [id_current_position, screen]


def addx_bis(to_add_to_X, id_current_position, current_X, screen):
    [id_current_position, screen] = noop_bis(id_current_position, current_X, screen)
    [id_current_position, screen] = noop_bis(id_current_position, current_X, screen)
    current_X += to_add_to_X
    return [id_current_position, current_X, screen]


def total_bis():
    id_current_position = -1
    current_X = 1
    screen = []
    for i in range(len(liste)):
        if liste[i] == "noop":
            [id_current_position, screen] = noop_bis(id_current_position, current_X, screen)
        elif liste[i] == "addx":
            [id_current_position, current_X, screen] = addx_bis(int(liste[i + 1]), id_current_position, current_X, screen)
    return screen


total_bis()
