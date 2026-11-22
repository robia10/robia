import telebot

TOKEN = "9028447508:AAEuUeui8aLKVUSLwYeRsVNWSvPa2oj3GeU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! 🥰 Я твой первый Telegram-бот!")

bot.infinity_polling()
