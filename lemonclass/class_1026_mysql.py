# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/26 17:43
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : class_1026_mysql.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import mysql.connector
import  configparser
#进行实例化
cf=configparser.ConfigParser()
#读取配置文件
cf.read("class_1026_mysql_config.conf",encoding="utf-8")   #自带Read函数读取

cnn=mysql.connector.connect(**eval(cf.get("Mysql","config")))
cursor=cnn.cursor()

sql_create_table='CREATE TABLE student1\
( id int(10) NOT NULL AUTO_INCREMENT,\
name varchar(10) DEFAULT NULL,\
age int(3) DEFAULT NULL,\
PRIMARY KEY (id))\
ENGINE=MyISAM DEFAULT CHARSET=utf8'
# cursor.execute("create database siye")
sql_create_table2="create table student(\
	id int not null PRIMARY key auto_increment,\
	name varchar(12),\
	sex varchar(12) ,\
	class_id int(11) ,\
	address varchar(12) ,\
	create_date datetime,\
	update_date datetime\
) DEFAULT CHARSET=utf8;"

sql_create_table3="create table test_data(\
    id int not null PRIMARY key auto_increment,\
    url varchar(100),\
    mobilephone VARCHAR(11),\
    amount INT ,\
    http_method VARCHAR(10)\
)DEFAULT CHARSET=utf8;"


# auto_increment 自增长 赋值时可不填
sql_insert="insert into student values(1,'siye','boy', 1,'lemonclass',sysdate(),sysdate())"
sql_insert2="insert into student(id,name,sex) VALUES(2,'siye2','boy')"

#数据放到元组里
insert_1="insert into student (name,sex,class_id)VALUES (%s,%s,1)"
data1=("nuanyang","girl")    #元组数据
# cursor.execute(insert_1,data1)   #插入元组类型的数据

insert_2="insert into student (name,sex,class_id)VALUES (%(name)s,%(sex)s,1)"
data2={"name":"siye2","sex":"boy"}        #字典数据
# cursor.execute(insert_2,data2)   #插入元组类型的数据

insert_3="insert into student (name,sex,class_id)VALUES (%s,%s,1)"
data3=[("siye3","boy"),("feifei","girl")]           #列表数据,列表内不许是元组
# cursor.executemany(insert_3,data3)
# result=cursor.fetchall()   #读取数据
# cursor.execute(insert_1,data)   #插入元组类型的数据
select="select * from student WHERE id >%s and sex = %s"     #查询操作
cursor.execute(select,(0,"girl"))   #select,(0,)数据必须是元组


result2=cursor.fetchall()    #输出列表类型数据
# result3=cursor.fetchone()  #输出元组类型数据
print(result2)



#修改操作
update="update student set name ='SIYE' WHERE name ='siye2'"
cursor.execute(update)

#删除操作
#drop databse siye  删除数据库
#drop table student    删除表
delete="delete from student WHERE 1   AND (OR ) 2"

try:
    cursor.execute("sql语句")
    cursor.execute("commit")    #执行成功就保存
except mysql.connector.Error as e:
    print(e)    #raise e
    cursor.execute("rollback")   #执行失败就回滚
finally:
    cursor.close()
    cnn.close()