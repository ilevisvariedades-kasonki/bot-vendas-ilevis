import os
import telebot
from flask import Flask
from threading import Thread

# 1. Configuração do Servidor Web
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot IlevisVariedades Online!"

# 2. Configuração do Bot do Telegram
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! O Bot IlevisVariedades está pronto para trabalhar.")

@bot.message_handler(commands=['testar'])
def testar(message):
    bot.reply_to(message, "✅ Conexão com o bot está funcionando!")

def run_bot():
    bot.infinity_polling()

# 3. Execução Principal (Onde estava o erro de indentação)
if __name__ == "__main__":
    # Importante: Estas linhas abaixo DEVEM ter o recuo (espaço) à esquerda
    t = Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
