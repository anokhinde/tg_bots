import telegram.ext

with open('venv/config.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text('Hello world')

def help(update, context):
    update.message.reply_text ('''
        Команды бота:
                               
        /start -> Welcome message
        /help -> This message
        /content -> Info
        /contact -> Contacts 
  ''')
    
def content(update, context):
    update.message.reply_text('Message')

def contact(update, context):
    update.message.reply_text('message2')

updater =telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))

updater.start_polling()
updater.idle()
