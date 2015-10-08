# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
from time import sleep
import LMAPPUtil.xPath as GD
from LMAPPUtil.Capabilities import QYSettings_iOS

class QYMain(QYSettings_iOS):
# ===================================
# （1）回复功能
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
        