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
    # create random username and user email address
    user_name = "".join([random.choice(string.ascii_lowercase + string.digits) for _ in range(8)])
    user_email = (user_name + "@example.com")

    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)

    # test registration function
    driver.find_element(By.XPATH, '//a[@href="#/register"]').click()
    driver.find_element(By.XPATH, '//*[@placeholder="Username"]').send_keys(user_name)
    driver.find_element(By.XPATH, '//*[@placeholder="Email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys("Abcd123$")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    driver.find_element_by_class_name("swal-button-container").click()
    time.sleep(1)

    # check login
    assert driver.find_element(By.XPATH, f'//a[@href="#/@{user_name}/"]').text == user_name
    time.sleep(1)

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
