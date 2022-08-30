"""
封装获取cookie方法

"""
import urllib3

from common.request import Request
from testdata.variable_data import VariableData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from common.config import Config

import time
class MemberCenter:


    def __init__(self):
        self.config = Config()
        self.host = self.config.app_host

    def get_scroll_bar(self):
        '''
        获取测试文案
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="scroll_ball",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.get_request()
        return memberCenter_response


    def get_jsapi_ticket(self):
        '''
        获取APPID
        :return:
        '''
        # goods_name = "ZL_Test"+str(int(time.time()))
        # setattr(VariableData,"goods_name",goods_name)
        memberCenter_request = Request(application="WK",module="member_center",api_name="jsapi-ticket",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.get_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response


    def member_level_list(self):
        '''
        获取会员等级列表
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="member_level_list",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response


    def get_bind_info(self):#设备详情
        '''
        获取设备详情
        :return:
        '''
        # goods_name = "ZL_Test"+str(int(time.time()))
        # setattr(VariableData,"goods_name",goods_name)
        memberCenter_request = Request(application="WK",module="member_center",api_name="bind_info",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.get_request()
        return memberCenter_response

    def get_coupon_list(self):
        '''
        获取能量兑好礼礼品列表
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="coupon_list",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response


    def get_member_info(self):
        '''
        获取会员详情
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="member_info",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response


    def get_backendConfig(self):
        '''
        获取后端配置
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="query_config",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response


    def get_query_banner(self):
        '''
        获取方形BANNER
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="query_banner",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response


    def get_signHistory(self):
        '''
        获取后端配置
        :return:
        '''
        memberCenter_request = Request(application="WK",module="member_center",api_name="sign_history",domain="https://"+self.host,token=VariableData.userToken)
        memberCenter_response = memberCenter_request.post_request()
        # goods_id = memberCenter_response["body"]["data"]
        # setattr(VariableData,"goods_id",goods_id)
        return memberCenter_response

