# -*- coding: UTF-8 -*-

'''
Created on 2015年9月23日

@author: NJNUGGET
'''
# ===================================
# 测试主入口，在这里控制执行哪些测试用例
# ===================================
import unittest
from LMAPPTestiOS.Selected_Test import QYSelected
from LMAPPTestiOS.Buy_Process_Test import QYBuy_Process
from LMAPPTestiOS.Mine_Test import QYMine
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(QYBuy_Process)
    unittest.TextTestRunner(verbosity=2).run(suite)