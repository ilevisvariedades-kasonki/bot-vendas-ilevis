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
    # Garanta que as linhas abaixo tenham 4 espaços de recuo à esquerda
    t = Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    # 2. Depois liga o servidor web
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
