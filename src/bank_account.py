import datetime

from src.exceptions import InsufficientFundsError, WithdrawalOutsideBusinessHoursError


class BankAccount:
    def __init__(self, initial_balance=0, log_file=None):
        self.balance = initial_balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposito de {amount} realizado")
        else:
            self._log_transaction(f"Deposito de {amount} fallido: Monto no positivo")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 9 or now.hour > 17:
            self._log_transaction(f"Retiro de {amount} fallido: Fuera del horario permitido")
            raise WithdrawalOutsideBusinessHoursError("Retiro fuera del horario permitido")
        elif amount <= self.balance and amount > 0:
            self.balance -= amount
            self._log_transaction(f"Retiro de {amount} realizado")
        else:
            self._log_transaction(f"Retiro de {amount} fallido: Fondos insuficientes")
            raise InsufficientFundsError("Fondos insuficientes")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Saldo actual: {self.balance}")
        return self.balance

    def transfer(self, accountToTransfer, amountToTransfer):
        if amountToTransfer > self.balance:
            self._log_transaction(
                f"Transferencia de {amountToTransfer} fallida: Fondos insuficientes"
            )
            raise ValueError("Fondos insuficientes")
        self.withdraw(amountToTransfer)
        self._log_transaction(f"Transferencia de {amountToTransfer} realizada exitosamente")
        accountToTransfer.deposit(amountToTransfer)
