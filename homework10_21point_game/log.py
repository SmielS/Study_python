from datetime import datetime as dt

def logging(update, winner):
    time = dt.now().strftime('%H:%M')
    if winner == -1:
        name = 'bot'
    elif winner == 1:
        name = update.effective_user.first_name
    else:
        name = 'nobody'
    with open('log.txt', 'a') as file:
        file.write(f'{time} >>>> {winner} - {name}\n')

def stat(update,context):
    counter_bot = 0
    counter_user = 0

    with open ('log.txt', 'r') as file:
        for line in file:
            stroka = line.split()
            if stroka[4] == 'bot':
                counter_bot+=1
            elif stroka[4] == update.effective_user.first_name:
                counter_user+=1
    context.bot.send_message(update.effective_chat.id, 
                            f"bot - {counter_bot}\n"
                            f'{update.effective_user.first_name} - {counter_user}')
