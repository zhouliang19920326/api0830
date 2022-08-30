# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:22
# @Author  : maxiang
# @File    : Request.py

"""
封装request

"""
from common.assertion import *
import requests
from common.logger import *
import json
from common.get_api_data import GetData
from testdata.variable_data import *
from common.file_utils import *
import warnings
warnings.simplefilter("ignore", ResourceWarning)
logger = Logger().getlog()
test = Assertions()
s = requests.Session()
null = None


class Request:

    def __init__(self, application, module, api_name, domain, token="",**request_data):
        """
        初始化数据
        @:param application exel 文件名称
        @:param module: excel sheet 名称
        @:param api_name: excel 接口名称
        @:param domain: 域名
        @:param token : 登录的 返回的token
        @:param request_data : 需要修改的字段
        :return:

        """
        self.module = module
        self.api_name = api_name
        self.application = application
        self.token = token
        self.req = GetData(self.application, self.module, self.api_name)#获取测试数据
        self.data = eval(self.req.request_data['data'].strip('\n'))
        # self.data = self.req.request_data["data"]#eval()函数是用来执行一个字符串表达式，并返回表达式的值
        self.apiurl = self.req.request_data['url']
        self.header = eval(self.req.request_data['header'].strip('\n'))#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        # 新增 Authorization
        if (len(token) > 0):
            self.header['Authorization'] = token
        # 如果传的参数为空使用 excel表格 data数据
        if (all(value == "" for value in request_data.values()) == False):
            self.data = self.replace_dict_value(self.data, request_data)
        self.url = domain + self.apiurl

    def get_request(self):
        """
        Get请求
        :return:

        """

        try:
            if (len(self.data) == 0):
                logger.info('请求地址：%s' % (self.url))
                logger.info('请求入参：%s' % (self.data))
                response = requests.get(url=self.url, headers=self.header, verify=False)
                assert test.assert_code(response.status_code, 200)
            else:
                logger.info('请求地址：%s' % (self.url))
                logger.info('请求入参：%s' % (self.data))
                response = requests.get(url=self.url, params=self.data, headers=self.header, verify=False)
                assert test.assert_code(response.status_code, 200)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', self.url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', self.url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        response_dicts['history'] = response.history
        logger.info(self.url + ': 返回结果：%s' % (response.json()))
        return response_dicts

    def post_request(self):
        """ Post requet
        @:param post 请求 url 参数在URL地址
        @:param  post 请求 data 为 list
        :return: request.Response
        """
        try:
            if(len(self.data) == 0):

                logger.info('请求地址：%s' % (self.url))
                logger.info('请求header：%s' % (self.header))
                response = requests.post(self.url, headers=self.header, verify=False)

            else:
                ContentType = self.header["Content-Type"]
                if (ContentType == "application/json"):
                    data_str = json.dumps(self.data)
                else:
                    data_str = self.data
                logger.info('请求地址：%s' % (self.url))
                logger.info('请求入参：%s' % (data_str))
                logger.info('请求header：%s' % (self.header))
                response = requests.post(self.url, data=data_str, headers=self.header, verify=False)
                assert test.assert_code(response.status_code, 200)
                logger.info('response.status_code：%s' % (response.status_code))

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', self.url))
            print(e)
            return e

        except Exception as e:
            print('%s%s' % ('Exception url: ', self.url))
            print(e)
            return e

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        logger.info(self.url + ': 返回结果：%s' % (response.json()))
        return response_dicts

    def post_request_multipart(self, path):
        """
        提交Multipart/form-data 格式的Post请求
        :return:
        """

        try:
            logger.info('请求地址：%s' % (self.url))
            # 获取上传文件的类型

            mimeType = get_mime(path)

            img = open(path, 'rb')
            file = {'file': (path, img, 'Content-Type:' + mimeType)}
            logger.info('请求地址files：%s' % (img))
            response = requests.post(self.url, files=file, headers=self.header, verify=False)
            assert test.assert_code(response.status_code, 200)
            img.close()
            logger.info(response)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', self.url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', self.url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def del_request(self, apiurl=''):
        """
         del_request  请求
         :return:

         """

        try:
            if (len(self.data) == 0):
                logger.info('请求地址：%s' % (self.url))
                logger.info('请求入参：%s' % (self.data))
                url = self.url + apiurl
                response = requests.delete(url=url, headers=self.header,verify=False)
                assert test.assert_code(response.status_code, 200)
            else:
                logger.info('请求地址：%s' % (self.url))
                logger.info('请求入参：%s' % (self.data))
                response = requests.delete(url=self.url, params=self.data, headers=self.header, verify=False)
                assert test.assert_code(response.status_code, 200)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', self.url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', self.url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        response_dicts['history'] = response.history
        logger.info(self.url + ': 返回结果：%s' % (response.json()))
        return response_dicts

    def replace_dict_value(self, org_dict, replace_dict):
        """
        检查replace_dict中的key，如果与org_dict中的key值相同，则把org_dict中该key对应的value值替换成replace_dict中的value值
        :param org_dict: 原始字典
        :param replace_dict: 替换字典
        :return: 修改后的原始字典，key值不变，value值需从replace_dict中寻找匹配
        """
        # 如果是嵌套的字典，有可能其value是列表或者元组
        if isinstance(org_dict, (list, tuple)):
            list_temp = list()
            for i in org_dict:
                list_temp.append(self.replace_dict_value(i, replace_dict))
            return list_temp
        if isinstance(org_dict, str) and org_dict.startswith('{') and org_dict.endswith('}'):  # 此处不严谨，后续修改
            org_dict = json.loads(
                org_dict.replace('null', '"null_re"').replace('false', '"false_re"').replace('true', '"true_re"'))
            org_dict = self.replace_dict_value(org_dict, replace_dict)
            org_dict = json.dumps(org_dict, ensure_ascii=False).replace('"null_re"', 'null').replace('"false_re"',
                                                                                                     'false').replace(
                '"false_re"', 'true')
            return org_dict
        if isinstance(org_dict, dict):
            for key, value in org_dict.items():
                org_dict[key] = self.replace_dict_value(value, replace_dict)
                if key in replace_dict:
                    org_dict[key] = replace_dict[key]
            return org_dict
        return org_dict

