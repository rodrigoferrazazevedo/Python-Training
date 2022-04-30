from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\src\apps\webdrivers\chromedriver.exe')
driver.get('https://www.github.com')
