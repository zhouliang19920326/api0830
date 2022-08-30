"""
封装获取cookie方法

"""
import urllib3

from common.request import Request
from testdata.variable_data import VariableData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from common.config import Config

import time
class driveRecord:


    def __init__(self):
        self.config = Config()
        self.host = self.config.app_host

    def get_driveRecordList(self):
        '''
        分页查询获取试驾记录列表
        :return:
        '''
        Record_request = Request(application="TESTDRIVE",module="driveRecord",api_name="record_list",domain="http://"+self.host,token=VariableData.userToken)
        Record_response = Record_request.post_request()
        print(Record_response)
        return Record_response


    def get_driveRecordDetail(self):
        '''
        查询试驾记录详情
        :return:
        '''
        Record_request = Request(application="TESTDRIVE",module="driveRecord",api_name="record_detail",domain="http://"+self.host,token=VariableData.userToken)
        Record_response = Record_request.post_request()
        print(Record_response)
        return Record_response


