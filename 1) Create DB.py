import mysql.connector as sql, datetime as dt
import datetime

conn = sql.connect(host="localhost", user="root", passwd="ayush")
mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE gasmng")

if conn.is_connected():
    print(
                "_______________________________________________________________________________"
            )
    print("<<<<<<<<<<<<---------- Database Created ---------->>>>>>>>>>>>")
    print(
                "_______________________________________________________________________________"
            )
   
mycursor = conn.cursor()
conn.commit()
