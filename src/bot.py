# This file contains the source code of Rajah Telegram Bot.

from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
from config.auth import token
from zelda_items import materials
from util import beautifier_nasa, beautifier_material, beautifier_help, beautifier_notfound
import requests
import random


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="HELLO BUDDY!🐯")


def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=beautifier_help(),
                             parse_mode='HTML')


def keyboard(update, context):
    reply_markup = ReplyKeyboardMarkup([['/start', ], ['/nasa', '/fox'], ['/help', ]])
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Here you have a menu🐯",
                             reply_markup=reply_markup)


def nasa(update, context):
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    r = requests.get(url).json()
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=beautifier_nasa(r),
                             parse_mode='HTML')


def animations(update, context):
    context.bot.send_photo(chat_id=update.message.chat_id,
                           photo=f'https://randomfox.ca//images//{random.randrange(121)}.jpg')


def list_items(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='\n'.join(list(materials.keys())))


def item(update, context):
    # Take the context and transform it in a object
    user_says = " ".join(context.args)
    if user_says in materials:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=beautifier_material(user_says, materials[user_says]),
                                 parse_mode='HTML')
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=beautifier_notfound(),
                                 parse_mode='HTML')


def main():
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    # On different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('keyboard', keyboard))
    dp.add_handler(CommandHandler('fox', animations))
    dp.add_handler(CommandHandler('nasa', nasa))
    dp.add_handler(CommandHandler('list', list_items))
    dp.add_handler(CommandHandler('zelda', item))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
