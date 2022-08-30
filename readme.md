# 接口自动化框架python+unittest+request 
+ 该Demo帮助有诉求的同学快速上手搭建接口自动化。

## 项目使用条件
1. 安装python3，从官网下载python3以上版本即可；
2. 安装python3库，依赖包请自行检查各个文件哪里爆红安装哪里；
3. xlrd安装版本1.2.0版本

## 文件目录说明
```bash
perfdog-service-demo-v2  
+---common 基础公共类
|   \---request.py 底层请求封装模块
|   \---__pycache__
+---conf  配置信息
|   \---__pycache__
+---Log  日志信息
+---report 报告存放
+---testcase 测试用例合集
|   +---testdrive1 试驾测试用例集合
|   |   +---testdrive
|   +---wangka_test 王卡公众号测试用例集合
|   |   +---wangka_gzh
+---testdata  测试数据存放
+---testdrivebase 试驾测试类
|   \---__pycache__
+---ut  存放猴子补丁给测试用例编号

```
- runAll.py 脚本执行入口


## 使用步骤
1. 在conf文件下修改对应的配置信息
2. 编辑common下config.py文件指向刚才编辑的配置
3. 编写测试数据data的xlsx文件，需要注意文件名 、sheet名，api名称 例如：对应的是测试类中的application="TESTDRIVE",module="driveRecord",api_name="record_list"
4. 编写对应的测试类，可以将一类接口归到一起写一个测试类，例如testdrive_record.py中，将试驾记录归为一个测试类，有两个方法1.查询试驾记录列表 2.查询试驾记录详情
5. 写完对应的测试类，到testcase下建一个测试用例文件夹，放置对应的测试用例：如test_recordList.py 中写了两个测试用例，一个查询试驾列表，一个查询试驾详情
6. 写完测试用例之后，在caselist中指定需要测试的测试用例即可，caselist.txt中添加的为测试用例的文件名：例如test_recordList；即可指定在runAll时跑哪些测试用例。
7. 准备好以上步骤之后可以，运行runAll脚本。然后查看控制台信息，查看报告可以到report下查看该报告详情，亦可以用命令行方式执行
```python
注意：
运行过程中出现的报错，耐心解决，不要慌。多半是某些第三方包没有引入导致，开始尝试吧
