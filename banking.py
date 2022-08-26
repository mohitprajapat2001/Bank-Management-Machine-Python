from bankservices import *
class UserDetails:
    def __init__(self,username):
        self.username = username
    def CashDeposit(self):
        CashDeposit(self.username)
    def CashWithdraw(self):
        CashWithdraw(self.username)
    def BalanceInquiry(self):
        BalanceInquiry(self.username)
    def MiniStatement(self):
        MiniStatement(self.username)

def UserAccount(username):
    userobj = UserDetails(username)
    option = int(input(f"Welcome {username.capitalize()} Choose One of the Banking Services\n"
                       f"1. Cash Deposit\n"
                       f"2. Cash WithDraw\n"
                       f"3. Balance Inquiry\n"
                       f"4. Mini Statement :"))
    if option == 1:
        userobj.CashDeposit()
    if option == 2:
        userobj.CashWithdraw()
    if option == 3:
        userobj.BalanceInquiry()
    if option == 4:
        userobj.MiniStatement()