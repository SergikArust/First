
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.lambdatest.com/selenium-playground/table-data-download-demo')
driver.maximize_window()

class1 = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div/div[1]/div/div/a/img')

sleep(5)


