from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
import undetected_chromedriver as uc

# proxy_ip_port = '23.109.113.228:9000'
# proxy = Proxy()

# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = proxy_ip_port
# proxy.ssl_proxy = proxy_ip_port
# proxy.socksUsername = 'bZmI45Izfn3Zv4Kc'
# proxy.socksPassword = 'wifi;;;;'

capabilities = webdriver.DesiredCapabilities.CHROME
# proxy.add_to_capabilities(capabilities)

options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://chat.openai.com/')

sleep(3)
btnLogin = driver.find_element(By.XPATH, '/html/body/div/div/div/div[4]/button[1]').click()
sleep(2)
btnGoogle = driver.find_element(By.CLASS_NAME, 'c65b543dc').click()
sleep(2)
txtUser = driver.find_element(By.ID, 'identifierId').send_keys('byoussef128970@gmail.com')
sleep(1)
btnUserNext = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
sleep(2)
txtPassword = driver.find_element(By.NAME, 'password').send_keys('Tabasco17!')
sleep(1)
btnPasswordNext = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
sleep(3)
btnDialog = driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button').click()
sleep(2)
btnDialog = driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
sleep(3)
btnDone = driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
sleep(3)

textArea = driver.find_element(By.TAG_NAME, 'textarea')
btnReset = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/nav/a[1]')
textArea.send_keys('Hello')
sleep(1)
textArea.send_keys(Keys.ENTER)
sleep(20)
btnReset.click()
sleep(600)
