# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
# ===================================
# 测试主入口，在这里控制执行哪些测试用例
# ===================================
import unittest
import os
import multiprocessing
from LMAPPTestiOS.Selected_Test import QYSelected
from LMAPPTestiOS.Buy_Process_Test import QYBuy_Process
from LMAPPTestiOS.Mine_Test import QYMine
from LMAPPTestiOS.MainPage_Test import QYMain
from findertools import sleep
class run():
    caps = {}
    caps['app'] = 'com.qyer.lastminute'
    caps['udid'] = '1adb25f0165219f08ddfca03a2b1c5cef8d19f7d'
    caps['address'] = '172.1.7.54'
    caps['port'] = '3000'
    def connect(self):
        caps = self.caps
        node_path = '/Applications/Appium.app/Contents/Resources/node/bin/node'
        appium_path = '/Applications/Appium.app/Contents/Resources/node_modules/appium/bin/appium.js'
        sum = ""
        for item in caps:
            command = ' --'+item+' '+caps[item]
            sum += command
        os.system(node_path+' '+appium_path+sum)
    def kill(self):
        res = os.system('lsof -i tcp:'+self.caps['port']+' >>tmp.txt')
        for line in open("tmp.txt"):
            new_line = line.split(" ")
            if (new_line[0] == "node"):
                print new_line[4]
                os.system('kill '+new_line[4])
                os.remove("tmp.txt")
                break
# run_test = run()
# run_test.connect()
# threads = []
# t1 = threading.Thread(target=run_test.connect,args=())
# threads.append(t1)
# suite = unittest.TestLoader().loadTestsFromTestCase(QYBuy_Process)
# t2 = threading.Thread(target=unittest.TextTestRunner(verbosity=2).run(suite),args=())
# threads.append(t2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(QYBuy_Process)
    target_test = unittest.TextTestRunner(verbosity=2).run(suite)
