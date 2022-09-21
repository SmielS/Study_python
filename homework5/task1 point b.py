# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candys = 100

while candys != 0:
    first_player_turn = int(input('1st player move: > '))
    candys -= first_player_turn
    print('remained ', candys, 'candys')
    if candys == 0: 
        print ('1st player win')
        break
    if candys / 28 > 2:
        second_palyer_turn = randint(1,28)
    elif candys <= 28:
        second_palyer_turn = candys
    elif candys == 29:
        print ('2nd player leave the game. Congratulation player 1!')
        break
    else: 
        second_palyer_turn = candys % 28 -1
    print('2nd player moved ', second_palyer_turn, 'candys')
    candys -= second_palyer_turn
    print('remained ', candys, 'candys')
    if candys == 0: 
        print ('2nd player win')
        break
    if candys < 0:
        print ('candys cant be negative. Play again')

