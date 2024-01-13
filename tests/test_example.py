﻿# tests/test_example.py
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from utils.bubble_page import BubblePage
from utils.hamburger_menu import HamburgerMenu


@pytest.mark.usefixtures("screen_recorder")
def test_example(driver):
    bubble_page = BubblePage(driver)
    hamburger_menu = HamburgerMenu(driver)
    if bubble_page.popup_we_together():
        bubble_page.click_on_scape()
    bubble_page.click_hamburger()
    assert hamburger_menu.quick_look().text == 'מבט מהיר'
