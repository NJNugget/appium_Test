# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
import xPath as GD
from time import sleep
from LMAPPUtil.Capabilities import QYSettings_iOS

class QYSelected(QYSettings_iOS):
# ===================================
# （7）选择穷游精选
# 滑动屏幕激活
# 点击［穷游精选］按钮
# 点击选择精选中的折扣
# ===================================
    def test_check_Qyer_choiceness(self):
        sleep(2)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,150, 150, 170, 70)
#         self.driver.find_element_by_name("Tab Discover").click()
        self.driver.find_element_by_xpath(GD.SELECTED_BUTTON_IOS).click()
        sleep(3)
        self.driver.find_element_by_xpath(GD.SELECTED_PRODUCT_IOS).click()
        sleep(3)