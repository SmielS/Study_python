#  Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

# n = input()[::-1]
# print(n)


def reversed3(stroka): 
    if len(stroka) == 1:
        return stroka
    return stroka[-1] + reversed3(stroka[:-1])

n = reversed3(input())
print(n)