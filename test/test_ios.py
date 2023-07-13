import unittest
from appium.webdriver.common.appiumby import AppiumBy
from driver.appium_driver import ios_driver


class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = ios_driver()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_iOS(self):
        item = self.driver.find_element(AppiumBy.XPATH, '(//*[@label = "Sauce Labs Backpack"])[1]')
        item.click()

        add_to_card_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button')
        add_to_card_btn.click()

        tab_bar_option_cart_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'tab bar option cart')
        tab_bar_option_cart_btn.click()

        remove_item_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'remove item')
        remove_item_btn.click()

if __name__ == '__main__':
    unittest.main()
