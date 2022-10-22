import mysql.connector as sql, datetime as dt
import datetime
from Usr_Pswd import UsrNm, Pswd

conn = sql.connect(host="localhost", user = UsrNm, passwd = Pswd)
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
