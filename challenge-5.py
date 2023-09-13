class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def withdrawal(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
    
    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return self.balance*(self.interestRate)/100

account_obj = Account('Shashank', 2000)
account_obj.deposit(500)
print(account_obj.getBalance())

account_obj = Account('Shashank', 2000)
account_obj.withdrawal(500)
print(account_obj.getBalance())

savingsAccount_obj = SavingsAccount('Shashank', 2000, 5)
print(savingsAccount_obj.interestAmount())
