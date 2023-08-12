
from selenium.webdriver.common.keys import Keys
import time

# telebot
import time
import telebot
from telebot import types
import os
import glob


# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
# headless mode
options.headless = True

driver = webdriver.Chrome(
    executable_path="/home/insta_bot/chromedriver",
    options=options
)

# элементы бота
api = ''
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,text='Welcome to the instaH3lperBot',parse_mode="Markdown")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Загрузить фото профиля'))
    bot.send_message(message.chat.id, text=f'Hi, {message.from_user.first_name}', reply_markup=keyboard)


def after_text_2(message):
    try:
        driver.get("https://saveinsta.app/ru")
        time.sleep(0.5)
        text_bot = driver.find_element_by_name("q")
        name_url = message.text
        text_bot.send_keys(name_url)
        time.sleep(0.5)
        driver.find_element_by_class_name("input-group-btn").click()
        time.sleep(0.5)
        driver.find_element_by_id("closeModalBtn").click()
        time.sleep(0.5)
        driver.find_element_by_class_name("download-items__btn").click()
        filename = glob.glob('/Users/ejksi/Downloads/*.mp4')
        filename1 = filename[0]
        print(filename1)
        file = open(filename1, "rb")
        bot.send_video(message.chat.id, file, "here it is!")
        time.sleep(2)
        filename2 = f'{filename1}'
        os.remove(filename2)
    except Exception as es:
        print('ex')
    finally:
        driver.close()
        driver.quit()

@bot.message_handler(content_types=['text'])
def get_answer(message):
    if(message.text == 'Загрузить фото профиля'):
        msg = bot.send_message(message.chat.id,text='Введите ссылку в инстаграме',parse_mode="Markdown")
        bot.register_next_step_handler(msg, after_text_2)

bot.polling(none_stop=True)

