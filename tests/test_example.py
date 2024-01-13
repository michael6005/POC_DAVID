# tests/test_example.py
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from utils.bubble_page import BubblePage


@pytest.mark.usefixtures("screen_recorder")
def test_example(driver):
    bubble_page = BubblePage(driver)
    bubble_page.click_hamburger()
    assert driver.find_element(AppiumBy.ID, 'com.ideomobile.maccabi:id/search_icon').is_displayed()
