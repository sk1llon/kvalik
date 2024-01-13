import telebot
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN


with sqlite3.connect('telegram_bot.db', check_same_thread=False) as conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    table_num INTEGER NOT NULL,
    order_dishes VARCHAR NOT NULL)""")


name = ''
table_number = 0
order_dishes = ''
menu = {'Fish': 300, 'Meat': 400, 'Juice': 100}

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Hi! I can help you to choose and order food you want!\nEnter your name')
    bot.register_next_step_handler(msg, get_table)


def get_table(message):
    global name
    name = message.text
    msg = bot.send_message(message.chat.id, 'Now enter the number of the table you are sitting at (1 - 20)')
    bot.register_next_step_handler(msg, is_correct_table_num_value)


def is_correct_table_num_value(message):
    if message.text.isdigit() and int(message.text) in range(1, 21):
        get_order(message)
    else:
        msg = bot.send_message(message.chat.id, 'Incorrect value. Enter the number of the table again (1 - 20)')
        bot.register_next_step_handler(msg, is_correct_table_num_value)


def get_order(message):
    global table_number
    table_number = message.text
    bot.send_message(message.chat.id, 'Our menu:')
    for keys, values in menu.items():
        bot.send_message(message.chat.id, '{key} - {value} rub'.format(key=keys, value=values))
    msg = bot.send_message(message.chat.id, 'What do you want?', reply_markup=dish_from_menu_markup())
    bot.register_next_step_handler(msg, order_processing)


def dish_from_menu_markup():
    markup = InlineKeyboardMarkup()
    for i_dish in menu.keys():
        dish = InlineKeyboardButton(text=i_dish, callback_data=i_dish)
        markup.add(dish)
    return markup


def order_processing(message):
    global order_dishes
    if isinstance(message, str):
        order_dishes += message
    else:
        order_dishes += message
    order_dishes += ', '
    msg = bot.send_message(message.chat.id, 'Something else?', reply_markup=something_else_markup())
    bot.register_next_step_handler(msg, check_order)


def something_else_markup():
    markup = InlineKeyboardMarkup()
    for i_dish in menu.keys():
        dish = InlineKeyboardButton(text=i_dish, callback_data=i_dish)
        markup.add(dish)
    call_no = InlineKeyboardButton('No', callback_data='No')
    markup.add(call_no)
    return markup


def check_order(message):
    if message.text == 'No':
        print_info(message)
    else:
        order_processing(message)


def print_info(message):
    global order_dishes
    order_dishes = order_dishes[:len(order_dishes) - 2]
    bot.send_message(message.chat.id, 'Let`s check your order.\nTable number - {table_number}\nOrder - {order}'.format(
        table_number=table_number,
        order=order_dishes
    ))
    msg = bot.send_message(message.chat.id, 'Is everything right?', reply_markup=print_info_markup())
    bot.register_next_step_handler(msg, check)


def print_info_markup():
    markup = InlineKeyboardMarkup()
    call_yes = InlineKeyboardButton('Yes', callback_data='Yes')
    call_no = InlineKeyboardButton('No', callback_data='No')
    markup.add(call_yes, call_no)
    return markup


def insert_data(u_name, u_table, u_order):
    cursor.execute('INSERT INTO users (name, table_num, order_dishes) VALUES (?, ?, ?)',
                   (u_name, u_table, u_order))
    conn.commit()


def check(message):
    global order_dishes
    if message.text == 'Yes':
        bot.send_message(message.chat.id, 'Great! Order will be ready in 15 minutes')
        insert_data(name, table_number, order_dishes)
        order_dishes = ''
    elif message.text == 'No':
        order_dishes = ''
        bot.send_message(message.chat.id, 'Let`s try again')
        start(message)


bot.polling(non_stop=True)
