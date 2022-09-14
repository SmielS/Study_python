# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('enter k: > '))
polynomial = ''

while k > 1:
    polynomial += (str(randint(2,10))+'x^'+str(k)+' + ')
    k-=1
polynomial+=(str(randint(2,10))+' = 0')

print(polynomial)