import os


class ELEVADOR:
    
    def __init__(self, quant_andares:int, cap_maxima:int):
        self._andar_atual = 0
        self._quant_andares = quant_andares
        self._cap_maxima = cap_maxima
        self._quant_atual = 0
      
        
    def estado_atual(self):
        print(f"Andares max: {self._quant_andares}\nCap max: {self._cap_maxima}")
        print(f"Passageiros atual: {self._quant_atual}\nAndar atual: {self._andar_atual}\n")
    
    
    
    def menu(self):
        self.estado_atual()
            
        print("1. Subir")
        print("2. Descer")
        print("3. Entrar")
        print("4. Sair")
        print("5. Sair do programa")
            
        opcao = input("Escolha uma opção: ") 
            
        return opcao
            
        
    
    
    @property
    def subir(self):
        pass
    
    @subir.setter
    def subir(self, quantos:int):
        
        if quantos > 0 and self._andar_atual + quantos <= self._quant_andares:
            self._andar_atual += quantos
        else:
            print("Invalido\n")
            
            
    @property
    def descer(self):
        pass
    
    @descer.setter
    def descer(self, quantos:int):
        
        if quantos > 0 and self._andar_atual - quantos >= 0:
            self._andar_atual -= quantos
        else:
            print("Invalido\n")
            
    
    @property
    def entrar(self):
        pass
    
    @entrar.setter
    def entrar(self, quantos:int):
        
        if quantos > 0 and self._quant_atual + quantos <= self._cap_maxima:
            self._quant_atual += quantos
        else:
            print("Invalido\n")
            
    
    @property
    def sair(self):
        pass
    
    @sair.setter
    def sair(self, quantos:int):
        
        if quantos > 0 and self._quant_atual - quantos >= 0:
            self._quant_atual -= quantos
        else:
            print("Invalido\n")


def limpar_terminal():
        # Para Windows
        if os.name == 'nt':
            os.system('cls')
        # Para Mac e Linux
        else:
            os.system('clear')

def pausar():
        # Para Windows
        if os.name == 'nt':
            os.system('pause')
        # Para Mac e Linux
        else:
            os.system('read -p "Pressione enter para continuar"') 



def main():
    
    # inicia com a capacidade maxima e quantos andares
    elevador = ELEVADOR(10, 5)

    while True:
        limpar_terminal()

        opcao = elevador.menu()
        
        try:
            if opcao == '1':
                quantos = int(input("Quantos andares deseja subir?: "))
                elevador.subir = quantos 
                
            elif opcao == '2':
                quantos = int(input("Quantos andares deseja descer?: "))
                elevador.descer = quantos
                
            elif opcao == '3':
                quantos = int(input("Quantas pessoas irão entrar?: "))
                elevador.entrar = quantos  
                    
            elif opcao == '4':
                quantos = int(input("Quantas pessoas irão sair?:"))
                elevador.sair = quantos
                        
            elif opcao == '5':
                print("Saindo do programa...\n")
                break
            else:
                print("Opção inválida!")
                
        except:
            print("Num digitado invalido")
            
        print("\n")
        pausar()
        
        
        
main()
