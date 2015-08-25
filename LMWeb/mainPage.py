# -*- coding: UTF-8 -*-

'''
Created on 2015年8月13日

@author: NJNUGGET
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
driver.get('http://z.qyer.com')
sleep(8)
focusPics = driver.find_elements_by_css_selector("p.pagination>span")
for i in range(len(focusPics)):
    focusPics[i].click()
    
LM_type = driver.find_elements_by_css_selector("div.tab.clearfix.pd-type>ul>li>a")
for i in range(len(LM_type)-1):
    LM_type = driver.find_elements_by_css_selector("div.tab.clearfix.pd-type>ul>li>a")
    LM_type[i].click()
    sleep(1)
    
LM_dpt = driver.find_elements_by_css_selector("div.tab.clearfix.dpt>ul>li>a")
for j in range(len(LM_dpt)):
    LM_dpt = driver.find_elements_by_css_selector("div.tab.clearfix.dpt>ul>li>a")
    LM_dpt[j].click()
    sleep(1)
    
LM_month = driver.find_elements_by_css_selector("div.tab.clearfix.pr.travel-date>ul>li>a")
for k in range(len(LM_month)):
    LM_month = driver.find_elements_by_css_selector("div.tab.clearfix.pr.travel-date>ul>li>a")
    LM_month[k].click()
    sleep(1)
    
LM_dst = driver.find_elements_by_css_selector("div.tab.clearfix>ul>li>a")
for k in range(len(LM_dst)):
    LM_dst = driver.find_elements_by_css_selector("div.tab.clearfix>ul>li>a")
    LM_dst[k].click()
    sleep(1)
driver.quit()