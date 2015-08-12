# -*- coding: UTF-8 -*-

'''
Created on 2015年8月9日

@author: NJNUGGET
'''
class Singleton2(type):  
    def __init__(cls, name, bases, dict):  
        super(Singleton2, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)  
        return cls._instance  
  
class MyClass3(object):  
    __metaclass__ = Singleton2  
  
one = MyClass3()  
two = MyClass3()  
  
two.a = 3  
two.b = 6
print one.b  
#3  
print id(one)  
#31495472  
print id(two)  
#31495472  
print one == two  
#True  
print one is two  
#True  