# This file contains the source code of Rajah Telegram Bot.

from telegram.ext import Updater, CommandHandler
from config.auth import token
import requests


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="HELLO BUDDY!🐯")


def nasa(update, context):
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    r = requests.get(url).json()
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"🛰<b>{r['title']}</b>🛰(<a href='{r['url']}'>{r['date']}</a>) \n{r['explanation']}",
                             parse_mode='HTML')


if __name__ == '__main__':
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # Start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Nasa command
    nasa_handler = CommandHandler('nasa', nasa)
    dispatcher.add_handler(nasa_handler)

    updater.start_polling()
    updater.idle()
