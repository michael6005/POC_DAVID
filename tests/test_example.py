# tests/test_example.py
from appium.webdriver.common.appiumby import AppiumBy
from utils.bubble_page import BubblePage


def test_example(driver):
    bubble_page = BubblePage(driver)
    bubble_page.click_hamburger()
    assert driver.find_element(AppiumBy.ID, 'com.ideomobile.maccabi:id/search_icon').is_displayed()


