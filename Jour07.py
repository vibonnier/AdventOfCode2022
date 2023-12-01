# liste = open('Puzzles/FilesSystem_test').read()
liste = open('Puzzles/FilesSystem').read()
liste = liste.split("\n")
print(liste)


# family_size compte la taille + celle des enfants, etc.
class files:
    list_dico = []
    list_name = []
    list_size = []
    list_parent = []
    list_family_size = []

    def __init__(self, name, size, parent, directory):
        self.name = str(parent) + '/' + name
        self.size = size
        self.parent = parent
        self.directory = directory
        self.family_size = int(self.size)
        files.list_dico.append([self.name, self.size, self.parent, self.directory])
        files.list_name.append(self.name)
        files.list_size.append(self.size)
        files.list_parent.append(self.parent)
        files.list_family_size.append(self.family_size)


# Pour créer un parent de base artificiellement.
fichier_0 = files('parent0', 0, None, True)


# Création des fichiers à partir d'une ligne (un élément de liste).
# Chaque fichier peut être appelé par file_1, file_2... indexé suivant l'ordre de création de list_name.
def creation_files(ligne, id_parent):
    ligne = ligne.split()
    if ligne[0] == 'dir':
        globals()['fichier_' + str(len(files.list_name) - 1)] = files(ligne[1], 0, id_parent, True)
    else:
        globals()['fichier_' + str(len(files.list_name) - 1)] = files(ligne[1], ligne[0], id_parent, False)


# Appeler le file_i/fichier(i).
# globals()['files_' + str(i)] signifie que i est une variable qui change.
def fichier(i):
    fi = globals()['fichier_' + str(i)]
    return fi


# Créer des fichiers.
def ls(id_initial_ligne, id_parent):
    id_current_ligne = id_initial_ligne + 1
    while liste[id_current_ligne][0] != "$":
        creation_files(liste[id_current_ligne], id_parent)
        id_current_ligne += 1
    return id_current_ligne


# Changer le parent et mettre à jour family_size récursivement.
def cd(id_initial_ligne, id_parent):
    if liste[id_initial_ligne][-1] == "." and id_parent != 0:
        for j in range(len(files.list_parent)):
            if files.list_parent[j] == id_parent:
                fichier(id_parent).family_size += int(fichier(j).family_size)
                files.list_family_size[id_parent] = fichier(id_parent).family_size
        id_parent = fichier(id_parent).parent
    elif liste[id_initial_ligne][-1] == "." and id_parent == 0:
        pass
    else:
        id_parent = files.list_name.index(str(id_parent) + '/' + liste[id_initial_ligne][5:])
    return id_parent


# Organiser les fichiers suivant le FileSystem ie la liste.
def organisation_files():
    id_liste = 0
    id_parent = 0
    while id_liste < len(liste):
        if liste[id_liste][0] == "$":
            if liste[id_liste][2:4] == 'ls':
                id_liste = ls(id_liste, id_parent)
            else:
                id_parent = cd(id_liste, id_parent)
                id_liste += 1
        else:
            id_liste += 1


organisation_files()


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Sommer la taille totale des éléments directory et plus petit que 100'000.
def sum_under():
    sum = 0
    for i in range(1, len(files.list_family_size)):
        if files.list_family_size[i] < 100000 and fichier(i).directory:
            sum += files.list_family_size[i]
    return sum


print("La taille total de tous les directory de moins de 100'000 est", sum_under())


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Sommer la taille totale des éléments directory.
def sum_total():
    sum = 0
    for i in range(len(files.list_parent)):
        if fichier(i).parent == 0:
            sum += fichier(i).family_size
    return sum


# Trouver l'élément directory le plus petit et qui libère au moins 30'000'000'.
def lower_file_above():
    family_size_max = sum_total()
    total = sum_total()
    name_el_max = 0
    for i in range(1, len(files.list_family_size)):
        if total - fichier(i).family_size < 40000000 and fichier(i).family_size < family_size_max and fichier(i).directory:
            family_size_max = fichier(i).family_size
            name_el_max = fichier(i).name
    return [family_size_max, name_el_max]


print("Le fichier à supprimer est", lower_file_above()[1][-1], "et a une taille totale de", lower_file_above()[0])
