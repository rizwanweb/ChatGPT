from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import config

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.linkedin.com/')

uname = driver.find_element(By.ID, 'session_key')
password = driver.find_element(By.ID, 'session_password')
loginBtn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')

driver.implicitly_wait(3)

for c in config.USERNAME:
    uname.send_keys(c)
    sleep(0.1)
for c in config.PASSWORD:
    password.send_keys(c)
    sleep(0.1)

loginBtn.click()
sleep(3)

contacts = [
            "https://www.linkedin.com/in/sadaf-malik-0336a9135/", 
            "https://www.linkedin.com/in/filza-niazi-12b74082/",
            "https://www.linkedin.com/in/sumaiya-naeem79/"
            ]
msgs = [
    "This is to show Rob that Following and Sending msg is possible and easy with linkedin:D",
    "Msgs can be selected from list either by number, comparing string or randomly",
    "I hope this Demo helps with clearing any question about LinkedIn bot, but there are other issues too."
]

titles = [
    "Hello Rob",
    "Selecting Messages from list or file",
    "Thanks"
]
count = 0
for contact in contacts:
    driver.get(contact)
    msg = driver.find_element(By.LINK_TEXT, 'Message')
    sleep(3)
    msg.click()
    sleep(3)
    sub = driver.find_element(By.NAME, 'subject')
    sleep(1)
    for i in titles[count]:
        sub.send_keys(i)
        sleep(0.1)
    
    box = driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
    sleep(1)
    m = "This is to show Rob that Following and Sending msg is possible and easy with linkedin:D"
    for i in msgs[count]:
        box.send_keys(i)
        sleep(0.1)
    # btnSend = driver.find_element(By.CLASS_NAME, "msg-form__send-button")
    # sleep(2)
    Keys.ESCAPE
    # btnClose = driver.find_element(By.CLASS_NAME, "msg-overlay-bubble-header__control")
    # btnClose.click()
    sleep(2)
    count += 1
    


