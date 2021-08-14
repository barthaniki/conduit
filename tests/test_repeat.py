import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test repeat function
def test_new_articles():
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
    time.sleep(1)

    user_home = driver.find_element(By.XPATH, f'//a[@href="#/@{user_name}/"]')

    user_home.click()
    time.sleep(1)
    user_articles = len(driver.find_elements(By.XPATH, '//a//h1'))
    time.sleep(1)

    # test repeat function - create new articles from outer file
    count = 0
    with open("tests/new_articles.csv", "r") as data_file:
        data_file = csv.reader(data_file, delimiter=",")
        next(data_file)
        for row in data_file:
            driver.find_element(By.XPATH, '//a[@href="#/editor"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@placeholder="Article Title"]').send_keys(row[0])
            driver.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]').send_keys(row[1])
            driver.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]') \
                .send_keys(row[2])
            driver.find_element(By.XPATH, '//input[@placeholder="Enter tags"]').send_keys(row[3])
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            time.sleep(1)
            count += 1

    # check new articles in list
    user_home.click()
    time.sleep(1)
    user_articles_extended = len(driver.find_elements(By.XPATH, '//a//h1'))
    time.sleep(1)

    assert user_articles_extended == user_articles + count
    time.sleep(1)

    # delete new articles to clear

    for _ in range(count):
        user_home.click()
        time.sleep(2)
        all_articles = driver.find_elements(By.XPATH, '//a//h1')
        last_article = all_articles[-1]
        last_article.click()
        time.sleep(1)
        del_btn = driver.find_element(By.XPATH, '//button[@class="btn btn-outline-danger btn-sm"]')
        del_btn.click()
        time.sleep(2)

    # check after clear
    user_home.click()
    time.sleep(1)
    user_articles_cleared = len(driver.find_elements(By.XPATH, '//a//h1'))
    time.sleep(1)

    assert user_articles_cleared == user_articles

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
