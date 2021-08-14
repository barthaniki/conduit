import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test new post function
def test_new_post():
    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)

    # prerequisite: login with existing test user
    user_name = "testuser1"
    user_email = (user_name + "@example.com")
    password = "Abcd123$"
    driver.find_element(By.XPATH, '//a[@href="#/login"]').click()
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    # test new article function

    title = "title"
    about = "about"
    article = "my article"
    tag = "tag"
    comment = "my comment"

    driver.find_element(By.XPATH, '//a[@href="#/editor"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@placeholder="Article Title"]').send_keys(title)
    driver.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]').send_keys(about)
    driver.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]').send_keys(article)
    driver.find_element(By.XPATH, '//input[@placeholder="Enter tags"]').send_keys(tag)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(1)

    # check texts
    assert driver.find_element(By.XPATH, '//div[@class="container"]/h1').text == title
    assert driver.find_element(By.XPATH, '//div[@class="col-xs-12"]/div/p').text == article
    assert driver.find_element(By.XPATH, '//a[@href="#/tag/tag"]').text == tag
    time.sleep(1)

    # post new comment
    driver.find_element(By.XPATH, '//textarea[@placeholder="Write a comment..."]').send_keys(comment)
    driver.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]').click()
    time.sleep(1)

    # check posted comment
    assert driver.find_element(By.XPATH, '//div[@class="card"]/div/p').text == comment

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
