import telebot
import random
from telebot import types

bot = telebot.TeleBot('6321488475:AAH3CaCkZ5FO65a9Q2bPF2s1hBG5D3BcJZo')


@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Факт')
    item2 = types.KeyboardButton('Анекдот')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми:\nФакт - для получения интерсного факта.\nАнекдот - для получения анекдота', reply_markup=markup)


f = open('facts.txt', 'r', encoding='utf-8')
facts = f.read().split('\n')
f.close()

f = open('thinks.txt', 'r', encoding='utf-8')
thinks = f.read().split('\n')
f.close()


@bot.message_handler(content_types=['text'])
def text(message):
    global answer
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Анекдот':
        answer = random.choice(thinks)
    bot.send_message(message.chat.id, answer)


print('yes')
bot.infinity_polling()
