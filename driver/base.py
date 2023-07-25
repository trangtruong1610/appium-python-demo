import unittest

from config_local import platform

from driver.appium_driver import ios_driver, android_driver


class BaseTest(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = ios_driver() if platform == 'ios' else android_driver()
