#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from typing import Final
from auth import TELEGRAM_TOKEN
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flight_search import FlightSearch
from data_manager import DataManager
from strings import *

BOT_USERNAME: Final = '@ajmFlights_bot'


# # Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!')
    if str(update.message.chat.id) in user_data.data.keys():
        await update.message.reply_text('User Found!')
    else:
        await update.message.reply_text('New User, lets get you set up.')
        await update.message.reply_text('Please use the commands /sethome and /addcity to setup your account!')
        user_id = update.message.chat.id
        user_data.add_user(user_id)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('help!')


async def add_city_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('add city!')
    test_city = update.message.text.replace('/addcity', '').strip()
    code = my_search.get_destination_code(test_city)
    user_data.add_airport(str(update.message.chat.id), code)
    await update.message.reply_text(code)


async def set_home_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('set home')
    test_city = update.message.text.replace('/sethome', '')
    print(test_city)
    code = my_search.get_destination_code(test_city)
    print(code)
    user_data.set_home(str(update.message.chat.id), code)


async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Checking for flights!')


# # Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hey there'

    if 'how are you' in processed:
        return 'Im good'

    return "Sorry"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    await update.message.reply_text(user_data.data)
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    response: str = handle_response(text)
    print('Bot: ', response)
    await update.message.reply_text(response)


async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this was a reply')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def check_flights(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id='307799724', text='One message every minute')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Updater
    jq = app.job_queue
    # job_minute = jq.run_repeating(check_flights, interval=60, first=10)

    # Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('addCity', add_city_command))
    app.add_handler(CommandHandler('setHome', set_home_command))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors Handler
    app.add_error_handler(error)

    # Components
    my_search = FlightSearch()
    my_search.find_flights('PDX', 'LAX')

    # Loading User Data
    user_data = DataManager()

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
