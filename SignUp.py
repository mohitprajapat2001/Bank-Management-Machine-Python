from DatabaseConnect import *
import datetime

x = datetime.datetime.now()
def SignUp():
    fullname = input("Enter Fullname :")
    while True:
        username = input("Enter Username :")
        try:
            temp = db_query(f"SELECT username FROM bank_user where username = '{username}';")
            temp = temp.fetchall()[0][0]
            if temp == username:
                print("username already exist try Again")
        except:
            break
    password = input("Enter Password :")
    mobile = input("Enter Mobile No. :")
    db_query(f"INSERT INTO bank_user VALUES('{fullname}','{username}','{password}','{mobile}','true');")
    try:
        db_query(f"CREATE TABLE {username}_account(Date varchar(30),"
                     "Remarks varchar(20),"
                     "Amount varchar(20),"
                     "AvailableCash varchar(20),"
                     "istrue varchar(5))")
        db_query(f"INSERT INTO {username}_account VALUES('{x.now()}','New Account Created','0','0','true');")
    except:
        pass
    print("Signed Up Successfully")