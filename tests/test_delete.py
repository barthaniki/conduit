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


# test delete function
def test_delete():
    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)

    '''prerequisites:
    - existing test user login
    - create new article to delete'''
    user_name = "testuser1"
    user_email = (user_name + "@example.com")
    password = "Abcd123$"
    driver.find_element(By.XPATH, '//a[@href="#/login"]').click()
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    random_text = "".join([random.choice(string.ascii_lowercase) for _ in range(10)])
    driver.find_element(By.XPATH, '//a[@href="#/editor"]').click()
    time.sleep(2)
    article_title = driver.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
    article_title.send_keys(random_text)
    submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_btn.click()
    time.sleep(2)
    displayed_text = driver.find_element(By.XPATH, '//div[@class="container"]/h1').text
    assert displayed_text == random_text
    time.sleep(2)

    # delete article
    del_btn = driver.find_element(By.XPATH, '//button[@class="btn btn-outline-danger btn-sm"]')
    del_btn.click()
    time.sleep(2)

    # check delete
    driver.find_element(By.XPATH, f'//a[@href="#/@{user_name}/"]').click()
    time.sleep(2)
    displayed_text = len(driver.find_elements(By.XPATH, '//div[@class="container"]/h1'))
    assert displayed_text == 0

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
