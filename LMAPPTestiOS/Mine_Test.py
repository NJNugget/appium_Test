# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
from time import sleep
from LMAPPUtil.Capabilities import QYSettings_iOS
from appium.webdriver.common.touch_action import TouchAction
import LMAPPUtil.xPath as GD

class QYMine(QYSettings_iOS):
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
        self.util.scroll_screen(self.driver,150, 150, 170, 70)
        #进入我的页面
        #self.driver.find_element_by_xpath("//UIAWindow[1]/UIAButton[4]").click()
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        sleep(1)
        el = self.driver.find_element_by_xpath(GD.MINE_USERNAME_IOS)
        if(self.util.needLogOut(self.driver,el)==True):
            self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 351, "y": 41 })
            self.driver.switch_to_alert().accept()
            el.click()
        self.util.inputString(self.driver,"ok123ttt", "lixiang1990922")
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
        self.util.scroll_screen(self.driver,150, 150, 170, 70)
        #进入我的页面
        self.driver.find_element_by_xpath(GD.MINE_YHP_IOS).click()
        self.driver.find_element_by_name("我的优惠").click()
        self.driver.find_element_by_name("添加优惠券").click()
        el = self.driver.find_element_by_xpath(GD.MINE_USERNAME_IOS)
        if(self.util.needLogOut(self.driver, el)==False):
            self.inputString("ok123ttt", "lixiang1990922")
            self.driver.find_element_by_xpath(GD.MINE_QYLOGIN_BUTTON_IOS).click()
            sleep(2)
        self.util.inputString(self.driver,"YHP0003200002459","123456")
        self.driver.find_element_by_name("加入我的优惠券").click()
        sleep(2) 
# ===================================
# （3）查询订单
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的订单］按钮
# 滑动两次检查订单是否加载成功
# ===================================
    def test_check_order(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        self.driver.find_element_by_name("我的订单").click()
        sleep(2)
        self.util.scroll_screen(self.driver,300, 150, 100, 150)
        sleep(1)
        self.util.scroll_screen(self.driver,300, 150, 100, 150)
# ===================================
# （4）删除收藏
# 滑动屏幕激活
# 点击［我的］按钮
# 滑动已收藏折扣
# 点击［取消收藏］按钮
# ===================================
    def test_check_delete_colletion(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,150, 150, 170, 70)
        self.driver.find_element_by_xpath(GD.MINE_BUTTON_IOS).click()
        self.driver.find_element_by_name("我的收藏").click()
        sleep(2)
        self.util.scroll_screen(self.driver,300, 150, 100, 150)
        sleep(3)
        self.driver.find_element_by_name("取消 收藏").click()
        sleep(5)
# ===================================
# （5）添加删除提醒
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
        self.util.scroll_screen(self.driver,150, 150, 170, 70)
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
        self.util.scroll_screen(self.driver,300, 150, 100, 150)
        self.driver.find_element_by_xpath(GD.NOTICE_DELETE_IOS).click()
        self.driver.find_element_by_name("确定").click()
        sleep(3)