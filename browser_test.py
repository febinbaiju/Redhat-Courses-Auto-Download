from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import URL

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get(URL)