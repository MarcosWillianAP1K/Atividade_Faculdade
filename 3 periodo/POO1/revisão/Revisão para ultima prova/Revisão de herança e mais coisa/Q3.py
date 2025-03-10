import math as m


class Forma:
    
    def area(self):
        return 0
    
    
class Circulo(Forma):
    
    def __init__(self, raio:float):
        self._raio = raio
        
    @property
    def area(self):
        return m.pi * (self._raio**2)
    
class Retangulo(Forma):
    
    def __init__(self, altura:float, largura:float):
        self._altura = altura
        self._largura = largura
    
    @property
    def area(self):
        return self._largura * self._altura
    
    


forma1 = Circulo(8)
forma2 = Retangulo(2, 6)

print(forma1.area)
print(forma2.area)


        