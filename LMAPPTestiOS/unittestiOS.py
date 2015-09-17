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
# ===================================
#     通用功能
#     1、启动和终止功能
#     2、滚动屏幕
#     3、输入文本
#     4、判断是否需要登出
# ===================================

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
    
# ===================================
#     V1.7.1测试用例
#     1、登录登出
#     2、添加优惠券
#     3、购买流程
#     4、查询订单
#     5、删除收藏
#     6、添加删除提醒
#     7、选择穷游精选
#     8、搜索功能
#     9、筛选功能
# ===================================
# ===================================
# ===================================
# ===================================
# （1）登录登出
# 滑动屏幕激活
# 进入［我的］页面
# 点击头像，验证是否需要先登出，若需要则执行登出操作
# 输入用户名“ok123ttt”密码“lixiang1990922”
# 点击登录按钮
# ===================================
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
# ===================================
# （2）添加优惠券
# 滑动屏幕激活
# 进入［我的］页面
# 点击［我的优惠］按钮
# 点击［添加优惠券］按钮
# 输入优惠券号“YHP0003200002459”，优惠券密码“123456”
# 点击［加入我的优惠券］按钮
# ===================================
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
# ===================================
# （3）购买流程
# 滑动屏幕激活
# 点击［分类］按钮
# 点击［机票］类目按钮
# 点击列表中第一个折扣
# 点击［立即预订］按钮
# 点击［选择日期］按钮
# 选择一个有产品的日期
# 判断是否需要添加旅客，如若不需要，直接点击［提交订单］按钮
# ===================================
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
            self.driver.find_element_by_name("点击添加旅客").click()
            sleep(1)
            self.driver.find_element_by_xpath(GD.PASSANGER_CHECKBOX_IOS).click()
            sleep(1)
            self.scroll_screen(100, 150, 100, 70)
            self.driver.find_element_by_name("Confirm Btn").click()
            sleep(1)
            self.driver.find_element_by_name("提交订单").click()
            sleep(2)
        except:
            self.driver.find_element_by_name("提交订单").click()
            sleep(2)           
# ===================================
# （4）查询订单
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的订单］按钮
# 滑动两次检查订单是否加载成功
# ===================================
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
# ===================================
# （5）删除收藏
# 滑动屏幕激活
# 点击［我的］按钮
# 滑动已收藏折扣
# 点击［取消收藏］按钮
# ===================================
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
# ===================================
# （6）添加删除提醒
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的提醒］按钮
# 点击右上角添加提醒按钮
# 点击［旅行时间］按钮
# 选择［1-3个月］
# 滑动新添加的提醒
# 点击［删除］按钮
# 点击［确定］按钮
# ===================================
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
        
# ===================================
# （7）选择穷游精选
# 滑动屏幕激活
# 点击［穷游精选］按钮
# 点击选择精选中的折扣
# ===================================
    def test_check_Qyer_choiceness(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
#         self.driver.find_element_by_name("Tab Discover").click()
        self.driver.find_element_by_xpath(GD.SELECTED_BUTTON_IOS).click()
        sleep(3)
        self.driver.find_element_by_xpath(GD.SELECTED_PRODUCT_IOS).click()
        sleep(3)
              
# ===================================
# （8）搜索功能
# 滑动屏幕激活
# 点击搜索按钮
# 输入“japan”
# 点击确认
# ===================================
    def test_check_search(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.scroll_screen(150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.SEARCH_BUTTON_IOS).click()
        content = self.driver.find_element_by_xpath("//UIATextField")
        content.send_keys("japan")
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 343, "y": 646 })
        sleep(3)

# ===================================
# （9）排序功能
# 滑动屏幕激活
# 点击［分类］按钮
# 点击［机票］类目按钮
# 点击右上方筛选按钮
# 选择“价格从低到高”
# ===================================
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
        
# ===================================
#     V1.7.2测试用例
#     1、删除订单功能
#     2、回复帖子
# ===================================
# ===================================
# ===================================
# ===================================
# （1）删除订单功能
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的订单］按钮
# 点击状态为［订单关闭］的订单
# 点击［删除订单］按钮
# 点击［确定］按钮
# ===================================
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
# ===================================
# （2）回复功能
# 点击不规则运营位专题
# 如果运营位为帖子，点击［回复楼主］按钮
# 在回复内容框里输入“12345”
# 点击右上角确认回复按钮
# 如果不是帖子，控制台输出“此处不是帖子”
# ===================================
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