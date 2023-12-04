import copy


# liste = open('Puzzles/').read()
liste = open('Puzzles/Packets').read()
liste = liste.split()


def create_two_lists():
    liste1 = []
    liste2 = []
    for i in range(len(liste)):
        if i % 2 == 0:
            liste1.append(eval(liste[i]))
        else:
            liste2.append(eval(liste[i]))
    return [liste1, liste2]


liste1 = create_two_lists()[0]
liste2 = create_two_lists()[1]
print(liste1)
print(liste2)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def comparer_items(item1, item2):
    if item1 < item2:
        return True
    elif item1 > item2:
        return False


def comparer_listes(list1, list2):
    while list1 or list2:
        if list2 and not list1:
            return True
        elif list1 and not list2:
            return False
        elif isinstance(list1[0], int) and isinstance(list2[0], int):
            if isinstance(comparer_items(list1[0], list2[0]), bool):
                return comparer_items(list1[0], list2[0])
        elif isinstance(list1[0], list) and isinstance(list2[0], list):
            if isinstance(comparer_listes(list1[0], list2[0]), bool):
                return comparer_listes(list1[0], list2[0])
        elif isinstance(list1[0], int) and isinstance(list2[0], list):
            return comparer_listes([list1[0]], list2[0])
        elif isinstance(list1[0], list) and isinstance(list2[0], int):
            comparer_listes(list1[0], [list2[0]])
            return comparer_listes(list1[0], [list2[0]])
        list1.remove(list1[0])
        list2.remove(list2[0])


sum = 0
for i in range(len(liste1)):
    print('######################################################', i + 1)
    print(comparer_listes(liste1[i], liste2[i]))
    if comparer_listes(liste1[i], liste2[i]):
        sum += i + 1
print('The sum of the indices of paires in right order is', sum)


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


unique_liste = create_two_lists()[0] + create_two_lists()[1]
print(unique_liste)


def count():
    nb_items_before = 0
    nb_items_between = 0
    for i in range(len(unique_liste)):
        if comparer_listes(unique_liste[i], [[2]]):
            nb_items_before += 1
        elif comparer_listes(unique_liste[i], [[6]]):
            nb_items_between += 1
    return [nb_items_before, nb_items_between]


[nb_items_before, nb_items_between] = count()
print('The decoder key is', (nb_items_before + 1) * (nb_items_before + 1 + nb_items_between + 1))
