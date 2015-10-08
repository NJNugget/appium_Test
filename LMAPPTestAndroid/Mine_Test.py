# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
from time import sleep
from LMAPPUtil.SharedClass import SharedClass_Android
from LMAPPUtil.Capabilities import QYSettings_Android
from appium.webdriver.common.touch_action import TouchAction
import LMAPPUtil.xPath as GD
class QYMine(QYSettings_Android):
    
# ===================================
# （1）查询订单
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的订单］按钮
# 滑动两次检查订单是否加载成功
# ===================================          
    def test_check_order(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,500, 500, 700, 70)
        #进入我的页面
        self.util.findElementByText(self.driver,"我的")
        self.util.findElementByText(self.driver,"我的订单")
        if(self.driver.current_activity == ".activity.user.NewLoginActivity"):
            self.util.logIn(self.driver)
        #查看待付款和申请退款中
        self.util.scroll_screen(self.driver,900, 1000, 100, 1000)
        sleep(1)
        self.util.scroll_screen(self.driver,900, 1000, 100, 1000)
# ===================================
# （2）删除收藏
# 滑动屏幕激活
# 点击［我的］按钮
# 滑动已收藏折扣
# 点击［取消收藏］按钮
# ==================================   
    def test_check_delete_collection(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,500, 500, 700, 70)
        #进入我的收藏页面
        self.util.findElementByText(self.driver,"我的")
        self.util.findElementByText(self.driver,"我的收藏")
        if(self.driver.current_activity == ".activity.user.NewLoginActivity"):
            self.util.logIn(self.driver)
        try:
            #长按第一个收藏，并点击删除
            action1 = TouchAction(self.driver)  
    #         el = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[1]")
            el = self.driver.find_element_by_id(GD.COLLECT_PRODUCT_ID_ANDROID)
            action1.long_press(el).wait(1500).perform()
            self.util.findElementByText(self.driver,"确定")
        except:
            print("没有收藏，删除失败")
# ===================================
# （3）添加删除提醒
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的提醒］按钮
# 点击右上角添加提醒按钮
# 点击［折扣类型］按钮
# 选择［机票］类型
# 点击提醒右上方删除按钮
# 点击［确定］按钮
# ===================================
    def test_check_notice(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,500, 500, 700, 70)
        #进入我的提醒页面
        self.util.findElementByText(self.driver,"我的")
        self.util.findElementByText(self.driver,"我的提醒")
        if(self.driver.current_activity == ".activity.user.NewLoginActivity"):
            self.util.logIn(self.driver)
        els = self.driver.find_elements_by_xpath(GD.NOTICE_IMAGE_ANDROID)
        els[1].click()
        sleep(1)
        self.util.findElementByText(self.driver,"折扣类型")
        self.util.findElementByText(self.driver,"机票")
        self.util.findElementByText(self.driver,"确定")
        sleep(3)
        self.driver.find_element_by_id(GD.NOTICE_DELETE_ID_ANDROID).click()
        sleep(2)
        self.util.findElementByText(self.driver,"确定")
# ===================================
# （4）删除订单功能
# 滑动屏幕激活
# 点击［我的］按钮
# 点击［我的订单］按钮
# 点击状态为［订单关闭］的订单
# 点击［删除订单］按钮
# 点击［确定］按钮
# ===================================
    def test_check_delete_order(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,500, 500, 700, 70)
        #进入我的页面
        self.util.findElementByText(self.driver,"我的")
        self.util.findElementByText(self.driver,"我的订单")
        if(self.driver.current_activity == ".activity.user.NewLoginActivity"):
            self.util.logIn(self.driver)
        sleep(1)
        flag = True
        while(flag == True):
            try:
                self.util.findElementByText(self.driver,"订单关闭")
                sleep(3)
                self.util.findElementByText(self.driver,"删除订单")
                sleep(1)
                self.util.findElementByText(self.driver,"确定")
                sleep(2)
                flag = False
            except:
                self.util.scroll_screen(self.driver,500, 1500, 500, 600)
                 
# ===================================
# （5）添加优惠券
# 滑动屏幕激活
# 进入［我的］页面
# 点击［我的优惠］按钮
# 点击［添加优惠券］按钮
# 输入优惠券号“YHP0009300002785”，优惠券密码“123962”
# 点击［加入我的优惠券］按钮
# ===================================
    def test_addYHP(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver, 500, 500, 700, 70)
        #进入分类页面
        self.util.findElementByText(self.driver,"我的")
        self.util.findElementByText(self.driver,"我的优惠")
        print(self.driver.current_activity)
        if(self.driver.current_activity == ".activity.user.NewLoginActivity"):
            self.util.logIn(self.driver)
        self.util.findElementByText(self.driver,"添加优惠券")
        #输入优惠券信息
        self.util.inputString(self.driver,"YHP0009300002785", "123962")
        self.util.findElementByText(self.driver,"加入我的优惠券")