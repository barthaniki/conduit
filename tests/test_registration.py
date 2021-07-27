import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import string

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test registration function
def test_registration():
    url = "http://localhost:1667/#/"
    driver.get(url)

    # create test user data
    user_name = "".join([random.choice(string.ascii_lowercase + string.digits) for _ in range(10)])
    user_email = (user_name + "@example.com")
    password = "Abcd123$"

    # test registration function
    driver.find_element(By.XPATH, '//a[@href="#/register"]').click()
    driver.find_element(By.XPATH, '//*[@placeholder="Username"]').send_keys(user_name)
    driver.find_element(By.XPATH, '//*[@placeholder="Email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    driver.find_element_by_class_name("swal-button-container").click()
    time.sleep(2)

    # check login
    assert driver.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a').text == user_name
    time.sleep(2)

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
