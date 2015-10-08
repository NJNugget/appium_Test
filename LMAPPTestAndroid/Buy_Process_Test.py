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
    def test_Buy_Process(self):
        sleep(8)
        #滑动屏幕用以显示更多
        self.util.scroll_screen(self.driver, 500, 500, 700, 70)
        #进入分类页面
        self.util.findElementByText(self.driver,"分类")
        self.util.findElementByText(self.driver,"机票")
#         self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout/android.widget.FrameLayout").click()
        self.driver.find_element_by_xpath(GD.SALE_PRODECT_ANDROID).click()
        model = QYBuy_Android()
        model.Buy_flight(self.driver)