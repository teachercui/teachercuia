import pymysql

conn = pymysql.Connect(
    host="lockhost",
    user="root",
    password=123456,
    db="mysql",
    charset="utf8"
)

#创建光标
cur=conn.cursor()

