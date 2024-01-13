# utils/bubble_page.py
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest


class BubblePage:
    def __init__(self, driver):
        self.driver = driver

    def click_hamburger(self):
        hamburger = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='לחצן תפריט צד, לחץ פעמיים לפתיחת '
                                                                                 'התפריט')
        hamburger.click()
