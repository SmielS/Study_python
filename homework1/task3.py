# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter(x, y):
    if ((x > 0) and (y > 0)):
        print('1st')
    elif ((x < 0) and (y < 0)):
        print('3rd')
    elif ((x > 0) and (y < 0)):
        print('2nd')
    elif ((x < 0) and (y > 0)):
        print('4th')


x=int(input('enter x: '))
y=int(input('enter y: '))
quarter(x, y)
