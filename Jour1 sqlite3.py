import sqlite3

liste = open('Elf_list').read()
liste = liste.splitlines(True)


def associer_personnes_calories():
    liste_personnes = []
    id_current_personne = 1
    liste_calories = []
    for i in range(len(liste)):
        if len(liste[i]) > 1:
            liste_calories.append(int(liste[i]))
            liste_personnes.append( id_current_personne)
        else:
            id_current_personne += 1
    return [liste_calories, liste_personnes]


def preparation_data():
    [liste_calories, liste_parents] = associer_personnes_calories()
    liste_id_parents = list(range(1, liste_parents[-1] + 1))
    liste_calories_totales = [0] * len(liste_id_parents)
    liste_data_items = list(zip(liste_calories, liste_parents))
    liste_data_personnes = list(zip(liste_id_parents, liste_calories_totales))
    return [liste_data_items, liste_data_personnes]


[liste_data_items, liste_data_personnes] = preparation_data()


# Se lier avec la database et si elle n'existe pas la créer.
con = sqlite3.connect("Advent_of_Code_2022.sqlite")
cur = con.cursor()


# Quand création d'une table, ne pas oublier de la supprimer sinon error dans le code, car elle existe déjà.
cur.execute("DROP TABLE IF EXISTS personnes")
cur.execute("DROP TABLE IF EXISTS items")

cur.execute("CREATE TABLE personnes (id INTEGER, calories_totales INTEGER)")
cur.execute("CREATE TABLE items (calories INTEGER , personne_qui_porte INTEGER, FOREIGN KEY (personne_qui_porte) REFERENCES personnes(id))")

cur.executemany("INSERT INTO items VALUES (?,?)", liste_data_items)
cur.executemany("INSERT INTO personnes VALUES (?,?)", liste_data_personnes)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def count_calories_par_per(id_personne):
    for sum in cur.execute("SELECT SUM(calories) FROM items WHERE personne_qui_porte = ?", [id_personne]):
        return sum[0]


def update_calories_totales():
    for nb_personnes in cur.execute("SELECT * FROM personnes ORDER BY id DESC LIMIT 1"):
        for i in range(1, nb_personnes[0] + 1):
            j = count_calories_par_per(i)
            cur.execute("UPDATE personnes SET calories_totales = ? WHERE id = ?", [j, i])


def find_max_calories():
    for max in cur.execute("SELECT SUM(calories_totales) FROM personnes GROUP BY id HAVING calories_totales ORDER BY calories_totales DESC LIMIT 1"):
        print('The elf carrying the most carries', max[0], 'calories.')


def find_three_max_calories():
    sum = 0
    for i in range(3):
        for max_current in cur.execute("SELECT SUM(calories_totales) FROM personnes GROUP BY id HAVING calories_totales ORDER BY calories_totales DESC LIMIT 1 OFFSET ?", [i]):
            sum += max_current[0]
    print('The sum of the calories carried by the three elves carrying the most is', sum)


update_calories_totales()
find_max_calories()
find_three_max_calories()


# pour lire la database ailleurs !
con.commit()
cur.close()

