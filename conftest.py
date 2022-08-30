import pytest, requests, time
from pytest_train.test01 import *
from common.config import *
from common.assertion import *
from testdata.variable_data import *
from common.request import *
import requests
test = Assertions()
@pytest.fixture(scope='class')
def before_datas():
    before_data = cal01().add(4, 4)
    assert before_data == 8
    print("class")
    return before_data

@pytest.fixture(scope='function')
def func():
    before_data = cal01().add(4, 4)
    assert before_data == 8
    print("class")
    return before_data

@pytest.fixture(scope='session')
def session():
    before_data = cal01().add(4, 4)
    assert before_data == 7
    print("session")
    return session

def login():
        '''登录

        :return:
        '''
        # 调用common 的Request 方法 获取测试数据的入参
        login_request = Request("APPX", "wangka_gzh", "login", "https://" + Config().domain)
        # 调用post 方法
        login_response = login_request.post_request()
        code = login_response['body']['code']
        test.assert_code(code, '000000')
        token = login_response['body']['data']['token']
        logger.info("获取登录的token: %s" % token)
        appID = login_response['body']['data']['apps'][0]['appId']
        logger.info("获取登录的appid: %s" % appID)
        setattr(VariableData, "token", token)
        setattr(VariableData, 'appID', appID)

@pytest.fixture(scope='session')
def get_token():
        ''' 获取用户的authorization

        :return:
        '''
        login()
        getToken_requset = Request("APPX", "wangka_gzh", "get_token", "https://" + Config().domain,
                                   token=VariableData.token, appid=VariableData.appID)
        getToken_response = getToken_requset.get_request()
        code = getToken_response['body']['code']
        test.assert_code(code, '000000')
        authorization = getToken_response['body']['data']['token']
        setattr(VariableData, 'authorization', authorization)
        return authorization

















