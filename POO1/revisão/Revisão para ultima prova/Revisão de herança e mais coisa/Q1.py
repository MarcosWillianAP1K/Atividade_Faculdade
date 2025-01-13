class Veiculo:
    
    def __init__(self, marca: str, ano: int):
        self._marca = marca
        self._ano = ano
        
    
    def Exibir_info(self):
        print(f"Marca: {self._marca}\nAno: {self._ano}")
        
        

class Carro(Veiculo):
    
    def __init__(self, marca:str, ano:int, nome:str, portas:int):
        super().__init__(marca, ano)
        self._nome = nome
        self._portas = portas
        
    
    
    def Exibir_info(self):
        print(f"Nome: {self._nome}")
        super().Exibir_info()
        print(f"Quant portas: {self._portas}")
        
        
carro_ne = Carro("vodizvagem", 2500, "Relanpagu marquinhos", 3)

carro_ne.Exibir_info()
        
        