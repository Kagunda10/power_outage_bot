from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler,  CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "641140353:AAFg9_7e1T_m377LxkbwkQOsI4wPEMGv-zc"
updater = Updater(token=TOKEN)

def start(bot, update):
    menu_main = [[InlineKeyboardButton('Option 1', callback_data='m1')],
                 [InlineKeyboardButton('Option 2', callback_data='m2')],
                 [InlineKeyboardButton('Option 3', callback_data='m3')]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    update.message.reply_text('Choose the option:', reply_markup=reply_markup)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



updater.start_polling()