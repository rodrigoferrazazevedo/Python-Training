from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Google:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'q' #name
        self.btn_search = 'btnK' #name
        self.btn_lucky = 'btnI' #name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_name(self.search_bar).send_keys(word) 
        self.driver.find_element_by_name(self.search_bar).send_keys(Keys.ENTER)

    def lucky(self, word='None'):
        self.driver.find_element_by_name(self.search_bar).send_keys(word) 
        time.sleep(1)
        self.driver.find_element_by_name(self.search_bar).click()
        time.sleep(1)
        self.driver.find_element_by_name(self.search_bar).send_keys(Keys.ESCAPE)
        self.driver.find_element_by_name(self.btn_lucky).click()

ch = webdriver.Chrome(executable_path=r'D:\src\apps\webdrivers\chromedriver.exe')
g = Google(ch)
g.navigate()
#g.search('Rodrigo Ferraz Azevedo')
g.lucky('Rodrigo Ferraz Azevedo')