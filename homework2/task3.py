# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.

def nod(num):
    for i in range(2, num+1):
        if ((num % i) == 0):
            return i


number = int(input('enter a number: > '))
print(nod(number))
