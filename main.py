

# l = instaloader.Instaloader()
# l.load_session_from_file('elena_kalugina475')
# pp = input("Введите имя пользователя: ")
# l.download_profile(pp, profile_pic_only=True)






# пробный бот на instabot
import instaloader
import time
import telebot
from telebot import types

# элементы бота
api = ''
bot = telebot.TeleBot(api)

# общие переменные
arr = {}

l = instaloader.Instaloader()
l.load_session_from_file('elena_kalugina475')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,text='Welcome to the instaH3lperBot',parse_mode="Markdown")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Показать Ваших подписчиков'))
    bot.send_message(message.chat.id, text=f'Hi, {message.from_user.first_name}', reply_markup=keyboard)


def after_text_2(message):
    l.download_profile(message.text, profile_pic_only=True)
    bot.send_message(message.chat.id, text=f'Вот Ваши подписчики:')

@bot.message_handler(content_types=['text'])
def get_answer(message):
    if(message.text == 'Показать Ваших подписчиков'):
        msg = bot.send_message(message.chat.id,text='Введите свой никнейм в Instagram',parse_mode="Markdown")
        bot.register_next_step_handler(msg, after_text_2)

bot.polling(none_stop=True)







        # for follower in followers:
        #     user = bot.get_username_from_user_id(follower)
#     arr[user] = {
#         'user':user
#     }

# with open('arr.json', 'w') as file:
#     json.dump(arr, file, indent=4, ensure_ascii=False)
#     print(user)

