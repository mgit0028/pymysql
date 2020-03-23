03.26 15:00
pymysql建库建表代码缩进去空格
Warning: (1007, "Can't create database 'testdb'; database exists")
  result = self._query(query)

s3/pymysql建表9999.py.bak" && exit       <
  File "/storage/emulated/0/qpython/scripts3/pymysql建表9999.py.bak", line 7

##
第7行conn pymysql.connect主机用户根passwd db测试端口
缩进错误需要缩进的块1
##

conn = pymysql.connect(
host='118.89.43.175',
user='root',
passwd='0987abc123',
db='testdb',port=3306)   

#连接数据库
       ^
IndentationError: expected an indented block
1|:/ $

解决方法如下
代码缩进即可

conn=pymysql.connect(host='118.89.43.175',user='root',passwd='0987abc123',db='testdb',port=3306) 



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




