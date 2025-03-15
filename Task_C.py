# This project automates a YouTube search and interacts with the webpage using Selenium and PyAutoGUI. 
# Launches Chrome using Selenium.
# Opens YouTube (https://www.youtube.com/).
# Searches for "Python for beginners by Shradha" using the search bar and presses Enter.
# Uses PyAutoGUI to interact with the screen by moving the mouse and clicking at specific coordinates for liking the video and opening a specific git link and then closes the tab.
# Waits for user input before closing the browser (driver.quit()).

from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
import time
import pyautogui 


driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
time.sleep(3)


username = driver.find_element(By.NAME,'search_query')

username.send_keys('Python for beginners by Shradha')
username.send_keys(Keys.ENTER)
time.sleep(3)


pyautogui.moveTo(380,800)
time.sleep(3)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(520,820)
time.sleep(3)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(350,945)
time.sleep(3)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(1300,50)
time.sleep(3)
pyautogui.click()
time.sleep(3)

input('Press Enter to close.....')
driver.quit()