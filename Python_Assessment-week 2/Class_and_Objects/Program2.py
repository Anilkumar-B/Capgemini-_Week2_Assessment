"""•	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods.
 Implement logic to prevent overdraft."""

class BankAccount():
    def __init__(self,name,account_no,balance=0):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Deposited amount {amount} and Total balance is {self.balance}')
        else:
            print("Enter valid amount to deposit")
    
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn money is {amount} and total balance is {self.balance}")
            
        else:
            print("enter correct amount to withdraww")
            
account=BankAccount("Anil",12345,500)

account.deposit(1000)
account.withdraw(200)
account.withdraw(500)
account.deposit(100)

class  BanKAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit_amount(self,amount):
        if amount<0:
            return f"The amount should not be negative"
        else:
            self.balance+=amount
            print(f"Deposited Amount:${amount}")
    def withdrawal_amount(self,amount):
        if amount<0:
            print(f"The amount should not be negative")
        elif amount>self.balance:
            print(f"Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdrawal amount is:${amount}")
    def get_balance(self):
        return f"The CURRENT BALANCE IS ${self.balance}"

bank_operations=BanKAccount("1234567890",200)
print(bank_operations.get_balance()) 
bank_operations.deposit_amount(200)
print(bank_operations.get_balance())
bank_operations.withdrawal_amount(100)
print(bank_operations.get_balance())
bank_operations.withdrawal_amount(5000) # overdraft we are checking 
print(bank_operations.get_balance())