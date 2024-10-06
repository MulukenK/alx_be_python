


class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = float(account_balance)
        self.initial_balance = 0

       
    
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self,amount):
        if(self.account_balance >= amount):
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
       formatted = "{:.2f}".format(self.account_balance) 
       return print(f"Current Balance: ${formatted}")







        
