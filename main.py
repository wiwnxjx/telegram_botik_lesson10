#step1 pip install pytelegrambotapi
import telebot
token="5954530100:AAGUkVKnI-iJXspRGG-BIqNBiwdMRYfpddo"
#step2
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привіт ✌")
# step3 отримання повідомлення від юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ви казали: ' + message.text)
#запуск бота(обов'язково)
bot.polling()































































