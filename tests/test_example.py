# tests/test_example.py
import time
import allure
import pytest
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import datetime
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import random
import string

from utils.bubble_page import BubblePage


def test_example(driver):
    bubble_page = BubblePage(driver)
    bubble_page.click_hamburger()
    assert driver.find_element(AppiumBy.ID, 'com.ideomobile.maccabi:id/search_icon').is_displayed()

# @pytest.fixture(scope='class')
# def driver():
#     appium_service = AppiumService()
#     appium_service.start(args=['--address', "127.0.0.1", '--port', "4723", "--base-path", '/wd/hub'])
#     # Extracting of adb id device
#     get_connected_devices = lambda: [line.split('\t')[0] for line in subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True).stdout.strip().split('\n')[1:] if line.endswith('\tdevice')]
#     serial_number = get_connected_devices()
#     # Set up Webdriver options
#     options = UiAutomator2Options().load_capabilities({
#         'deviceName': serial_number[0],
#         # 'platformName': 'Android',
#         # 'platformVersion': '11',
#         # 'app': 'C:/applications/maccabi.apk',
#         'appPackage': 'com.ideomobile.maccabi',
#         'appActivity': '.ui.splash.SplashActivity',
#         'autoGrantPermissions': True,
#         'unlockType': 'pin',
#         'unlockKey': '1111'
#     })
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
#     driver.implicitly_wait(30)
#     yield driver
#     driver.quit()
#     appium_service.stop()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def take_screenshot(driver):
#     yield
#     with allure.step('Take a screenshot'):
#         allure.attach(
#             driver.get_screenshot_as_png(),
#             name='screenshot',
#             attachment_type=allure.attachment_type.PNG
#         )
#
#
# @pytest.mark.usefixtures('driver')
# class TestExample:
#     @allure.description("Test checks for pop-up on startup ")
#     @pytest.mark.skip
#     def test_login(self, driver):
#         driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/dynamicActionButton")
#         assert driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/dynamicActionButton").is_displayed()

