from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')

    driver.get("https://www.google.com")

    # Find the search input element by name attribute value
    search_box = driver.find_element("name", "q")

    # Type a search query
    search_box.send_keys("duda")

    # Submit the form
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    # Close the browser
    driver.quit()

