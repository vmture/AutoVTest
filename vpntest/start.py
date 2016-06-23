# -*- coding: utf-8 -*-
__author__ = 'dengzihong'
#from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
import os
from appium import webdriver
from time import sleep
import time
import unittest
class VpnTest(unittest.TestCase):


    def setUp(self):
        'start appium test'
        desired_caps = {}
        # desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '810BBM422E25'
        desired_caps['appPackage'] = 'com.lantern.safecommand'
        desired_caps['appActivity'] = 'com.lantern.safecommand.act.WelcomeAct'
        desired_caps['app'] = os.path.abspath('C:\\Users\\dengzihong.ZENMEN\\Desktop\\vpn\\SafeVpn_20160622171044_2929_159_.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # driver.shake()
        # driver.press(2,3)
        # driver.implicitly_wait(60)


    def tearDown(self):
        self.driver.quit()


    def test(self):

        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)
        sleep(5)

        self.driver.swipe(900, 960, 100, 960, 500)
        sleep(5)

        a1 = self.driver.find_element_by_id("com.lantern.safecommand:id/next_page")
        self.assertEqual('立即体验',a1.text)
        a1.click()

        sleep(5)

        a2 = self.driver.find_element_by_id("com.lantern.safecommand:id/btn_already_invite")
        self.assertEqual('已体验用户',a2.text)
        a2.click()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(VpnTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()