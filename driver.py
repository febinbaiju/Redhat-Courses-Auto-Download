from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from config import URL


def fetch_and_download_raw(_id):
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=selenium")
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    driver.get(URL)
    driver.find_element_by_class_name('showmenu').click()
    driver.find_element_by_id(_id).find_element_by_class_name('button-wrap').find_element_by_tag_name(
        'button').click()
    elem = driver.find_element_by_id('rhtk_player').click()  # click the player to start streaming
    # print(pyautogui.displayMousePosition())
    time.sleep(8)  # we need a delay before we can click the extension
    pyautogui.click(x=1266, y=49, clicks=1)
    time.sleep(3)
    pyautogui.click(x=1200, y=153, clicks=1)
    time.sleep(3)
    pyautogui.click(x=1183, y=423, clicks=1)  # downloading the file
    # driver.close()

