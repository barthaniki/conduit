import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


# test save function
def test_save():
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

    # save titles of testuser's articles to a file

    my_feed = driver.find_element(By.XPATH, '//a[@href="#/my-feed"]')
    my_feed.click()
    time.sleep(2)

    with open("my_articles.csv", "w") as file:
        titles = driver.find_elements(By.XPATH, '//div[@class="home-my-feed"]//h1')
        titles_list = []

        for title in titles:
            titles_list.append(title.text)

        my_articles = str(titles_list).replace(", ", "\n")
        file.write(my_articles)

    # logout
    driver.find_element(By.XPATH, '//a[@active-class="active"]').click()
    driver.close()
    driver.quit()
