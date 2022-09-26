from menu import menu
from datetime import datetime as dt


def logging(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}: added string - {}\n'
                   .format(time, data))
