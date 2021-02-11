import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

from commands import cmd_help
from commands import cmd_start

import keyboard

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

with open('.env', 'r') as handler:
    lines = [ i.strip() for i in handler.readlines() ]
    
    env = dict()
    for line in lines:
        items = line.split('=')
        env |= dict([items])

# Create the Updater and pass it your bot's token.
updater = Updater(env["TELEGRAM_BOT_TOKEN"])

print(dir(updater))
print(updater.bot)

updater.dispatcher.add_handler(CallbackQueryHandler(keyboard.handle))

updater.dispatcher.add_handler(CommandHandler('start', cmd_start))
updater.dispatcher.add_handler(CommandHandler('help', cmd_help))

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()