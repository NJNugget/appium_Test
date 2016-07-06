# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
from time import sleep
import xPath as GD

# ===================================
#     Android通用功能
#     1、滚动屏幕
#     2、按照文本寻找元素
#     3、在WebView中按文本寻找元素
#     4、输入文本
#     5、判断activity是否改变
#     6、登录
# ===================================
class AndroidUtility():
    def scroll_screen(self,driver,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    #findElementByText_method   
    def findElementByText(self,driver,text):
        driver.find_element_by_xpath("//*[@text='%s']"%text).click()
        sleep(1)
    #WebViewfindElement
    def webViewFindElement(self,driver,text):
        driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'%s')]"%text).click()
    #inputYHPinfo
    def inputString(self,driver,text1,text2=""):
        elm = driver.find_elements_by_xpath(GD.EIDTTEXT_ANDROID)
        elm[0].send_keys(text1)
        elm[1].send_keys(text2) 
    def activityIsChanged(self,driver,element):
        before = driver.current_activity
        element.click()
        after = driver.current_activity
        if before == after:
            return False
        else:
            return True
    def preciseTap(self,driver,position=(0,0)):
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": position[0], "y": position[1] })
    def logIn(self,driver):
        self.inputString(driver,"1234", "1234")
        driver.find_elements_by_xpath("//*[@text='登录']")[1].click()
        sleep(2)   
    def calendar_Select(self,driver):
        flag = True
        for i in range(1,7):
            if(flag==True):
                for j in range(1,8):
                    driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.view.View[%s]"%(i,j)).click()
#                     el = driver.find_element_by_xpath("//*[@text='下一步，填写订单']")
                    el = driver.find_element_by_id(GD.ORDER_SUBMIT_ANDROID_1)
                    if(self.activityIsChanged(driver,el)):
                        flag = False
                        break 
        
# ===================================
#     iOS通用功能
#     1、滚动屏幕
#     2、输入文本
#     3、在WebView中按文本寻找元素
#     4、判断是否需要登出
# ===================================
class iOSUtility():
    def scroll_screen(self,driver,x1,y1,x2,y2):
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        driver.swipe(x1, y1, x2, y2, 1000)
        sleep(1)
    def findElementByContent(self,driver,text):
        driver.find_element_by_xpath("//*[contains(@name,'%s')]"%text).click()
    def calendar_Select(self,driver):
        dates = driver.find_elements_by_xpath("//UIATableCell[@name='出发日期']/UIAButton")
        print(len(dates))
        pricelabel = driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]").get_attribute("value")
        for i in range(len(dates)):
            print(i)
            if(dates[i].is_enabled() == True):
                dates[-1-i].click()
                if(pricelabel!="0.00"):
                    break
    def inputString(self,driver,text1,text2):
        user = driver.find_element_by_xpath("//UIATextField")
        password = driver.find_element_by_xpath("//UIASecureTextField")
        user.click()
        user.send_keys(text1)    
        password.click()
        password.send_keys(text2)   
    def preciseTap(self,driver,position=(0,0)):
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": position[0], "y": position[1] })
    def needLogOut(self,driver,element):
        before = driver.find_element_by_xpath("//UIAStaticText[1]").get_attribute("value")
        print(before)
        element.click()
        if before is None:
            return False
        else:
            return True