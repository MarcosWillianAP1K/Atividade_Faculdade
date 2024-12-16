class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo_inicial):
        self._titular = titular
        self._numero_conta = numero_conta
        self._saldo = saldo_inicial

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        self._titular = novo_titular
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @numero_conta.setter
    def numero_conta(self, novo_numero):
        self._numero_conta = novo_numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def realizar_deposito(self, valor):
        self._saldo += valor

    def realizar_saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print('Saldo insuficiente para saque.')

    def aplicar_taxa(self, taxa):
        self._saldo += self._saldo * taxa

    def __str__(self):
        return f'Titular: {self._titular}, Conta: {self._numero_conta}, Saldo: R$ {self._saldo:.2f}'


class ContaCorrente(ContaBancaria):
    def aplicar_taxa(self, taxa):
        super().aplicar_taxa(taxa * 2)

    def realizar_deposito(self, valor):
        super().realizar_deposito(valor - 0.10)


class ContaPoupanca(ContaBancaria):
    def aplicar_taxa(self, taxa):
        super().aplicar_taxa(taxa * 3)


class GestorDeContas:
    def __init__(self, taxa_juros, saldo_total=0):
        self._taxa_juros = taxa_juros
        self._saldo_total = saldo_total

    @property
    def taxa_juros(self):
        return self._taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, nova_taxa):
        self._taxa_juros = nova_taxa

    @property
    def saldo_total(self):
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self, novo_saldo_total):
        self._saldo_total = novo_saldo_total

    def processar_contas(self, contas):
        for conta in contas:
            print(f'Saldo inicial da conta: {conta.saldo}')
            conta.aplicar_taxa(self._taxa_juros)
            self._saldo_total += conta.saldo
            print(f'Saldo total atualizado: R$ {self._saldo_total:.2f}')


if __name__ == '__main__':
    conta_corrente_jose = ContaCorrente('José', '101-11', 1500)
    conta_poupanca_ana = ContaPoupanca('Ana', '202-22', 2000)
    
    contas_lista = [conta_corrente_jose, conta_poupanca_ana]
    gestor_contas = GestorDeContas(0.02)
    gestor_contas.processar_contas(contas_lista)

    conta_corrente_jose.realizar_deposito(300)
    conta_poupanca_ana.realizar_deposito(300)

    conta_corrente_jose.realizar_saque(100)
    conta_poupanca_ana.realizar_saque(100)

    conta_corrente_jose.aplicar_taxa(0.02)
    conta_poupanca_ana.aplicar_taxa(0.02)

    print(conta_poupanca_ana)