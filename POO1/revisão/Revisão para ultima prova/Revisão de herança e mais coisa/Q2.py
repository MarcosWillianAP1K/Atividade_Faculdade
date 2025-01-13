# class Nadador:
#     def nadar(self):
#         print("Estou nadando!")


# class Corredor:
#     def correr(self):
#         print("Estou correndo!")


# class Triatleta(Nadador, Corredor):
#     pass


# # Criando um objeto da classe Triatleta
# atleta = Triatleta()

# # Usando os métodos herdados
# atleta.nadar()
# atleta.correr()


#Exemplo de diamante


class A:
    def falar(self):
        print("Classe A")

class B(A):
    def falar(self):
        print("Classe B")

class C(A):
    def falar(self):
        print("Classe C")

class D(B, C):  # D herda de B e C
    pass

d = D()
d.falar()  # Qual método será chamado?
