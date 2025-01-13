"""
    O decorador property é uma forma de criar métodos de acesso a atributos de uma classe, sem a necessidade de criar métodos get e set para cada atributo.
"""


class Produto:
    
    def __init__(self, nome:str, preco:float):
        self._nome = nome
        self._preco = preco
        
        
    @property    
    def Preco(self):
        return self._preco
    
    
    @Preco.setter
    def Preco(self, novo_preco):
        
        if novo_preco < 0:
            print("Valor invalido")
        
        else:
            self._preco = novo_preco    
            
            
    def Exibir_infos(self):
        print(f"Nome: {self._nome}\nPreço: {self._preco}")
        
    
    

produto_teste = Produto("tangerina", 25.50)

produto_teste.Exibir_infos()

print("preco get:", produto_teste.Preco)

produto_teste.Precoreco = 15.50

produto_teste.Exibir_infos()


        