

class Bank_Account:
    def __init__(self):
        self. balance=0
        print("Hello!!! welcome to the deposit & withdrawl machine")

    def deposit(self):
        amount =float(input("enter amount to be deposited:"))
        self. balance+=amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount=float(input("enter amount to be withdrawn:"))
        if self.balance>=amount:
          self. balance-=amount
          print("\n you withdrew:", amount)
        else:
          print("\n Insufficient Balance")

    def display(self):
          print("\n Account Balance=", self. balance)




s =Bank_Account()


s.deposit()
s.withdraw()
s.display()
      