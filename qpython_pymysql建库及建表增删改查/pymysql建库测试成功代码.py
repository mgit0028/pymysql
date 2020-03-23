# -*- coding: UTF-8 -*-

import pymysql
# 建库
try:
    conn = pymysql.connect(host='118.89.43.175',user='root',passwd='0987abc123',port=3306)   #连接数据库
    cur=conn.cursor()
    create_database_sql='CREATE DATABASE IF NOT EXISTS testdb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
    cur.execute(create_database_sql)
    cur.close()
    print('创建数据库 testdb 成功！')
except pymysql.Error as e:
    print('pymysql.Error: ',e.args[0],e.args[1])