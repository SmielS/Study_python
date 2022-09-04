# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def check_quarter(quarter):
    if quarter == 1:
        print('(x > 0) and (y > 0)')
    elif quarter == 3:
        print('(x < 0) and (y < 0)')
    elif quarter == 2:
        print('(x > 0) and (y < 0)')
    elif quarter == 4:
        print('(x < 0) and (y > 0)')
    else: print('num of quarter shold be from 1 to 4')


quarter = int(input("enter a quarter: "))
check_quarter(quarter)
