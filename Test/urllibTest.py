# -*- coding: UTF-8 -*-

'''
Created on 2015年8月13日

@author: NJNUGGET
'''
import requests

headers = {
    'Referer':'http://z.qyer.com/zt/20150820/?campaign=shoujiao&category=20150801',
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
usr_list = {'ok123ttt':'lixiang1990922',
            '1234':'1234'}
data_login = {'password':'',
                         'input':'',
                         'type':'mail',
                         'remember':'1'}

print(usr_list.items()[0])
def login(data):
    url = 'http://login.qyer.com/qcross/login/auth.php?action=login'
    r1 = requests.post(url,data=data,headers=headers)
    try:
        url = r1.json()['data']['arr_synlogin'][0]
        print(url)
        r2 = requests.get(url,headers=headers)
        r3 = requests.post('http://z.qyer.com/topic.php?action=sign820',data={'action':'sign820'},headers = headers,cookies=r2.cookies)
        try:
            str = r3.json()['data']['msg']+','+u'总共已经签到'+r3.json()['data']['signs']+u'次'
            print(str)
        except:
            pass
#         print(r3.json()['data']['msg']+','+u'总共已经签到')
    except:
        print('fail to login')
    
for (k,v) in usr_list.items():
    print((k,v))
    data_login['input'] = k
    data_login['password'] = v
    login(data_login)
