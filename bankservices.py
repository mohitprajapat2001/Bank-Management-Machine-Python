import datetime
from DatabaseConnect import *
date = datetime.datetime.now()
def CashDeposit(username):
    deposit = int(input("Enter The Amount to Deposit :"))
    temp = db_query(f"SELECT AvailableCash FROM {username}_account;")
    temp = int(temp.fetchall()[-1][0])
    total = deposit+temp
    db_query(f"INSERT INTO {username}_account VALUES('{date.now()}','DEPOSIT','{deposit}','{total}','true');")
    temp = db_query(f"SELECT AvailableCash FROM {username}_account;")
    temp = int(temp.fetchall()[-1][0])
    print("Cash Deposited Successfully\n"
          "Available Amount :",temp)
    mydb.commit()

def CashWithdraw(username):
    temp = db_query(f"SELECT AvailableCash FROM {username}_account;")
    temp = int(temp.fetchall()[-1][0])
    while True:
        withdraw = int(input("Enter The Amount to Withdraw :"))
        if temp < withdraw:
            print("Amount Not Available\n"
                  "Available Balance :", temp)
        elif temp > withdraw:
            total = temp - withdraw
            db_query(f"INSERT INTO {username}_account VALUES('{date.now()}','CREDITED','{withdraw}','{total}','true');")
            temp = db_query(f"SELECT AvailableCash FROM {username}_account;")
            temp = int(temp.fetchall()[-1][0])
            print("Cash Withdraw SuccessFully\n"
                  "Available Balance :", temp)
            break
def BalanceInquiry(username):
    temp = db_query(f"SELECT AvailableCash FROM {username}_account;")
    temp = int(temp.fetchall()[-1][0])
    print("Available Balance :", temp)
def MiniStatement(username):
    temp = db_query(f"SELECT Date,Remarks,Amount,AvailableCash FROM {username}_account;")
    temp = temp.fetchall()
    x = len(temp)
    for i in temp[x-5:x]:
        print(i)
