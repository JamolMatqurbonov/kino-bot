import telebot
from config import BOT_TOKEN
import handlers
import admin

bot = telebot.TeleBot(BOT_TOKEN)

handlers.register(bot)
admin.register(bot)

if __name__ == "__main__":
    print("🤖 Bot ishga tushdi!")
    bot.infinity_polling()  