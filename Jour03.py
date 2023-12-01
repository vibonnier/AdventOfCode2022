# liste = open('Puzzles/Rucksack_test').read()
liste = open('Puzzles/Rucksack').read()
liste = liste.split()


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Vérifier si certains nombres sont dans 2 listes.
def find_common_element(list1, list2):
    a = set(list1)
    b = set(list2)
    if a & b:
        return list(a & b)[0]


# Transformer les strings de la liste en nombre via l'écriture ASCII.
# D'abord, il faut translater, car les lettres commence à 96 et les majuscules à 64 en ASCII.
def transforme_en_nombre(string):
    if ord(string) < 96:
        return ord(string) - 64 + 26
    else:
        return ord(string) - 96


# Créer 2 listes pour chaque ligne et transforme les lettres en chiffres : a=1 et A=27.
# "a" est la somme de tous les éléments qui apparaissent dans les deux sets.
sum_common_nb = 0
for i in range(len(liste)):
    list1 = []
    list2 = []
    for j in range(len(liste[i])):
        if j < len(liste[i]) / 2:
            list1.append(transforme_en_nombre(liste[i][j]))
        else:
            list2.append(transforme_en_nombre(liste[i][j]))
    sum_common_nb += find_common_element(list1, list2)
print('Pour 2 sets, la somme est de', sum_common_nb)


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Vérifie si certains nombres sont dans 3 listes.
def find_common_element_3(list1, list2, list3):
    a = set(list1)
    b = set(list2)
    c = set(list3)
    if a & b & c:
        return list(a & b & c)[0]


# "b" est la somme de tous les éléments qui apparaissent dans les trois sets.
sum_common_nb = 0
for i in range(0, len(liste), 3):
    list1 = []
    list2 = []
    list3 = []
    for j in range(len(liste[i])):
        list1.append(transforme_en_nombre(liste[i][j]))
    for j in range(len(liste[i + 1])):
        list2.append(transforme_en_nombre(liste[i + 1][j]))
    for j in range(len(liste[i + 2])):
        list3.append(transforme_en_nombre(liste[i + 2][j]))
    sum_common_nb += find_common_element_3(list1, list2, list3)

print('Pour 3 sets, la somme est de', sum_common_nb)
