import telebot
import keyboard

BOT_TOKEN = '8061819959:AAFPjnBdL7ARh5F8mdxLgGat2gVg0caeUfw'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text = message.text
    if msg_text == 'Фото':
        bot.send_message(message.chat.id, text='Фоточкиии', reply_markup=keyboard.keyboard2)
    elif msg_text == 'Текст':
        bot.send_message(message.chat.id, text='НУ текст типо', reply_markup=keyboard.keyboard2)
    else:
        bot.send_message(message.chat.id, text='...', reply_markup=keyboard.keyboard1)
bot.polling()