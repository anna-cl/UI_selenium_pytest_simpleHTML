# UI Test Selenium with Pytest

# ---------- Installation ----------
# selenium: $sudo pip3 install selenium   or  $pip install selenium
# check version: $pip freeze | grep "selenium"  or  $python -c "import selenium; print(selenium.__version__)"  
# pytest: $pip3 install pytest
# check version: $pytest --version

# ---------- Run the test -----------
# $pytest   or  $pytest -v
# -------------- reference -------------- 
# https://www.youtube.com/watch?v=cG9iymSS3II&ab_channel=AutomationStepbyStep

from selenium import webdriver
from selenium.webdriver.common.by import By
from e1utils import construct_headless_chrome_driver, get_landing_page_url, wait_for_page_load
import time

def test_nonsecret_scenario():
    landing_page = get_landing_page_url()
    driver = construct_headless_chrome_driver()
    
    # ---- You can place additional test code here to drive this one test:
    # driver = webdriver.Chrome()
    driver.get(landing_page)
    wait_for_page_load(driver)

    #driver.find_element_by_id() and driver.find_element_by_name() are removed in selenium 4.3.0:
    driver.find_element("id", "preferredname").send_keys("Name filled") 
    driver.find_element("id", "food").send_keys("Food_filled")
    driver.find_element("id", "secret").send_keys("nonsecret123")
    driver.find_element("id", "submit").click()
    
    # time.sleep(3)  #------- comment out
    driver.quit()


def test_secret_scenario1():
    landing_page = get_landing_page_url()
    driver = construct_headless_chrome_driver()
    # driver = webdriver.Chrome()
    driver.get(landing_page)
    wait_for_page_load(driver)

    driver.find_element("id", "preferredname").send_keys("NAME123") 
    driver.find_element("id", "food").send_keys("FAST_food")
    driver.find_element("id", "secret").send_keys("magic")
    driver.find_element("id", "submit").click()

    driver.find_element("id", "secretButton").click()

    # time.sleep(5)  #------- comment out
    driver.quit()


def test_secret_scenario2():
    landing_page = get_landing_page_url()
    driver = construct_headless_chrome_driver()
    # driver = webdriver.Chrome()
    driver.get(landing_page)
    wait_for_page_load(driver)

    driver.find_element("id", "preferredname").send_keys("456NAME") 
    driver.find_element("id", "food").send_keys("COLOR_food")
    driver.find_element("id", "secret").send_keys("abracadabra")
    driver.find_element("id", "submit").click()

    driver.find_element("id", "secretButton").click()

    # time.sleep(5)  #------- comment out
    driver.quit()


# def test_teardown():
#     landing_page = get_landing_page_url()
#     driver = construct_headless_chrome_driver()
#     # driver = webdriver.Chrome()
#     driver.get(landing_page)
#     driver.quit()
