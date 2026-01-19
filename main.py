import os
import telebot
from flask import Flask
from threading import Thread

# 1. Configuração do Servidor Web para o Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot IlevisVariedades Online!"

# 2. Configuração do Bot
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! O Bot IlevisVariedades finalmente está online e pronto!")

@bot.message_handler(commands=['testar'])
def testar(message):
    bot.reply_to(message, "✅ O bot está recebendo suas mensagens corretamente!")

def run_bot():
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

# 3. Execução (A parte que estava dando erro)
if __name__ == "__main__":
    # Inicia o bot em segundo plano
    t = Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    # Inicia o servidor na porta correta do Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
