from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
# chrome_options.add_extension('./HLS-Downloader_v1.7.2.crx')
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get('https://www.redhat.com/rhtapps/promo-rh024/?segment=0')
element = driver.find_element_by_id('rhtk_player').click() # click the player to start streaming

time.sleep(5)  # we need a delay before we can click the extension
import pyautogui
#print(pyautogui.displayMousePosition())
pyautogui.click(x=1236,y=51,clicks=1)

