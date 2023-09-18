import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define a list of account credentials
accounts = [
    {"email": "your_email", "password": "your_password", "message": "Hey guys, How're you doin!"},
    {"email": "your_email", "password": "your_password", "message": "I guess all noobs are sleeping!"},
]

def login_and_automate(account):
    email = account["email"]
    password = account["password"]
    message = account["message"]

    # Open a new tab
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
    driver.switch_to.window(driver.window_handles[-1])

    # Open YouTube
    driver.get('https://www.youtube.com')
    time.sleep(4)

    # Click the "Sign in" button
    signIn_btn = driver.find_element(By.XPATH, '//a[@aria-label="Sign in"]')
    signIn_btn.click()
    time.sleep(5)

    # Type the email
    pyautogui.write(email)
    pyautogui.press("enter")
    time.sleep(4)

    # Type the password and press Enter
    pyautogui.write(password)
    pyautogui.press("enter")
    time.sleep(5)

    driver.get("https://www.youtube.com/watch?v=7mn6Gt0Z-_U")
    time.sleep(13)

    pyautogui.click(x=940, y=688)

    pyautogui.write(message)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(10)  # Wait for 10 seconds

    # Click the avatar (account) button
    avatar_btn = driver.find_element(By.ID, 'avatar-btn')
    avatar_btn.click()
    time.sleep(2)

    # Click the "Sign out" button
    sign_out_btn = driver.find_element(By.XPATH, '//yt-formatted-string[text()="Sign out"]')
    sign_out_btn.click()
    time.sleep(5)

# Initialize the Selenium webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Process all accounts sequentially in separate tabs
for account in accounts:
    login_and_automate(account)

# Don't quit the browser here to keep it open after processing all accounts
