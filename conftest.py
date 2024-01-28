# conftest.py
import base64
import subprocess
import time
import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
import allure
import os


def start_appium_service():
    AppiumService().start(args=['--address', '127.0.0.1', '--port', '4723', '--base-path', '/wd/hub'])


def get_connected_devices():
    return [line.split('\t')[0] for line in
            subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True).stdout.strip().split('\n')[
            1:] if
            line.endswith('\tdevice')]


def initialize_driver():
    options = UiAutomator2Options().load_capabilities({
        'deviceName': get_connected_devices()[0],
        'appPackage': 'com.ideomobile.maccabi',
        'appActivity': '.ui.splash.SplashActivity',
        'automationName': 'UiAutomator2',
        'autoGrantPermissions': True,
        'unlockType': 'pin',
        'unlockKey': '1111'
    })
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    driver.implicitly_wait(30)
    return driver


@pytest.fixture(scope='session')
def driver():
    start_appium_service()
    driver = initialize_driver()
    yield driver
    driver.quit()
    AppiumService().stop()


@pytest.fixture(scope='function')
def screen_recorder(driver):
    driver.start_recording_screen()
    video_name = time.strftime("%Y_%m_%d_%H_%M_%S")
    filepath = os.path.join("screen_records", video_name + ".mp4")

    if not os.path.exists("screen_records"):
        os.makedirs("screen_records")

    yield

    video_rawdata = driver.stop_recording_screen()
    with open(filepath, "wb") as vd:
        vd.write(base64.b64decode(video_rawdata))

    allure.attach.file(filepath, name="Screen Recording", attachment_type=allure.attachment_type.MP4)


