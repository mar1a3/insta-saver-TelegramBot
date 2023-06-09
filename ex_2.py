# webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
import glob

# элементы вэбрайвера
driver = webdriver.Chrome(ChromeDriverManager().install())
opts = Options()
opts.add_experimental_option("detach", True)

def get_video():
    try:
        driver.get("https://ru.savefrom.net/240/")
        time.sleep(2)
        input_savefrom = driver.find_element_by_name("sf_url")
        url = "https://www.instagram.com/reel/CHEeTvzFVPB/"
        input_savefrom.send_keys(url)
        driver.find_element_by_id("sf_submit").click()
        print('btn submit click')
        time.sleep(4)
        driver.find_element_by_class_name("def-btn-box").click()
        print('clicked')
        time.sleep(4)
        photo_path = glob.glob('/Users/aleksandramirnova/Downloads/*.mp4')
        downloaded_photo = photo_path[-1]
        print(downloaded_photo)
    except Exception as ex:
        print(ex)
get_video()