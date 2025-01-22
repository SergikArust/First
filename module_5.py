from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')
driver.maximize_window()

first_element = driver.find_elements(By.XPATH, '(//input[@type="text"])')



sleep(5)