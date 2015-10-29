# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
import unittest
import os
from appium import webdriver
from LMAPPUtil.Utility import AndroidUtility, iOSUtility


class QYSettings_Android(unittest.TestCase):
    util = AndroidUtility()

    def setUp(self):
        # set up appium
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['app'] = os.path.abspath(
            '/Users/NJNUGGET/Documents/Python/WorkSpace/AndroidTestApp/aLAST.apk')
        self.driver = webdriver.Remote(
            'http://172.1.7.54:3000/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


class QYSettings_iOS(unittest.TestCase):
    util = iOSUtility()

    def setUp(self):
        # set up appium
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.3'
        desired_caps['deviceName'] = 'iPhone 6'

        self.driver = webdriver.Remote(
            'http://172.1.7.54:3000/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
