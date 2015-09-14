# -*- coding: UTF-8 -*-

'''
Created on 2015年8月12日

@author: NJNUGGET
'''
import unittest
import os
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from types import NoneType
#from LMAPPTest.AddYHP import findElementByText

class QYLM171AndroidTests(unittest.TestCase):
    '''
    通用功能
    1、启动和终止功能
    2、滚动屏幕
    3、按照文本寻找元素
    4、输入文本
    5、判断activity是否改变
    '''

    def setUp(self):
        # set up appium
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['app'] = os.path.abspath('/Users/NJNUGGET/Documents/Python/WorkSpace/AndroidTestApp/aLAST.apk')
        self.driver = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
        #self.driver.find_element_by_name(name)    
    def scroll_screen(self,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        self.driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    #findElementByText_method   
    def findElementByText(self,text):
        self.driver.find_element_by_xpath("//*[@text='%s']"%text).click()
        sleep(1)
    #inputYHPinfo
    def inputString(self,text1,text2=""):
        elm = self.driver.find_elements_by_xpath("//android.widget.EditText")
        elm[0].send_keys(text1)
        elm[1].send_keys(text2) 
    def activityIsChanged(self,element):
        before = self.driver.current_activity
        element.click()
        after = self.driver.current_activity
        if before == after:
            return False
        else:
            return True
    
    '''
    V1.7.1测试用例
    1、添加优惠券
    2、登录登出
    3、购买流程
    4、查询订单
    5、删除收藏
    6、添加删除提醒
    7、选择穷游精选
    8、搜索功能
    9、筛选功能
    '''
    def test_addYHP(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入分类页面
        self.findElementByText("我的")
        self.findElementByText("我的优惠")
        self.findElementByText("添加优惠券")
        #输入优惠券信息
        self.inputString("YHP0009300002785", "123962")
        self.findElementByText("加入我的优惠券")
    def test_logIn(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入分类页面
        self.findElementByText("我的")
        els = self.driver.find_elements_by_xpath("//*[@clickable='true']")
        before = self.driver.current_activity
#         print(before)
        els[1].click()
        sleep(1)
        after = self.driver.current_activity
#         print(after)
        if(before == after):
            els[2].click()
            self.findElementByText("确定")
            els[1].click()
            #     wd.find_element_by_xpath("//*[@clickable='true']").click()
        self.inputString("1234", "1234")
        self.driver.find_elements_by_xpath("//*[@text='登录']")[1].click()
        sleep(2)
    def test_buyAtOnce(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入分类页面
        self.findElementByText("分类")
        self.findElementByText("酒店")
        self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout/android.widget.FrameLayout").click()
        self.findElementByText("立即预订")
        sleep(1)
        self.scroll_screen(500, 300, 500, 200)
        self.findElementByText("选择日期")
           
        flag = True
        while(flag == True):
            self.scroll_screen(500,1750,500,1)
            for i in range(1,7):
                if(flag==True):
                    for j in range(1,8):
                        el = self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.view.View[%s]"%(i,j))
                        if(self.activityIsChanged(el)):
                            flag = False
                            break
               
        self.findElementByText("提交订单")          
    def test_check_order(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入我的页面
        self.findElementByText("我的")
        self.findElementByText("我的订单")
        #查看待付款和申请退款中
        self.scroll_screen(900, 1000, 100, 1000)
        sleep(1)
        self.scroll_screen(900, 1000, 100, 1000)     
    def test_check_delete_collection(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入我的收藏页面
        self.findElementByText("我的")
        self.findElementByText("我的收藏")
        #长按第一个收藏，并点击删除
        action1 = TouchAction(self.driver)  
#         el = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[1]")
        el = self.driver.find_element_by_id("com.qyer.android.lastminute:id/deal_layout")
        action1.long_press(el).wait(1500).perform()
        self.findElementByText("确定")
    def test_check_notice(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入我的提醒页面
        self.findElementByText("我的")
        self.findElementByText("我的提醒")
        els = self.driver.find_elements_by_xpath("//android.widget.ImageView")
        els[1].click()
        sleep(1)
        self.findElementByText("折扣类型")
        self.findElementByText("机票")
        self.findElementByText("确定")
        sleep(3)
        self.driver.find_element_by_id("com.qyer.android.lastminute:id/iv_notifi_delete").click()
        sleep(2)
        self.findElementByText("确定")
            
    def test_check_Qyer_choiceness(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入我的提醒页面
        self.findElementByText("穷游精选")
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.FrameLayout[1]").click()
        sleep(2)
        self.driver.find_element_by_id("com.qyer.android.lastminute:id/llLeftPanle").click()
        sleep(3)
            
    def test_check_search(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        self.driver.find_element_by_id("com.qyer.android.lastminute:id/ic_left_image").click()
        self.findElementByText("日本")
        sleep(3)
            
    def test_check_sort(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入分类页面
        self.findElementByText("分类")
        self.findElementByText("酒店")
        self.driver.find_element_by_id("com.qyer.android.lastminute:id/ivOrderType").click()
        self.findElementByText("价格从低到高")
        sleep(3)
    
        
class QYLM172AndroidTests(unittest.TestCase):
    '''
    通用功能
    1、启动和终止功能
    2、滚动屏幕
    3、按照文本寻找元素
    4、输入文本
    5、判断activity是否改变
    '''

    def setUp(self):
        # set up appium
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['app'] = os.path.abspath('/Users/NJNUGGET/Documents/Python/WorkSpace/AndroidTestApp/aLAST.apk')
        self.driver = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
        #self.driver.find_element_by_name(name)    
    def scroll_screen(self,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        self.driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    #findElementByText_method   
    def findElementByText(self,text):
        self.driver.find_element_by_xpath("//*[@text='%s']"%text).click()
        sleep(1)
    #inputYHPinfo
    def inputString(self,text1,text2=""):
        elm = self.driver.find_elements_by_xpath("//android.widget.EditText")
        elm[0].send_keys(text1)
        elm[1].send_keys(text2) 
    def activityIsChanged(self,element):
        before = self.driver.current_activity
        element.click()
        after = self.driver.current_activity
        if before == after:
            return False
        else:
            return True

    '''
#   V1.7.2测试用例
    1、删除订单功能
    2、回复帖子
    '''
    def test_check_delete_order(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.scroll_screen(500, 500, 700, 70)
        #进入我的页面
        self.findElementByText("我的")
        self.findElementByText("我的订单")
        sleep(1)
        flag = True
        while(flag == True):
            try:
                self.findElementByText("订单关闭")
                sleep(3)
                self.findElementByText("删除订单")
                sleep(1)
                self.findElementByText("确定")
                sleep(2)
                flag = False
            except:
                self.scroll_screen(500, 1500, 500, 600)
    def test_reply(self):
        sleep(8)  
        self.driver.find_element_by_id("com.qyer.android.lastminute:id/ivSale1").click()
        sleep(2)
        self.findElementByText("回复楼主")
        inputEdit = self.driver.find_elements_by_class_name("android.widget.EditText")
        inputEdit[0].click()
        inputEdit[0].send_keys("This is a test")
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[3]/android.widget.ImageView[1]").click()
        sleep(3)
if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(QYLM171AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(QYLM172AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite2)
