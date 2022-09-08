# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.

# Входные данные
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток.
# В каждой из последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.

def solution(coins):
    tail = 1
    eagle = 0
    if coins.count(tail) >= coins.count(eagle):
        answer = coins.count(eagle)
    else:
        answer = coins.count(tail)
    return answer


quantity = int(input('enter number of coins: > '))
coins = []
for i in range(quantity):
    coins.append(
        int(input('enter a value coin (where 0 - eagle and 1 - tail): > ')))


answer = solution(coins)

print('answer is:', answer)
