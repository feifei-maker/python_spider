# @Time : 2020/9/3 11:16 
# @Author : fei_fei
# @File : mysql_util.py
# @Software: PyCharm
import pymysql;


def connection_mysql():
    connection = pymysql.connect(host='localhost', user='root', passwd='root', db='pythonsql', charset='utf8');
    cursor = connection.cursor();
    return connection, cursor;


def execute_insert_update_delete(cursor, sql):
    status = cursor.execute(sql);
    return status;


def execute_query(cursor, sql):
    cursor.execute(sql);
    # fetchall()返回多个元组，即返回多条记录(rows),如果没有结果,则返回None
    return cursor.fetchall();


def execute_commit(cursor):
    cursor.connection.commit();


def connection_close(connection, cursor):
    connection.close();
    cursor.close();


# 执行sql语句
def execute_sql(sql):
    # 连接数据库
    connection, cursor = connection_mysql();
    # 执行sql语句
    if sql.startswith("select"):
        result = execute_query(cursor, sql);
    else:
        result = execute_insert_update_delete(cursor, sql);
    # 提交
    execute_commit(cursor);
    # 关闭资源
    connection_close(connection, cursor);
    return result;
