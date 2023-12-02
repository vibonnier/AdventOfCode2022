# Rappel: A, X rock - B, Y paper - C, Z scissors.
# liste = open('Puzzles/PSR_list_test').read()
liste = open('Puzzles/PSR_list').read()
liste = liste.splitlines(False)
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


the_rules = {'A Z': 'lose', 'B X': 'lose', 'C Y': 'lose', 'A Y': 'win', 'B Z': 'win', 'C X': 'win', 'A X': 'draw', 'B Y': 'draw', 'C Z': 'draw'}
score_victory = {'win': 6, 'lose': 0, 'draw': 3}
score_choose = {'X': 1, 'Y': 2, 'Z': 3}

score_total = 0

for i in range(len(liste)):
    score_total += score_victory[the_rules[liste[i]]] + score_choose[liste[i][-1]]

print('Notre score est de', score_total)


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


victory = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
score_choose = {'win': {'A': 2, 'B': 3, 'C': 1}, 'lose': {'A': 3, 'B': 1, 'C': 2}, 'draw': {'A': 1, 'B': 2, 'C': 3}}

score_total = 0

for i in range(len(liste)):
    who_win = victory[liste[i][-1]]
    score_total += score_victory[who_win] + score_choose[who_win][liste[i][0]]

print("Notre nouveau score est", score_total)
