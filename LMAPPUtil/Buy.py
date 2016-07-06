# -*- coding: UTF-8 -*-

'''
Created on 2015年9月25日

@author: NJNUGGET
'''

# ===================================
# Android购买流程测试方法
# 1、自由行
# 2、Wifi
# 3、门票
# 4、一日游
# 5、接机
# 6、送机
# 7、酒店
# 8、签证
# ===================================
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
    def Buy_freetour(self,driver):
#         self.util.findElementByText(driver,"立即预订")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_4).click()
        sleep(2)
        self.util.scroll_screen(driver,500, 1600, 500, 800)
        self.util.calendar_Select(driver)
        driver.find_element_by_id(GD.CHOOSE_PASSANGER_ANDROID).click()
        sleep(3)
        driver.find_element_by_class_name("android.widget.CheckBox").click()
        driver.find_element_by_xpath(GD.ADD_PASSANGER_SUCCESS_ANDROID).click()
        self.util.scroll_screen(driver,500, 1600, 500, 800)
        self.util.findElementByText(driver, "提交订单")
        sleep(5)
        
    def Buy_wifi(self,driver):
        print("wifi")
#         self.util.findElementByText(driver,"立即预订")
        sleep(1)
        self.util.scroll_screen(driver,500, 1600, 500, 800)
        self.util.findElementByText(driver, "取设备日期")
        self.util.findElementByText(driver, "完成")
        self.util.findElementByText(driver, "还设备日期")
#         driver.find_element_by_xpath(GD.DATE_PICKER_ANDROID_DAY_AFTER).click()
        self.util.findElementByText(driver, "完成")
#         driver.find_element_by_xpath(GD.WIFI_RETURN_TIME_ANDROID).click()
#         driver.find_element_by_xpath(GD.WIFI_TIME_LIST_ANDROID_2)
#         self.util.findElementByText(driver, "下一步，填写订单")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_1).click()
        sleep(3)
        self.util.scroll_screen(driver, 500, 1600, 500, 200)
        els = driver.find_elements_by_xpath("//*[@text='选择地点']")
        els[0].click()
#         driver.find_element_by_xpath(GD.WIFI_GET_PLACE_ANDROID).click()
        driver.find_element_by_xpath(GD.TIME_LIST_ANDROID_1).click()
        els[1].click()
#         driver.find_element_by_xpath(GD.WIFI_RETURN_PLACE_ANDROID).click()
        driver.find_element_by_xpath(GD.TIME_LIST_ANDROID_1).click()
#         self.util.findElementByText(driver, "填写使用人")
        driver.find_element_by_xpath(GD.APPLICANT_PEOPLE_ANDROID).click()
        self.util.inputString(driver, "JIANG", "ZIHAO")
        self.util.findElementByText(driver, "保存")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
    def Buy_ticket(self,driver):
        print("ticket")
