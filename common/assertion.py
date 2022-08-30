# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午10:14
# @Author  : zhouliang
# @File    : Assert.py


"""
封装Assert方法

"""

import json

from common.logger import Logger

logger = Logger().getlog()
class Assertions:
    def __init__(self):
        pass


    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            logger.info(" statusCode is %s " % (code))
            return True
        except:
            logger.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            raise

    def assert_body(self,body,body_msg,expected_msg,module=None):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        msg = body[body_msg]
        try:
            assert msg==expected_msg
            logger.info(" body_msg is %s " % (msg))
            return True

        except:
            logger.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s,module is %s" % (expected_msg, msg,module))
            raise

    def assert_in_text(self, body, expected_msg,module=""):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            logger.info(" body_msg is %s " % (text))
            assert expected_msg in text
            return True

        except:
            logger.error("Response body Does not contain expected_msg, expected_msg is %s,msg is %s" % (expected_msg,module))
            raise

    def assert_text(self, body, expected_msg,msg=None):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            logger.info(" body_msg is %s " % (body))
            return True

        except:

            logger.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s,module is %s" % (expected_msg, body,msg))

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            raise

    def assert_length(self, length, expected_length,msg):
        """
        验证response body result 结果是否为空
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert len(length) == expected_length
            return True

        except:
            logger.error("Response length > expected_length, expected_length is %s, Response length is %s，msg is %s" % (expected_length, len(length),msg))
            raise