import logging
import telegram.ext

# модуль ведения журнала логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# читаем API KEY из файла
with open('venv/config.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("Привет! Я твой служебный бот - Selenas_memoris_bot")

def help(update, context):
    update.message.reply_text('''
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

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Sorry, I didn't understand that command.")
    
if __name__ == '__main__':
    # создание экземпляра бота через `ApplicationBuilder`
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler("start", start))
    disp.add_handler(telegram.ext.CommandHandler("help", help))
    disp.add_handler(telegram.ext.CommandHandler("content", content))
    disp.add_handler(telegram.ext.CommandHandler("contact", contact))

    updater.start_polling()
    updater.idle()
