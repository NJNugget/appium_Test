# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
import LMAPPUtil.xPath as GD
from time import sleep
from LMAPPUtil.Buy import QYBuy_Android
from LMAPPUtil.Capabilities import QYSettings_Android

class QYBuy_Process(QYSettings_Android):
    model = QYBuy_Android()
#     def test_Buy_FreeTour(self):
#         sleep(8)
#         self.util.findElementByText(self.driver,"自由行")
# #         self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout/android.widget.FrameLayout").click()
#         self.driver.find_element_by_xpath(GD.SALE_PRODECT_ANDROID_1).click()
#         self.model.Buy_freetour(self.driver)
#         self.util.findElementByText(self.driver, "滑动查看订单详情")
#         self.util.scroll_screen(self.driver, 500, 1000, 500, 500)
#         self.util.findElementByText(self.driver, "去支付")
#         sleep(5)
    def test_Buy_Wifi(self):
        sleep(8)
        self.util.findElementByText(self.driver, "城市玩乐")
        self.driver.find_element_by_xpath(GD.SALE_PRODECT_ANDROID_4).click()
        self.model.Buy_wifi(self.driver)