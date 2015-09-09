# -*- coding: UTF-8 -*-

'''
Created on 2015年8月20日

@author: NJNUGGET
'''
import requests

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

def login(data):
    url = 'http://login.qyer.com/qcross/login/auth.php?action=login'
    r1 = requests.post(url,data=data,headers=headers)
    url = r1.json()['data']['arr_synlogin'][0]
    #print(url)
    r2 = requests.get(url,headers=headers)
    time = 1440089040659
    for i in range(3):

        url = 'http://m.qyer.com/z/game/dzp?action=getprize&_=%s'%time
        r3 = requests.get(url,headers = headers,cookies=r2.cookies)
        #print(url)
        #str = r3.json()['data']['msg']+','+u'总共已经签到'+r3.json()['data']['signs']+u'次'
        str = r3.json()['data']
        try:
            if str['awardLevel']>-1:
                print("************************")
                print(u'中奖啦')
                print("************************")
        except:
            print(str['error'])
        print(str)
        
#         print(r3.json()['data']['msg']+','+u'总共已经签到')        
for (k,v) in usr_list.items():
    
    data_login['input'] = k
    data_login['password'] = v
    print('==========================')
    print(u'用户名为'+k)
    print('==========================')
    login(data_login)
