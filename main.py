import os
from flask import Flask
import telebot

# Configurações que você vai colocar no Render
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot IlevisVariedades Online!"

# Comando inicial para testar se o bot está vivo
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! O Bot Vendas Master está pronto para postar ofertas no IlevisVariedades.")

if __name__ == "__main__":
    # Inicia o servidor para o Render não desligar o bot
    from threading import Thread
    Thread(target=bot.infinity_polling).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
