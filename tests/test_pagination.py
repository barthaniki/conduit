import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test pagination function
def test_pagination():
    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)

    # prerequisite: existing test user login
    user_name = "testuser1"
    user_email = (user_name + "@example.com")
    password = "Abcd123$"
    driver.find_element(By.XPATH, '//a[@href="#/login"]').click()
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    # test pagination function
    p_buttons = driver.find_elements(By.CLASS_NAME, "page-link")

    for button in p_buttons:
        if button.is_enabled():
            button.click()
            time.sleep(1)
        else:
            break

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
