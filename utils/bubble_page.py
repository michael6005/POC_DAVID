# utils/bubble_page.py
from appium.webdriver.common.appiumby import AppiumBy


class BubblePage:
    def __init__(self, driver):
        self.driver = driver

    def click_hamburger(self):
        hamburger = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='לחצן תפריט צד, לחץ פעמיים לפתיחת '
                                                                                 'התפריט')
        hamburger.click()
