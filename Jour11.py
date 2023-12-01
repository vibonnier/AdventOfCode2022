import math


# liste = open('Puzzles/Monkeys_test').read()
liste = open('Puzzles/Monkeys').read()
liste = liste.split("\n")
print(liste)


class monkeys:

    def __init__(self, items, operation, diviseur, id_true_monkey, id_false_monkey):
        self.items = items
        self.operation = operation
        self.diviseur = diviseur
        self.id_true_monkey = id_true_monkey
        self.id_false_monkey = id_false_monkey
        self.nb_items_inspected = 0


def find_nb_monkeys():
    nb_monkeys = 0
    for i in range(0, len(liste), 7):
        nb_monkeys += 1
    return nb_monkeys


def find_starting_items(id_monkey):
    id_in_liste = 1 + 7 * id_monkey
    liste_starting_items = []
    liste[id_in_liste] = liste[id_in_liste].split()
    liste[id_in_liste].remove('Starting')
    liste[id_in_liste].remove('items:')
    for i in range(len(liste[id_in_liste])):
        liste[id_in_liste][i] = liste[id_in_liste][i].replace(',', '')
        liste_starting_items.append(int(liste[id_in_liste][i]))
    return liste_starting_items


def find_operation(id_monkey):
    id_in_liste = 2 + 7 * id_monkey
    liste[id_in_liste] = liste[id_in_liste].split("=")
    operation = liste[id_in_liste][-1]
    return operation


def find_diviseur(id_monkey):
    id_in_liste = 3 + 7 * id_monkey
    diviseur = liste[id_in_liste][21:]
    return int(diviseur)


# Trouve l'id du singe qui receptionne l'objet sur la divisibilité est vrai.
def find_true_monkey(id_monkey):
    id_in_liste = 4 + 7 * id_monkey
    id_true_monkey = liste[id_in_liste][29:]
    return id_true_monkey


# Trouve l'id du singe qui receptionne l'objet sur la divisibilité n'est pas vrai.
def find_false_monkey(id_monkey):
    id_in_liste = 5 + 7 * id_monkey
    id_false_monkey = liste[id_in_liste][30:]
    return id_false_monkey


def create_monkeys():
    nb_monkeys = find_nb_monkeys()
    for id_monkey in range(nb_monkeys):
        liste_starting_items = find_starting_items(id_monkey)
        operation = find_operation(id_monkey)
        diviseur = find_diviseur(id_monkey)
        id_true_monkey = find_true_monkey(id_monkey)
        id_false_monkey = find_false_monkey(id_monkey)
        globals()['monkey_' + str(id_monkey)] = monkeys(liste_starting_items, operation, diviseur, id_true_monkey, id_false_monkey)


create_monkeys()


def monkey(id_monkey):
    monkey_i = globals()['monkey_' + str(id_monkey)]
    return monkey_i


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Calculer le nouveau worry level via l'opération associée à chaque singe.
def calculate_operation(id_monkey, worry_level_current):
    operation = monkey(id_monkey).operation
    operation = operation.replace('old', str(worry_level_current))
    worry_level_current = math.floor(eval(operation) / 3)
    return worry_level_current


def update_items_apres_lancer(id_monkey_qui_receptionne, worry_level_current):
    liste_items = monkey(id_monkey_qui_receptionne).items
    liste_items.append(worry_level_current)
    monkey(id_monkey_qui_receptionne).items = liste_items


def round_per_monkey(id_monkey):
    liste_items = monkey(id_monkey).items
    diviseur = monkey(id_monkey).diviseur
    for i in range(len(liste_items)):
        worry_level_current = liste_items[i]
        worry_level_current = calculate_operation(id_monkey, worry_level_current)
        if worry_level_current % diviseur == 0:
            id_monkey_qui_receptionne = monkey(id_monkey).id_true_monkey
            update_items_apres_lancer(id_monkey_qui_receptionne, worry_level_current)
        else:
            id_monkey_qui_receptionne = monkey(id_monkey).id_false_monkey
            update_items_apres_lancer(id_monkey_qui_receptionne, worry_level_current)
    monkey(id_monkey).nb_items_inspected += len(liste_items)
    monkey(id_monkey).items = []


def round_total(nb_round, nb_monkeys):
    for current_round in range(1, nb_round + 1):
        for id_monkey in range(nb_monkeys):
            round_per_monkey(id_monkey)


def find_nb_item_inspected(nb_round):
    nb_monkeys = find_nb_monkeys()
    round_total(nb_round, nb_monkeys)
    liste_nb_items_inspected = []
    for id_monkey in range(nb_monkeys):
        liste_nb_items_inspected.append(monkey(id_monkey).nb_items_inspected)
    return liste_nb_items_inspected


def count():
    product = 1
    compteur = 0
    while compteur < 2:
        compteur += 1
        product *= max(liste_nb_items_inspected)
        liste_nb_items_inspected.remove(max(liste_nb_items_inspected))
    return product


liste_nb_items_inspected = find_nb_item_inspected(20)
print(liste_nb_items_inspected)
print("The level of monkey business after 20 rounds is", count())


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


def reset(nb_monkeys):
    for id_monkey in range(nb_monkeys):
        monkey(id_monkey).nb_items_inspected = 0
        id_in_liste = 1 + 7 * id_monkey
        monkey(id_monkey).items = liste[id_in_liste]


def find_modulo(nb_monkeys):
    modulo_total = 1
    for id_monkey in range(nb_monkeys):
        modulo_total *= monkey(id_monkey).diviseur
    return modulo_total


def calculate_operation_bis(id_monkey, worry_level_current, modulo):
    operation = monkey(id_monkey).operation
    operation = operation.replace('old', str(worry_level_current))
    worry_level_current = math.floor(eval(operation) % modulo)
    return worry_level_current


def round_per_monkey_bis(id_monkey, modulo):
    liste_items = monkey(id_monkey).items
    diviseur = monkey(id_monkey).diviseur
    for i in range(len(liste_items)):
        worry_level_current = liste_items[i]
        worry_level_current = calculate_operation_bis(id_monkey, worry_level_current, modulo)
        if worry_level_current % diviseur == 0:
            id_monkey_qui_receptionne = monkey(id_monkey).id_true_monkey
            update_items_apres_lancer(id_monkey_qui_receptionne, worry_level_current)
        else:
            id_monkey_qui_receptionne = monkey(id_monkey).id_false_monkey
            update_items_apres_lancer(id_monkey_qui_receptionne, worry_level_current)
    monkey(id_monkey).nb_items_inspected += len(liste_items)
    monkey(id_monkey).items = []


def round_total_bis(nb_round, nb_monkeys):
    modulo = find_modulo(nb_monkeys)
    for current_round in range(1, nb_round + 1):
        for id_monkey in range(nb_monkeys):
            round_per_monkey_bis(id_monkey, modulo)


def find_nb_item_inspected_bis(nb_round):
    nb_monkeys = find_nb_monkeys()
    reset(nb_monkeys)
    round_total_bis(nb_round, nb_monkeys)
    liste_nb_items_inspected = []
    for id_monkey in range(nb_monkeys):
        liste_nb_items_inspected.append(monkey(id_monkey).nb_items_inspected)
    return liste_nb_items_inspected


liste_nb_items_inspected = find_nb_item_inspected_bis(10000)
print(liste_nb_items_inspected)
print("Without divide by three, the level of monkey business after 10'000 rounds is", count())
