# utils/bubble_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BubblePage:
    def __init__(self, driver):
        self.driver = driver

    def click_hamburger(self):
        hamburger = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='לחצן תפריט צד, לחץ פעמיים לפתיחת '
                                                                                 'התפריט')
        hamburger.click()

    def popup_we_together(self):
        we_together = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, 'com.ideomobile.maccabi:id/constrainLayoutRootView'))
        )
        return we_together.is_displayed()

    def click_on_scape(self):
        click_on_scape = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.ideomobile.maccabi:id/dynamicActionButton'))
        )
        click_on_scape.click()
