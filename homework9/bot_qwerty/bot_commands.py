def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'print your string and'
                             'i will delete all words which including "абв"')



def message(update, context):
    text = update.message.text
    new_text = (' '.join(list(filter(lambda x: 'абв' not in x.lower(), text.split()))))
    context.bot.send_message(update.effective_chat.id, new_text)









# stroka = 'Привабвет каабв твои дела? чем сегоабв занят?'

# print(' '.join(list(filter(lambda x: 'абв' not in x.lower(), stroka.split()))))
