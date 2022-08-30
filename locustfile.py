#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from locust import HttpUser, task, between, events
import urllib3
import requests
from locust.contrib.fasthttp import FastHttpLocust
urllib3.disable_warnings()


@events.test_start.add_listener
def on_test_start(**kwargs):
    print('===测试最开始提示===')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束了提示===')


class TestTask(HttpUser):
    wait_time = between(1, 5)
    # host = 'https://www.baidu.com'

    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')

    # @task(1)
    # def getBaidu(self):
    #     self.client.get(url="/", verify=False)

    # @task(1)
    # def getQuerylist(self):
    #     header = {"Accept":	"application/json, text/plain, */*",
    #               "Content-Type":"application/json;charset=UTF-8"}
    #     data ={}
    #     req = self.client.post(url="/client/v1/record/list", data=data,headers=header,verify=False)
    #     if req.status_code == 200:
    #         print("success")
    #
    #     else:
    #         print("fails")

    @task(1)
    def getQuerylist(self):
        header = {"Content-Type": "application/json","authorization": "bearer oLVpVt7BrVhC_3xgTI-mI1AtARvQ"}
        data ={"timestamp":1636533786857,"type":1}
        req = self.client.get(url="/backend/kcm/scroll_bar/type", data=data,headers=header,verify=False)
        if req.status_code == 200:
            print("success")

        else:
            print("fails")
    def on_stop(self):
        print('这是TEARDOWN，每次销毁User实例时都会执行！')

class TestTask(HttpUser):
    wait_time = between(1, 5)
    # host = 'https://www.baidu.com'

    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')

    # @task(1)
    # def getBaidu(self):
    #     self.client.get(url="/", verify=False)

    @task(1)
    def getQuerylist(self):
        header = {"Accept":	"application/json, text/plain, */*",
                  "Content-Type":"application/json;charset=UTF-8"}
        data ={}
        req = self.client.post(url="/client/v1/record/list", data=data,headers=header,verify=False)
        if req.status_code == 200:
            print("success")

        else:
            print("fails")

    # @task(1)
    # def getQuerylist(self):
    #     header = {"Content-Type": "application/json","authorization": "bearer oLVpVt7BrVhC_3xgTI-mI1AtARvQ"}
    #     data ={"timestamp":1636533786857,"type":1}
    #     req = self.client.get(url="/backend/kcm/scroll_bar/type", data=data,headers=header,verify=False)
    #     if req.status_code == 200:
    #         print("success")
    #
    #     else:
    #         print("fails")
    def on_stop(self):
        print('这是TEARDOWN，每次销毁User实例时都会执行！')

# class MyLocust(FastHttpLocust):
#     task_set = TestTask
#     min_wait = 1000
#     max_wait = 60000
if __name__ == "__main__":
    import os

    os.system("locust -f locustfile.py --host=http://10.31.1.34:30734")

