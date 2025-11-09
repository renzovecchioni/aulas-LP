# ["Carlos Ivan", "eu adoro a emap"]
# t = "Carlos Ivan"
# s = "eu adoro a emap"
# s.lower()
from datetime import datetime

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

        Args:
            owner (str): _description_
            currency (str, optional): _description_. Defaults to "BRL".
            initial_balance (float, optional): _description_. Defaults to 0.0.
        """
        self.owner = owner
        self.currency = currency 
        self._balance = initial_balance
        self.created_at = datetime.now().isoformat(timespec="seconds")

        print(f"[INFO] Account created for {self.owner} in {self.currency} currency")
    
    def deposit(self, amount: float) -> None:
        """Lindo"""
        if amount<=0:
            print("[ERROR] Deposit must be positive")
            return 
        self.set_balance(self.get_balance() + amount)
        print(f"[OK] Deposited {amount:.2f} {self.currency}.")

    def withdraw(self, amount: float)-> None:
        """Lindo"""
        if amount <= 0:
            print("[ERROR] Withdraw must be positive")
            return 
        if amount > self.get_balance():
            print("[ERROR] Insufficient")
            return 
        self.set_balance(self.get_balance() - amount)
        print(f"[OK] Withdraw {amount:.2f} {self.currency}")

    def get_balance(self) -> float:
        return self._balance

    def set_balance(self, new_balance: float) -> float:
        if new_balance != new_balance:
            print("[ERROR] Balance cannot be set to NaN")
            return 
        self._balance = float(new_balance)
    def show_balance(self) -> None:
        print("#" * 40)
        print(f"Owner: {self.owner}")
        print(f"Currency: {self.currency}")
        print(f"Balance: {self._balance}")
        print(f"Created at : {self.created_at}")
        print("#" * 40)

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

acc1.show_balance()
acc2.show_balance()

acc1.deposit(1000)
acc1.show_balance()
acc1.withdraw(10)
acc1.show_balance()
