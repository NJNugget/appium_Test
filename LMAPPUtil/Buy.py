# -*- coding: UTF-8 -*-

'''
Created on 2015年9月25日

@author: NJNUGGET
'''
from time import sleep
from LMAPPUtil.Utility import AndroidUtility
from LMAPPUtil.Utility import iOSUtility
from LMAPPUtil import xPath as GD
class QYBuy_Android(object):
    util = AndroidUtility()
    def Buy(self,driver):
#         driver.find_element_by_xpath(GD.SALE_PRODECT_ANDROID).click()
        self.util.findElementByText(driver,"立即预订")
        sleep(1)
        self.util.scroll_screen(driver,500, 300, 500, 200)
        try:
            self.util.findElementByText(driver,"选择日期")
            sleep(3)    
            flag = True
            while(flag == True):
                self.util.scroll_screen(driver,500,1750,500,1)
                for i in range(1,7):
                    if(flag==True):
                        for j in range(1,8):
                            el = driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.view.View[%s]"%(i,j))
                            el.click()
                            if(self.activityIsChanged(el)):
                                flag = False
                                break
        except:
            self.util.findElementByText(driver,"提交订单")
            sleep(2)
            return
        try:
            self.util.findElementByText(driver, "点击添加新旅客")
            sleep(1)
            driver.find_element_by_xpath("//android.widget.CheckBox[1]").click()
            driver.find_element_by_xpath(GD.ADD_PASSANGER_SUCCESS_ANDROID).click()
            sleep(2)
            self.util.findElementByText(driver,"提交订单")
            sleep(2)
        except:
            self.util.findElementByText(driver,"提交订单")
            sleep(2)
            return
    def Buy_flight(self,driver):
        self.util.findElementByText(driver,"立即预订")
        sleep(1)
        self.util.scroll_screen(driver,500, 300, 500, 200)
        self.util.findElementByText(driver,"选择日期")
        sleep(3)    
        flag = True
        while(flag == True):
            self.util.scroll_screen(driver,500,1750,500,1)
            for i in range(1,7):
                if(flag==True):
                    for j in range(1,8):
                        el = driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.view.View[%s]"%(i,j))
#                         el.click()
                        if(self.util.activityIsChanged(driver,el)):
                            flag = False
                            break
        self.util.scroll_screen(driver, 500, 1400, 500, 700)
        self.util.findElementByText(driver, "点击添加新旅客")
        sleep(1)
        driver.find_element_by_xpath("//android.widget.CheckBox[1]").click()
        driver.find_element_by_xpath(GD.ADD_PASSANGER_SUCCESS_ANDROID).click()
        sleep(2)
        self.util.findElementByText(driver,"提交订单")
        sleep(2)
            
class QYBuy_iOS(object):
    util = iOSUtility()
    def Buy(self,driver):
#         driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS).click()
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 311, "y": 639 })
        sleep(1)
        try:
            driver.find_element_by_name("选择日期").click()
            sleep(1)
            dates = driver.find_elements_by_xpath(GD.CALENDAR_BUTTON_IOS)
               
            print(len(dates))
            for i in range(len(dates)):
    #             此处注意enabled这个属性不能用get_attributes查看，有专用的is_enabled
                if(dates[i].is_enabled()):
                    dates[i].click()
                    break        
                #         scroll_screen(200, 500, 200, 300)
        except:
            driver.find_element_by_name("提交订单").click()
            sleep(2)
        try:
            driver.find_element_by_name("点击添加旅客").click()
            sleep(1)
            driver.find_element_by_xpath(GD.PASSANGER_CHECKBOX_IOS).click()
            sleep(1)
            self.util.scroll_screen(driver,100, 150, 100, 70)
            driver.find_element_by_name("Confirm Btn").click()
            sleep(1)
            driver.find_element_by_name("提交订单").click()
            sleep(2)
        except:
            driver.find_element_by_name("提交订单").click()
            sleep(2) 
    def Buy_flight(self,driver):
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 311, "y": 639 })
        sleep(1)
        driver.find_element_by_name("选择日期").click()
        sleep(1)
        dates = driver.find_elements_by_xpath(GD.CALENDAR_BUTTON_IOS)
           
        print(len(dates))
        for i in range(len(dates)):
#             此处注意enabled这个属性不能用get_attributes查看，有专用的is_enabled
            if(dates[i].is_enabled()):
                dates[i].click()
                break        
            #         scroll_screen(200, 500, 200, 300)
        driver.find_element_by_name("点击添加旅客").click()
        sleep(1)
        driver.find_element_by_xpath(GD.PASSANGER_CHECKBOX_IOS).click()
        sleep(1)
        self.util.scroll_screen(driver,100, 150, 100, 70)
        driver.find_element_by_name("Confirm Btn").click()
        sleep(1)
        driver.find_element_by_name("提交订单").click()
        sleep(2)
