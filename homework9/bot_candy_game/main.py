from telegram import Bot, Update
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          ConversationHandler)
from bot_commands import *


bot = Bot(token='5749226236:AAE03fILULbf87NHB6u_l4wSde6GkA5ZJQA')
updater = Updater(token='5749226236:AAE03fILULbf87NHB6u_l4wSde6GkA5ZJQA')
dispatcher = updater.dispatcher





# start_handler = CommandHandler('start', start)
# candys_handler = CommandHandler('candygame', candy_game)

# players_turn_handler = MessageHandler()
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        A: [MessageHandler(Filters.command, candy_game)],
        B: [MessageHandler(Filters.text, players_turn)],
        C: [MessageHandler(Filters.text, candy_game)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)


# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(candys_handler)
dispatcher.add_handler(conv_handler)


print('server start')
updater.start_polling()
updater.idle()
