# -*- coding: UTF-8 -*-

'''
Created on 2015年8月12日

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
        desired_caps['platformVersion'] = '8.1'
        desired_caps['deviceName'] = 'iPhone 6'

        self.driver = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
        #self.driver.find_element_by_name(name)
    
    def scroll_screen(self,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        self.driver.swipe(x1, y1, x2, y2, 1000)

        sleep(1)

    def inputString(self,text1,text2):
        user = self.driver.find_element_by_xpath("//UIATextField")
        user.send_keys(text2)
        password = self.driver.find_element_by_xpath("//UIASecureTextField")    
        password.send_keys(text2)
    
    def needLogOut(self,element):
        before = self.driver.find_element_by_xpath("//UIAStaticText[1]").get_attribute("value")
        print(before)
        element.click()
        if before is None:
            return False
        else:
            return True
    
    def test_logIn(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        #进入我的页面
        #self.driver.find_element_by_xpath("//UIAWindow[1]/UIAButton[4]").click()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        sleep(1)
        el = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]")
        if(self.needLogOut(el)==True):
            self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 351, "y": 41 })
            self.driver.switch_to_alert().accept()
            el.click()
        self.inputString("ok123ttt", "lixiang1990922")
        self.driver.find_element_by_xpath("//*[@label='QYLoginButton']").click()
        sleep(2)
            
    def test_addYHP(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        #进入我的页面
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.driver.find_element_by_name("我的优惠").click()
        self.driver.find_element_by_name("添加优惠券").click()
        self.inputString("YHPusr", "YHPpself.driver")
        self.driver.find_element_by_name("加入我的优惠券").click()
        sleep(2)
        
    def test_buyAtOnce(self):
        sleep(2)
        self.scroll_screen(150, 150, 170, 70)
        #进入分类页面
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        sleep(2)       
        #     self.driver.find_element_by_name("Category Hotel").click()
        self.driver.find_element_by_xpath("//UIAScrollView[1]/UIAButton[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]").click()
        sleep(5)
        #     self.driver.find_element_by_xpath("///UIAWindow[1]/UIAButton[2]")
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 311, "y": 639 })
        sleep(1)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[2]").click()
        sleep(1)
        dates = self.driver.find_elements_by_xpath("//UIATableCell/UIAButton")
    
        print(len(dates))
        for i in range(len(dates)):
            if(dates[i].is_enabled()):
                dates[i].click()
                break        
            #         scroll_screen(200, 500, 200, 300)
            self.driver.find_element_by_name("点击添加旅客").click()
            sleep(1)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]").click()
            sleep(1)
            self.driver.find_element_by_name("Confirm Btn").click()
            sleep(1)
            self.driver.find_element_by_name("提交订单").click()
            sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)