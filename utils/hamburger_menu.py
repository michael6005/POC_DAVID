from appium.webdriver.common.appiumby import AppiumBy


class HamburgerMenu:
    def __init__(self, driver):
        self.driver = driver

    def quick_look(self):
        return self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='לחצן למעבר למבט מהיר')
