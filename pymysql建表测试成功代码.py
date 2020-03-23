# -*- coding: UTF-8 -*-

import pymysql
# 建表
try:
    conn=pymysql.connect(host='118.89.43.175',port=3306,user='root',passwd='0987abc123',db='testdb',charset='utf8')
    cur=conn.cursor()
    cur.execute('drop table if exists user;')
    create_table_sql='''
        CREATE TABLE user(
            id int(11) DEFAULT NULL ,
            name VARCHAR(50) DEFAULT NULL ,
            password VARCHAR(30) DEFAULT NULL ,
            birthday TIMESTAMP DEFAULT now() 
        )engine=innodb DEFAULT CHARACTER set utf8;
    '''
    cur.execute(create_table_sql)
    print('创建数据库表成功！')
except pymysql.Error as e:
    print('mysql.Error: ',e.args[0],e.args[1])