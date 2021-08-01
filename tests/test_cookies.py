import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options)


# test cookie function
def test_cookies():
    url = "http://localhost:1667/#/"
    driver.get(url)
    time.sleep(2)

    # accept cookies
    list_divs_by_id = driver.find_elements(By.XPATH, '//div[@id="cookie-policy-panel"]')
    assert len(list_divs_by_id) == 1
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@id="cookie-policy-panel"]//div[contains(text(), "I accept!")]').click()

    # check cookie-policy-panel is disappeared
    time.sleep(2)
    list_divs_by_id = driver.find_elements(By.XPATH, '//div[@id="cookie-policy-panel"]')
    assert len(list_divs_by_id) == 0

    driver.close()
    driver.quit()
