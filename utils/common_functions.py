# utils/common_functions.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def handle_popup_skip(driver, element_id):
    try:
        popup_skip = driver.find_element(AppiumBy.ID, element_id)
        if popup_skip.is_displayed():
            popup_skip.click()
    except NoSuchElementException:
        pass
