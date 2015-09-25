# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
from time import sleep
import xPath as GD
from LMAPPUtil.SharedClass import SharedClass_Android
from LMAPPUtil.Capabilities import QYSettings_Android

class QYMain(QYSettings_Android):
#===================================
# （1）回复功能
# 点击不规则运营位专题
# 如果运营位为帖子，点击［回复楼主］按钮
# 在回复内容框里输入“This is a test”
# 点击右上角确认回复按钮
# 如果不是帖子，控制台输出“此处不是帖子”
# ===================================
    def test_reply(self):
        print(GD.IRREGULAR_IMAGE_1_ID_ANDROID)
        sleep(8)  
        #不规则运营位的1号位
        print(GD.IRREGULAR_IMAGE_1_ID_ANDROID)
        self.driver.find_element_by_id(GD.IRREGULAR_IMAGE_1_ID_ANDROID).click()
        sleep(2)
        try:
            self.util.findElementByText(self.driver,"回复楼主")
            inputEdit = self.driver.find_elements_by_class_name("android.widget.EditText")
            inputEdit[0].click()
            inputEdit[0].send_keys("This is a test")
            self.driver.find_element_by_xpath(GD.NOTICE_IMAGE_ANDROID).click()
            sleep(3)
        except:
            print("此处不是帖子")

#===================================
# （2）分享功能
# 点击运营位专题
# 在回复内容框里输入“This is a test”
# 点击右上角确认回复按钮
# 如果不是帖子，控制台输出“此处不是帖子”
# ===================================            
    def test_share(self):
        sleep(3)
        self.util.scroll_screen(self.driver, 500, 500, 700, 70)
#         sleep(2)
        self.driver.find_element_by_xpath(GD.OPREATION_IMAGE_ADNROID).click()
        self.driver.find_element_by_xpath(GD.SHARE_TOPIC_BUTTON_ANDROID).click()
        share = SharedClass_Android()
        share.sharedWeibo(self.driver)
        sleep(3)
            