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

cursor.execute(sql_create_table3)

cursor.close()
cnn.close()