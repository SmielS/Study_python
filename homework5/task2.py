# Создайте программу для игры в ""Крестики-нолики"".

desk = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9']

def print_desk(desk):
        print()
        print (desk[0], '\t', desk[1], '\t', desk[2], '\t')
        print()
        print (desk[3], '\t', desk[4], '\t', desk[5], '\t')
        print()
        print (desk[6], '\t', desk[7], '\t', desk[8], '\t')
        print()

def check_win(desk):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if desk[each[0]] == desk[each[1]] == desk[each[2]]:
          return True
   return False

def game(desk):
    s = ''
    for i in range(9):
        if i % 2 == 0:
            print ('1st player')
            s = 'X'
            position = int(input('where is X?: > '))
            desk[position-1] = s
            print_desk(desk)
            if check_win(desk) == True:
                print(' X wins \n')  
                return
        else:
            print ('2nd player')
            s = 'o'
            position = int(input('where is 0?: > '))
            desk[position-1] = s
            print_desk(desk)
            if check_win(desk) == True:
                print(' o wins \n')
                return
    if check_win(desk) == False:
        print ('draw \n')

print_desk(desk)
game(desk)