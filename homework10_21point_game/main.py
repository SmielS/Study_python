from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from game import *



bot = Bot(token='5749226236:AAE03fILULbf87NHB6u_l4wSde6GkA5ZJQA')
updater = Updater(token='5749226236:AAE03fILULbf87NHB6u_l4wSde6GkA5ZJQA')
dispatcher = updater.dispatcher









start_handler = CommandHandler('start', start)
still_handler = CommandHandler('yet', yet)
stop_handler = CommandHandler('stop', stop)
stat_handler = CommandHandler('stat', stat)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(still_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(stat_handler)

print('server is up')
updater.start_polling()
updater.idle()  # ctrl + c