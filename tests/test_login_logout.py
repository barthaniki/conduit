import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test login and logout functions
def test_login_logout():
    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)
    # driver.set_window_size(1366, 728)

    # prerequisite: existing test user
    user_name = "testuser1"
    user_email = (user_name + "@example.com")
    password = "Abcd123$"

    # test login function
    driver.find_element(By.XPATH, '//a[@href="#/login"]').click()
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)

    # check login
    assert driver.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a').text == user_name
    time.sleep(2)

    # test logout function
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()

    # check logout
    assert driver.find_element(By.XPATH, '//a[@href="#/login"]').is_displayed()
    time.sleep(2)

    driver.close()
    driver.quit()
