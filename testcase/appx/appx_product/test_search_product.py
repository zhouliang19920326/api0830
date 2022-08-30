# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : maxiang
# @File    : TestAddProduct.py

from common.logger import *
from common.assertion import *
import time
import unittest

from appx.login import APPXLogin
from appx.product import APPXProduct
from logger import Logger

logger = Logger().getlog()
from ut.core import _TestCase

test = Assertions()
from appx.login import *
from appx.product import *
#
# class TestAddLogistics(_TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         APPXLogin().getUserToken()
#         logger.info('测试用例开始执行')
#
#     def tearDown(self):
#         logger.info('测试用例执行完毕')
#
#     def test_search_product(self):
#         ''' 搜索商品'''
#         pass




class Test_delProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.goods = APPXProduct()
        logger.info('查询商品测试用例开始执行')


    def test_searchProduct(self):
        result = self.goods.search_product()
        print(result)
        res = result["body"]["code"]
        self.assertEqual("000000",res,"删除商品返回的code码不正确")
        res2 = result["body"]["comment"]
        self.assertEqual("Completed successfully",res2,"删除商品失败")

    def tearDown(self):
        logger.info('查询商品测试用例执行完毕')

if __name__ == '__main__':
    unittest.main()

