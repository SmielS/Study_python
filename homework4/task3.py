# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 2, 6, 3, 3, 4, 5, 6, 7, 9, 7]
numbers.sort()

exclusive_numbers = list()

i = 0
while i < len(numbers) -1 :
    if numbers[i] != numbers[i+1]:
        exclusive_numbers.append(numbers[i])
    i+=1
if numbers[len(numbers)-1] != numbers[len(numbers)-2]:
    exclusive_numbers.append(numbers[len(numbers)-1])

print (exclusive_numbers)