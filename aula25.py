from abc import ABC, abstractmethod

###################################

class Depositable(ABC):
    @abstractmethod
    def deposit(self, amount:float): ...
class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount:float): ...
class InterestBearing(ABC):
    @abstractmethod
    def apply_interest(self, amount:float): ...
class FeeChargeable(ABC):
    @abstractmethod
    def charge_fee(self, amount: float): ...

###########################################################

class SavingsAccount(Depositable, Withdrawable, InterestBearing):
    def deposit(self, amount:float): print(f"Depositando {amount}")
    def withdraw(self, amount:float): print(f"Sacando {amount}")
    def apply_interest(self, amount:float): print(f"Aplicando Juros: {amount}")

class CheckingAccount(Depositable, Withdrawable, FeeChargeable):
    def deposit(self, amount:float): print(f"Depositando {amount}")
    def withdraw(self, amount:float): print(f"Sacando {amount}")
    def charge_fee(self, amount: float): print(f"Cobrando a taxa mensal")

class InvestimentAccount(Depositable, Withdrawable, InterestBearing, FeeChargeable):
    def deposit(self, amount:float): print(f"Depositando {amount}")
    def withdraw(self, amount:float): print(f"Sacando {amount}")
    def apply_interest(self, amount:float): print(f"Aplicando Juros: {amount}")
    def charge_fee(self, amount: float): print(f"Cobrando a taxa mensal")

###########################################################

savings = SavingsAccount(1000)
checking = CheckingAccount()
investment = InvestimentAccount()

savings.apply_interest(6)
checking.charge_fee(20)
investment.apply_interest(6)