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

logger = Logger().getlog()


class TestProcess1(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("进入试驾记录")

        cls.record_obj = driveRecord()

    def test_query_driveRecordList(self):#获取试驾记录列表，断言数据条数，断言可以自行添加
        response = self.record_obj.get_driveRecordList()
        result = response["body"]["data"]["page"]["totalCount"]
        print(result)
        self.assertEqual(result,4,"试驾记录数据不正确")


    def test_query_driveRecordDetail(self):#获取试驾记录详情,断言客户名称
        response = self.record_obj.get_driveRecordDetail()
        result = response["body"]["data"]["customerName"]
        print(result)
        self.assertEqual(result,"周亮","试驾单查询不正确")






    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("试驾记录流程结束")



if __name__ == '__main__':
    unittest.main()

