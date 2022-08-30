#/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time
import logging
import json
import requests
import xlrd
import codecs
from jsonpath_rw import jsonpath, parse

CHECK_HTTPCODE = 'CHECK_HTTPCODE'
CHECK_VALUE_CONTAINS = 'CHECK_VALUE_CONTAINS'
CHECK_VALUE_EQUAL = 'CHECK_VALUE_EQUAL'

SPLIT_MARK = ';'
EQUAL_MARK = '='
POINT_SPLIT_MARK = '.'

HTTP_METHOD_GET = 'GET'
HTTP_METHOD_POST = 'POST'
HTTP_METHOD_PUT = 'PUT'

log_dir = "./"
current_date = time.strftime('%Y%m%d')
log_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
date_format = '%m/%d/%Y %H:%M:%S %p'
logging.basicConfig(filename= log_dir +current_date+'.log', level=logging.DEBUG, format=log_format, datefmt=date_format)

def set_log(log_dir):
    # 日志配置
    logging.basicConfig(filename= log_dir +current_date+'.log', level=logging.DEBUG, format=log_format, datefmt=date_format)
    logging.debug("begin at:"+ time.strftime('%Y-%m-%d %H:%M:%S'))

'''
   Csv操作类
'''
class ExcelUtil:

    api_name = {}
    max_col = 0
    max_row = 0
    variable_value_map = {}
    case_list = []
    input_api_codes = []
    log_dir = "./"
    out_put_file = "./defaul_log.log"

    @classmethod
    def load(cls, file_name):
        '''
            加载配置
        '''
        xl = xlrd.open_workbook(file_name)
        table = xl.sheet_by_name(u"测试用例")
        cls.max_col = table.ncols
        cls.max_row = table.nrows
        log_dir_value = table.cell(1,1).value
        if log_dir_value != None:
            cls.log_dir = log_dir_value
        out_put_file_value = table.cell(2,1).value
        if out_put_file_value != None:
            cls.out_put_file = out_put_file_value

        '''
            加载变量
        '''
        for i in range(1,cls.max_col):
            if table.cell(6,i).value == 'Y':
                cls.variable_value_map[table.cell(4,i).value] = table.cell(5,i).value
        '''
            加载case
        '''
        for j in range(9,cls.max_row):
            if table.cell(j,1).value == 'Y':
                cls.input_api_codes.append(table.cell(j,0).value)
                key_name = table.cell(j,0).value
                case_value = cls.parse_row_to_case(table.row(j))
                cls.case_list.append({key_name : case_value})
                cls.api_name[key_name] = case_value.name

    @classmethod
    def parse_row_to_case(cls,row_value):
        code = row_value[0].value
        name = row_value[2].value
        description = row_value[3].value
        url = row_value[4].value
        method = row_value[5].value
        header = row_value[6].value
        payload = row_value[7].value
        check_rule_set = {}
        expected_http_code = row_value[8].value
        expected_contains_value = row_value[9].value
        expected_equal_value = row_value[10].value
        variable_replace_rule = row_value[11].value
        if expected_http_code != None and expected_http_code != '':
            check_rule_set[CHECK_HTTPCODE] = str(int(expected_http_code))
        if expected_contains_value != None and expected_contains_value != '':
            check_rule_set[CHECK_VALUE_CONTAINS] = expected_contains_value
        if expected_equal_value != None and expected_equal_value!= '':
            check_rule_set[CHECK_VALUE_EQUAL] = expected_equal_value
        return TestCase(code, name, description, url, method, header, payload, check_rule_set, variable_replace_rule)

    @classmethod
    def get_case(cls):
        return cls.case_list

    @classmethod
    def get_input_api_codes(cls):
        return cls.input_api_codes

    @classmethod
    def get_output_file(cls):
        return cls.out_put_file

    @classmethod
    def get_log_dir(cls):
        return cls.log_dir

    @classmethod
    def get_api_names(cls):
        return cls.api_name


'''
   测试案例POJO
'''
class TestCase:
    def __init__(self, code, name ,description, url,  method, header ,payload, check_rule_set, variable_replace_rule):
        self.code = code
        self.name = name
        self.description = description
        self.url = url
        self.method = method
        self.header = header
        self.payload = payload
        self.check_rule_set = check_rule_set
        self.variable_replace_rule = variable_replace_rule
'''
   测试结果
'''
class CheckResult:
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason

