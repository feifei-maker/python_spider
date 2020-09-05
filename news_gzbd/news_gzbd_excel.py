# @Time : 2020/9/5 21:38 
# @Author : fei_fei
# @File : news_gzbd_excel.py 
# @Software: PyCharm
import excel_util,mysql_util;


def write_excel():
    query_sql = "select * from news_gzbd order by news_gzbd_time desc limit 7";
    query_result = mysql_util.execute_sql(query_sql);
    header = ["地区", "日期", "确诊人数", "境外输入人数", "治愈人数", "死亡人数", "隔离人数", "待观察人数"];
    filepath = "E://python_production_projects/python_excel/gzbd_excel.xlsx";
    body = list();
    for line_data in query_result:
        single_data = [];
        for i in range(1,len(line_data)):
            single_data.append(line_data[i]);
        body.append(single_data);
    excel_util.creat_excel(header, body, filepath);


if __name__=="__main__":
    # write_excel();
    pass;