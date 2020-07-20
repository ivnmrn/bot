# This file contains the source code of Rajah Telegram Bot.

from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
from config.auth import token
from zelda_items import materials
from util import beautifier_nasa, beautifier_material, beautifier_help
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
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=beautifier_material(user_says, materials[user_says]),
                             parse_mode='HTML')


if __name__ == '__main__':
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # Start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Help command
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    # Display keyboard
    keyboard_handler = CommandHandler('keyboard', keyboard)
    dispatcher.add_handler(keyboard_handler)

    # Animations command
    animations_handler = CommandHandler('fox', animations)
    dispatcher.add_handler(animations_handler)

    # Nasa command
    nasa_handler = CommandHandler('nasa', nasa)
    dispatcher.add_handler(nasa_handler)

    # List command, show all items
    list_items_handler = CommandHandler('list', list_items)
    dispatcher.add_handler(list_items_handler)

    # Zelda command, when you use this command you will get the information of the item sent
    # /Zelda {item to search}
    zelda_handler = CommandHandler('zelda', item)
    dispatcher.add_handler(zelda_handler)

    updater.start_polling()
    updater.idle()
