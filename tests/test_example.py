# tests/test_example.py
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from utils.bubble_page import BubblePage
from utils.hamburger_menu import HamburgerMenu
from utils.login_page import LoginPage
from utils.common_functions import handle_popup_skip


@pytest.mark.skip
@pytest.mark.usefixtures("screen_recorder")
def test_example(driver):
    bubble_page = BubblePage(driver)
    hamburger_menu = HamburgerMenu(driver)
    if bubble_page.popup_we_together():
        bubble_page.click_on_scape()
    bubble_page.click_hamburger()
    assert hamburger_menu.quick_look().text == 'מבט מהיר'


@pytest.mark.usefixtures("screen_recorder")
def test_login(driver):
    bubble_page = BubblePage(driver)
    hamburger_menu = HamburgerMenu(driver)
    login_page = LoginPage(driver)
    bubble_page.whats_new_close()
    if bubble_page.popup_we_together():
        bubble_page.click_on_scape()
    bubble_page.click_hamburger()
    hamburger_menu.quick_look().click()
    login_page.skip_fingerprint_login()
    login_page.password_login_tab().click()
    login_page.login_with_credentials("125", "Aa123456")
    driver.press_keycode(4)
    login_page.enter_button().click()
    handle_popup_skip(driver, "com.ideomobile.maccabi:id/btnAction1")
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "מבט מהיר").get_attribute("content-desc") == "מבט מהיר"
