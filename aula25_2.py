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
        """
        self._customer = owner
        self._currency = currency 
        self._balance = float(initial_balance)
        self._created_at = datetime.now().isoformat(timespec="seconds")
        self._customer.add_account(self)
        
    @property
    def balance(self) ->float:
        return self._balance
    def deposit(self, amount: float)->None:
        self._balance += amount
    def withdraw(self, amount: float)->None:
        self._balance -= amount
    def monthly_update(self)-> None:
        print(f"A classe {self.__class__.__name__} nao precisa de atualizacao mensal")
        

class Customer:
    """Lindo"""
    def __init__(self, name: str, email: str): 
        self._name = name
        self._email = email 
        self._accounts :list[Account] = []

    def add_account(self, account: Account): 
        self._accounts.append(account)

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

