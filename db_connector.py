import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="Mohit Prajapat",
                               passwd="7877",
                               database="banking")

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE Bank_User(fullname varchar(30),"
                     "username varchar(20),"
                     "password varchar(20),"
                     "mobile varchar(20),"
                     "istrue varchar(5))")
except Exception as e:
    pass
mydb.commit()