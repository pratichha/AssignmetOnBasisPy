#Bank common activities
class bank_act:
    def __init__(self):
        self.balance = 0
        print("Welcome to bank")

    def deposit(self):
         amount = float(input("enter a amount to deposte:"))
         self.balance =  self.balance + amount
         print("Deposit  Amount:",amount)

    def withdraw(self):
         amount = float(input("enter a amount to withdraw from account:"))
         if self.balance >= amount:
             self.balance -= amount
             print("Withdraw amount is :", amount)
         else:
             print("Insufficeint Amount:")

b = bank_act()
b.deposit()
b.withdraw()          


