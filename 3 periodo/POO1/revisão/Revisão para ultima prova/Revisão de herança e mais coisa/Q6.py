class A:
    def mostrar(self):
        print("Classe A")

class B:
    def mostrar(self):
        print("Classe B")

class C:
    def mostrar(self):
        print("Classe C")

class D(B, C):  # D herda de B e C
    pass

class E(C, A):  # E herda de C e A
    pass

class F(D, E):  # F herda de D e E
    pass

# Criando um objeto da classe F
objeto = F()

# Chamando o método mostrar()
objeto.mostrar()

# Exibindo o MRO da classe F
print("\nOrdem de Resolução de Métodos (MRO):")
print(F.mro())

# Outra forma de visualizar o MRO usando help()
print("\nAjuda sobre a classe F:")
help(F)
