# 1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

# bad_student():

with open('1.txt', 'r') as file:
    marks = (file.read())
new_marks = ''
for i in marks:
    if i != '4' and i != '5':
        new_marks+=i
    elif i == '4':
        new_marks+='2'
    elif i == '5':
        new_marks+='1'


with open ('1.txt', 'w') as file:
    file.write((new_marks))
    