'''
  http请求类
'''
class HttpUtil:

    @classmethod
    def post(cls, url, headers, payload ):
        logging.info("request url: %s, headers: %s, payload: %s", url, headers, payload)
        pre_headers = json.loads(headers)
        post_headers = cls.valid(pre_headers)
        response = requests.post(url, json=json.loads(payload), headers=post_headers)
        logging.info("response: %s, %s", response.status_code, response.json())
        return response

    @classmethod
    def get(cls, url, headers):
        logging.info("request url: %s, headers: %s", url, headers)
        pre_headers = json.loads(headers)
        post_headers = cls.valid(pre_headers)
        response = requests.get(url, headers=post_headers)
        logging.info("response: %s, %s", response.status_code, response.json())
        return response

    @classmethod
    def put(cls, url, headers, payload ):
        logging.info("request url: %s, headers: %s, payload: %s", url, headers, payload)
        pre_headers = json.loads(headers)
        post_headers = cls.valid(pre_headers)
        response = requests.put(url, json=json.loads(payload), headers=post_headers)
        logging.info("response: %s, %s", response.status_code, response.json())
        return response

    '''
        header 头请求不能为 非str类型 需要进行校验
    '''
    @classmethod
    def valid(cls, pre_headers):
        post_headers = {}
        for key,value in pre_headers.items():
            if  type(value) == str:
                post_headers[key] = value
            else:
                post_headers[key] = str(value)
        return post_headers

