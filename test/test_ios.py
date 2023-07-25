from appium.webdriver.common.appiumby import AppiumBy
from driver.base import BaseTest


class TestAppium(BaseTest):

    def test_iOS(self):
        item = self.driver.find_element(AppiumBy.XPATH, '(//*[@label = "Sauce Labs Backpack"])[1]')
        item.click()

        add_to_card_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button')
        add_to_card_btn.click()

        tab_bar_option_cart_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'tab bar option cart')
        tab_bar_option_cart_btn.click()

        remove_item_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'remove item')
        remove_item_btn.click()

        assert 4 == 1

