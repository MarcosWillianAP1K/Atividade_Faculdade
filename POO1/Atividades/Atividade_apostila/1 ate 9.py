import abc 

class Conta(abc.ABC):
    
    def __init__(self, numero: str, titular: str, saldo:float = 0.0, limite: float =1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    @abc.abstractmethod
    def atualizar(self, taxa: float):
        pass
    
    
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular: str):
        self._titular = titular
    
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero: str):
        self._numero = numero
        
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo(self, saldo: float):
        self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite
    
    
    def depositar(self, valor: float):
        
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor: float):
        
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")

    def __str__(self):
        return 'Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)

class ContaCorrente(Conta):
    
    def atualizar(self, taxa: float):
        self._saldo += self._saldo * taxa * 2
        return self._saldo
    
    def __str__(self):
       return 'CONTA CORRENTE: Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)

class ContaPoupanca(Conta):
    
    def atualizar(self, taxa: float):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
    
    def __str__(self):
        return 'CONTA POUPANCA: Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)
    
    
class ContaInvestimento(Conta):
    
    def atualizar(self, taxa: float):
        self._saldo += self._saldo * taxa * 5
        return self._saldo
    
    def __str__(self):
        return 'CONTA INVESTIMENTO: Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)




if __name__ == '__main__':
    Conta_corrente = ContaCorrente('123-4', 'Joao', 1000, 2000)
    Conta_poupanca = ContaPoupanca('123-5', 'Jose', 1000, 2000)
    Conta_investimento = ContaInvestimento('123-6', 'Maria', 1000, 2000)

    Conta_corrente.atualizar(0.01)
    Conta_poupanca.atualizar(0.02)
    Conta_investimento.atualizar(0.05)
    Conta_investimento.depositar(1000)
    print(Conta_investimento._saldo)

    print(Conta_corrente._saldo)
    print(Conta_poupanca._saldo)
    print(Conta_investimento._saldo)

    contas = [Conta_corrente, Conta_poupanca, Conta_investimento]
    
    for conta in contas:
        print(conta)