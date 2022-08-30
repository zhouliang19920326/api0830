# -*- coding: utf-8 -*-
# @Time : 2021/5/6 9:46
# @Author : zl
# @File : test_member_center.py
# @Software: PyCharm

import unittest

from Wangka_gzh.memberCenter import MemberCenter
from Wangka_gzh.myEnergy import MyEnergy
from common.logger import Logger
# from appx.product import APPXProduct
# from ut.core import _TestCase

logger = Logger().getlog()


class TestProcess1(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("进入会员福利-我的能量")
        cls.MyEnergy_obj = MyEnergy()


    def test_query_jsapi_ticket(self):#我的能量-获取appid接口
        response = self.MyEnergy_obj.get_jsapi_ticket()
        result = response
        print(result)
        res = response["body"]["data"]["appId"]
        # print(tyep(res),res)
        self.assertEqual(res,"wxbaaa8147a67567d6","appId错误")


    def test_getMemberInfo(self):#我的能量-获取会员详情
        response = self.MyEnergy_obj.get_member_info()
        print(response)
        result = response["body"]["success"]
        print(result)
        self.assertEqual(result,True,"会员详情返回失败")
        res = response["body"]["data"]["nickname"]
        self.assertEqual(res,"想流浪的鱼","会员详情返回数据异常")



    def test_getEnergyHistoryRecord(self):#获取能量历史记录_全部
        response = self.MyEnergy_obj.get_energyHistoryRecord()
        result = response["body"]["success"]
        print(result)
        self.assertEqual(result,True,"获取能量历史列表失败")
        res = len(response["body"]["data"])
        self.assertGreater(res,0,"能量列表数据异常")

    def test_getEnergyHistoryRecord_in(self):#获取能量历史记录_获得
        response = self.MyEnergy_obj.get_energyHistoryRecord_in()
        result = response["body"]["success"]
        print(result)
        self.assertEqual(result,True,"获取能量历史列表失败")
        res = response["body"]["data"][0]["type"]
        self.assertEqual(res,1,"能量列表数据不是获得")


    def test_getEnergyHistoryRecord_out(self):#获取能量历史记录_支出
        response = self.MyEnergy_obj.get_energyHistoryRecord_out()
        result = response["body"]["success"]
        print(result)
        self.assertEqual(result,True,"获取能量历史列表失败")
        res = response["body"]["data"][0]["type"]
        self.assertEqual(res,2, "能量列表数据不是支出")


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("会员中心-我的能量-流程结束")



if __name__ == '__main__':
    unittest.main()

