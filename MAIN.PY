import os
from flask import Flask
import telebot
from threading import Thread

# 1. Configurações de segurança (pegas do Render)
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

# 2. Inicialização do Bot e do Servidor Web
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 3. Rota para o Render saber que o bot está vivo
@app.route('/')
def home():
    return "Bot IlevisVariedades está online e rodando!"

# 4. Exemplo de comando: Se você digitar /testar no bot, ele posta no canal
@bot.message_handler(commands=['testar'])
def testar_postagem(message):
    texto = "🚀 **Teste de Postagem Automática**\n\nEste é um exemplo de como os achadinhos aparecerão no canal IlevisVariedades!"
    bot.send_message(CHANNEL_ID, texto, parse_mode='Markdown')
    bot.reply_to(message, "✅ Postagem de teste enviada para o canal!")

# 5. Função para manter o bot ouvindo o Telegram
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Inicia o bot em uma 'linha' separada para não travar o servidor
    t = Thread(target=run_bot)
    t.start()
    
    # Inicia o servidor web que o Render exige
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
