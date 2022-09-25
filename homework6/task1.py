

def multiplication(x, y):
    table = list()
    print()
    for i in range(1, x+1):
        for j in range (1, y+1):
            print ((i)*(j), '\t', end = ' ')
        print()

def addition(x,y):
    for i in range(1,x+1):
        print ((i), '\t \t', end = ' ')
    print()
    for i in range(2, x+1):
        for j in range (1, y+1):
            print (i**(j), '\t \t', end = ' ')
        print()

def sum(x,y):
    for i in range(0, x+1):
        for j in range (0, y+1):
            print ((i)+(j), '\t', end = ' ')
        print()


def print_operation_table(operation,x,y):
    list = operation(x,y)
    print()
    return list

# multiplication(x,y)
# addition(x,y)
# sum(10,10)

print_operation_table(addition,10,10)