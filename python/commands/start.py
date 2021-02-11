# cmd
# Ответ на сообщение-команду "/start"

from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

def cmd_start(update, context) -> None:
    # update: telegram.Update
    # context: telegram.ext.CallbackContext

    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)