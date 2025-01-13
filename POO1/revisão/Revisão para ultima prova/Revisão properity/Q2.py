class Funcionario:
    
    def __init__(self, salario:float):
        self._salario = salario
        
    
    @property
    def Salario(self):
        return self._salario
    
    @Salario.setter
    def Salario(self, novo_salario:float):
        
        if novo_salario < 0:
            raise ValueError("Valor negativo")
                
        elif novo_salario < 1500:
            raise ValueError("Menos que o salario minimo")
            
        else:
            self._salario = novo_salario
            
            
pedrim = Funcionario(2000)

print(pedrim.Salario)

try:
    pedrim.Salario = 1000
    
except ValueError as e:
    print(e)
    
try:
    pedrim.Salario = 2500
    
except ValueError as e:
    print(e)

print(pedrim.Salario)

    