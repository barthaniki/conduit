import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test cookie function
def test_cookies():
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

    # test cookie function - accept
    assert driver.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]').is_displayed() is True
    driver.find_element(By.XPATH,
                        '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]').click()

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
