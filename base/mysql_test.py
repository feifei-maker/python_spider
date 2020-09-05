# @Time : 2020/9/3 9:01 
# @Author : fei_fei
# @File : mysql_test.py 
# @Software: PyCharm
import mysql_util as myu;


if __name__ == "__main__":
    insert_sql = "insert into school (school_name) value ('南京大学')";
    status = myu.insert_update_delete(insert_sql);
    print(status);
    delete_sql = "delete from school where school_name='北京大学'";
    myu.insert_update_delete(delete_sql);0
    update_sql = "update school set school_name='四川大学' where school_id=1";
    myu.insert_update_delete(update_sql);
    query_sql = "select * from school";
    result = myu.query(query_sql);
    print(result);