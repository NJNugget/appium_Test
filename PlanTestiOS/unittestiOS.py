# -*- coding: UTF-8 -*-

'''
Created on 2015年8月26日

@author: NJNUGGET
'''
import unittest
import os
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):
    
    def setUp(self):
        # set up appium
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.3'
        desired_caps['deviceName'] = 'iPhone 6'

        self.driver = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.quit()
    def scroll_screen(self,x1,y1,x2,y2):
        self.driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    def inputString(self,YHPnum,YHPpwd):
        number = self.driver.find_element_by_xpath("//UIATextField")
        number.send_keys(YHPnum)
        password = self.driver.find_element_by_xpath("//UIASecureTextField")    
        password.send_keys(YHPpwd)
    def test_Login(self):
        sleep(3)
#         self.driver.find_element_by_name("default_user_avatar").click()    
        self.driver.find_element_by_xpath("//UIAImage[1]/UIAButton[1]").click()
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 189, "y": 99 })
        self.driver.find_element_by_name("登 录").click()
        self.inputString("ok123ttt", "lixiang1990922")
        self.driver.find_element_by_name("登 录").click()
        sleep(2)
        self.driver.find_element_by_name("退出登录").click()
        self.driver.find_element_by_name("退出").click()
        sleep(2)
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)