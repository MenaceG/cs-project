import mysql.connector as sql, datetime as dt
import datetime

conn = sql.connect(host="localhost", user="root", passwd="ayush", database="gasmng")
if conn.is_connected():
    print("connected")
mycursor = conn.cursor()
mycursor.execute(
    "create table gasmng(v_customer varchar(30) primary key , v_accno bigint,v_date date,v_add varchar(40), v_cng bigint, v_lpg bigint, v_debit bigint,v_amtobe_paid bigint , v_credit bigint)"
)
mycursor.execute(
    "create table user ( username varchar(10) not null primary key, password varchar(10))"
)
print(
                "_______________________________________________________________________________"
            )
print("<<<<<<<<<<<<---------- Table Created ---------->>>>>>>>>>>>")
print(
                "_______________________________________________________________________________"
            )
conn.commit()
