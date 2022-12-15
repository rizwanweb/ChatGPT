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


class Chat():

    def __init__(self):
        self.link = 'https://chat.openai.com/'
        self.options = webdriver.ChromeOptions()
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

        # LOGIN DETAILS
        self.Username = 'byoussef128970@gmail.com'
        self.Password = 'Tabasco17!'
        
        # ELEMENTS
        self.btnLoginXpath = '/html/body/div/div/div/div[4]/button[1]'
        self.btnGoogleClass = 'c65b543dc'
        self.txtUserID = 'identifierId'
        self.btnUserNextXPath = '//*[@id="identifierNext"]/div/button'
        self.txtPasswordName = 'password'
        self.btnPasswordNextXPath = '//*[@id="passwordNext"]/div/button'
        self.btnDialogXPath = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button'
        self.btnDialog2XPath = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'
        self.btnDoneXPath = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'
        self.textArea = 'textarea'
        self.btnResetXPath = '//*[@id="__next"]/div/div[2]/div/div/nav/a[1]'

    def OpenChatGPT(self):
        # driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get(self.link)

    def Login(self):
        btnLogin = self.driver.find_element(By.XPATH, self.btnLoginXpath).click()
        sleep(2)
        btnGoogle = self.driver.find_element(By.CLASS_NAME, self.btnGoogleClass).click()
        sleep(2)
        txtUser = self.driver.find_element(By.ID, self.txtUserID).send_keys(self.Username)
        sleep(1)
        btnUserNext = self.driver.find_element(By.XPATH, self.btnUserNextXPath).click()
        sleep(2)
        txtPassword = self.driver.find_element(By.NAME, self.txtPasswordName).send_keys(self.Password)
        sleep(1)
        btnPasswordNext = self.driver.find_element(By.XPATH, self.btnPasswordNextXPath).click()
        sleep(3)
        btnDialog = self.driver.find_element(By.XPATH, self.btnDialogXPath).click()
        sleep(2)
        btnDialog2 = self.driver.find_element(By.XPATH, self.btnDialog2XPath).click()
        sleep(3)
        btnDone = self.driver.find_element(By.XPATH, self.btnDoneXPath).click()
        sleep(3)

    def SendMessesage(self, msg):
        textArea = self.driver.find_element(By.TAG_NAME, self.textArea)
        for i in msg:
            textArea.send_keys(i)
            sleep(0.8)
        textArea.send_keys(Keys.ENTER)
    
    def GetData(self):
        pass

    def ClearChat(self):
        reset = self.driver.find_element(By.XPATH, self.btnResetXPath).click()

     
if __name__ == "__main__":

    bot = Chat()

    bot.OpenChatGPT()
    sleep(3)
    bot.Login()
    sleep(3)
    bot.SendMessesage("Hello Chat GPT")
    sleep(20)
    bot.ClearChat()
    sleep(100)