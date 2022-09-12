# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


n = int(input("enter n: > "))
fib_all = list()


def fib(n, fib_all):
    fib1 = 1
    fib2 = 1
    fib_all.append(0)
    fib_all.append(1)
    fib_all.append(1)
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        fib_all.append(fib_sum)
        i += 1


def negafib(n, fib_all):
    fib1 = 1
    fib2 = -1
    fib_all.insert(0, 1)
    fib_all.insert(0, -1)
    i = 2
    while i < n:
        fib_sum = fib1 - fib2
        fib1 = fib2
        fib2 = fib_sum
        fib_all.insert(0, fib_sum)
        i += 1


fib(n, fib_all)
negafib(n, fib_all)

print(fib_all)
