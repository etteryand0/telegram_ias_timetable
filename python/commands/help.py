# cmd
# Ответ на сообщение-команду "/help"

def cmd_help(update, context) -> None:
    # update: telegram.Update
    # context: telegram.ext.CallbackContext
    
    update.message.reply_text("Use /start to test this bot.")