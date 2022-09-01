# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 上午10:46
# @Author  : string
# @File    : Config.py

from configparser import ConfigParser
import os
from common.file_path import project_path


class Config:
    # titles:
    TITLE_APPX = "appx"

    TITLE_DBSHOP = "dbshop"

    TITLE_WANGKA = "wangka"

    TITLE_TESTDRIVE = "testdrive"

    TITLE_WEBMALL = "webmall"

    # values:
    # [debug\release]

    VALUE_HOST = "host"

    VALUE_APIKEY = "apikey"

    VALUE_WANGKA = "host_wangka"

    VALUE_TESTDRIVE = "testdrive_host"

    VALUE_WEBMALL = "webmallhost"


    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.conf_path = os.path.join(project_path, 'conf', 'config.ini')

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        # APPX
        self.config.read(self.conf_path, encoding='utf-8')

        # self.app_host = self.get_conf(Config.TITLE_APPX, Config.VALUE_HOST)
        #
        # self.dbshop_apikey = self.get_conf(Config.TITLE_DBSHOP,Config.VALUE_APIKEY)
        #王卡
        self.app_host = self.get_conf(Config.TITLE_WANGKA, Config.VALUE_WANGKA)

        # webmall
        # self.app_host = self.get_conf(Config.TITLE_WEBMALL, Config.VALUE_WEBMALL)
        #试驾
        # self.app_host = self.get_conf(Config.TITLE_TESTDRIVE, Config.VALUE_TESTDRIVE)
        # self.dbshop_apikey = self.get_conf(Config.TITLE_DBSHOP, Config.VALUE_APIKEY)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__ == '__main__':
    k = Config().get_conf("webmall","testdrive_host")
    print(k)