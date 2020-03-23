# -*- coding: UTF-8 -*-

import pymysql
# 数据库操作
# 连接
def db_conn(host,port,user,passwd,db_name):
    try:
        conn=pymysql.connect(
            host=host,
            port=port,
            user=user',
            passwd=password,
            db=db_name,
            charset='utf8',
        )
        # cur=conn.cursor()
        print('数据库连接成功！')
        # 返回连接
        return conn
    except pymysql.Error as e:
        print('数据库连接失败')
        print('mysql.Error: ',e.args[0],e.args[1])

def db_cur(conn):
    # 获取游标
    cur=conn.cursor()
    return cur

def db_close(cur,conn):
    # 游标关闭
    cur.close()
    # 提交事务
    conn.commit()
    # 连接关闭
    conn.close()

# 插入单行数据
def db_insert_data(sql,cur,*args):
    try:
        # print(args)
        result=cur.execute(sql,args)
        print('添加语句受影响的行数：',result)
    except Exception as e:
        print('db_insert_data error: ',e.args)

# 批量插入数据
def db_insert_datas(sql,cur,list_datas):
    try:
        result=cur.executemany(sql,list_datas)
        print('批量插入受影响的行数：',result)
    except Exception as e:
        print('db_insert_datas error: ',e.args)

# 修改单行数据
def db_update(sql,cur):
    result=cur.execute(sql)
    print('修改语句受影响的行数：',result)

# 批量修改数据
def db_update_datas(sql,cur,list_datas):
    try:
        result=cur.executemany(sql,list_datas)
        print('批量修改受影响的行数：',result)
    except Exception as e:
        print('db_update_datas error: ',e.args)

# 删除单行数据
def db_delete_data(sql,cur):
    result=cur.execute(sql)
    print('删除语句受影响的行数：',result)

# 批量删除数据
def db_delete_datas(sql,cur,list_datas):
    try:
        result=cur.executemany(sql,list_datas)
        print('批量删除受影响的行数：',result)
    except Exception as e:
        print('db_delete_datas error: ',e.args)

# 回滚
def roll_back(conn):
    try:
        conn.rollback()
        print('回滚完成！')
    except Exception as e:
        print('rollback error: ',e.args)

def db_select_data(sql,cur):
    result=cur.execute(sql)
    print('查询语句受影响的行数：',result)

def db_select_datas(sql,cur,list_datas):
    try:
        result=cur.executemany(sql,list_datas)
        print('批量查询受影响的行数：',result)
    except Exception as e:
        print('db_select_datas error: ',e.args)

if __name__=="__main__":

    host='127.0.0.1'
    port=3306
    user='root'
    passwd='123456'
    db='py3_tstgr'
    conn=db_conn(host,port,user,passwd,db)
    print(conn)
    cur=db_cur(conn)
    print(cur)
    
    insert_sql="insert into user values(1,'tom','123','1990-01-01');"
    db_insert_data(insert_sql,cur)

    insert_sql2="insert into user values(%s,%s,%s,%s);"
    db_insert_data(insert_sql2,cur,2,'lucy','aaa','1991-02-02')
    
    insert_datas_sql="insert into user values(%s,%s,%s,%s);"
    list_datas=[(2,'ha2','222','1992-02-02'),(3,'ha3','333','1993-03-03'),(4,'ha4','444','1994-04-04')]
    db_insert_datas(insert_datas_sql,cur,list_datas)
    
    # 查询数据
    sql="select * from user;"
    cur.execute(sql)
    res1=cur.fetchone()   # 获取一行数据
    print(res1)
    res2=cur.fetchmany(2)  #获取多行数据
    print(res2)
    res3=cur.fetchall()  # 获取所有数据
    print(res3)
    print(cur.fetchone())  # None
    # 重置游标
    cur.scroll(1,mode='relative')
    print(cur.fetchone())
    
    # 更新数据
    up_sql="update user set name='lala' where password='123';"
    db_update(up_sql,cur)
    
    # 批量更新数据
    up_sqls="update user set name=%s where password=%s;"
    up_datas=[('lw','123'),('lc','aaa')]
    db_update_datas(up_sqls,cur,up_datas)
    
    # 删除数据
    delete_sql="delete from user where name='lw';"
    db_delete_data(delete_sql,cur)
    
    delete_sqls="delete from user where name=%s;"
    db_delete_datas(delete_sqls,cur,[('lc'),('hah2'),('hah3')])

    # print(cur.rownumber)  # 0 获取所在行号

    # cur.scroll(0,mode='absolute')
    # cur.execute('select * from user;')

    select_sql="select * from user;"
    db_select_data(select_sql,cur)
    print(cur.fetchall())
    

    # roll_back(conn)  # 回滚
    # print(cur.rownumber)
    # cur.scroll(0, mode='absolute')
    # cur.execute('select * from user;')

    # 查询单行
    select_sql = "select * from user;"
    db_select_data(select_sql, cur)
    
    # 批量查询
    select_sqls="select * from user where name=%s;"
    db_select_datas(select_sqls,cur,[('ha1'),('ha2'),('ha3')])
    print(cur.fetchall())

    db_close(cur,conn)  # 断开连接