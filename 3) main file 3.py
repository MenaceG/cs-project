v_credit = 0

import mysql.connector as sql, datetime as dt
import datetime

conn = sql.connect(host="localhost", user="root", passwd="ayush", database="gasmng")


if conn.is_connected():
    print("connected")
mycursor = conn.cursor()


print("..............GAS INVENTORY MANAGEMENT SYSTEN.............")


username = input("ENTER THE YOUR USERNAME TO LOGIN TO THE SOFTWARE: ")
password = input("ENTER YOUR PASSWORD IN 10  CHARACRTER TO LOGIN TO THE SOFTWARE: ")
if username == "ayush" and password == "1234":
    print("                      USER IS IDENTIFIED                            ")
    print(
        "                                                                                                   "
    )
    print(
        "_____________________________________________________________________________________________"
    )
    print(
        "                                                                                                                                                                                                 "
    )
    print(
        "                                                                                                                                                                                                 "
    )
    print("                     YOU CAN PROCEED                                  ")
    for i in range(0, 99999999999):
        print("1.CREATE ACCOUNT")
        print("2.TO GET DETAILS OF THE CUSTOMER")
        print("3.TO MAKE BILL")
        print("4.TO GET THE DETAILS OF EVERY CUSTOMER")
        print("5.TO GET DETAILS OF A PARTICULAR CUSTOMER")
        print("6.TO INSERT MULTIPLE VALUES")
        print("7.ENTER 0 TO LOG OUT")

        choice = int(input("Enter Your Choice As Per The Above Information: "))
        if choice == 1:

            v_customer = input("Enter the name of the customer: ")
            v_accno = int(input("Enter your account number: "))
            v_date = datetime.datetime.now()
            v_add = input("Enter your complete address: ")
            v_cng = int(input("Enter your CNG Details: "))
            v_lpg = int(input("Enter your LPG Details: "))
            v_debit = int(input("Enter your debit card number: "))
            v_amtobe_paid = int(input("Enter amount to be paid: "))
            v_credit = int(input("Enter your credit amount: "))

            query = """insert into gasmng (v_customer, v_accno, v_date, v_add, v_cng, v_lpg, v_debit, v_amtobe_paid, v_credit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            data = (
                v_customer,
                v_accno,
                v_date,
                v_add,
                v_cng,
                v_lpg,
                v_debit,
                v_amtobe_paid,
                v_credit,
            )

            mycursor.execute(query, data)
            conn.commit()

            print("Account is created")
            print(
                "_______________________________________________________________________________"
            )
            print(
                "                                                                                                                                                                                                 "
            )
            print(
                "                                                                                                                                                                                                 "
            )

            continue
        elif choice == 2:
            mycursor.execute("select * from gasmng")
            re = mycursor.fetchall()
            print("YOUR RESULT IS ")
            for x in re:
                print(x)
                print(
                    "_______________________________________________________________________________"
                )
                print(
                    "                                                                                                                                                                                                 "
                )
                print(
                    "                                                                                                                                                                                                 "
                )
                continue

        elif choice == 3:
            customer_name = input("Enter The Name Of The Customer: ")
            import datetime

            v_date = datetime.datetime.now()
            date = v_date
            print("The Date & Time Is:", v_date)
            print(
                "Choose a Choice From The Following As Per The GAS Bought By: ",
                customer_name,
            )
            print("1. C N G ......Rs.75/l")
            print("2.L P G .......Rs.80/l")
            print("3.Both LPG.....Rs.75/l & CNG.... Rs.80/l")
            print(
                "                                                                                                                                                                                                 "
            )
            ch = int(input("Enter Your Choice: "))
            print(
                "                                                                                                                                                                                                 "
            )
            print(
                "                                                                                                                                                                                                 "
            )
            if ch == 1:
                cng = int(input("Enter The Quantity Bought: "))
                amount = 75 * cng
                print("THE AMOUNT TO BE PAID IS: ", amount)
                upd_val = (cng, amount, customer_name)
                mycursor.execute(
                    "update gasmng set v_cng = %s, v_amtobe_paid = %s where v_customer = %s",
                    upd_val,
                )

                cho =input(
                        "If Transaction Is To Be Done Through The Credit Amount Enter Y: "
                    )
                if cho == "Y":
                    remaining = v_credit - amount

                    rem_val = (remaining, date, customer_name)
                    mycursor.execute(
                        "update gasmng set v_credit =  %s, v_date =  %s where v_customer = %s ",
                        rem_val,
                    )
                    print("Your Record Is Updated")
                    conn.commit()
                else:
                    print("INVALID CODE")

            if ch == 2:
                lpg = int(input("Enter The Amount Bought By The Customer: "))
                pay = 80 * lpg
                print("The Amount To Be Paid Is: ", pay)

                amt_val = (lpg, pay, customer_name)
                mycursor.execute(
                    "update gasmng set v_lpg = %s, v_amtobe_paid = %s where v_customer = %s ",
                    amt_val,
                )

                print("Your Record Is Updated")
                choo = input(
                        "If Transaction Is To Be Done Through The Credit Amount Enter Y: "
                    )

                if choo == "Y":
                    remain = v_credit - pay
                    remain_val = (remain, date, customer_name)
                    mycursor.execute(
                        "update gasmng set v_credit = %s, v_date = %s where v_customer = %s", remain_val
                    )
                    print("Your Record Is Updated")
                    
                    print(
                        "                                                                                                                                                                                                 "
                    )
                    print(
                        "                                                                                                                                                                                                 "
                    )
                    conn.commit()
            if ch == 3:
                lpgas = int(input("Enter The Amount Of LPG GAS Bought: "))
                cngas = int(input("Enter The Amount Of CNG GAS Bought: "))
                total = 80 * lpgas + 75 * cngas
                print("The Amount To Be Is: ", total)
                
                total_val = (lpgas, cngas, total, customer_name)
                mycursor.execute(
                    "update gasmng set v_lpg = %s, v_cng = %s, v_amtobe_paid = %s where v_customer = %s", total_val
                )
                print("Your Record Is Updated")

                chio = input(
                        "If Transaction Is To Be Done Through The Credit Amount, Enter Y: "
                    )


                if chio == "Y":
                    remaind = v_credit - total

                    remnd_val = (remaind, date, customer_name)
                    mycursor.execute(
                        "update gasmng set v_credit = %s, v_date = %s where v_customer = %s",remnd_val
                    )
            else:
                print("<<<<<<<<<<.............INVALID INPUT..........>>>>>>>>>>>")
                print("<<<<<<<...........Re-enter the suitable input  ........>>>>>>>>>>>")
                print(
                    "________________________________________________________________________________________________________________________"
                )
                print(
                    "                                                                                                                                                                                                 "
                )
                print(
                    "                                                                                                                                                                                                 "
                )
                conn.commit()
                continue
        elif choice == 4:
            mycursor.execute("select * from gasmng")
            se = mycursor.fetchall()
            print(
                "...........................     THE STORED DATA IS    ............................."
            )
            print(
                "                                                                                                                                                                                                 "
            )
            print(
                "                                                                                                                                                                                                 "
            )
            print(
                "                                                                                                                                                                                                 "
            )

            for x in se:
                print(x)
                print(
                    "____________________________________________________________________________________________________"
                )
            conn.commit()
            continue
        elif choice == 5:
            customer_name = input("ENTER YOUR NAME: ")
            mycursor.execute(
                "select  v_credit, v_debit, v_accno, v_add from gasmng where v_customer = '%s' " %(customer_name)
            )
            record = mycursor.fetchall()
            for x in record:
                print(x)
            print(" Continue Your Work") 
            print(
                "                                                                                                                                                                                                 "
            )
            print(
                "                                                                                                                                                                                                 "
            )
            print(
                "                                                                                                                                                                                                 "
            )
            conn.commit()
            continue

        elif choice == 6:
            v_customer = input("Enter The Name Of The Customer: ")
            v_accno = input("Enter Your Acount Number: ")
            v_date = datetime.datetime.now()
            # date = v_date
            v_add = input("Enter Your Complete Address: ")
            v_debit = input("Enter Your Debit Card Number: ")
            v_credit = int(input("Enter Your Credit Amount: "))


            mycursor.execute(
                "insert into gasmng (v_customer, v_accno, v_date, v_add, v_debit, v_credit) VALUES ('%s', '%s','%s','%s','%s',%s)" %(v_customer, v_accno, v_date, v_add, v_debit, v_credit)
                )
            print("Inserted")
            print(
                "_______________________________________________________________________________"
            )
        elif choice == 0:
            break
        else:
            print("<<<<<<  ...........INVALID INPUT..........>>>>>>>>>>>")
            print("<<<<<<<...........Re-enter the suitable input........>>>>>>>>>>>")
            print(
                "_______________________________________________________________________________"
            )
            conn.commit()
            continue
else:
    print(
        "             SORRY!!! ......... THE PERSON IS UNIDETIFIED...........!!!        "
    )
    print(
        "        SORRY!!! ......... YOU ARE NOT SUPPOSE TO USE THE SOFTWARE......... !!!"
    )
    quit
conn.commit()
