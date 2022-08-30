# -*- coding: utf-8 -*-
# @Time : 2021/5/6 9:46
# @Author : zl
# @File : test_member_center.py
# @Software: PyCharm

import unittest

from common.logger import Logger
from appx.product import APPXProduct
from ut.core import _TestCase

logger = Logger().getlog()


class TestProcess1(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("新增商品、编辑商品、下架、删除商品流程开始")
        cls.goods = APPXProduct()

    def test_addProduct(self):
        response = self.goods.goods_add()
        result = response["body"]["code"]
        self.assertEqual(result,"000000","新增商品返回code码错误")
        result2 = response["body"]["comment"]
        self.assertEqual(result2,"Completed successfully","新增商品失败")
        result3 = len(response["body"]["data"])
        self.assertTrue(result3,"新增商品未返回商品id")

    def test_editProduct(self):
        self.goods.getInfo()#调用商品详情接口，获取商品的类别Id
        self.goods.getSkus()#调用商品的sku接口,获取商品的SkuId
        response = self.goods.edit_product()
        # print(response)
        result = response["body"]["code"]
        self.assertEqual(result,"000000","编辑商品返回code码错误")
        result2 = response["body"]["comment"]
        self.assertEqual(result2,"Completed successfully","编辑商品失败")
        result3 = response["body"]["data"]
        self.assertTrue(result3,"编辑商品未返回商品Id")


    def test_soldoutProduct(self):
        response = self.goods.soldout_product()
        result = response["body"]["code"]
        self.assertEqual(result,"000000","下架商品返回code码错误")
        result2 = response["body"]["comment"]
        self.assertEqual(result2,"Completed successfully","下架商品失败")


    def test_deleteProduct(self):
        response = self.goods.del_product()
        print(response)
        result = response["body"]["code"]
        self.assertEqual(result,"000000","删除商品返回code码错误")
        result2 = response["body"]["comment"]
        self.assertEqual(result2,"Completed successfully","删除商品失败")


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("新增商品、编辑商品、下架、删除商品流程流程结束")



if __name__ == '__main__':
    unittest.main()

