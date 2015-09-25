# -*- coding: UTF-8 -*-
'''
Created on 2015年9月22日

@author: NJNUGGET
'''
from time import sleep
from LMAPPUtil.Utility import AndroidUtility
from LMAPPUtil.Utility import iOSUtility
class SharedClass_Android(object):
    util = AndroidUtility()
    def sharedWeibo(self,driver):
        print("weibo")
        self.util.findElementByText(driver, "微博")
        sleep(3)
        self.util.findElementByText(driver, "发送")
        print("shared success")
        sleep(3)
    def sharedWeChat(self,driver):
        print("weChat")
        self.util.findElementByText(driver, "朋友圈")
        sleep(3)
        self.util.findElementByText(driver, "发送")  
class SharedClass_iOS(object):
    util = iOSUtility()
    def shareWeibo(self,driver):
#         driver.find_element_by_name("Green Share").click()
        driver.find_element_by_name("新浪微博").click()
        sleep(4)
        try:
            driver.find_element_by_name("Green Share").click()
            driver.find_element_by_name("新浪微博").click()
            sleep(3)
        except:
            driver.find_element_by_name("发送").click()
            sleep(3)
    def shareWeixin(self,driver):
        driver.find_element_by_name("微信朋友圈").click()
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 352, "y": 46 })
        sleep(3)