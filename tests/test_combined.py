import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def test_google_search():
    service = Service('/home/p/Desktop/repositories/chromedriver-linux64/geckodriver')
    driver = webdriver.Firefox(service=service)
 
    driver.get("https://www.google.com")

    # Find the search input element by name attribute value
    search_box = driver.find_element("name", "q")

    # Type a search query
    search_box.send_keys("OpenAI")
    search_box.send_keys(Keys.RETURN)

    # Wait for a while to observe the browser
    time.sleep(3)

    driver.quit()

@pytest.mark.selenium
def test_selenium_ide_exported_script():
    pass

