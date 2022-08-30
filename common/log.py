# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import logging
import os
import threading
from typing import Any
class Log:
    __instance = None

    def __new__(cls) -> Any:
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self) -> None:
        # create logger
        self.logger = logging.getLogger('simple_example')
        self.logger.setLevel(logging.DEBUG)
        # 日志文件
        log_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "log", "log.log"))

        # create console handler and set level to debug
        # ch = self.loggerlogging.StreamHandler()
        ch = logging.FileHandler(filename=log_file, encoding="utf-8", mode="wt")

        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)

    def getLogger(self):

        return self.logger


class MyLog:
    log = None
    mutex = threading.Lock()
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log().getLogger()
            MyLog.mutex.release()
        return MyLog.log


