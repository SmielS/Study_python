# 1. Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)
# 2. Создайте программу для игры с конфетами человек против бота(интелект). (Дополнительно)
# 3. Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования(Дополнительно)

from telegram import Bot, Update
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          ConversationHandler)
import time
from random import randint
A = 0
B = 1
C = 2

candys = 100


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Hello, {update.effective_user.first_name}, we will paly "Candy Game"\n'
                             'print /candygame to start'
                             'print /cancel to stop the game')
    context.bot.send_message(update.effective_chat.id, f'{update.effective_user.first_name}, we have 100 candys.\n'
                             'Every step we can take 28 or less candys.\n'
                             'the winner is the one who takes the last one\n')
    return A


def candy_game(update, context):
    global candys
    if candys != 0:
        context.bot.send_message(
            update.effective_chat.id, f'remaining {candys} candys')
        context.bot.send_message(
            update.effective_chat.id, 'Yours turn to take candys!')
        return B
    else:
        context.bot.send_message('u win!')
        candys = 100
        return ConversationHandler.END


def players_turn(update, context):
    global candys
    if candys != 0:
        turn = update.message.text
        if turn == '/cancel':
            return ConversationHandler.END
        print(f'candys = {candys}')
        print(f'turn = {turn}')
        candys -= int(turn)
        if candys == 0:
            context.bot.send_message(update.effective_chat.id, 'you win!')
            return ConversationHandler.END
        if candys / 28 > 2:
            bot_turn = randint(1, 28)
        elif candys <= 28:
            bot_turn = candys
        elif candys == 29:
            context.bot.send_message('bot leave the game. Congratulation!')
            return ConversationHandler.END

        else:
            bot_turn = candys % 28 - 1
        context.bot.send_message(
            update.effective_chat.id, f'bot takes {bot_turn} candys')
        candys -= bot_turn
        context.bot.send_message(
            update.effective_chat.id, f'{candys} remaining')
        if candys != 0:
            context.bot.send_message(
                update.effective_chat.id, 'Yours turn to take candys!')
        if candys == 0:
            context.bot.send_message(update.effective_chat.id, 'bot wins!')
            candys = 100
            return ConversationHandler.END

        if candys < 0:
            context.bot.send_message(
                update.effective_chat.id, 'candys cant be negative. Play again')
            return ConversationHandler.END
        return B
    else:
        return A


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'saddenly that you leave the game'
                             'i hope you come back later',
                             )
    return ConversationHandler.END
