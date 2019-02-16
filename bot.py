from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler,  CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

TOKEN = "641140353:AAFg9_7e1T_m377LxkbwkQOsI4wPEMGv-zc"
updater = Updater(token=TOKEN)

logging.info("***************INITIALIZING BOT****************")
# Menu function
def menu(bot, update):
    #Main Menu Function
    #This will display the options from the main menu

    # Create buttons
    menu_main = [[InlineKeyboardButton('Set Location', callback_data='set_loc')],
                 [InlineKeyboardButton('Update Location', callback_data='update_loc')],
                 [InlineKeyboardButton("FAQ'S", callback_data='faq')],
                 [InlineKeyboardButton("About The Bot", callback_data='about')]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    update.message.reply_text('Choose the option:', reply_markup=reply_markup)
# def get_location(bot, update):
#     message = None
#     if update.edited_message:
#         message = update.edited_message
#     else:
#         message = update.message
#     current_pos = (message.location.latitude, message.location.longitude)


#All other Sub Menus
def menu_actions(bot, update):
    query = update.callback_query

    # TO DO: Request user Location
    if query.data == 'set_loc':
        set_loc_menu = [[InlineKeyboardButton('Set Home Location', callback_data='home_loc')], 
                        [InlineKeyboardButton('Set Work Location', callback_data='work_loc')]]
        reply_markup = InlineKeyboardMarkup(set_loc_menu)
        bot.edit_message_text(chat_id=query.message.chat_id, 
                                message_id = query.message.message_id,
                                text = "Choose an Option: ",
                                reply_markup=reply_markup)
    # Update Location thats already set
    # To Do check for set location before calling update location
    elif query.data == 'update_loc':
        
        menu_2 = [[InlineKeyboardButton('Update Home Location', callback_data='m2_1')],
                  [InlineKeyboardButton('Update Work Location', callback_data='m2_2')]]
        reply_markup = InlineKeyboardMarkup(menu_2)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text='Choose the option:',
                              reply_markup=reply_markup)

    elif query.data == 'home_loc':
        location_keyboard = KeyboardButton(text="send_location",  request_location=True)           #creating location button object
        contact_keyboard = KeyboardButton('Share contact', request_contact=True)  #creating contact button object
        custom_keyboard = [[ location_keyboard, contact_keyboard ]] #creating keyboard object
        reply_markup = ReplyKeyboardMarkup(custom_keyboard) 
        bot.send_message(chat_id=query.message.chat_id, 
                  text="Would you mind sharing your location and contact with me?", 
                 reply_markup=reply_markup)

dispatcher = updater.dispatcher
menu_handler = CommandHandler('menu', menu)
# location_handler = MessageHandler(Filters.location,get_location, edited_updates=True)
# dispatcher.add_handler(location_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(CallbackQueryHandler(menu_actions))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater.start_polling()

updater.idle()