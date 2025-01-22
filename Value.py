from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')
driver.maximize_window()

value = driver.find_element(By.XPATH, '//*[@value=""]')


sleep(5)