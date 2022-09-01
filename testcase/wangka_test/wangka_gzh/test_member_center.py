# -*- coding: utf-8 -*-
# @Time : 2021/5/6 9:46
# @Author : zl
# @File : test_member_center.py
# @Software: PyCharm

import unittest

from Wangka_gzh.memberCenter import MemberCenter
from common.logger import Logger
# from appx.product import APPXProduct
# from ut.core import _TestCase

logger = Logger().getlog()


class TestProcess1(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("进入会员中心")
        cls.memberCenter_obj = MemberCenter()

    def test_query_scroll_ball(self):#获取测试文案接口
        response = self.memberCenter_obj.get_scroll_bar()
        result = response["body"]["success"]
        print(result)
        res = response["body"]["data"]["content"]
        print(res)
        self.assertEqual(res,"大家好, 这里是测试环境的公众号, 如果你是在测试环境测试, 那么可以继续","查询测试文案返回码错误")


    def test_query_jsapi_ticket(self):#获取appid接口
        response = self.memberCenter_obj.get_jsapi_ticket()
        result = response
        print(result)
        # self.assertEqual(result,None,"查询测试文案返回码错误")

    #
    # def test_getMemberLevelList(self):#获取会员等级列表
    #     response = self.memberCenter_obj.member_level_list()
    #     print(response)
    #     result = response["body"]["success"]
    #     print(result)
    #     self.assertEqual(result,True,"会员等级列表返回失败")
    #     res = len(response["body"]["data"])
    #     self.assertEqual(res,5,"会员等级返回数据异常")
    #
    #
    # def test_getBindInfo(self):#获取设备详情
    #     response = self.memberCenter_obj.get_bind_info()
    #     result = response["body"]["success"]
    #     print(result)
    #     self.assertEqual(result,True,"获取设备详情失败")
    #     res = len(response["body"]["data"])
    #     self.assertEqual(res,1,"设备数量与实际不一致")
    #
    #
    # def test_getCouponList(self):#获取非0能量礼品列表
    #     response = self.memberCenter_obj.get_coupon_list()
    #     result = response["body"]["success"]
    #     print(result)
    #     self.assertEqual(result,True,"获取设备详情失败")
    #     res = len(response["body"]["data"])
    #     self.assertEqual(res,6,"礼品数量不正确")
    #
    # def test_getMemberInfo(self):#获取会员详情
    #     response = self.memberCenter_obj.get_member_info()
    #     result = response["body"]["success"]
    #     print(result)
    #     self.assertEqual(result,True,"获取设备详情失败")
    #     res = response["body"]["data"]["nickname"]
    #     self.assertEqual(res,"想流浪的鱼","用户详情错误")
    #
    # def test_getBackendConfig(self):#获取后端配置
    #     response = self.memberCenter_obj.get_backendConfig()
    #     result = response["body"]["success"]
    #     #print(result)
    #     self.assertEqual(result,True,"获取后端配置失败")
    #     res = response["body"]["data"]
    #     self.assertEqual(res,None,"配置信息返回错误")
    #
    # def test_query_banner(self):#获取BANNER
    #     response = self.memberCenter_obj.get_query_banner()
    #     result = response["body"]["success"]
    #     #print(result)
    #     self.assertEqual(result, True, "获取Banner信息失败")
    #     res = response["body"]["data"]
    #     self.assertEqual(res, None, "BANNER信息返回错误")
    #
    # def test_getSignHistory(self):#获取待签到历史
    #     response = self.memberCenter_obj.get_signHistory()
    #     result = response["body"]["success"]
    #     print(result)
    #     self.assertEqual(result,True,"获取待签到列表失败")
    #     res = len(response["body"]["data"]["signHistories"])
    #     self.assertEqual(res,7,"获取待签到列表信息错误")


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("会员中心流程结束")



if __name__ == '__main__':
    unittest.main()

