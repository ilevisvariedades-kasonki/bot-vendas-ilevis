import os
from flask import Flask
import telebot
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot IlevisVariedades Online!"

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot IlevisVariedades funcionando!")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    if __name__ == "__main__":
    # 1. Primeiro liga o bot em uma Thread (segundo plano)
    t = Thread(target=run_bot)
    t.daemon = True  # Isso garante que ele não trave o servidor
    t.start()
    
    # 2. Depois liga o servidor web
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
