from SignIn import *
from SignUp import *
from banking import *

class BankConnect:
    def SignIn(self):
        username = SignIn()
        UserAccount(username)
        mydb.commit()

    def SignUp(self):
        SignUp()
        mydb.commit()

def ConnectBank():
    bankobj = BankConnect()
    while True:
        option = int(input("Welcome To Our Banking Services\n"
                       "Press 1 For Sign In\n"
                       "Press 2 For Sign Up :"))
        if option == 1:
            bankobj.SignIn()
            break
        elif option == 2:
            bankobj.SignUp()
            bankobj.SignIn()
            break
        else:
            print("Try again")
            pass
ConnectBank()
print("Thank You For Banking With Us")