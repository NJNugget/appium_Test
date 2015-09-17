# -*- coding: UTF-8 -*-

'''
Created on 2015年8月12日

@author: NJNUGGET
'''
import unittest
from appium import webdriver
from time import sleep
import xPath as GD

class QYLM171iOSTests(unittest.TestCase):
    '''
    通用功能
    1、启动和终止功能
    2、滚动屏幕
    3、输入文本
    4、判断是否需要登出
    '''

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
        #self.driver.find_element_by_name(name)    
    def scroll_screen(self,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        self.driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    def inputString(self,text1,text2):
        user = self.driver.find_element_by_xpath("//UIATextField")
        password = self.driver.find_element_by_xpath("//UIASecureTextField")
        user.click()
        user.send_keys(text1)    
        password.click()
        password.send_keys(text2)    
    def needLogOut(self,element):
        before = self.driver.find_element_by_xpath("//UIAStaticText[1]").get_attribute("value")
        print(before)
        element.click()
        if before is None:
            return False
        else:
            return True
    
    '''
    V1.7.1测试用例
    1、登录登出
    2、添加优惠券
    3、购买流程
    4、查询订单
    5、删除收藏
    6、添加删除提醒
    7、选择穷游精选
    8、搜索功能
    9、筛选功能

    '''
    def test_logIn(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        #进入我的页面
        #self.driver.find_element_by_xpath("//UIAWindow[1]/UIAButton[4]").click()
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        sleep(1)
        el = self.driver.find_element_by_xpath(GD.MINE_USERNAME_IOS)
        if(self.needLogOut(el)==True):
            self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 351, "y": 41 })
            self.driver.switch_to_alert().accept()
            el.click()
        self.inputString("ok123ttt", "lixiang1990922")
        self.driver.find_element_by_xpath(GD.MINE_QYLOGIN_BUTTON_IOS).click()
        sleep(2)            
    def test_addYHP(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        #进入我的页面
        self.driver.find_element_by_xpath(GD.MINE_YHP_IOS).click()
        self.driver.find_element_by_name("我的优惠").click()
        self.driver.find_element_by_name("添加优惠券").click()
        self.inputString("YHP0003200002459","123456")
        self.driver.find_element_by_name("加入我的优惠券").click()
        sleep(2)        
    def test_buyAtOnce(self):
        sleep(2)
        self.scroll_screen(150, 150, 170, 70)
        #进入分类页面
        self.driver.find_element_by_xpath(GD.CATEGORY_BUTTON_IOS).click()
        sleep(2)       
        #self.driver.find_element_by_name("酒店").click()
        self.driver.find_element_by_xpath(GD.CATEGORY_FLIGHT_IOS).click()
        sleep(1)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS).click()
        sleep(8)
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 311, "y": 639 })
        sleep(1)
            
#         self.driver.find_element_by_xpath(GD.SUBMIT_DATE_IOS).click()
        self.driver.find_element_by_name("选择日期").click()
        sleep(1)
        dates = self.driver.find_elements_by_xpath(GD.CALENDAR_BUTTON_IOS)
           
        print(len(dates))
        for i in range(len(dates)):
