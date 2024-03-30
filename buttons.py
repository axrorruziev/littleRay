from telebot import types


def languages():
    buttons = types.ReplyKeyboardMarkup(row_width=2)

    btn1 = types.KeyboardButton('русский')
    btn2 = types.KeyboardButton('ozbek  tili')
    buttons.add(btn1, btn2)
    return buttons


def buttons1():
    buttons1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton('Адресс🚗')
    btn2 = types.KeyboardButton('Телефон администратора📞')
    btn3 = types.KeyboardButton('Посмотреть одежду👗')
    buttons1.add(btn1, btn2, btn3)
    return buttons1


def buttons2():
    buttons2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton('ADRESS🚗')
    btn2 = types.KeyboardButton('Administrator nomeri📞')
    btn3 = types.KeyboardButton('Kiyimlarni korish👗')
    buttons2.add(btn1, btn2, btn3)
    return buttons2

