"""
==========================
Author   : 文闯
Time     : 2022/07/28 13:42
FileName : excel.py
Company  : 功夫豆
==========================
"""
from openpyxl import load_workbook

class MyExcel:

    def __init__(self, excel_path, sheet_name):
        # 1、加载一个excel，得到工作薄 Workbook
        wb = load_workbook(excel_path)
        # 2、选择一个表单- 通过表单名 Sheet
        self.sh = wb[sheet_name]

    def read_data(self):
        # 注意：接口的请求数据，读取出来是字符串。
        # 存储表单下读取到的所有数据 - 每一个成员都是一个字典
        all_data = []
        data = list(self.sh.values)
        keys = data[0]  # 获取所有的列名
        for row in data[1:]:
            row_dict = dict(zip(keys, row))
            all_data.append(row_dict)
        return all_data

if __name__ == '__main__':
    # excel的文件路径
    excel_path = r"/Users/gfd/Desktop/gfd/testdatas/gcp.xlsx"
    me = MyExcel(excel_path, "gcp")
    cases = me.read_data()
    for case in cases:
        print(case)