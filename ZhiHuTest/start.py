#-*- coding: utf-8 -*-
__author__ = 'vmture'
import time
from time import sleep
import os
import HTMLTestRunner
import devices
from appium import webdriver
from Appium import StartAppium
import unittest
class ZhihuTest(unittest.TestCase):
    def setUp(self):
        StartAppium.cmd_start()
        desired_caps = {}
        desired_caps.update(devices.Emulator)
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.4'
        # desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appPackage'] = 'com.zhihu.android'
        # desired_caps['appActivity'] = 'com.zhihu.android.app.ui.activity.MainActivity'
        desired_caps['app'] = os.path.abspath('C:\\Users\\dengzihong.ZENMEN\\AutoVTest\\ZhiHuTest\\app\\知乎.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
        StartAppium.cmd_stop()

    def test1(self):
        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)
        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)

        a1 = self.driver.find_element_by_id("com.zhihu.android:id/login_btn")
        self.assertEqual('登录',(a1.text).encode("UTF-8"))
        a1.click()
        print(u"\n弹出登录框")
        sleep(5)

    def test2(self):
        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)
        sleep(5)
        self.driver.swipe(900, 960, 100, 960, 500)

        a1 = self.driver.find_element_by_id("com.zhihu.android:id/login_btn")
        a1.click()
        sleep(5)

        a2 = self.driver.find_element_by_id("com.zhihu.android:id/title")
        self.assertEqual('登录',(a2.text).encode("UTF-8"))

        a3 = self.driver.find_element_by_id('com.zhihu.android:id/btn_cannot_login')
        self.assertEqual('无法登录？',(a3.text).encode("UTF-8"))

        a4 = self.driver.find_element_by_id('com.zhihu.android:id/btn_social_login')
        self.assertEqual('社交帐号登录',(a4.text).encode("UTF-8"))

        a5 = self.driver.find_element_by_id('com.zhihu.android:id/btn_progress')
        self.assertEqual('登录',(a5.text).encode("UTF-8"))

        self.driver.find_element_by_id('com.zhihu.android:id/username').send_keys('*******')
        sleep(1)
        self.driver.find_element_by_id('com.zhihu.android:id/password').send_keys('*******')
        sleep(1)
        self.driver.find_element_by_id('com.zhihu.android:id/btn_progress').click()
        sleep(2)

        a6 = self.driver.find_element_by_id("com.zhihu.android:id/input")
        self.assertEqual('搜索话题、问题或人',(a6.text).encode("UTF-8"))
        print(u'\n登录成功')


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(ZhihuTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
    # testunit = unittest.makeSuite(ZhihuTest)
    time = time.strftime('%Y_%m_%d_%H_%M',time.localtime(time.time()))
    html = time+'.html'
    filename = 'C:\\Users\\dengzihong.ZENMEN\\AutoVTest\\ZhiHuTest\\report\\test_report'+html
    fp = file(filename,'wb')
    # all = [ZhihuTest.test1(),]
    testunit = unittest.TestSuite()
    testunit.addTest(ZhihuTest('test1'))
    testunit.addTest(ZhihuTest('test2'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='test_report',description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()