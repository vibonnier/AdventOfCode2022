# liste = open('Puzzles/Signal_test').read()
liste = open('Puzzles/Signal').read()
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


# Check s'il y a répétition dans chaque 4-tuple.
for i in range(len(liste)):
    list_4tuple = []
    for j in range(4):
        try:
            list_4tuple.append(liste[i + j])
        except ValueError:
            break
    if len(set(list_4tuple)) == len(list_4tuple):
        print("Signal maker", i + 4)
        print(''.join(list_4tuple))
        break


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# Le 4-tuple devient un 14-tuple.
for i in range(len(liste)):
    list_14tuple = []
    for j in range(14):
        try:
            list_14tuple.append(liste[i + j])
        except ValueError:
            break
    if len(set(list_14tuple)) == len(list_14tuple):
        print("Message maker", i + 14)
        print(''.join(list_14tuple))
        break