'''
   测试工具类
'''
class TestTools:

    def __init__(self):
        self.input_case = []
        self.test_result = {}

    def init(self):
        self.input_case  = ExcelUtil.get_case()
        self.input_api_codes = ExcelUtil.get_input_api_codes()
        self.output_file = ExcelUtil.get_output_file()
        self.api_name = ExcelUtil.get_api_names()

    def do_test(self):
        self.init()
        if self.input_api_codes == None:
            logging.error("input_api is None")
            return
        for api_case_item in self.input_case:
            api_code = list(api_case_item.keys())[0]
            case = list(api_case_item.values())[0]
            try :
                logging.info("tset api code is: %s", api_code)
                print("开始测试:", api_code)
                self.test_item(case)
            except Exception as e:
                if str(type(e)) == '<class \'requests.exceptions.ConnectionError\'>':
                    logging.error("exception 连接错误: %s", str(e))
                    check_result = CheckResult(False, "exception :" + str(e))
                else:
                    logging.error("exception 其他错误: %s", e.message)
                    check_result = CheckResult(False, "exception :" + e.message)
                self.test_result[case.code] = check_result
            else:
                logging.error("No such case: %s", api_code)
        self.generate_test_result()

    def test_item(self, case):
        if case != None:
            method = case.method
            response = None
            logging.info("method is :%s", method)
            self.init_case_variables(case)
            if method == HTTP_METHOD_GET:
                response = HttpUtil.get(case.url, case.header)
            elif method == HTTP_METHOD_POST:
                response = HttpUtil.post (case.url, case.header, case.payload)
            elif method == HTTP_METHOD_PUT:
                response = HttpUtil.http_get(case.url, case.header, case.payload)
            else:
                pass
            # print("test_item ", case.payload, response.json())
            check_result = self.check(response,case.check_rule_set)
            self.set_case_variables(case, response)
        else:
            check_result = CheckResult(False,"case is none")
        self.test_result[case.code] = check_result

    def init_case_variables(self, case):
        for const_key, const_value in ExcelUtil.variable_value_map.items():
            # print(const_key, const_value)
            if const_value != None and const_value != '':
                if not isinstance(const_value, str):
                    const_value = str(const_value)
                const_key_plus = "{" + const_key + "}"
                # print("init_case_variables", const_key_plus,const_value )
                case.url = case.url.replace(const_key_plus, const_value)
                case.header = case.header.replace(const_key_plus, const_value)
                case.payload = case.payload.replace(const_key_plus, const_value)
                for key, rule in case.check_rule_set.items() :
                    rule = rule.replace(const_key_plus, const_value)
                    case.check_rule_set[key] = rule
            # print("init_case_variables case.payload", case.payload )

    def set_case_variables(self, case, response):
        value = case.variable_replace_rule
        print(value)
        if value != None:
            if SPLIT_MARK not in value:
                self.replace_case_variables(response, value)
            else:
                check_equal_items = value.split(SPLIT_MARK)
                for check_equal_item in check_equal_items:
                    self.replace_case_variables(response, check_equal_item)
                  
    def replace_case_variables(self, response, check_equal_item):
        item_relation = check_equal_item.split(EQUAL_MARK)
        if len(item_relation) != 2:
            return 
        variable_key = item_relation[0]
        expected_json_path_key= item_relation[1]
        print("replace_case_variables", variable_key, expected_json_path_key)
        variable_value = None
        res = parse(expected_json_path_key)
        cont = res.find(response.json())
        for x in cont:
            variable_value = x.value
        print("replace_case_variables result", variable_key, variable_value)
        ExcelUtil.variable_value_map[variable_key] = variable_value

        
    def check(self,response, check_rule_set):
        logging.info("response: %s, check_rule_set keys: %s", response, check_rule_set.keys())
        try:
            if check_rule_set == None:
                return CheckResult(True, "无校验规则" )
            if response == None:
                return CheckResult(False, "返回为空" )
            else:
                for key,value in check_rule_set.items():
                    if key == CHECK_HTTPCODE:
                        if str(response.status_code) != value:
                            return CheckResult(False, " 校验HTTP状态码失败 , 返回状态码: " + str(response.status_code) + ', 校验值: '  + str(value))
                        else:
                            logging.info(" pass HTTP状态码校验OK ")
                    if key == CHECK_VALUE_CONTAINS:
                        if str(response.json()).find(value) == -1:
                            return CheckResult(False, "错误 值包含错误，不包含如下值: " + value)
                        else:
                            # print("值包含校验OK ", key,value,str(response.json()).find(value) )
                            logging.info(" pass 值包含校验OK ")
                    if key == CHECK_VALUE_EQUAL:
                        if SPLIT_MARK not in value:
                            chek_result = self.check_equal(response, value)
                            if chek_result.result == False:
                                return chek_result
                        else:
                            check_equal_items = value.split(SPLIT_MARK)
                            for check_equal_item in check_equal_items:
                                chek_result = self.check_equal(response, check_equal_item)
                                if chek_result.result == False:
                                    return chek_result
                        logging.info(" pass 值相等校验OK ")
                return CheckResult(True, "校验规则通过" )

        except Exception as e:
            logging.error("catch exception: %s", e.message)
            check_result = CheckResult(False, "异常 :" + e.message)
        logging.info("check result: %s", str(check_result.result)+ "  " +check_result.reason)
        return check_result


    def check_equal(self ,response, check_equal_item):
        response_json = response.json()
        check_equal_item_relation = check_equal_item.split(EQUAL_MARK)
        if len(check_equal_item_relation) != 2:
            return CheckResult(False, "invalid rules: "+ check_equal_item)
        response_value = None
        expected_value = check_equal_item_relation[1]
        try:
            json_path_key = check_equal_item_relation[0]
            res = parse(json_path_key)
            cont = res.find(response_json)
            for x in cont:
                response_value = x.value
        except Exception as e:
            logging.error("校验失败,规则: %s, 错误原因: %s",check_equal_item, e.message)
        if response_value == None:
            return CheckResult(False, "校验失败 返回为空 ,规则: "+ check_equal_item)
        if str(response_value) == str(expected_value):
            return CheckResult(True, "通过校验规则: "+ check_equal_item)
        else:
            return CheckResult(False, "校验规则失败 : "+ check_equal_item + "返回值 : " + str(response_value)+ ", 校验值 : " + str(expected_value))

    def generate_test_result(self):
        count = len(self.test_result)
        success_count = 0
        for _, result_item in self.test_result.items():
            if result_item.result:
                success_count = success_count + 1
        failed_count = count - success_count
        with codecs.open(self.output_file, 'w+', encoding='utf-8') as f:
            f.write('*********************** 校验结果 **************************\n')
            format_time='%Y-%m-%d_%a_%H-%M-%S'
            time_tup = time.localtime(time.time())
            cur_time = time.strftime(format_time, time_tup)
            time_string = cur_time + '  总数: ' + str(count) +  ', 成功: '  + str(success_count) +', 失败: '+  str(failed_count) + '\n'
            print(time_string)
            f.write(time_string)
            for key ,result in self.test_result.items():
                result_string = key +  "  " + self.api_name[key] + "   " +  str(result.result) + "  " + result.reason + "\n"
                f.write(result_string)
                print(result_string)
            f.write('\n\n')

def main():
    file_name = "D:\\automation-api-demo\\自动化测试Case.xlsx"
    import sys
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    ExcelUtil.load(file_name)
    set_log(ExcelUtil.get_log_dir())
    test_tool = TestTools()
    test_tool.do_test()

if __name__ == "__main__":
    main()