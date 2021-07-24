import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True


# test login and logout functions
def test_login_logout():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)
    # driver.set_window_size(1366, 728)

    # test login function
    driver.find_element(By.XPATH, '//a[@href="#/login"]').click()
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys("testuser1@example.com")
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("Abcd123$")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)

    # check login
    assert driver.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a').text == "testuser1"
    time.sleep(2)

    # test logout function
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
