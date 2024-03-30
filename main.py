import telebot
import buttons
from telebot import types

bot = telebot.TeleBot('6513905951:AAFConaNx1NtfQrdzAdkNuSgGeS0RXpMuts')


@bot.message_handler(commands=['start'])
def message_start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Здравствуйте выберите язык\nAssalomu aleykum tilni tanglang', reply_markup=buttons.languages())
    bot.register_next_step_handler(message, languages)


def languages(message):
    user_id = message.from_user.id
    if message.text == 'русский':
        bot.send_message(user_id, 'Здравствуйте,добро пожаловать выберите команду',
                         reply_markup=buttons.buttons1())
        bot.register_next_step_handler(message, comm_rus)

    elif message.text == 'ozbek  tili':
        bot.send_message(user_id, 'Assalomu aleykum,hush kelibsiz harakatni tangkang',
                         reply_markup=buttons.buttons2())
        bot.register_next_step_handler(message, comm_uzb)
def comm_uzb(message):
    user_id = message.from_user.id
    if message.text == 'ADRESS🚗':
        bot.send_message(user_id, 'ADRESS🚗:korasuv33',
                         reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Administrator nomeri📞':
        bot.send_message(user_id, 'ADMINNI NOMERI📞:+998 95 969 76 16',
                         reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Kiyimlarni korish👗':
       bot.send_message(user_id, '👗buzning instagramimizda hamma malumot bor inst:https://www.instagram.com/little_ray_uz?igsh=bHFtNTY0NXRwamlh', reply_markup=types.ReplyKeyboardRemove())

    else:
        bot.register_next_step_handler(comm_uzb)


def comm_rus(message):
    user_id = message.from_user.id
    if message.text == 'Адресс🚗':
        bot.send_message(user_id, 'Aдресс🚗: корасув33 (мы также есть в яндексе)',
                         reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Телефон администратора📞':
        bot.send_message(user_id, 'Телефон администратора📞:+998 95 969 76 16 (заказывать онлайн вы можете либо написав в личку либо написав в instagram \n inst:https://www.instagram.com/little_ray_uz?igsh=bHFtNTY0NXRwamlh',
                         reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Посмотреть одежду👗':
        bot.send_message(user_id, '👗В нашей инсте есть самая новая инфа inst:https://www.instagram.com/little_ray_uz?igsh=bHFtNTY0NXRwamlh',reply_markup=types.ReplyKeyboardRemove())
    else:bot.register_next_step_handler(comm_rus)




bot.infinity_polling()
