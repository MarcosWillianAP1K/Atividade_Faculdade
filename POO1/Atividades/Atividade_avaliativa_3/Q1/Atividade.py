import datetime



class pessoa:
    
    def __init__(self):
        
        self._nome = ""
        self._data_nascimento = "00/00/0000"
        self._altura = 0.0
    
    

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome = None):
         
        if novo_nome == None:
            novo_nome = input("Digite um nome: ")
        
        if novo_nome != "":
            self._nome  = novo_nome
        else:
            print("\nNome vazio\n")
    
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, nova_altura = None):
        if nova_altura == None:
            nova_altura = input("Digite altura: ")
            
        try:
            nova_altura = float(nova_altura)
            
            if nova_altura != 0:
                self._altura  = nova_altura
            else:
                print("\nAltura invalida\n")
        
        except:
            print("\nAltura invalida\n")
            
    
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data = None):
        
        if nova_data == None:
            nova_data = input("Digite a data de nascimento (DD/MM/AAAA): ")
        try:
            data = datetime.datetime.strptime(nova_data, "%d/%m/%Y")
            data_atual = datetime.datetime.now()
            
            if not data > data_atual:
                self._data_nascimento = nova_data
        except ValueError:
            print("\nData inválida\n")
            
            
    
    def calcular_idade(self):
        if self._data_nascimento == "00/00/0000" or self._data_nascimento == "":
            return 0
        
        
        data = datetime.datetime.strptime(self._data_nascimento, "%d/%m/%Y")
        
        data_atual = datetime.datetime.now()
        idade = data_atual.year - data.year
        
        if data_atual.month < data.month or (data_atual.month == data.month and data_atual.day < data.day):
            idade -= 1
        
        return idade        
    
            
    def imprimir_pessoa(self):
        print(f"Nome: {self._nome}\nData nascimento: {self._data_nascimento}\nAltura: {self._altura}\nIdade: {self.calcular_idade()}\n")
        


p = pessoa()

p.imprimir_pessoa()

p.nome = "Marcos"
p.data_nascimento = "18/05/2004"
p.altura = 1.75

p.imprimir_pessoa()
