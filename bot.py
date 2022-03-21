import logging
import settings
from telegram.ext import Updater, CommandHandler,CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def start_bot(update: Updater, context: CallbackContext):
    print(update)
    mytext = """Дарова {} Я только появился и буду в скором времени развиваться :) 
    
p.s. Санчо мой создатель  """.format(update.message.chat.first_name)
    logging.info('User {} press /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)


def name(update: Updater):
    update.message.chat.first_name

def reply(update: Updater):
    text = update.message.text
    update.message.reply_text(text)

def chat(update: Updater, context: CallbackContext):
    text = update.message.text
    logging.info(text)

    if name == 'Санчо':
        reply + 'Ты прекрасен Санчо'
    else:
        reply()

def main():
    updtr = Updater(settings.TOKEN_TG)

    updtr.dispatcher.add_handler(CommandHandler("start",start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logging.info('Bot started!')
    main()

