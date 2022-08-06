import telebot

API_TOKEN = '5154893323:AAFFmpAQN73XXfDt7HlHUydOOUWwloq4z3c'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if message.from_user.language_code == "en":
        bot.reply_to(message, """\
բարեվ դզեզ
""")
#     if message.language_code == "hy":
        
#                bot.reply_to(message, """\
#                    inch ka
# """)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()











































# 5154893323:AAFFmpAQN73XXfDt7HlHUydOOUWwloq4z3c