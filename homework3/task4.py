# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_number = int(input('dec number = '))

bin_number = ''

while dec_number > 0:
    bin_number = str(dec_number % 2) + bin_number
    dec_number = dec_number // 2

print('bin numbers = ', bin_number)