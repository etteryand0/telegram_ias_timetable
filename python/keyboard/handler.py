# inline keyboard
# Контроль нажатий пользовтеля на кнопки

def handle(update, context) -> None:
    # update: Update
    # context: CallbackContext

    query = update.callback_query

    query.answer()

    if query.data == '1':
        print('Click!')
    elif query.data == '2':
        pass
    elif query.data == '3':
        pass

    query.edit_message_text(text=f"Selected option: {query.data}")

    

# keyboard = [
#     [
#         InlineKeyboardButton("Hi", callback_data='Hi'),
#         InlineKeyboardButton("Hello", callback_data='Hello'),
#     ],
#     [InlineKeyboardButton("Bye", callback_data='Bye')],
# ]
# reply_markup = InlineKeyboardMarkup(keyboard)

# query.edit_message_text(text=f"Selected option: {query.data}", reply_markup=reply_markup)