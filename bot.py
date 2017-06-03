from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def main():
    updater = Updater("382759234:AAHa38exQk8Ky0q2jjm6AjTHE0tYvcCOSFk")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()
def greet_user(bot, update):
    text = 'Вы запустили своего виртуального друга нажатием на клавишу start'
    print(text)
    update.message.reply_text(text)
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text+';)')   
main()       
greet_user()
talk_to_me()