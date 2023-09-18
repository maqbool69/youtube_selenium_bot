import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import csv
import os

# Initialize the Selenium webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# base_url = 
# Initialize the Selenium webdriver
driver.get('https://www.youtube.com')
time.sleep(4)

signIn_btn = driver.find_element(By.XPATH,'//a[@aria-label="Sign in"]').click()
time.sleep(5)

# Type the text you want to write
pyautogui.write("your_email_address")

# Press the Enter key
pyautogui.press("enter")
time.sleep(4)
pyautogui.write("your_password")

# Press the Enter key
pyautogui.press("enter")

time.sleep(5)
driver.get("https://www.youtube.com/watch?v=7mn6Gt0Z-_U")
time.sleep(13)

pyautogui.click(x=940, y=688)

pyautogui.write("Hello, world!")
time.sleep(1)
pyautogui.press("enter")
time.sleep(4000)