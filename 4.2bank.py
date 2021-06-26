class Bank_Account:
    def __init__(self,Account_no,Name,Type_of_account):
        self.acc_no=Account_no
        self.name=Name
        self.acc_type=Type_of_account
        self.balance=0
    def deposit(self):
        amount=float(input("Enter an amount to deposit :"))
        self.balance+=amount
        print("Amount deposited to the account is Rs.",amount)
    def display(self):
        print("Your account number : ",self.acc_no)
        print("Your name : ",self.name)
        print("Your account type : ",self.acc_type)
        print("Your balance : Rs.",self.balance)
    def withdraw(self):
        amount=float(input("Enter amount to withdraw : "))
        if(self.balance>amount):
            self.balance-=amount
            print("Amount withdrawn is Rs.",amount)
        else:
            print("Insufficient Balance!!")
customer=Bank_Account(6021743,"John","Current")
customer.deposit()
customer.display()
customer.withdraw()
customer.display()
