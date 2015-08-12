# -*- coding: UTF-8 -*-

'''
Created on 2015年8月11日

@author: NJNUGGET
'''
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import os
from time import sleep
from objc._objc import NULL

success = True
flag = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = 'iPhone 6'

wd = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
wd.implicitly_wait(20)


def scroll_screen(x1,y1,x2,y2):
    #TouchAction(wd).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
    wd.swipe(x1, y1, x2, y2, 1000)

    sleep(1)

def inputString(YHPnum,YHPpwd=""):
    number = wd.find_element_by_xpath("//UIATextField")
    number.send_keys(YHPnum)
    password = wd.find_element_by_xpath("//UIASecureTextField")    
    password.send_keys(YHPpwd)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    
    #滑动屏幕用以显示更多
    scroll_screen(150, 150, 170, 70)
    #进入分类页面
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
    sleep(2)       
#     wd.find_element_by_name("Category Hotel").click()
    wd.find_element_by_xpath("//UIAScrollView[1]/UIAButton[1]").click()
    sleep(1)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]").click()
    sleep(5)
#     wd.find_element_by_xpath("///UIAWindow[1]/UIAButton[2]")
    wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 311, "y": 639 })
    sleep(1)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[2]").click()
    sleep(1)
    dates = wd.find_elements_by_xpath("//UIATableCell/UIAButton")
    
    print(len(dates))
    for i in range(len(dates)):
        if(dates[i].is_enabled()):
            dates[i].click()
            break        
#         scroll_screen(200, 500, 200, 300)
    wd.find_element_by_name("点击添加旅客").click()
    sleep(1)
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]").click()
    sleep(1)
    wd.find_element_by_name("Confirm Btn").click()
    sleep(1)
    wd.find_element_by_name("提交订单").click()
    sleep(2)


finally:
    
    wd.quit()
    print('success')
    if not success:
        raise Exception("Test failed.")

