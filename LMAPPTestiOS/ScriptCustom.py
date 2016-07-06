# -*- coding: UTF-8 -*-

'''
Created on 2016年6月27日

@author: NJNUGGET
'''
from LMAPPUtil import xPath as GD
from time import sleep
from LMAPPUtil.Capabilities import QYSettings_iOS
from LMAPPUtil.Utility import iOSUtility
from LMAPPUtil.Buy import QYBuy_iOS

class CustomCases(QYSettings_iOS):
    util = iOSUtility()
#     def test_199_login(self):
#         sleep(3)
#         self.driver.find_element_by_xpath(GD.TOOLBAR_MINE).click()
#         self.driver.find_element_by_xpath(GD.MINE_LOGIN_BUTTON).click()
#         self.util.inputString(self.driver, "ok123ttt", "lixiang1990922")
#         self.driver.find_element_by_name("QYLoginButton").click()
#         sleep(2)
    #按照折扣id搜索产品
    def test_199_Buy_by_pnum(self):
#         sleep(3)
        #进入搜索页面
        i = 22
        self.driver.find_element_by_xpath(GD.SEARCH_BUTTON_IOS).click()
        self.driver.find_element_by_xpath(GD.SEARCH_HISTORY_1_IOS).click()
        #选择列表中的折扣
        self.driver.find_element_by_xpath(GD.PRODUCT_LIST_3_IOS).click()
        sleep(1)
        while i>0 :
            self.Buy_199()
            i -= 1
            print i
    def Buy_199(self):
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        self.driver.find_element_by_xpath(GD.SET_LIST_2_IOS).click()
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(2)
        self.driver.find_element_by_name("Common Back").click()
        self.driver.find_element_by_name("稍后支付").click()
        self.driver.find_element_by_name("Common Back").click()
