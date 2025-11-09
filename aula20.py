# ["Carlos Ivan", "eu adoro a emap"]
# t = "Carlos Ivan"
# s = "eu adoro a emap"
# s.lower()
from datetime import datetime

class BankingError(Exception): pass
class NegativeAmountError(BankingError): pass 
class InsufficientFundsError(BankingError): pass 


class Account:
    """
    Representa uma conta bancaria simples.

    Atributes:
        owner (str): Name of account holder
        currency (str) : Account currency code (e.g. "BRL", "USD")
        balance (float): Current balance of the account
    Methods:
        deposit(amount): ...
        withdraw(amount): ...
        show_balance(): ...
    Example:
        ...
    """
    def __init__(self, owner: str, currency: str = "BRL", initial_balance: float = 0.0):
        """Lindo
        """
        self.customer = owner
        self.currency = currency 
        self._balance = initial_balance
        self.created_at = datetime.now().isoformat(timespec="seconds")

        if hasattr(self.customer, "add_account"):
            self.customer.add_account(self)

        print(f"[INFO] Account created for {self.owner} in {self.currency} currency")
    
    def deposit(self, amount: float) -> None:
        """Lindo"""
        if amount<=0:
            raise NegativeAmountError("[ERROR] Deposit must be positive")
        self.balance = self.balance + amount
        print(f"[OK] Deposited {amount:.2f} {self.currency}.")


    def withdraw(self, amount: float)-> None:
        """Lindo"""
        if amount <= 0:
            raise NegativeAmountError("[ERROR] Withdraw must be positive")
        if amount > self.balance():
            raise InsufficientFundsError("[ERROR] Insufficient")
            return 
        self.balance(self.balance() - amount)
        print(f"[OK] Withdraw {amount:.2f} {self.currency}")
        return self.balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, new_balance: float) -> float:
        if new_balance != new_balance:
            raise BankingError("[ERROR] Balance cannot be set to NaN")
        self._balance = float(new_balance)

    def __str__(self) -> str:
        return f"Account (owner={self.customer}), currency= {self.currency}, balance = {self.balance}"

class Customer:
    """Lindo"""
    def __init__(self, name: str, email: str): 
        self.name = name
        self.email = email 
        self._accounts :list[Account] = []

    def add_account(self, account: Account): 
        if account not in self._accounts:
            self._accounts.append(account)

    @property 
    def accounts(self) -> list[Account]: 
        return list(self._accounts)
    
    

#Driver Code

acc1 = Account("Ana", "BRL", 20.0)
acc2 = Account("Vitória", "USD", 10.0)
# print(dir(acc1))
# print(acc1)

# acc1.owner = "Matheus"
# print(acc1.owner)
# print(acc1.balance)
# acc1.balance += 1000
# print(acc1.balance)

acc1.deposit(1000)
acc1.show_balance()
acc1.withdraw(10)
acc1.show_balance()

