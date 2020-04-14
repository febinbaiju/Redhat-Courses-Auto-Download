from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui


def fetch_and_download_raw(_id):
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=selenium")
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    driver.get('https://www.redhat.com/rhtapps/promo-rh024/?segment=0')
    driver.find_element_by_class_name('showmenu').click()
    driver.find_element_by_id(_id).find_element_by_class_name('button-wrap').find_element_by_tag_name('button').click()
    element = driver.find_element_by_id('rhtk_player').click() # click the player to start streaming

    time.sleep(5)  # we need a delay before we can click the extension
    pyautogui.click(x=1266, y=49, clicks=1)
    arrows = pyautogui.locateOnScreen("./arrow.png")
    pyautogui.click(x=arrows[0], y=arrows[1], clicks=1, interval=0.0, button="left")
    # print(pyautogui.displayMousePosition())
    pyautogui.click(x=1140, y=419, clicks=1) #downloading the file

