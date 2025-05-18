import telebot
import keyboard
import fsm

BOT_TOKEN = '8061819959:AAFPjnBdL7ARh5F8mdxLgGat2gVg0caeUfw'
stater = fsm.FSM()
bot = telebot.TeleBot(BOT_TOKEN)

def handle_default_state(message):
    if message.text == 'Фото':
        stater.set_state(message.chat.id, fsm.IMAGE_STATE)
        bot.send_message(message.chat.id, text='Напиши описание фото', reply_markup=keyboard.keyboard2)
    elif message.text == 'Текст':
        stater.set_state(message.chat.id, fsm.TEXT_STATE)
        bot.send_message(message.chat.id, text='Напиши то, о чём ты хочешь спросить меня', reply_markup=keyboard.keyboard2)
    else:
        return_to_menu(message.chat.id)

def handle_image_state(message):
    if message.text == 'В меню':
        return_to_menu(message.chat.id)
    else:
        # TODO
        bot.send_message(message.chat.id, text='Генерирую фото...')

def handle_text_state(message):
    if message.text == 'В меню':
        return_to_menu(message.chat.id)
    else:
        # TODO
        bot.send_message(message.chat.id, text='Генерирую текст...')

def return_to_menu(chat_id):
    stater.set_state(chat_id, fsm.DEFAULT_STATE)
    bot.send_message(chat_id, text='Главное меню', reply_markup=keyboard.keyboard1)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    state = stater.get_state(message.chat.id)

    if state == fsm.DEFAULT_STATE:
        handle_default_state(message)
    elif state == fsm.IMAGE_STATE:
        handle_image_state(message)
    elif state == fsm.TEXT_STATE:
        handle_text_state(message)
    else:
        return_to_menu(message.chat.id)

bot.polling()