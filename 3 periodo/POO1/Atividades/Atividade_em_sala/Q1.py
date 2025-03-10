class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        
class Estudante (Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
        
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Curso: {self.curso}')
        
pessoa1 = Pessoa("joao", 20)
pessoa1.exibir_dados()

estudante1 = Estudante("maria", 22, "Engenharia")
estudante1.exibir_dados()


"""
    Apesar que em teoria o codigo não atende as boas praticas de utilziar o super() para chamar o construtor da classe pai, o codigo está correto e funcionando.
    
    Exemplo de como poderia ser feito: 
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f'Curso: {self.curso}')
        
"""