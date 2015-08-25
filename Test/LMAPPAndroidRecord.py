# -*- coding: UTF-8 -*-
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
    #TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y2).release().perform()
        wd.swipe(x1, y1, x2, y2, 1000)

        sleep(1)
#findElementByText_method   
def findElementByText(text):
    wd.find_element_by_xpath("//*[@text='%s']"%text).click()

def loop_calendar():
    for i in range(5):
        for j in range(7):
            wd.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.view.View[%s]"%(i,j)).click()
            sleep(1)
            break

def inputString(text1,text2=""):
        elm = wd.find_elements_by_xpath("//android.widget.EditText")
        elm[0].send_keys(text1)
        elm[1].send_keys(text2)
        
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
    sleep(1)
    findElementByText("我的")
    findElementByText("我的订单")
    print(wd.current_activity)
    if(wd.current_activity == '.activity.user.NewLoginActivity'):
        inputString('ok123ttt', 'lixiang1990922')
        wd.find_elements_by_xpath("//*[@text='登录']")[1].click()
    sleep(2)
    scroll_screen(900, 1100, 100, 1100)
    sleep(1)
    scroll_screen(900, 1100, 100, 1100)
finally:
    
    wd.quit()
    print('success')
    if not success:
        raise Exception("Test failed.")


