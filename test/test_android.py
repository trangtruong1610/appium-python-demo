from appium.webdriver.common.appiumby import AppiumBy
from driver.base import BaseTest


class TestAppium(BaseTest):

    def test_android(self):
        signup_btn = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/signup_btn')
        signup_btn.click()

        name = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/name')
        name.send_keys('test')

        address = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/address')
        address.send_keys('demo')

        city = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/city')
        city.send_keys('city')

        state = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/state')
        state.send_keys('state')

        pin = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/pin')
        pin.send_keys('1234')

        mobile = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/mobile')
        mobile.send_keys('123456789')

        email = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/email')
        email.send_keys('test@gmail.com')

        date_birth = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/date_birth')
        date_birth.click()

        ok_btn = self.driver.find_element(AppiumBy.XPATH, '//*[@text="OK"]')
        ok_btn.click()

        password = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/password')
        password.send_keys('password')

        email_sign_up_button = self.driver.find_element(AppiumBy.ID, 'com.call4site.handymanservices:id/email_sign_up_button')
        email_sign_up_button.click()

        assert 4 == 1

