# -*- coding: UTF-8 -*-

'''
Created on 2015年8月11日

@author: NJNUGGET
'''
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import os
from time import sleep

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = 'Nexus 5'
desired_caps['app'] = os.path.abspath('/Users/NJNUGGET/Documents/Python/WorkSpace/AndroidTestApp/aLAST.apk')

wd = webdriver.Remote('http://172.1.7.54:3000/wd/hub', desired_caps)
wd.implicitly_wait(60)

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
    
#inputYHPinfo
def inputString(username,pwd):
    elm = wd.find_elements_by_xpath("//android.widget.EditText")
    elm[0].send_keys(username)
    elm[1].send_keys(pwd)
    
                
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
    findElementByText("我的")
    els = wd.find_elements_by_xpath("//*[@clickable='true']")
    before = wd.current_activity
    print(before)
    els[1].click()
    sleep(1)
    after = wd.current_activity
    print(after)
    if(before == after):
        els[2].click()
        findElementByText("确定")
        els[1].click()
#     wd.find_element_by_xpath("//*[@clickable='true']").click()
    inputString("1234", "1234")
    wd.find_elements_by_xpath("//*[@text='登录']")[1].click()
    sleep(2)    
    
    
finally:
    
    wd.quit()
    print('success')
    if not success:
        raise Exception("Test failed.")
