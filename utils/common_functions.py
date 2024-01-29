# utils/common_functions.py
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def handle_popup_skip(driver, element_id, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            popup_skip = driver.find_element(AppiumBy.ID, element_id)
            if popup_skip.is_displayed():
                popup_skip.click()
                return True
        except NoSuchElementException as e:
            logging.warning(f"Element with ID '{element_id}' not found. Attempt {attempt + 1}/{max_attempts}")

    logging.error(f"Element with ID '{element_id}' not found after {max_attempts} attempts.")
    return False  # Element not found
