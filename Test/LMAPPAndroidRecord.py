# -*- coding: UTF-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import os
import time
from time import sleep

success = True
global_path = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
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

#findElementByText_method   
def findElementByText(text):
    wd.find_element_by_xpath("//*[@text='%s']"%text).click()

def loop_calendar():
    for i in range(5):
        for j in range(7):
            wd.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.view.View[%s]"%(i,j)).click()
            sleep(1)
            break
                
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
    sleep(2)
    #选择酒店
    wd.find_element_by_xpath("//android.widget.GridView[1]/android.widget.FrameLayout[2]").click()
    #wd.find_element_by_xpath(global_path+"/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]").click()
    sleep(1)
    #找到“8-4-折扣app-秒杀”
    findElementByText("8-4-折扣app-秒杀")
    #el = wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.TextView[1]")
    #print(el.get_attribute("text"))
    #el.click()
    sleep(4)
    #点击“立即预订”
    findElementByText("立即预订")
    #elm = wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
    #print(elm.get_attribute("text"))
    #elm.click()
    sleep(1)
    #选择“无单房差”产品
    findElementByText("距离开始时间很久")
    sleep(1)
    scroll_screen(500, 500, 500, 450)
    sleep(1)
    findElementByText("选择日期")
    #elm = wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
    #print(elm.get_attribute("text"))
    #elm.click()
    sleep(1)
    #选择出发日期
    
    wd.find_element_by_xpath("//android.widget.LinearLayout[3]/android.view.View[3]").click()
    sleep(1)
    #滚动屏幕
    scroll_screen(500, 500, 500, 450)
    sleep(1)
    #点击添加新旅客
    findElementByText("点击添加新旅客")
    sleep(1)
    wd.find_element_by_xpath("//android.widget.CheckBox[1]").click()
    sleep(1)
    wd.find_element_by_xpath("//android.widget.LinearLayout[3]/android.widget.ImageView[1]").click()
    sleep(1)
    #点击使用优惠券
    scroll_screen(100, 100, 100, 20)
    sleep(1)
    findElementByText("使用优惠券")
    #wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
    sleep(1)
    #选择优惠券
    wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]").click()
    sleep(1)
    #点击提交订单
    wd.find_element_by_xpath("//android.widget.Button[1]").click()
finally:
    
    wd.quit()
    print('success')
    if not success:
        raise Exception("Test failed.")


