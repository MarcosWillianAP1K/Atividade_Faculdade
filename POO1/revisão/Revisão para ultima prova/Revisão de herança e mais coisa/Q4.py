import abc

class Animal(abc.ABC):
    
    @abc.abstractmethod
    def falar(self):
        pass
    
    @abc.abstractmethod
    def mover(self):
        pass
    
    
class Cachorro(Animal):
    
    def falar(self):
        return "Au Au"
    
    def mover(self):
        return "Corre"
    
    
class Passaro(Animal):
    
    def falar(self):
        return "Piu piu"
    
    def mover(self):
        return "Voa"
    
    
passaro = Passaro()

cachorro = Cachorro()
        
print(cachorro.mover(), cachorro.falar())
print(passaro.falar(), passaro.mover())