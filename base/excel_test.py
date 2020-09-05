# @Time : 2020/9/3 9:32 
# @Author : fei_fei
# @File : excel_test.py 
# @Software: PyCharm
import excel_util;


def write_excel():
    header = ["第一季度", "第二季度", "第三季度", "第四季度"];
    filepath = "E://python_production_projects/python_excel/python_test2.xlsx";
    body = list();
    for i in range(1, 10):
        line = list();
        for j in range(1, len(header) + 1):
            line.append(j);
        body.append(line);
    print(body);
    excel_util.creat_excel(header,body,filepath);


if __name__ == "__main__":
    write_excel();
