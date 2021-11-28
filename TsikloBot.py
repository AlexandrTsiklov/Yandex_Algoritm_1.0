import requests
from CourseDollar import course
import telebot
from xml.etree import ElementTree
from time import sleep
import re
from random import randint
import types
from telebot.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



#____________________________Общие функции______________________________


# Является ли цифрой
def data_is_good_digit(digit):
    try:
        digit = int(digit)
        return True
    except:
        return False


#_______________________Фотки, музыка___________________________

dict_data = {  
    'girl': [
        'https://avatars.mds.yandex.net/get-zen_doc/235144/pub_5a9abeea9d5cb3f3c2550c13_5a9abf511410c309f64e0d2b/scale_1200',
        'https://yobte.ru/uploads/posts/2019-11/krasivye-devushki-v-krasnyh-platjah-78-foto-65.jpg',
        'https://bipbap.ru/wp-content/uploads/2015/02/71accf_f4a84ee668bc4f819fba68f556df3aa9_mv2_d_1638_2048_s_2.jpg',
    ],

    'music': [
        open('D:\\My_Documents\\Music\\Hensy_Pobolelo_i_proshlo.mp3', 'rb'),
        open('D:\\My_Documents\\Music\\Ljosha_Svik_Malinovyjj_svet.mp3', 'rb'),
        open('D:\\My_Documents\\Music\\Skillet_Hero.mp3', 'rb')
    ]
            }



bot = telebot.TeleBot('1594700330:AAHWqZzeWKwIscqfIBfQOfuQrZPAZtp9F-M')


# Стартуем
@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Loading...')
    # sleep(3)
    bot.send_message(message.chat.id, '3')
    # sleep(1)
    bot.send_message(message.chat.id, '2')
    # sleep(1)
    bot.send_message(message.chat.id, '1')
    # sleep(1)
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAP9YHRhbbj-G3Vss5taPhLhiUpXetYAAh0EAAJXRBQG1GsyPYhA3iQeBA')
    bot.send_message(message.chat.id, 'Привет, меня зовут TsikloBot. А тебя как?')


name = ''
age = 0


# Знакомимся с юзером
@bot.message_handler(content_types=['text'])
def get_name(message):
    global name
    mt = message.text.lower()
    if 1 < len(mt) <= 15 and len(re.search(r'[a-zA-Z]*', mt).group()) == len(mt):
        bot.send_message(message.chat.id, 'Понял')
        # sleep(1)
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEBK1xgdtWsos9vwUhD7cwPnw8WiW6TaAACsQQAAldEFAajUp1EqftVux8E')
        # sleep(2)
        bot.send_message(message.chat.id, 'А сколько тебе лет?')
        name = mt.capitalize()
        bot.register_next_step_handler(message, get_age)
    else:
        if randint(0, 1) == 0:
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEBK25gdtaBBpz_p7xb8xgpln7p45O3VgAC3QQAAldEFAYOh4TioypQ-R8E')
        else:    
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEBK4NgdtbKXsuA8GifgEuU-uQ83K5hnQAC-gMAAldEFAYdBZVwt955Sh8E')
        bot.send_message(message.chat.id, 'Чёт кривое имя, пробуй снова')


# Добавляем клаву и кнопки
b1 = InlineKeyboardButton(text='Найти инфу по доллару', callback_data='dollar')
b2 = InlineKeyboardButton(text='Подрубить гуууд музло', callback_data='music')
b3 = InlineKeyboardButton(text='Show beautiful girls 😉', callback_data='girl')
k1 = InlineKeyboardMarkup().add(b1).add(b2).add(b3)
# ====111111====Как сделать в строку, но чтобы видно всю надпись было==========


# Распределяет по функциям нажатые кнопки
@bot.callback_query_handler(func=lambda call_5: True)
def button_way(click):
    global user_id
    user_id = click.from_user.id

    if click.data == 'girl':
        msg = bot.send_message(click.from_user.id, 'Сколько фоток? (p.s. Не больше 3)')
        bot.register_next_step_handler(msg, go_photo_girls)
    elif click.data == 'music':
        msg = bot.send_message(click.from_user.id, 'Сколько треков? (p.s. Не больше 3)')
        bot.register_next_step_handler(msg, go_listen_music)
    else:
        year_ago = course.dollar_year_ago()
        month_ago = course.dollar_month_ago()
        week_ago = course.dollar_week_ago()
        yesterday = course.dollar_yesterday()
        today = course.dollar_today()
        bot.send_message(user_id, text=f'Год назад:  {year_ago}\n\
Месяц назад:  {month_ago}\n\
Неделю назад:  {week_ago}\n\
Вчера:  {yesterday}\n\
Сегодня:  {today}\n', 
        )

    
# Отвечает за фотки девушек
def go_photo_girls(message):
    if data_is_good_digit(message.text) and int(message.text) in range(1, 4):
        for i in range(int(message.text)):
                bot.send_photo(message.chat.id, dict_data['girl'][i])
                sleep(1)
        

# Отвечает за музыку
def go_listen_music(message):
    if data_is_good_digit(message.text) and int(message.text) in range(1, 4):
        for i in range(int(message.text)):
                bot.send_audio(message.chat.id, dict_data['music'][i])


# Узнаём возраст, бросаем клавиатуру
def get_age(message):
    global age
    if data_is_good_digit(message.text) is True:
        age = int(message.text)
        if 0 < age < 118:               # ====222222====Как выровнять надпись по ширине==========
            bot.send_message(message.chat.id, 'Ураaaaa!!!\nТеперь смотри, что я могу:', reply_markup=k1)
        else:
            bot.send_message(message.chat.id, 'Подозрительно, введи нормальный возраст!')
            bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.chat.id, 'Цифрами плз')
        bot.register_next_step_handler(message, get_age)


bot.polling(none_stop=True)
