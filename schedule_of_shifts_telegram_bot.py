import telebot
from telebot import types
kb3 = types.InlineKeyboardMarkup(row_width=3)

bot = telebot.TeleBot("5560343365:AAFWsgh3glvdFLV5r4MUkI7sts885CHh1Cg")


@bot.message_handler(commands=['start'])
def start_message(message):
    wellcome_message = f'Здравствуйте, {message.from_user.first_name}! Я помогу вам назначить сотрудников на смены.'
    bot.send_message(message.chat.id, wellcome_message)


@bot.message_handler(commands=['help'])
def create_buttons(message):
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    shift_1_button = types.InlineKeyboardButton(text='Утренняя смена', callback_data='shift_1')
    shift_2_button = types.InlineKeyboardButton(text='Дневная смена', callback_data='shift_2')
    shift_3_button = types.InlineKeyboardButton(text='Вечерняя смена', callback_data='shift_3')

    markup_inline.add(shift_1_button, shift_2_button, shift_3_button)
    bot.send_message(message.chat.id, 'Желаете составить график?', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def choose_button_get_action(call):
    if call.data == 'shift_1':
        pass
    elif call.data == 'shift_2':
        pass
    elif call.data == 'shift_3':
        pass


@bot.message_handler(content_types=['text'])
def unknown_message_from_user(message):
    bot.send_message(message.chat.id, 'Позвольте предложить вам воспользоваться одной из команд:'
                                      ' start; help; add; remove;')


bot.polling()
