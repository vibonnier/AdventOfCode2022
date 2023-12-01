# liste = open('Assignment_test').read()
liste = open('Assignment').read()
liste = liste.split()


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# % signifie modulo.
# Transforme une list en deux listes list1, list2.
# En mettant le 1er élément dans la 1ère liste, le 2ème dans la 2ème, le 3ème dans la 1ère, etc.
def ajouter(list, list1, list2):
    for j in range(len(list)):
        if j % 2 == 0:
            list1.append(list[j])
        else:
            list2.append(list[j])


# Créer deux listes, chaque ligne est un bout de la paire.
list1 = []
list2 = []
listi = []
for i in range(len(liste)):
    listi = str(liste[i])
    listi = listi.split(",")
    ajouter(listi, list2, list1)


# Comparaison entre deux listes éléments à éléments.
def comparer(list1, list2):
    nb_commun = 0
    for i in range(0, len(list1), 2):
        if list1[i] == list2[i]:
            nb_commun += 1
        elif list1[i] < list2[i] and list1[i + 1] >= list2[i + 1]:
            nb_commun += 1
        elif list1[i] > list2[i] and list1[i + 1] <= list2[i + 1]:
            nb_commun += 1
    return nb_commun


# Transforme la liste en une liste d'entier.
def integer(list):
    for i in range(len(list)):
        list[i] = int(list[i])


# Chaque élément de la liste est de la forme ...-...
# Permet de séparer chaque élément en deux éléments (on coupe au tiret) et transforme en entier.
def transformer_en_nombre(list):
    futur_liste = []
    for i in range(len(list)):
        id_tiret = list[i].index("-")
        futur_liste.append(list[i][:id_tiret])
        futur_liste.append(list[i][id_tiret + 1:])
        integer(futur_liste)
    return futur_liste


print('Il y a', comparer(transformer_en_nombre(list1), transformer_en_nombre(list2)),
      'paires contenues les unes dans les autres')


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# La comparaison est différente.
def comparer_bis(list1, list2):
    nb_commun = 0
    for i in range(0, len(list1), 2):
        if list1[i + 1] >= list2[i] and list1[i] <= list2[i + 1]:
            nb_commun += 1
    return nb_commun


print('Il y a', comparer_bis(transformer_en_nombre(list1), transformer_en_nombre(list2)),
      'paires qui overlapent')
