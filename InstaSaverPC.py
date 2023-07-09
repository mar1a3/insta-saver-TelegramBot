
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# telebot
import time
import telebot
from telebot import types
import os
import glob


# элементы бота
api = ''
bot = telebot.TeleBot(api)

# элементы вэбрайвера
driver = webdriver.Chrome(ChromeDriverManager().install())
opts = Options()
opts.add_experimental_option("detach", True)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,text='Привет!\nБот позволяет сохранять фото,\n все типы видео, '
                                          'галереи и прочее из Instagram.'
                                          ,parse_mode="Markdown")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Прислать ссылку на видео'), types.KeyboardButton('Прислать ссылку на фото'))
    bot.send_message(message.chat.id, text=f'Приступим, {message.from_user.first_name}', reply_markup=keyboard)


def after_text_2(message):
    try:
        driver.get("https://saveinsta.app/ru")
        time.sleep(1)
        bot.send_message(message.chat.id, text='Перехожу на страницу...')
        text_bot = driver.find_element_by_name("q")
        name_url = message.text
        text_bot.send_keys(name_url)
        time.sleep(1)
        bot.send_message(message.chat.id, text='Присылаю ссылку на сервер')
        driver.find_element_by_class_name("input-group-btn").click()
        print('Нажимаю на кнопку загрузки')
        time.sleep(1)
        driver.find_element_by_id("closeModalBtn").click()
        time.sleep(1)
        bot.send_message(message.chat.id, text='Закрываю модальное окно')
        driver.find_element_by_class_name("download-items__btn").click()
        time.sleep(3)
        video_name = glob.glob('/Users/aleksandramirnova/Downloads/*.mp4')
        video_name1 = video_name[-1]
        print(video_name1)
        bot.send_message(message.chat.id, text='Последнияя секунда 3..2..1')
        file = open(video_name1, "rb")
        bot.send_video(message.chat.id, file, "Готово!")
        time.sleep(5)
        filename2 = f'{video_name1}'
        os.remove(filename2)
    except Exception as ex:
        print(ex)
        # bot.send_message(message.chat.id,text='Возможно, ваша ссылка из приватного аккаунта, я пока не умею такие скачивать :(')
    finally:
        driver.close()
        driver.quit()
def send_photo(message):
    try:
        driver.get("https://saveinsta.app/ru")
        time.sleep(0.5)
        bot.send_message(message.chat.id, text='Начинаю загрузку...')
        text_bot = driver.find_element_by_name("q")
        name_url = message.text
        text_bot.send_keys(name_url)
        time.sleep(0.5)
        bot.send_message(message.chat.id, text='Получаю ответ от сервера')
        driver.find_element_by_class_name("input-group-btn").click()
        print('нажимаю на загрузку')
        time.sleep(0.5)
        driver.find_element_by_id("closeModalBtn").click()
        time.sleep(1)
        bot.send_message(message.chat.id, text='Нахожу нужное фото')
        driver.find_element_by_class_name("download-items__btn").click()
        print('Нашел кнопку загрузки')
        filename_photo = glob.glob('/Users/aleksandramirnova/Downloads/*.jpg')
        filename_photo1 = filename_photo[-1]
        print(filename_photo1)
        bot.send_message(message.chat.id, text='Последнияя секунда 3..2..1')
        file_photo = open(filename_photo1, "rb")
        bot.send_photo(message.chat.id, file_photo, "here it is!")
        time.sleep(2)
        filename_photo2 = f'{filename_photo1}'
        os.remove(filename_photo2)
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, text='Возможно, ваша ссылка из приватного аккаунта, я пока не умею такие скачивать :(')
    finally:
        driver.close()
        driver.quit()
@bot.message_handler(content_types=['text'])
def get_answer(message):
    if(message.text == 'Прислать ссылку на видео'):
        msg = bot.send_message(message.chat.id,text='Введите ссылку на видео: ',parse_mode="Markdown",reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, after_text_2)
    if(message.text == 'Прислать ссылку на фото'):
        resp = bot.send_message(message.chat.id,text='Введите ссылку на фото: ',parse_mode="Markdown")
        bot.register_next_step_handler(resp, send_photo)
bot.polling(none_stop=True)
