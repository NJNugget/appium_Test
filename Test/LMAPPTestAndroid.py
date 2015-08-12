# -*- coding: UTF-8 -*-
import os 
from time import sleep

import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['app'] = PATH(
            '../../../AndroidTestApp/aLAST.apk'
        )

        self.driver = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        e1 = TouchAction()
        e1.press(x=110, y=200) \
            .move_to(x=1, y=1)
        e1.release()
        sleep(8)
        elm_category = []
        #elm.append(self.driver.find_element_by_xpath("//*[@text='穷游精选']"))
        
        textlist = ['分类','自由行']
        for i in range (len(textlist)):
            #print(i)
    
            #elm.append(self.driver.find_element_by_xpath("//*[@text=%s"%textlist[i]))
            elm_category.append(self.driver.find_element_by_xpath("//*[@text='%s']"%textlist[i]))
        
        for i in range(len(elm_category)):
            elm_category[i].click()
            sleep(1)
        
        sleep(1)
        els_booking = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        els_booking[6].click()
        #self.loop_for_list(els_booking)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='立即预订']").click()
        sleep(2)
        self.book_detail()
        self.driver.find_element_by_xpath("//*[@text='提交订单']").click()
        
        
    def book_detail(self):
        self.driver.find_element_by_xpath("//*[@text='选择日期']").click()
        sleep(1)
        elm = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        self.loop_for_list(elm)
        sleep(1)
        
        self.driver.find_element_by_xpath("//*[@text='点击添加新旅客']").click()
        sleep(1)
        
        elm_addCustmor = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        #choose custmor
        elm_addCustmor[3].click()
        sleep(1)
        #accept
        elm_addCustmor[1].click()
    
    def loop_for_list(self,elm):
        print(len(elm))
        for i in range(len(elm)):
            elm[i].click()
            sleep(1)
                        
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
