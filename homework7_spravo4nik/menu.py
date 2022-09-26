def menu():    
    answer =  input(('would u like add contact?\n "y" or "n"?\n'))
    if answer == 'y':
        with open ('base.txt', 'a') as data:
            name_number = input('enter name and number\n')
            data.write(name_number+'\n')
    if answer == 'n':
        print('see ya')
    return name_number