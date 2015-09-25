# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
import unittest
from LMAPPTestAndroid.Mine_Test import QYMine
from LMAPPTestAndroid.Selected_Test import QYSelected
from LMAPPTestAndroid.Buy_Process_Test import QYBuy_Process
from LMAPPTestAndroid.MainPage_Test import QYMain
if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(QYBuy_Process)
#     unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(QYMine)
    unittest.TextTestRunner(verbosity=2).run(suite)
#     suite = unittest.TestLoader().loadTestsFromTestCase(QYMain)
#     unittest.TextTestRunner(verbosity=2).run(suite)
#     suite = unittest.TestLoader().loadTestsFromTestCase(QYSelected)
#     unittest.TextTestRunner(verbosity=2).run(suite)