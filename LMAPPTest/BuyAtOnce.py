# -*- coding: UTF-8 -*-

'''
Created on 2015年8月10日

@author: NJNUGGET
'''
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import os
from time import sleep

success = True
flag = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = 'Nexus 5'
desired_caps['app'] = os.path.abspath('/Users/NJNUGGET/Documents/Python/WorkSpace/AndroidTestApp/aLAST.apk')

wd = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
wd.implicitly_wait(20)

#scroll_method
def scroll_screen(x1,y1,x2,y2):
    #TouchAction(wd).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
    wd.swipe(x1, y1, x2, y2, 1000)

    sleep(1)
#findElementByText_method   
def findElementByText(text1,text2=""):
    try:
        el = wd.find_element_by_xpath("//*[@text='%s']"%text1)
    except:
        el = wd.find_element_by_xpath("//*[@text='%s']"%text2)
        
    el.click()
    sleep(1)

#ActivityIsChanged
def activityIsChange(element):
    before = wd.current_activity
    element.click()
    after = wd.current_activity
    if before == after:
        return False
    else:
        return True
#inputYHPinfo
def inputString(YHPnum,YHPpwd=""):
    elm = wd.find_elements_by_xpath("//android.widget.EditText")
    elm[0].send_keys(YHPnum)
    elm[1].send_keys(YHPpwd)
    
                
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    sleep(8)
    #滑动屏幕用以显示更多
    scroll_screen(500, 500, 700, 70)
    #进入分类页面
    findElementByText("分类")
    findElementByText("酒店")
    wd.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout/android.widget.FrameLayout").click()
    findElementByText("立即预订","在线预订")
    sleep(1)
    scroll_screen(500, 300, 500, 200)
    findElementByText("选择日期")
    
    for i in range(1,7):
        for j in range(1,8):
            el = wd.find_element_by_xpath("//android.widget.LinearLayout[2]/android.view.View[%s]"%j)
            if(activityIsChange(el)):
                flag = False
                break
        if(flag == True):
            scroll_screen(500, 600, 500, 280)
        else:
            break
    
    findElementByText("提交订单")
finally:
    
    wd.quit()
    print('success')
    if not success:
        raise Exception("Test failed.")


