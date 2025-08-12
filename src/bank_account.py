class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, accountToTransfer, amountToTransfer):
        if amountToTransfer > self.balance:
            raise ValueError("Fondos insuficientes")
        self.withdraw(amountToTransfer)
        accountToTransfer.deposit(amountToTransfer)
