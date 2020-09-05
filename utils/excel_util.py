# @Time : 2020/9/3 10:01 
# @Author : fei_fei
# @File : excel_util.py 
# @Software: PyCharm
import openpyxl;


def creat_excel(header,body,filepath):
    # 创建一个Workbook对象
    workbook = openpyxl.Workbook();
    # 创建一个sheet对象
    active_sheet = workbook.get_active_sheet();
    # ---------数据操作----------------
    # 设置表头
    active_sheet.append(header);
    for single_data in body:
        active_sheet.append(single_data);

    # 保存文件
    workbook.save(filepath);
    print("creat excel success");

