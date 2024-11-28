import datetime



class PESSOA:
    
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
            print("\nAltura invalida")
            
    
    
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
        

class AGENDA:
    
    def __init__(self, quant_maxima:int):
        self._pessoas = []
        self._quant = quant_maxima
    
    
    def validar_nome(self, nome:str):
        for pessoa in self._pessoas:
            if pessoa.nome == nome:
                print("Nome ja existe")
                return False
        return True
    
    
    def imprimir_agenda(self):
        
        if self._pessoas != []:
            for i in self._pessoas:
                i.imprimir_pessoa()
        else:
            print("Agenda vazia\n")
    
    
    def buscar(self, nome:str):
        if self._pessoas != []:
            for i in self._pessoas:
                
                if i.nome == nome:
                    i.imprimir_pessoa()
                    return 
        else:
            print("Agenda vazia\n")
    
    @property
    def armazernar(self):
        return self._pessoas
    
    @armazernar.setter
    def armazernar(self, quant:int):
        
        if((len(self._pessoas) + quant) <= self._quant):
            
            while(quant > 0):
                
                try:
                    pessoa = PESSOA()
                    
                    pessoa.nome = None
                    
                    if(self.validar_nome(pessoa.nome) and pessoa.nome != ""):
                        pessoa.data_nascimento = None
                        
                        if pessoa.data_nascimento != "00/00/0000":
                            pessoa.altura = None

                            if pessoa.altura != 0:
                                self._pessoas.append(pessoa)
                                quant -= 1
                except:
                    continue
                print("\n")
        else:
            print("Armazenamento cheio")
    
    
    @property
    def remover(self):
        pass
    
    @remover.setter
    def remover(self, nome:str):
        for pessoa in self._pessoas:
            if pessoa.nome == nome:
                self._pessoas.remove(pessoa)
                print(f"{nome} removido da agenda.\n")
                return
        print(f"{nome} não encontrado na agenda.\n")
    
    
            
        
    
    
    
    
agenda = AGENDA(10)

agenda.armazernar = 1
agenda.remover = "marcos"
agenda.imprimir_agenda()
print()
agenda.buscar("teste")


