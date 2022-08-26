from DatabaseConnect import *
def SignIn():
    while True:
        username = input("Enter Username :")
        try:
            temp = db_query(f"SELECT username FROM Bank_User WHERE username = '{username}';")
            temp = temp.fetchall()[0][0]
            if username == temp:
                while True:
                    password = input(f"Welcome {username.capitalize()} Enter Password :")
                    temp = db_query(f"SELECT password FROM Bank_User WHERE username = '{username}';")
                    temp = temp.fetchall()[0][0]
                    if password == temp:
                        print("Signed In")
                        break
                    else:
                        print("Password is Incorrect Try Again")
                break
        except:
            print("username is incorrect try again")
    return username