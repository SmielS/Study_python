#
# int, float, boolean, str, list, None

# value = None
# a = 123
# b = 1.23
# # print(type(value))
# # print(type(a))
# # print(type(b))
# value = 12334
# # print(type(value))

# s = 'hello \'world'

# print(s)
# print(a, '-',b, '-',s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {s} - {b}')

# f = False
# print(f)


#
# lists

# list = ['1','2','3']
# col = ['hello', 1,2,3.4,True]
# print(list)
# print(col)


#
# input/output

# print('enter a');
# a = float(input())
# print('enter b');
# b = int(input())
# print(a,' + ', b, ' = ',a+b )
# # print('{} {}'.format(a,b))
# # print(f'{a} {b}')


#
# arythmetic
# +, -, * , /, %, //, **
# Приоритет операций
# ** , ⊕, ⊖, * , /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 1.321123
# b = 3
# c = round(a*b, 5)
# print(c)

# a = 3
# a+=5
# print(a)


#
# logic
#
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,
# ^
# Кое-что ещё: is, is not, in, not in

# f = [1, 2, 3, 4]
# # print(f)
# # print(2 in f)  # 2 in list f?

# is_odd = not f[0] % 2
# print(is_odd)


#
# if/else

# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a)
# elif a==b:
#     print(a)
# else:
#     print(b)


#
# circles

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print("stop it!")
# print(inverted)


#
# for

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)


#
# strings

# text = 'съещь еще баланды, братишка'

# # help(text.istitle)

# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('баланды','говна'))

# for c in text:
#     print(c)


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#
# lists

# colors = ['r', 'g', 'b']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('GRAY')
# print(colors)
# colors.remove('r') # del colors[0]
# print(colors)


#
#FUNCTIONS

def f(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))