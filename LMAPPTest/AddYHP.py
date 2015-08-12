# -*- coding: UTF-8 -*-

'''
Created on 2015年8月7日

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
    TouchAction(wd).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
    sleep(1)

#findElementByText_method   
def findElementByText(text):
    wd.find_element_by_xpath("//*[@text='%s']"%text).click()
    sleep(1)
    
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
    findElementByText("我的")
    findElementByText("我的优惠")
    findElementByText("添加优惠券")
    #输入优惠券信息
    inputString("YHP0009300002785", "123962")
    findElementByText("加入我的优惠券")
    
    
finally:
    
    wd.quit()
    print('success')
    if not success:
        raise Exception("Test failed.")


