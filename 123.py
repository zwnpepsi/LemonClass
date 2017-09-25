#!/bin/env Python
# -*- coding:utf-8 -*-
import pymysql
conn = pymysql.connect(
    user="root",
    password="root@123456",
    port=3306,
    host="127.0.0.1",   #本地数据库  等同于localhost
    db="MYSQL",
    charset="utf8"
)
conn.cursor()       #获取对应的操作游标