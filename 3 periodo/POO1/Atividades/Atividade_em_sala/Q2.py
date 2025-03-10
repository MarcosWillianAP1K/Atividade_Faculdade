class Carro:
    
    def __init__(self, modelo:str, ano:int, placa:str, emprestao:bool = False):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.emprestado = emprestao
        
        
    def exibir_dados(self):
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Placa: {self.placa}')
        print(f'Emprestado: {self.emprestado}\n')
        
        
        

class Emprestimo:
    
    def __init__(self, carros:list):
        self.carros = {}
        self.pessoas = {}
        
        for carro in carros:
            self.carros[carro.placa] = carro
            
    
    def adicionar_emprestimo(self, carro:Carro, pessoa:str):
        placa = carro.placa
        
        if self.carros[placa].emprestado == False:
            self.carros[placa].emprestado = True
            
            if pessoa in self.pessoas:
                self.pessoas[pessoa].append(placa)
            else:
                self.pessoas[pessoa] = [placa]
            
        else:
            print("Carro já emprestado")
        
        
    def devolver_carro(self, carro:Carro, pessoa:str):
        
        placa = carro.placa
        
        if pessoa in self.pessoas:
            if placa in self.pessoas[pessoa]:
                self.pessoas[pessoa].remove(placa)
                self.carros[placa].emprestado = False
        else:
            print("Pessoa não possui carro emprestado")
            
            
    def listar_carros(self):
        for carro in self.carros.values():
            carro.exibir_dados()
            print()
    
    def listar_pessoas(self):
        for pessoa, carros in self.pessoas.items():
            print(f'Pessoa: {pessoa}')
            print(f'Carros emprestados: {carros}\n')
    
    
        
carro1 = Carro("Fusca", 1970, "ABC-1234")
carro2 = Carro("Celta", 2005, "DEF-5678")
carro3 = Carro("Gol", 2010, "GHI-9101")

emprestimo = Emprestimo([carro1, carro2, carro3])

emprestimo.adicionar_emprestimo(carro1, "Joao")

print("Carros emprestados")
emprestimo.listar_carros()

emprestimo.listar_pessoas()


emprestimo.devolver_carro(carro1, "Joao")

print("Carros emprestados")
emprestimo.listar_carros()

emprestimo.listar_pessoas()