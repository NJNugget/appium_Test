# -*- coding: UTF-8 -*-

'''
Created on 2016年2月14日

@author: NJNUGGET
'''
# #==========================md5========================  
# def md5(str):
#     import hashlib
#     import types
#     if type(str) is types.StringType:
#         m = hashlib.md5()   
#         m.update(str)
#         return m.hexdigest()
#     else:
#         return ''      
#     
# print md5("weiyanru")

# -*- coding: utf-8 -*-
import string
import hashlib
file=open("hello.txt","a")

md5input='8f0eaaa4ebed7754ffbed2f9129ce026'
apt=string.printable[:-38]+"."+","
print apt
def dfs(s,num):
    m=hashlib.md5()
    m.update(s)
    md5temp=m.hexdigest()
    if md5temp==md5input:
        print(s)
        file.write("md5是："+md5input+"    明文是："+s+"\n")
        file.close()
        exit(-1)
    else:
        print "no:"+s
    if len(s)==num:
        return
    for i in apt:
        dfs(s+i,num)

myinput=14               #生成字符的位数
for j in range(14,15):
    dfs("wohenkaixin",j)
file.close()
