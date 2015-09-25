# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
import xPath as GD
from time import sleep
from LMAPPUtil.SharedClass import SharedClass_Android
from LMAPPUtil.Capabilities import QYSettings_Android



class QYSelected(QYSettings_Android):
        
    def test_QYSelected(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver,500, 500, 700, 70)
        #进入我的提醒页面
        self.util.findElementByText(self.driver,"穷游精选")
        sleep(5)
#         self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.FrameLayout[1]").click()
        self.driver.find_element_by_xpath(GD.SELECTED_PRODUCT_ANDROID).click()
        sleep(2)
        self.driver.find_element_by_id(GD.SELECTED_PRODUCT_LEFT_ID_ANDROID).click()
        sleep(3)