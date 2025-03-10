import abc

class Pagamento(abc.ABC):
    """Interface para classes de pagamento."""

    @abc.abstractmethod
    def autorizar(self):
        """Valida os dados do pagamento."""
        pass

    @abc.abstractmethod
    def processar_pagamento(self):
        """Realiza o processamento do pagamento."""
        pass


class CartaoCredito(Pagamento):
    """Implementação da interface Pagamento para Cartão de Crédito."""
    
    def __init__(self, numero_cartao: str):
        self.numero_cartao = numero_cartao

    def autorizar(self):
        """Valida se o número do cartão possui 16 dígitos."""
        if len(self.numero_cartao) == 16 and self.numero_cartao.isdigit():
            print("Cartão de crédito autorizado.")
            return True
        else:
            raise ValueError("Número do cartão inválido. Deve conter 16 dígitos numéricos.")

    def processar_pagamento(self):
        """Realiza o processamento do pagamento via cartão de crédito."""
        print("Pagamento processado com cartão de crédito.")


class Pix(Pagamento):
    """Implementação da interface Pagamento para Pix."""
    
    def __init__(self, chave_pix: str):
        self.chave_pix = chave_pix

    def autorizar(self):
        """Valida se a chave Pix é uma string não vazia."""
        if isinstance(self.chave_pix, str) and self.chave_pix.strip():
            print("Chave Pix autorizada.")
            return True
        else:
            raise ValueError("Chave Pix inválida. Deve ser uma string válida e não vazia.")

    def processar_pagamento(self):
        """Realiza o processamento do pagamento via Pix."""
        print("Pagamento processado via Pix.")


# Demonstração do uso
def demonstrar_pagamento(pagamento: Pagamento):
    try:
        if pagamento.autorizar():
            pagamento.processar_pagamento()
    except ValueError as e:
        print(f"Erro: {e}")

# Criando objetos de CartaoCredito e Pix
cartao = CartaoCredito("1234567890123456")  # Número válido
pix = Pix("minha_chave_pix")  # Chave Pix válida

# Testando os pagamentos
print("Teste com Cartão de Crédito:")
demonstrar_pagamento(cartao)

print("\nTeste com Pix:")
demonstrar_pagamento(pix)

# Testando com entradas inválidas
print("\nTeste com Cartão de Crédito Inválido:")
cartao_invalido = CartaoCredito("1234567890")
demonstrar_pagamento(cartao_invalido)

print("\nTeste com Pix Inválido:")
pix_invalido = Pix("")
demonstrar_pagamento(pix_invalido)
