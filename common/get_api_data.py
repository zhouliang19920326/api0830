from common.excel_utils import *
from common.file_path import date_dir
from pathlib import Path

class GetData:
    """
    获取测试数据
    """
    def __init__(self,application, module, api_name):
        """
        :param module: excel  sheetName
        :param api_name: excel  接口名称
        :return: request data
        """
        self.module = module
        self.api_name = api_name
        self.application = application
        #self.data_file_path = str(Path(date_dir))+'\DemoAPITestCase.xlsx'
        self.data_file_path=list(Path(date_dir).rglob('{}.xlsx'.format(self.application)))[0]#根据Path模块中传入的date_dir路径，在路径下进行递归查找所有xlsx后缀的文件，与我们传入的文件名称进行匹配，取第一条
        print(type(self.data_file_path),self.data_file_path)



    def get_api_data(self):
        func = ExcelUtils(self.data_file_path,self.module,self.api_name)
        file_content = func.read_data()
        return file_content


    @property
    def request_data(self):
        data_dict = {}
        data = self.get_api_data()[0].get('data')
        url = self.get_api_data()[0].get('url')
        header = self.get_api_data()[0].get('header')
        if data:
            data_dict['data'] = data
        if url:
            data_dict['url'] = url
        if header:
           data_dict['header'] = header
        return data_dict




if __name__ == '__main__':

    request_info = GetData('WK','member_center','scroll_ball')
    print(request_info.request_data)
    s = request_info.request_data
    print(type(s),s)












