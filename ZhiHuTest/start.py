#-*- coding: utf-8 -*-
__author__ = 'dengzihong'
import os
from appium import webdriver
from time import sleep
import unittest
class ZhihuTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.zhihu.android'
        desired_caps['appActivity'] = 'com.zhihu.android.app.ui.activity.MainActivity'
        desired_caps['app'] = os.path.abspath('C:\\WDJDownload\\Apps\\知乎.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)
        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)
        a1 = self.driver.find_element_by_id("com.zhihu.android:id/login_btn")
        self.assertEqual('登录',(a1.text).encode("UTF-8"))
        a1.click()
        sleep(5)
        a2 = self.driver.find_element_by_id("com.zhihu.android:id/title")
        self.assertEqual('登录',(a2.text).encode("UTF-8"))
        a3 = self.driver.find_element_by_id('com.zhihu.android:id/btn_cannot_login')
        self.assertEqual('无法登录？',(a3.text).encode("UTF-8"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ZhihuTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()

