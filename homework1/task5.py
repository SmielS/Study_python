# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def distance_between_points(xa, ya, xb, yb):
    distance = round(((((xb-xa)**2+(yb-ya)**2))**0.5),3)
    print(distance)


xa = float(input('enter Ax:'))
ya = float(input('enter Ay:'))
xb = float(input('enter Bx:'))
yb = float(input('enter By:'))
distance_between_points(xa, ya, xb, yb)
