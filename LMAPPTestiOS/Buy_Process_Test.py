# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
from LMAPPUtil import xPath as GD
from time import sleep
from LMAPPUtil.Capabilities import QYSettings_iOS
from LMAPPUtil.Buy import QYBuy_iOS

class QYBuy_Process(QYSettings_iOS):
    model = QYBuy_iOS()
# ===================================
# （1）购买流程
# 滑动屏幕激活
# 点击［分类］按钮
# 点击［机票］类目按钮
# 点击列表中第一个折扣
# 点击［立即预订］按钮
# 点击［选择日期］按钮
# 选择一个有产品的日期
# 判断是否需要添加旅客，如若不需要，直接点击［提交订单］按钮
# ===================================
#     def test_buyAtOnce(self):
#         sleep(2)
#         self.util.scroll_screen(self.driver, 150, 150, 170, 70)
#         #进入分类页面
#         self.driver.find_element_by_xpath(GD.CATEGORY_BUTTON_IOS).click()
#         sleep(2)       
#         #self.driver.find_element_by_name("酒店").click()
#         self.driver.find_element_by_xpath(GD.CATEGORY_FLIGHT_IOS).click()
#         sleep(1)
#         self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS).click()
#         model = QYBuy_iOS()
#         model.Buy_flight(self.driver)
        
    def test_freetour(self):
        print("freetour/flight/ship")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_FREETOUR).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_1).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS) 
        self.model.Buy_freetour(self.driver)
    def test_buyWifi(self):
        print("wifi")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_4).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS) 
        self.model.Buy_wifi(self.driver)
    def test_buyTicket(self):
        print("ticket")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_6).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        self.model.Buy_ticket(self.driver)
    def test_buyDaytrip(self):
        print("daytrip")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_6).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS) 
        self.model.Buy_daytrip(self.driver)  
    def test_buyPickup(self):
        print("pickup")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_5).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS) 
        self.model.Buy_pickup(self.driver)
    def test_buyReceive(self):
        print("receive")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_5).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS) 
        self.model.Buy_receive(self.driver)
    def test_buyChartered(self):
        print("chartered")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_5).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS) 
        self.model.Buy_chartered(self.driver)
    def test_buyHotel(self):
        print("hotel")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_2).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        self.model.Buy_hotel(self.driver)
    def test_buyVisa(self):
        print("visa")
        sleep(3)
        self.driver.find_element_by_xpath(GD.MAIN_CATEGORY_IOS_CITYFUN).click()
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS_3).click()
        sleep(13)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        self.model.Buy_visa(self.driver) 


        