# -*- coding: utf-8 -*-
# @Time : 2021/5/6 9:46
# @Author : zl
# @File : test_member_center.py
# @Software: PyCharm

import unittest

from testdrivebase.testdrive_record import driveRecord
from common.logger import Logger

# from appx.product import APPXProduct
# from ut.core import _TestCase
from webmallbase.webmalllist import ProductList

logger = Logger().getlog()


class Testwebmall_login(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("进入webmall")

        cls.record_obj = ProductList()

    def test_query_productList(self):#获取试驾记录列表，断言数据条数，断言可以自行添加
        response = self.record_obj.get_productList()
        result = response["body"]["data"]["total"]
        print(result)
        self.assertEqual(result,11,"商品数量不正确")


    # def test_query_driveRecordDetail(self):#获取试驾记录详情,断言客户名称
    #     response = self.record_obj.get_driveRecordDetail()
    #     result = response["body"]["data"]["customerName"]
    #     print(result)
    #     self.assertEqual(result,"周亮","试驾单查询不正确")






    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("webmall商品列表查询结束")


if __name__ == '__main__':
    unittest.main()

