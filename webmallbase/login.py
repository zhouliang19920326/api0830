"""
封装获取cookie方法

"""
import urllib3

from common.request import Request
from testdata.variable_data import VariableData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from common.config import Config

import time
class WebmallLogin:


    def __init__(self):
        self.config = Config()
        self.host = self.config.app_host

    def webmallLogin(self):
        '''
        商城登录
        :return:
        '''
        Record_request = Request(application="WEBMALL",module="productlist",api_name="product_list",domain="https://"+self.host,token=VariableData.userToken)
        Record_response = Record_request.post_request()
        print(Record_response)
        return Record_response




