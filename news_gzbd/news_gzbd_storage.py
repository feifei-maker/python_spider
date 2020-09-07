# @Time : 2020/9/3 22:31 
# @Author : fei_fei
# @File : news_gzbd_storage.py
# @Software: PyCharm
import mysql_util;
from news_gzbd import news_requests_data


# 处理数据（把从页面爬到的数据异常位置变成null）
def resolve_data():
    district = "四川省";
    all_page_data = news_requests_data.get_all_page_data();
    for single_page_data in all_page_data:
        for single_data in single_page_data:
            # 插入地区
            single_data.insert(0, district);
            if len(single_data) < 8:
                for i in range(len(single_data), 8):
                    single_data.append("Null");
    return all_page_data;


# 添加新闻信息
def insert_news(all_page_data):
    insert_status = 0;
    for single_page_data in all_page_data:
        for single_data in single_page_data:
            insert_sql = "insert into news_gzbd(news_gzbd_district,news_gzbd_time,news_gzbd_confirmed,news_gzbd_outsideinput,news_gzbd_cure,news_gzbd_death," \
                         + "news_gzbd_isolation,news_gzbd_observe) value ('%s','%s',%s,%s,%s,%s,%s,%s)" \
                         % (single_data[0], single_data[1], single_data[2], single_data[3],
                            single_data[4], single_data[5], single_data[6], single_data[7]);
            # 查询数据，判断是否需要插入
            query_result = query_news(single_data[1]);
            if len(query_result) == 0:
                insert_status += mysql_util.execute_sql(insert_sql);
                if insert_status > 0:
                    print("insert success");
                else:
                    print("insert error");
    return insert_status;


# 删除所有新闻信息
def delete_news():
    delete_sql = "delete from news_gzbd";
    delete_status = 0;
    delete_status += mysql_util.execute_sql(delete_sql);
    return delete_status;


# 查询
def query_news(news_time):
    sql = "select * from news_gzbd where news_gzbd_time='%s'" % news_time;
    result = mysql_util.execute_sql(sql);
    return result;


# 准备数据
def get_storage_data():
    query_sql = "select * from news_gzbd order by news_gzbd_time desc limit 7";
    query_result = mysql_util.execute_sql(query_sql);
    district = query_result[0][1];  # 地区
    time = [];  # 日期
    confirmed = [];  # 确诊人数
    outsideinput = [];  # 境外输入人数
    cure = [];  # 治愈人数
    death = [];  # 死亡人数
    isolation = [];  # 隔离人数
    observe = [];  # 待观察人数
    for single_data in query_result:
        time.append(single_data[2]);
        confirmed.append(single_data[3]);
        outsideinput.append(single_data[4]);
        cure.append(single_data[5]);
        death.append(single_data[6]);
        isolation.append(single_data[7]);
        observe.append(single_data[8]);
    storage_data = {
        "district": district,
        "time": time,
        "confirmed": confirmed,
        "outsideinput": outsideinput,
        "cure": cure,
        "death": death,
        "isolation": isolation,
        "observe": observe
    };
    return storage_data;


if __name__ == "__main__":
    # 插入数据
    all_page_data = resolve_data();
    # insert_result = insert_news(all_page_data);
    # print("已添加：" + str(insert_result));
    # resolve_data();
    # 按日期查询
    # news_time = "8月30日";
    # query_result = query_news(news_time);
    # print(query_result);

    # 删除所有信息
    # delete_result = delete_news();
    # print("已删除：" + str(delete_result));
    # pass;
