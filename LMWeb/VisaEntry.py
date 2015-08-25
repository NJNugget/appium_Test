# -*- coding: UTF-8 -*-

'''
Created on 2015年8月13日

@author: NJNUGGET
'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
driver.get('http://z.qyer.com')
element = driver.find_element_by_id("qyer_head_nav_item_yd")
ActionChains(driver).move_to_element(element).perform()
sleep(2)
driver.find_element_by_class_name("qyer_head_nav_item_visa").click()
sleep(3)
driver.quit()