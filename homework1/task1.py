# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("enter a number of the day")
day = int(input())
if 0 < day < 6:
    print('working day')
elif 5 < day < 8:
    print('weekend')
else:
    print('number is not a day of the week')
