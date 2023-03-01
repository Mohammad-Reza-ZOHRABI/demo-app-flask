import os
import time
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters

def send_text_file(bot, chat_id, text_file_path):
    with open(text_file_path, 'rb') as f:
        bot.send_document(chat_id, document=f)
    os.remove(text_file_path)

def delete_message(bot, chat_id, message_id):
    time.sleep(20)
    bot.delete_message(chat_id, message_id)

def handle_message(bot, update):
    chat_id = update.message.chat_id
    text_file_path = 'file.txt'  # Replace with your text file path
    send_text_file(bot, chat_id, text_file_path)
    message_id = bot.send_message(chat_id, 'This message will be deleted in 20 seconds.').message_id
    delete_message(bot, chat_id, message_id)

if __name__ == '__main__':
    bot = Bot(TOKEN)
    bot.set_webhook()
    bot.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()