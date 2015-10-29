# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
import LMAPPUtil.xPath as GD
from time import sleep
from LMAPPUtil.Buy import QYBuy_Android
from LMAPPUtil.Capabilities import QYSettings_Android

# ===================================
# 购买流程测试用例
# 1、自由行产品购买
# 2、Wifi产品购买
# 3、门票产品购买
# 4、一日游产品购买
# 5、接机产品购买
# 6、送机产品购买
# 7、酒店产品购买
# 8、签证产品购买
# ===================================
class QYBuy_Process(QYSettings_Android):
    model = QYBuy_Android()
    def test_Buy_FreeTour(self):
        sleep(8)
        self.util.findElementByText(self.driver,"自由行")
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_1).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_freetour(self.driver)
        self.util.findElementByText(self.driver, "滑动查看订单详情")
        self.util.scroll_screen(self.driver, 500, 1000, 500, 500)
        self.util.findElementByText(self.driver, "去支付")
        sleep(5)
    def test_Buy_Wifi(self):
        sleep(8)
        self.util.findElementByText(self.driver, "城市玩乐")
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_4).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_wifi(self.driver)
    def test_Buy_Ticket(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_6).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_ticket(self.driver)
    def test_Buy_Daytrip(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_6).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_daytrip(self.driver)
    def test_Buy_Pickup(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_5).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_pickup(self.driver)
    def test_Buy_Receive(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_5).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_receive(self.driver)
    def test_Buy_Chartered(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_5).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_chartered(self.driver)
    def test_Buy_Hotel(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_2).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_hotel(self.driver)
    def test_Buy_Visa(self):
        sleep(8)
        self.util.findElementByText(self.driver,"城市玩乐")
        sleep(2)
        self.util.scroll_screen(self.driver, 500, 1600, 500, 1000)
        self.driver.find_element_by_xpath(GD.SALE_PRODUCT_ANDROID_3).click()
        self.util.findElementByText(self.driver,"立即预订")
        self.model.Buy_visa(self.driver)