#         self.util.findElementByText(driver,"立即预订")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_3).click()
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_1).click()
        sleep(2)
        self.util.scroll_screen(driver,500, 1600, 500, 1000)
        self.util.findElementByText(driver, "选择日期")
        self.util.findElementByText(driver, "确定")
        self.util.findElementByText(driver, "选择班次/场次")
        driver.find_element_by_xpath(GD.TIME_LIST_ANDROID_1).click()
        driver.find_element_by_xpath(GD.APPLICANT_PEOPLE_ANDROID).click()
        self.util.inputString(driver, "JIANG", "ZIHAO")
        self.util.findElementByText(driver, "保存")
        self.util.findElementByText(driver, "填写快递信息")
        els = driver.find_elements_by_xpath(GD.EIDTTEXT_ANDROID)
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.name)
        els[1].click()
        els[1].send_keys(p.passanger.mobile)
        els[2].click()
        els[2].send_keys(p.passanger.zipcode)
        els[3].click()
        els[3].send_keys(p.passanger.address)
        self.util.findElementByText(driver, "保存")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
    def Buy_daytrip(self,driver):
        print("day trip")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_6).click()
        sleep(1)
        self.util.calendar_Select(driver)
        sleep(2)
        self.util.scroll_screen(driver, 500, 1600, 500, 1000)
        self.util.findElementByText(driver, "选择班次/场次")
        driver.find_element_by_xpath(GD.TIME_LIST_ANDROID_1).click()
        driver.find_element_by_xpath(GD.APPLICANT_PEOPLE_ANDROID).click()
        self.util.inputString(driver, "JIANG", "ZIHAO")
        self.util.findElementByText(driver, "保存")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
    def Buy_pickup(self,driver):
        print("pickup")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_3).click()
        sleep(1)
        self.util.calendar_Select(driver)
        sleep(2)
        self.util.scroll_screen(driver, 500, 1600, 500, 1000)
        self.util.findElementByText(driver, "填写接机信息")
        import LMAPPUtil.Passanger as p
        self.util.inputString(driver,p.passanger.flightnumber)
        self.util.findElementByText(driver, "预计到达时间")
        sleep(1)
        self.util.findElementByText(driver, "确定")
        self.util.findElementByText(driver, "保存")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
    def Buy_receive(self,driver):
        print("receive")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_4).click()
        sleep(1)
        self.util.calendar_Select(driver)
        sleep(2)
        self.util.scroll_screen(driver, 500, 1600, 500, 1000)
        self.util.findElementByText(driver, "填写送机信息")
        import LMAPPUtil.Passanger as p
        self.util.inputString(driver,p.passanger.flightnumber)
        self.util.findElementByText(driver, "预计到达时间")
        sleep(1)
        self.util.findElementByText(driver, "确定")
        self.util.findElementByText(driver, "保存")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
    def Buy_chartered(self,driver):
        print("Chartered")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_5).click()
        sleep(1)
        self.util.calendar_Select(driver)
        sleep(2)
        self.util.scroll_screen(driver, 500, 1600, 500, 1000)
        self.util.findElementByText(driver, "选择班次/场次")
        driver.find_element_by_xpath(GD.TIME_LIST_ANDROID_1).click()
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
    def Buy_hotel(self,driver):
        print("hotel")
        sleep(1)
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_ANDROID_3).click()
        sleep(2)
        self.util.scroll_screen(driver, 500, 1600, 500, 1000)
        import LMAPPUtil.Passanger as p
        self.util.inputString(driver,p.passanger.surname,p.passanger.name)
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2)
        sleep(5) 
    def Buy_visa(self,driver):
        print("visa")
        sleep(1)
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_1).click() 
        sleep(2) 
        self.util.scroll_screen(driver, 500, 1600, 500, 1000)
        self.util.findElementByText(driver, "选择日期")
        self.util.findElementByText(driver, "确定")
        self.util.findElementByText(driver, "填写快递信息")
        els = driver.find_elements_by_xpath(GD.EIDTTEXT_ANDROID)
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.name)
        els[1].click()
        els[1].send_keys(p.passanger.mobile)
        els[2].click()
        els[2].send_keys(p.passanger.zipcode)
        els[3].click()
        els[3].send_keys(p.passanger.address)
        self.util.findElementByText(driver, "保存")
        driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_2).click()
        sleep(5)
         
# ===================================
# iOS购买流程测试方法
# 1、自由行
# 2、Wifi
# 3、门票
# 4、一日游
# 5、接机
# 6、送机
# 7、酒店
# 8、签证
# ===================================
            
class QYBuy_iOS(object):
    util = iOSUtility()
    def Buy(self,driver):
#         driver.find_element_by_xpath(GD.SALE_PRODUCT_IOS).click()
#         driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 311, "y": 639 })
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(1)
        try:
            driver.find_element_by_name("选择日期").click()
            sleep(1)
            dates = driver.find_elements_by_xpath(GD.CALENDAR_BUTTON_FREETOUR_IOS)
               
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
    def Buy_freetour(self,driver):
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_4).click()
        sleep(3)
        dates = driver.find_elements_by_xpath(GD.CALENDAR_BUTTON_FREETOUR_IOS)
        print(len(dates))
        dates[1].click()
#         for i in range(len(dates)):
# #             此处注意enabled这个属性不能用get_attributes查看，有专用的is_enabled
#             if(dates[i].is_enabled()):
#                 dates[i].click()
#                 break        
            #         scroll_screen(200, 500, 200, 300)
        driver.find_element_by_name("Fill New Order Normal").click()
        sleep(1)
#         driver.find_element_by_name("旅客1 *").click()
        self.util.findElementByContent(driver, "旅客1")
        els = driver.find_elements_by_name("check Icon Normol")
        if len(els)>0:
            els[0].click()
        else:
            print("need to add passanger")
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_wifi(self,driver):
        print("wifi")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_1).click()
        driver.find_element_by_name("取设备日期").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_WIFI_script_IOS)
        driver.find_element_by_name("还设备日期").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_WIFI_script_IOS)
        driver.find_element_by_name("取设备时间").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_WIFI_script_IOS)
        driver.find_element_by_name("还设备时间").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_WIFI_script_IOS)
        driver.find_element_by_name("Fill New Order Normal").click()
        sleep(2)
        self.util.scroll_screen(driver, 200, 300, 200, 100)
        els = driver.find_elements_by_name("选择地点")
        els[0].click()
        self.util.preciseTap(driver, GD.SUBMIT_PLACE_script_IOS)
        els[1].click()
        self.util.preciseTap(driver, GD.SUBMIT_PLACE_script_IOS)
        driver.find_element_by_name("填写使用人").click()
        
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.surname)
        els[1].click()
        els[1].send_keys(p.passanger.name)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("提交订单").click()
        sleep(5)
