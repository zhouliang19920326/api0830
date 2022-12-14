import xlrd
import os

from common.file_path import date_dir


class ExcelUtils:
    """读取excel文件数据"""

    def __init__(self, fileName, SheetName=None, interfaceName=None):
        """读取excel文件数据

        @:param fileName excel 文件名称
        @:param SheetName sheet 名称
        @:param interfaceName 文件单元格 接口名称
        :return:
        """

        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_name(SheetName)
        self.interfaceName = interfaceName
        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                if (api_dict['Id'] == self.interfaceName):
                    listApiData.append(api_dict)
            return listApiData
        else:
            print("表格是空数据!")
            return None

if __name__ == '__main__':
    file_path = date_dir
    new_file_path = os.path.join(date_dir,"WK.xls")

    s = ExcelUtils(new_file_path,"member_center","scroll_ball")
    k = s.read_data()
    print(k)