#             此处注意enabled这个属性不能用get_attributes查看，有专用的is_enabled
            if(dates[i].is_enabled()):
                dates[i].click()
                break        
            #         scroll_screen(200, 500, 200, 300)
        try:
            self.driver.find_element_by_name("提交订单").click()
            sleep(2)
        except:
            self.driver.find_element_by_name("点击添加旅客").click()
            sleep(1)
            self.driver.find_element_by_xpath(GD.PASSANGER_CHECKBOX_IOS).click()
            sleep(1)
            self.scroll_screen(100, 150, 100, 70)
            self.driver.find_element_by_name("Confirm Btn").click()
            sleep(1)
            self.driver.find_element_by_name("提交订单").click()
            sleep(2)            
    def test_check_order(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        self.driver.find_element_by_name("我的订单").click()
        sleep(2)
        self.scroll_screen(300, 150, 100, 150)
        sleep(1)
        self.scroll_screen(300, 150, 100, 150)
    def test_check_delete_colletion(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        self.driver.find_element_by_name("我的收藏").click()
        sleep(2)
        self.scroll_screen(300, 150, 100, 150)
        sleep(3)
        self.driver.find_element_by_name("取消 收藏").click()
        sleep(5)
    def test_check_notice(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
#         self.driver.find_element_by_name("Tab Mine").click()
        self.driver.find_element_by_name("我的提醒").click()
        sleep(2)
        self.driver.find_element_by_name("My Remind Add").click()
        sleep(2)
        self.driver.find_element_by_name("旅行时间").click()
        self.driver.find_element_by_xpath(GD.NOTICE_TRAVELTIME_IOS).click()
        #//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAImage[3]/UIAStaticText[1]
        sleep(1)
        self.driver.find_element_by_name("确定").click()
        sleep(8)
        self.scroll_screen(300, 150, 100, 150)
        self.driver.find_element_by_xpath(GD.NOTICE_DELETE_IOS).click()
        self.driver.find_element_by_name("确定").click()
      
        sleep(3)
    def test_check_Qyer_choiceness(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
#         self.driver.find_element_by_name("Tab Discover").click()
        self.driver.find_element_by_xpath(GD.SELECTED_BUTTON_IOS).click()
        sleep(3)
        self.driver.find_element_by_xpath(GD.SELECTED_PRODUCT_IOS).click()
        sleep(3)
              
    def test_check_search(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.SEARCH_BUTTON_IOS).click()
        content = self.driver.find_element_by_xpath("//UIATextField")
        content.send_keys("japan")
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 343, "y": 646 })
        sleep(3)
    def test_check_sort(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.CATEGORY_BUTTON_IOS).click()
        sleep(2)       
        #     self.driver.find_element_by_name("Category Hotel").click()
        self.driver.find_element_by_name("机票").click()
        self.driver.find_element_by_name("Search Sort").click()  
        self.driver.find_element_by_name("价格从低到高").click()
        sleep(3)
    

class QYLM172iOSTests(unittest.TestCase):
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
        #self.driver.find_element_by_name(name)    
    def scroll_screen(self,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        self.driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    def inputString(self,text1,text2):
        user = self.driver.find_element_by_xpath("//UIATextField")
        password = self.driver.find_element_by_xpath("//UIASecureTextField")
        user.click()
        user.send_keys(text1)    
        password.click()
        password.send_keys(text2)    
    def needLogOut(self,element):
        before = self.driver.find_element_by_xpath("//UIAStaticText[1]").get_attribute("value")
        print(before)
        element.click()
        if before is None:
            return False
        else:
            return True
        
    '''
    V1.7.2测试用例
    1、删除订单功能
    2、回复帖子
    '''
    def test_check_delete_order(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        self.driver.find_element_by_name("我的订单").click()
        sleep(2)
        els = self.driver.find_elements_by_name("订单关闭")
        els[1].click()
        sleep(3)
        self.driver.find_element_by_xpath(GD.ORDER_DELETE_IOS).click()
        self.driver.find_element_by_name("确定").click()
        sleep(3)
    def test_reply(self):
        sleep(5)
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 394 })
        sleep(3)
        try:
            self.driver.find_element_by_xpath(GD.REPLY_BUTTON_IOS).click()
            inputEdit = self.driver.find_element_by_xpath(GD.REPLY_TEXTFIELD_IOS)
            inputEdit.send_keys("12345")
            self.driver.find_element_by_name("Confirm Btn").click()
            sleep(5)
        except:
            print("此处并不是帖子")

        
if __name__ == '__main__':
    suite171 = unittest.TestLoader().loadTestsFromTestCase(QYLM171iOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite171)
    suite172 = unittest.TestLoader().loadTestsFromTestCase(QYLM172iOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite172)