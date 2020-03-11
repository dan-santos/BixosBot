# https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6

import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler


def all_callback(bot, update: Update, **optional_args):
    update.message.reply_text(os.environ['USERS_TO_PING'], quote=False)


def webhook(request):
    bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
    dispatcher = Dispatcher(bot, None, 0)
    dispatcher.add_handler(CommandHandler('all', all_callback))

    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'
