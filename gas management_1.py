import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='@18110922rajiv',database='gasin')
if conn.is_connected():
    print("connected")
mycursor=conn.cursor()
data="create table gasin(v_customer varchar(30) primary key ,v_accno bigint,v_date date,v_add varchar(40),v_cng bigint,v_lpg bigint,v_debit bigint,v_amtobe_paid bigint ,v_credit bigint)"
mycursor.execute(data)

print("created successfully ")