#         self.util.scroll_screen(driver, 100, 100, 100, 20)
#         els[2].click()
#         els[2].send_keys(p.passanger.email)
#         els[3].click()
#         els[3].send_keys(p.passanger.weChat)
#         self.util.scroll_screen(driver, 100, 100, 100, 20)
#         driver.find_element_by_name("填写快递信息").click()
#         txts = driver.find_elements_by_xpath("//UIATextField")
#         txts[0].click()
#         txts[0].send_keys(p.passanger.name)
#         txts[1].click()
#         txts[1].send_keys(p.passanger.mobile)
#         txts[2].click()
#         txts[2].send_keys(p.passanger.zipcode)
#         txts[3].click()
#         txts[3].send_keys(p.passanger.address)
        print("success")
    def Buy_ticket(self,driver):
        print("ticket")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_3).click()
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        self.util.scroll_screen(driver, 200, 300, 200, 100)
        driver.find_element_by_name("选择日期").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_TICKET_script_IOS)
        driver.find_element_by_name("选择班次/场次").click()
        self.util.preciseTap(driver, GD.SUBMIT_PLACE_script_IOS)
        driver.find_element_by_name("填写使用人 *").click()
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.surname)
        els[1].click()
        els[1].send_keys(p.passanger.name)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("填写快递信息 *").click()
        eli = driver.find_elements_by_xpath("//UIATextField")
        eli[0].click()
        eli[0].send_keys(p.passanger.name)
        eli[1].click()
        eli[1].send_keys(p.passanger.mobile)
        eli[2].click()
        eli[2].send_keys(p.passanger.zipcode)
        address = driver.find_element_by_xpath("//UIATextView")
        address.click()
        address.send_keys(p.passanger.address)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_daytrip(self,driver):
        print("day trip")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_6).click()
        sleep(5)
        self.util.calendar_Select(driver)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        driver.find_element_by_name("选择班次/场次").click()
        self.util.preciseTap(driver, GD.SUBMIT_PLACE_script_IOS)
        driver.find_element_by_name("填写使用人 *").click()
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.surname)
        els[1].click()
        els[1].send_keys(p.passanger.name)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_pickup(self,driver):
        print("pickup")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_3).click()
        sleep(3)
        self.util.calendar_Select(driver)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        self.util.scroll_screen(driver, 200, 300, 200, 100)
        driver.find_element_by_name("填写接机信息 *").click()
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.flightnumber)
        driver.find_element_by_name("预计到达时间 *").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_TICKET_script_IOS)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_receive(self,driver):
        print("receive")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_4).click()
        sleep(3)
        self.util.calendar_Select(driver)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        driver.find_element_by_name("填写送机信息 *").click()
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.flightnumber)
        driver.find_element_by_name("航班起飞时间 *").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_TICKET_script_IOS)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_chartered(self,driver):
        print("Chartered")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_5).click()
        sleep(3)
        self.util.calendar_Select(driver)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        driver.find_element_by_name("选择班次/场次").click()
        self.util.preciseTap(driver, GD.SUBMIT_PLACE_script_IOS)
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_hotel(self,driver):
        print("hotel")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_3).click()
        sleep(3)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[-2].click()
        els[-2].send_keys(p.passanger.surname)
        els[-1].click()
        els[-1].send_keys(p.passanger.name)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(1)
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(5)
    def Buy_visa(self,driver):
        print("visa")
        driver.find_element_by_xpath(GD.PRODUCT_TYPE_IOS_1).click()
        self.util.preciseTap(driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(3)
        self.util.scroll_screen(driver, 200, 300, 200, 100)
        driver.find_element_by_name("选择日期").click()
        self.util.preciseTap(driver, GD.SUBMIT_DATE_TICKET_script_IOS)
        driver.find_element_by_name("申请人1").click()
        els = driver.find_elements_by_xpath("//UIATextField")
        import LMAPPUtil.Passanger as p
        els[0].click()
        els[0].send_keys(p.passanger.surname)
        els[1].click()
        els[1].send_keys(p.passanger.name)
        els[2].click()
        els[2].send_keys(p.passanger.address)
        els[3].click()
        els[3].send_keys(p.passanger.city)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("填写快递信息 *").click()
        eli = driver.find_elements_by_xpath("//UIATextField")
        eli[0].click()
        eli[0].send_keys(p.passanger.name)
        eli[1].click()
        eli[1].send_keys(p.passanger.mobile)
        eli[2].click()
        eli[2].send_keys(p.passanger.zipcode)
        address = driver.find_element_by_xpath("//UIATextView")
        address.click()
        address.send_keys(p.passanger.address)
        driver.find_element_by_name("保存").click()
        driver.find_element_by_name("提交订单").click()
        sleep(5)
    def Buy_199(self,driver):
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(2)
        driver.find_element_by_xpath(GD.SET_LIST_2_IOS).click()
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        self.util.preciseTap(self.driver, GD.SUBMIT_ORDER_script_IOS)
        sleep(2)
        driver.find_element_by_name("Common Back").click()
        driver.find_element_by_name("稍后支付").click()
        sleep(2)
        driver.find_element_by_name("Common Back").click()
        sleep(2)
