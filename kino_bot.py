import telebot
from config import BOT_TOKEN
import admin
import handlers

bot = telebot.TeleBot(BOT_TOKEN)

admin.register(bot)
handlers.register(bot)

if __name__ == "__main__":
    print("🤖 Bot ishga tushdi!")
    bot.infinity_polling()