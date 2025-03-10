class Conta():
    
    def __init__(self, titular, numero):
        self._titular = titular
        self._numero = numero
        self._saldo = 0
        
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


c1 = Conta("teu pai", "123")

c1.depositar(100)
print(c1.saldo)

c1.sacar(50)
print(c1.saldo)