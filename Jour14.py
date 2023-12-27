# liste = open('Puzzles/Sand_test').read()
liste = open('Puzzles/Sand').read()
liste = liste.split('\n')


# Création de la liste des positions des rocks.
new_liste = [[] for _ in range(len(liste))]
for id_liste in range(len(liste)):
    subliste = liste[id_liste].split('->')
    for id_subliste in range(len(subliste)):
        column = subliste[id_subliste].split(',')[0]
        line = subliste[id_subliste].split(',')[1]
        new_liste[id_liste].append([int(column), int(line)])
liste = new_liste
print(liste)


class cave:

    def __init__(self, column, line):
        self.column = int(column)
        self.line = int(line)
        self.state = '.'
        self.nom = 'position_' + str(self.column) + '_' + str(self.line)

    def __str__(self):
        return self.nom


def length_cave():
    min_column = 500
    max_column = 500
    max_line = 0
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j][0] < min_column:
                min_column = liste[i][j][0]
            if liste[i][j][0] > max_column:
                max_column = liste[i][j][0]
            if liste[i][j][1] > max_line:
                max_line = liste[i][j][1]
    return[min_column, max_column, max_line]


def creation_cave(min_column, max_column, max_line):
    for id_line in range(max_line + 1):
        for id_column in range(min_column - 1, max_column + 1):
            globals()['position_' + str(id_column) + '_' + str(id_line)] = cave(id_column, id_line)
    globals()['position_' + str(500) + '_' + str(0)].state = '+'


def position(i, j):
    return globals()['position_' + str(i) + '_' + str(j)]


def creation_rock():
    for i in range(len(liste)):
        j = 0
        while j < len(liste[i]) - 1:
            if liste[i][j][0] != liste[i][j + 1][0]:
                current_min = min(liste[i][j][0], liste[i][j + 1][0])
                current_max = max(liste[i][j][0], liste[i][j + 1][0])
                current_line = liste[i][j][1]
                for current_column in range(current_min, current_max + 1):
                    position(current_column, current_line).state = '#'
            else:
                current_min = min(liste[i][j][1], liste[i][j + 1][1])
                current_max = max(liste[i][j][1], liste[i][j + 1][1])
                current_column = liste[i][j][0]
                for current_line in range(current_min, current_max + 1):
                    position(current_column, current_line).state = '#'
            j += 1


def print_cave(min_column, max_column, max_line):
    for id_line in range(max_line + 1):
        for id_column in range(min_column, max_column + 1):
            print(position(id_column, id_line).state, end='')
        print(id_line)


[min_column, max_column, max_line] = length_cave()
creation_cave(min_column, max_column, max_line)
creation_rock()

####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def move_sand(max_line_rock, current_column, current_line):
    while current_line < max_line_rock and position(current_column, current_line + 1).state == '.':
        current_line += 1
    if position(current_column - 1, current_line + 1).state == '.':
        move_sand(max_line_rock, current_column - 1, current_line + 1)
    elif position(current_column + 1, current_line + 1).state == '.':
        move_sand(max_line_rock, current_column + 1, current_line + 1)
    else:
        position(current_column, current_line).state = 'o'


def count_units_sand_before_abyss():
    count = 0
    while count > -1:
        try:
            move_sand(length_cave()[2], 500, 0)
        except KeyError:
            return count
        count += 1


count = count_units_sand_before_abyss()
print_cave(min_column, max_column, max_line)
print('Le number of units of sand before sand flows into abyss is', count)


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Re-creation of the cave without sands.
# Add two lines at the bottom in order to represent the floor and a lot of columns in each side.
max_line = length_cave()[2] + 2
min_column = 500 - max_line
max_column = 500 + max_line
creation_cave(min_column, max_column, max_line)
creation_rock()


# Add rocks on the last line.
for current_column in range(min_column, max_column + 1):
    position(current_column, max_line).state = '#'


print_cave(min_column, max_column, max_line)


def count_units_sand_before_blocked():
    count = 0
    while position(500, 0).state != 'o':
        move_sand(length_cave()[2] + 2, 500, 0)
        count += 1
    return count


count = count_units_sand_before_blocked()
print_cave(min_column, max_column, max_line)
print('Le number of units of sand before the source becomes blocked is', count)
