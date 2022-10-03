# Напишите бота, удаляющего из текста все слова, содержащие "абв".
# (текст вводит пользователь)

from telegram import Bot, Update
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,)
from bot_commands import *

bot = Bot(token='5749226236:AAE03fILULbf87NHB6u_l4wSde6GkA5ZJQA')
updater = Updater(token='5749226236:AAE03fILULbf87NHB6u_l4wSde6GkA5ZJQA')
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


print('server start')
updater.start_polling()
updater.idle()