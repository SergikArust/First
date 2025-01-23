
from selenium import webdriver
from selenium.webdriver.common.by import By


file = open("log.txt", "w")
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
#option.add_experimental_option("detach", True)
option.add_argument("-headless")
driver = webdriver.Chrome(options=option)

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Login OK \n")

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    Password = "secret_sauce"
    password.send_keys(Password)
    file.write("Password OK \n")

    login_butt = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_butt.click()
    file.write("Success click OK \n")

def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "Test FAIL"
    file.write("Test is OK \n")

def test_context_after_login_is_correct():
    correct_text = "Products"
    concurrent_text = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
    assert correct_text == concurrent_text.text,"test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")
set_up()
login()
test_login_redirect()
test_context_after_login_is_correct()
file.close()
