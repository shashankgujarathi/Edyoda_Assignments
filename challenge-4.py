class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account_obj = Account('Ashish',5000)
savingsAccount_obj = SavingsAccount('Ashish',5000,5)

print(account_obj.title)
print(account_obj.balance)

print(savingsAccount_obj.title)
print(savingsAccount_obj.balance)
print(savingsAccount_obj.interestRate)
