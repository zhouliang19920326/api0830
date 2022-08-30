import unittest

from appx.login import APPXLogin
from appx.product import APPXProduct
from logger import Logger


class Test_delProduct(unittest.TestCase):


    def setUp(self) -> None:
        print("删除商品开始")
        self.logInfo = Logger().getlog()
        self.goods = APPXProduct()


    def test_delProduct(self):
        # self.goods.goods_add()
        # self.goods.soldout_product()
        result = self.goods.del_product()
        # print(result)
        res = result["body"]["code"]
        self.assertEqual("000000",res,"删除商品返回的code码不正确")
        res2 = result["body"]["comment"]
        self.assertEqual("Completed successfully",res2,"删除商品失败")

    def tearDown(self) -> None:
        print("删除商品结束")


if __name__ == '__main__':
    unittest.main()