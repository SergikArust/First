from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')
driver.maximize_window()

class1 = driver.find_element(By.XPATH, '//*[@class="mr-10"]')

sleep(5)