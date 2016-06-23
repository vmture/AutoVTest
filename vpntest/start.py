__author__ = 'dengzihong'
# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
import os
from appium import webdriver
import time
# import unittest(unittest.TestCase)
class VpnTest():


    def setUp(self):
        'start appium test'
        desired_caps = {}
        # desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '810BBM422E25'
        desired_caps['appPackage'] = 'com.lantern.safecommand'
        desired_caps['appActivity'] = '.act.WelcomeAct'
        # desired_caps['app'] = os.path.abspath('/Users/Vmture/Desktop/SafeVpn_20160309092542_2117_47_debug.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # driver.shake()
        # driver.press(2,3)
        # driver.implicitly_wait(60)


    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    self=VpnTest()
    self.setUp()
    self.quit()