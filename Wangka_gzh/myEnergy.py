"""
封装获取cookie方法

"""
import urllib3

from common.request import Request
from testdata.variable_data import VariableData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from common.config import Config

import time
class MyEnergy:
    # login_tk = APPXLogin().login(phoneNumber="18872342929",password="test123456")
    # login_uk = APPXLogin().getUserToken()


    def __init__(self):


        self.config = Config()
        self.host = self.config.app_host
        # self.g = APPXLogin().login(phoneNumber="18872342929",password="test123456")
        # self.uk = APPXLogin().getUserToken()


    def get_jsapi_ticket(self):
        '''
        我的能量-获取APPID
        :return:
        '''
        # goods_name = "ZL_Test"+str(int(time.time()))
        # setattr(VariableData,"goods_name",goods_name)
        MyEnergy_request = Request(application="WK",module="member_center",api_name="energy_jsapi-ticket",domain="https://"+self.host,token=VariableData.userToken)
        MyEnergy_response = MyEnergy_request.get_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return MyEnergy_response




    def get_member_info(self):
        '''
        我的能量-获取会员详情
        :return:
        '''
        MyEnergy_request = Request(application="WK",module="member_center",api_name="energy_member_info",domain="https://"+self.host,token=VariableData.userToken)
        MyEnergy_response = MyEnergy_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return MyEnergy_response

    def get_energyHistoryRecord(self):
        '''
        我的能量-获取能量历史记录
        :return:
        '''
        MyEnergy_request = Request(application="WK",module="member_center",api_name="energy_history_record",domain="https://"+self.host,token=VariableData.userToken)
        MyEnergy_response = MyEnergy_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return MyEnergy_response


    def get_energyHistoryRecord_in(self):
        '''
        我的能量-获取能量历史记录-获得
        :return:
        '''
        MyEnergy_request = Request(application="WK",module="member_center",api_name="energy_history_record_in",domain="https://"+self.host,token=VariableData.userToken)
        MyEnergy_response = MyEnergy_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return MyEnergy_response


    def get_energyHistoryRecord_out(self):
        '''
        我的能量-获取能量历史记录-支出
        :return:
        '''
        MyEnergy_request = Request(application="WK",module="member_center",api_name="energy_history_record_out",domain="https://"+self.host,token=VariableData.userToken)
        MyEnergy_response = MyEnergy_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return MyEnergy_response



