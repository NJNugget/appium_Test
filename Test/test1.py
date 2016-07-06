# -*- coding: UTF-8 -*-

'''
Created on 2015年8月6日

@author: NJNUGGET
'''

import os
from test.make_ssl_certs import TMP_CADIR
# import threading
# from time import sleep
# from multiprocessing import Process
# class test():
#     caps = {}
#     caps['app'] = 'com.qyer.lastminute'
#     caps['udid'] = '1adb25f0165219f08ddfca03a2b1c5cef8d19f7d'
#     caps['address'] = '172.1.7.54'
#     caps['port'] = '3000'
#     def connect(self):
#         caps = self.caps
#         node_path = '/Applications/Appium.app/Contents/Resources/node/bin/node'
#         appium_path = '/Applications/Appium.app/Contents/Resources/node_modules/appium/bin/appium.js'
#         
#         sum = ""
#         for item in caps:
#             command = ' --'+item+' '+caps[item]
#             sum += command
#         cmd = node_path+' '+appium_path+sum
# #         os.system(cmd)
#         t1 = runServer(cmd)
#         p = Process(target=t1.start())
#         p.start()        
#         self.abcd()
#     def kill(self):
#         os.system('lsof -i tcp:'+self.caps['port']+' >>tmp.txt')
#         for line in open("tmp.txt"):
#             new_line = line.split(" ")
#             if (new_line[0] == "node"):
#                 print new_line[4]
# #                 os.system('kill '+new_line[4])
#                 cmd = 'kill '+new_line[4]
#                 t2 = runServer(cmd)
#                 p = Process(target=t2.start())
#                 p.start()
#                 os.remove("tmp.txt")
#                 break
#         
#     def abcd(self):
#         print "================================"
#         print "================================"
#         print "================================"
#         sleep(10)
#         
# class runServer(threading.Thread):
# 
#     def __init__(self, cmd):
#         threading.Thread.__init__(self)
#         self.cmd = cmd
# 
#     def run(self):
#         os.system(self.cmd)
# if __name__ == '__main__':
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     print(os.path.join(base_dir, 'Appiumtest/templates').replace('\\','/'),)
#     abc = test()
#     abc.kill()
#     abc.connect()

if __name__ =='__main__':
    l = [4,1,9,13,34,26,10,7,4]
#     s = "adafkfwefweffff"
    s = "fjaispofjieowmtkln"

    print(os.listdir("/Applications/Appium.app"))
#=========================insert_sort=========================
    def insert_sort(l):
        for i in range(len(l)):
            print("i%d"%i)
            min_index = i
            for j in range(i+1,len(l)):
                print("j%d"%j)
                if(l[min_index]>l[j]):
                    min_index = j
                    print("min_index:%d"%min_index)
                print(str(l))
            tmp = l[i]
            l[i] = l[min_index]
            l[min_index] = tmp
            print(str(l))

#     insert_sort(l)
    print("insert_sort success!!!")
    
    
#==========================bubble_sort========================

    def bubble_sort(l):
        for i in range(len(l),0,-1):
            for j in range(len(l)-1):
                if l[j] > l[j+1]:
                    tmp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = tmp
                print(str(l))
        print("result: " + str(l))

#     bubble_sort(l)
    print("bubble_sort success!!!")
    
#==========================cut_String========================

    def lengthOfLongestSubstring(s):
#         s = "adafkfwefweffff"
        result = 0
        for i in range(1,len(s)):
            tmparr = []
            for j in range(len(s)):
                tmp =  s[j:i+j]
#                 print tmp
                tmparr.append(tmp) 
                if(j>1):
                    for obj in tmparr[0:-1]:
#                         print "obj = %s"%obj+"    "+"tmp = %s"%tmp
                        if obj == tmp:
                            print len(tmp)
                            result = len(tmp)
                            break
#                 print "tmparr = %s"%tmparr   
#     lengthOfLongestSubstring(s)
    
#==========================cut_String========================
    
    def longestwithoutrepeat(s):
        exist = []
        position = []
        for i in range(26):
            exist.append(False)
            position.append(0)
        for i in range(len(s)):
            print exist[s[i]-'a']
    longestwithoutrepeat(s)
    
   