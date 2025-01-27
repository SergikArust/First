
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open("log.txt", "w")
driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
#option.add_argument("-headless")
driver = webdriver.Chrome(options=option)
# End of setup
# Scenario functions
def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():

# End of scenario functions

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

def login_with_enter():
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Login OK \n")

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    Password = "secret_sauce"
    password.send_keys(Password)
    file.write("Password OK \n")

    password.send_keys(Keys.ENTER)
    file.write("Password Enter OK \n")
    
def fake_login():
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Login OK \n")

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    Password = "secret_sauce1"
    password.send_keys(Password)
    file.write("Password is fake \n")

    login_butt = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_butt.click()
    file.write("Success click OK \n")
# Start Tests
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
def test_fake_login_label():
     correct_text = "Epic sadface: Username and password do not match any user in this service"
     current_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
     assert correct_text== current_text.text, 'test_fake_login_label if Failed'
     file.write("test_fake_login_label is OK \n")


# End of tests
def sc_real_login():
    set_up()
    login()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_real_login_with_enter():
    set_up()
    login_with_enter()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_fake_login():
    set_up()
    fake_login()
    test_fake_login_label()

sc_real_login_with_enter()
file.close()
