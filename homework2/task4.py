# Петя впервые пришел на урок физкультуры в новой школе.
# Перед началом урока ученики выстраиваются по росту, в порядке невозрастания.
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать,
# чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию
# (то есть каждое следующее число не больше предыдущего).
# Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю).
# Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания.
# Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите единственное целое число – номер Пети в шеренге учеников.

pupils = int(input('enter a number of pupils: > '))
height = []
for i in range(pupils):
    height.append(int(input('enter a height of pupils from max to min: > ')))
petya_height = int(input('enter Petya`s height: > '))


position = 0
while position < len(height) and height[position] >= petya_height:
    position += 1
print(position+1)