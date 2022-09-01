"""
封装获取cookie方法

"""
import urllib3

from common.request import Request
from testdata.variable_data import VariableData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from common.config import Config

import time
class ProductList:


    def __init__(self):
        self.config = Config()
        self.host = self.config.app_host

    def get_productList(self):
        '''
        分页查询获取商品列表
        :return:
        '''
        Record_request = Request(application="WEBMALL",module="productlist",api_name="product_list",domain="https://"+self.host,token=VariableData.userToken)
        Record_response = Record_request.post_request()
        print(Record_response)
        return Record_response




