#!/usr/bin/
# -*- coding: GBK -*-

import logging
import os

from common.file_path import log_dir
class Logger(object):
    def __init__(self):
        self.loglevel = logging.DEBUG
        '''dirs = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,"log"))'''
        dirs = log_dir
        isExists = os.path.exists(dirs)
        if not isExists:
            os.makedirs(dirs)

        # create a logger
        self.logger = logging.getLogger("mylog")
        # �ж�logger�Ƿ��Ѿ���ӹ�handler������ֱ�ӷ���logger���󣬷���ִ��handler�趨�Լ�addHandler(ch)
        if not self.logger.handlers:
            self.logger.setLevel(self.loglevel)

            # create handler for write log file
            fh = logging.FileHandler(os.path.join(dirs,"log.txt"),encoding="UTF-8")
            fh.setLevel(self.loglevel)

            # create a handler for output to console
            ch = logging.StreamHandler()
            ch.setLevel(self.loglevel)

            # define handler's output formate
            formatter = logging.Formatter(
             '[%(asctime)s][%(filename)s][line: %(lineno)d][%(levelname)s] %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # add hander to logger
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


