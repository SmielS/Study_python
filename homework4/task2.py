# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input('input number: > '))

multipliers = list()


def simple_numbers(number):
    lst = list()
    for i in range(2, number+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


# print(simp_num)

def multiplier(number, simp_num, multipliers):
    i = 0
    while i < len(simp_num):
        if number % simp_num[i] == 0:
            multipliers.append(simp_num[i])
            number /= simp_num[i]
        else:
            i += 1


simp_num = simple_numbers(number)

multiplier(number, simp_num, multipliers)

print(multipliers)
