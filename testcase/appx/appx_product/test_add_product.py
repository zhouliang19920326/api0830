
import unittest

from appx.login import APPXLogin
from appx.product import APPXProduct
from logger import Logger
logger = Logger().getlog()

class Test_addProduct(unittest.TestCase):




    @classmethod
    def setUpClass(cls):
        cls.goods = APPXProduct()
        logger.info('查询商品测试用例开始执行')

    def test_addProduct(self):

        result = self.goods.goods_add()
        res = result["body"]["code"]
        self.assertEqual("000000",res,"新增商品返回的code码不正确")
        res2 = result["body"]["comment"]
        self.assertEqual("Completed successfully",res2,"新增商品失败")

    def tearDown(self) -> None:
        print("新增商品结束")


if __name__ == '__main__':
    unittest.main()


