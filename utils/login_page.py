# utils/login_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def skip_fingerprint_login(self):
        skip_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.ideomobile.maccabi:id/btn_positive'))
        )
        skip_btn.click()

    def password_login_tab(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "התחברות באמצעות סיסמה")

    def login_with_credentials(self, member_id, password):
        input_member_id = self.driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/textInputEditText")
        input_member_id.click()
        input_member_id.send_keys(member_id)
        input_member_password = self.driver.find_element(AppiumBy.ID,
                                                         "com.ideomobile.maccabi:id/textInputEditTextPassword")
        input_member_password.click()
        input_member_password.send_keys(password)

    def enter_button(self):
        return self.driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/enterButton")

