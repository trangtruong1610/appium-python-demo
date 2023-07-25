from appium import webdriver
import os

filepath = os.path.dirname(__file__)
app_path = os.path.dirname(filepath) + '/apps'

IMPLICITLY_WAIT = 10

appium_server_url = 'http://localhost:4723'
def android_driver(app_name='demo_android_app'):
    path = f"{app_path}/{app_name}.apk"

    desired_cap = {
    "deviceName"                       : "Android",
    "platformName"                     : "Android",
    "app"                              : path,
    "automationName"                   : "uiautomator2",
    "unicodeKeyboard"                  : True,
    "resetKeyboard"                    : True,
    "adbExecTimeout"                   : 300000,
    "androidInstallTimeout"            : 500000,
    "uiautomator2ServerInstallTimeout" : 300000,
    "uiautomator2ServerLaunchTimeout"  : 300000,
    }

    driver = webdriver.Remote(appium_server_url, desired_cap)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver

def ios_driver(app_name='demo_ios_app'):
    path = f"{app_path}/{app_name}.zip"

    desired_cap = {
    "platformName"                     : "iOS",
    "platformVersion"                  : "16.4",
    "deviceName"                       : "iPhone 14 Pro",
    "automationName"                   : "xcuitest",
    "app"                              : path,
    "udid"                             : '5F381E4D-E6E2-4A5D-B8B0-500E2655F036',
    "unicodeKeyboard"                  : True,
    "connectHardwareKeyboard"          : False,
    "sendKeyStrategy"                  : "setValue",
    "includeNonModalElements"          : True,
    "shouldUseTestManagerForVisibilityDetection": True,
    "simpleIsVisibleCheck"             : True,
    }

    driver = webdriver.Remote(appium_server_url, desired_cap)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    return driver
