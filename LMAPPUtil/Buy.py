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
    def Buy_wifi(self,driver):
        print("wifi")
    def Buy_ticket(self,driver):
        print("ticket")
    def Buy_daytrip(self,driver):
        print("day trip")
    def Buy_pickup(self,driver):
        print("pickup&receive")
    def Buy_chartered(self,driver):
        print("Chartered")
    def Buy_hotel(self,driver):
        print("hotel")
    def Buy_visa(self,driver):
        print("visa")
            
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
    def Buy_wifi(self,driver):
        print("wifi")
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.name)
        els[1].click()
        els[1].send_keys(p.passanger.mobile)
        self.util.scroll_screen(driver, 100, 100, 100, 20)
        els[2].click()
        els[2].send_keys(p.passanger.email)
        els[3].click()
        els[3].send_keys(p.passanger.weChat)
        self.util.scroll_screen(driver, 100, 100, 100, 20)
        driver.find_element_by_name("填写快递信息").click()
        txts = driver.find_elements_by_xpath("//UIATextField")
        txts[0].click()
        txts[0].send_keys(p.passanger.name)
        txts[1].click()
        txts[1].send_keys(p.passanger.mobile)
        txts[2].click()
        txts[2].send_keys(p.passanger.zipcode)
        txts[3].click()
        txts[3].send_keys(p.passanger.address)
        print("success")
    def Buy_ticket(self,driver):
        print("ticket")
    def Buy_daytrip(self,driver):
        print("day trip")
    def Buy_pickup(self,driver):
        print("pickup&receive")
    def Buy_chartered(self,driver):
        print("Chartered")
    def Buy_hotel(self,driver):
        print("hotel")
    def Buy_visa(self,driver):
        print("visa")
