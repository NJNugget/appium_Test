# -*- coding: UTF-8 -*-

'''
Created on 2015年8月13日

@author: NJNUGGET
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("/Applications/Google Chrome.app/Contents/MacOS/chromedriver")

driver.get('http://www.qyer.com')
driver.maximize_window()
driver.find_element_by_link_text("登录").click()
sleep(3)
driver.find_element_by_name("mail_input").send_keys("ok123ttt")
driver.find_element_by_name("password").send_keys("lixiang1990922")
driver.find_element_by_xpath("//input[@value='登录']").click()
sleep(3)
print driver.title

driver.quit()
    