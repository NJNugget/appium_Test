# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

@author: NJNUGGET
'''

import requests
from BeautifulSoup import BeautifulSoup as bsoup
headers = {
#     'Referer':'http://z.qyer.com/zt/20150820/?campaign=shoujiao&category=20150801',
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

usr_list = {'ok123ttt':'lixiang1990922',
            '1234':'1234',
            'nuggetjiang0922':'lixiang1990922',
            '281141082@qq.com':'ok123ttt',
            '7332':'gaoyuanjlu',
            'zjq910210':'jianqiao210',
            '670655440':'kuaile.123',
            'edie1019@sina.cn':'edie1019'
            }
data_login = {'password':'',
                         'input':'',
                         'type':'mail',
                         'remember':'1'}


data_order = {
                'pid':'147054',
                'cid':'4315885',
                'price':'99',
                'form_token':'',
                'sum':'1',
                'rooms':'1',
                'common_name':'叮当',
                'common_phone':'13681305572',
                'common_email':'shishengling0726@hotmail.com',
                "common_wechat": '',   
                'common_bind':'1',
                'ps_msg':'',    
                'coupon_code':'',    
                'coupon_pwd': '',   
                'coupon_coupon':'',    
                'notice_agree':'true'}

data_contact = {
'cid':'2610471',
'price':'569',
'pid':'96792',
'room-offset':'0',
'sum':'1',
'rooms':'1',
'name':'蒋子豪',
'form_token':'',
'phone':'15950000000',
'email':'zihao.jiang@qyer.com'}


# def order(data1,data2):
#     url1 = 'http://login.qyer.com/qcross/login/auth.php?action=login'
#     r1 = requests.post(url1,data=data1,headers=headers)
#     url2 = r1.json()['data']['arr_synlogin'][2]
#     r2 = requests.post(url2,headers=headers)
# #     cookies = r1.cookies+r2.cookies
#     print r2
#     url = 'http://z.qyer.com/orderformconfirm'
#     r3 = requests.post(url, data2,cookies=r2.cookies,headers=headers)
#     print "================"
#     print r3

class orderconfirm():
    def dealcookies(self,cookie1,cookie2,cookie3):
        tmpdict1 = requests.utils.dict_from_cookiejar(cookie1)
        tmpdict2 = requests.utils.dict_from_cookiejar(cookie2)
        tmpdict3 = requests.utils.dict_from_cookiejar(cookie3)
        for (k,v) in tmpdict2.items():
            tmpdict1[k] = v
        for (k,v) in tmpdict3.items():
            tmpdict1[k] = v
        tmpdict1['cdb_sid'] = 'deleted'
        cookie = requests.utils.cookiejar_from_dict(tmpdict1, cookiejar=None, overwrite=True)
        return cookie
    def order(self,data1,data2):
        s = requests.Session()
        url1 = 'http://login.qyer.com/qcross/login/auth.php?action=login'
        r1 = s.post(url1,data=data1,headers=headers)
        url2 = r1.json()['data']['arr_synlogin'][2]
        r2 = s.post(url2,headers=headers)
    #     cookies = r1.cookies+r2.cookies
        print r2.cookies
        url3 = 'http://z.qyer.com/orderformconfirm'
        r3 = s.post(url3, data2,cookies=r2.cookies,headers=headers)
        print "================"
        soup = bsoup(r3.text)
        token = soup.findAll("input")[3]["value"]
        data_order['form_token'] = token
#         ordercookie = self.dealcookies(r1.cookies,r2.cookies, r3.cookies)
#         print ordercookie
        url4 = 'http://z.qyer.com/orderform'
        headers['Referer'] = 'http://z.qyer.com/orderformconfirm'
        submit = s.post(url4,data = data_order,cookies=r3.cookies,headers=headers )
if __name__ == '__main__':
    data_login['input'] = '1234'
    data_login['password'] = '1234'
    orderbook = orderconfirm()
    orderbook.order(data_login, data_contact)
    