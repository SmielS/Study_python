# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6]
multiplication = list()

middle = len(numbers)//2
i = 0

if len(numbers) % 2 == 1:
    while i <= middle:
        multiplication.append(numbers[i] * numbers[len(numbers) -1 - i])
        i += 1
elif len(numbers) % 2 == 0:
    while i < middle:
        multiplication.append(numbers[i] * numbers[len(numbers) -1 - i])
        i += 1


print (multiplication)
