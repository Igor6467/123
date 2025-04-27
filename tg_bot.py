import telebot

BOT_TOKEN = '8061819959:AAFPjnBdL7ARh5F8mdxLgGat2gVg0caeUfw'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()