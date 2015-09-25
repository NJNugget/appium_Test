# -*- coding: UTF-8 -*-
'''
Created on 2015年9月22日

@author: NJNUGGET
'''
from time import sleep
from LMAPPUtil.Utility import AndroidUtility
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