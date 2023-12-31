import mysql.connector as sql , datetime as dt
import datetime
conn=sql.connect(host='localhost',user='root',passwd='@18110922rajiv',database='gasin')
if conn.is_connected():
    print("connected")
mycursor=conn.cursor()
mycursor.execute("create table user ( username varchar(10) not null primary key, password varchar(10))")
print("table is created")
conn.commit()
