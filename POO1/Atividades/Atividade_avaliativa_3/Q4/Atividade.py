import os


class TELEVISAO:
    
    def __init__(self, canais:list[str]):
        self._volume = 0
        self._canais = canais
        self._canal_atual = 0
        
    
    def imprimir_tv(self):
        print(f"Volume: {self._volume}\nCanal {self._canal_atual+1}: {self._canais[self._canal_atual]}\n")
    
    
    @property
    def canais(self):
        return self._canais
    
    
    @property
    def remover_canal(self):
        pass
    
    
    @remover_canal.setter
    def remover_canal(self, nome:str):
        
        if nome in self._canais:
            del self._canais[self._canais.index(nome)]
        else:
            print("Canal não encontrado\n")
        
    
    
    @property
    def adicionar_canal(self):
        pass
    
    @adicionar_canal.setter
    def adicionar_canal(self, nome:str):
        
        if nome not in self._canais:
            del self._canais[self._canais.index(nome)]
        else:
            print("Canal ja existe\n")
    
    
      
    @property
    def aumentar_volume(self):
        pass
    
    @aumentar_volume.setter
    def aumentar_volume(self, quant:float):
        
        if quant >= 0:
            if quant + self._volume > 100:
                self._volume = 100
            else:
                self._volume += quant
        else:
            print("Invalido\n")
                

    @property
    def diminuir_volume(self):
        pass
    
    @diminuir_volume.setter
    def diminuir_volume(self, quant:float):
        
        if quant >= 0:
            if self._volume - quant < 0:
                self._volume = 0
            else:
                self._volume -= quant
        else:
            print("Invalido\n")
                
    
    @property
    def selecionar_canal_num(self):
        pass
    
    @selecionar_canal_num.setter
    def selecionar_canal_num(self, num:int):
        
        if num > 0:
            try:
                self._canais[num - 1] 
                self._canal_atual = num - 1
                
            except:
                print("Não existe esse canal\n")
        else:
            print("Não existe esse canal\n")
            
            
            
    @property
    def selecionar_canal_nome(self, ):
        pass
    
    @selecionar_canal_nome.setter
    def selecionar_canal_nome(self, nome:str):
        
        if nome in self._canais:
            self._canal_atual = self._canais.index(nome)
        else:
            print("Não existe\n")
            
            
    @property
    def passar_frente_tras(self):
        pass
    
    @passar_frente_tras.setter
    # True para frente, False para tras
    def passar_frente_tras(self, frenteEtras:bool):
    
        if frenteEtras:
            # caso esteja no ultimo canal, vamos pro primeiro, pra fazer um loop
            if self._canal_atual + 1 > len(self._canais) - 1:
                self._canal_atual = 0
            else:
                self._canal_atual += 1
                
        else:
            # o inverso se aplica aqui
            if self._canal_atual - 1 < 0:
                self._canal_atual = len(self._canais) - 1
            else:
                self._canal_atual -= 1
    

class CONTROLE_REMOTO:
    
    def __init__(self, tv_controlada : TELEVISAO):
        self._tv = tv_controlada

    
    
    
    
    def aumentar_volume(self):
        try:
            self._tv.aumentar_volume = int(input("Quanto aumentar?: "))
            print()
        except:
            print("Invalido\n")
    
    
    def diminuir_volume(self):
        try:
            self._tv.diminuir_volume = int(input("Quanto diminuir?: "))
            print()
        except:
            print("Invalido\n")
    
    
    def selecionar_canal(self):
        
        print("1. Selecionar canal por número")
        print("2. Selecionar canal por nome")
        escolha = input("Escolha uma opção: ")
        print()
        
        try:
            if escolha == '1':
                self._tv.selecionar_canal_num = int(input("Digite o numero do canal: "))
                
            elif escolha == '2':
                self._tv.selecionar_canal_nome = input("Digite o nome do canal: ")
                
            else:
                print("Opção inválida")
                
        except:
            print("Opção inválida")
    
    
    def trocar_canal(self):
        
        print("1. Frente")
        print("2. Tras")
        escolha = input("Escolha uma opção: ")
        print()
        
        
        if escolha == '1':
            self._tv.passar_frente_tras = True
                
        elif escolha == '2':
            self._tv.passar_frente_tras = False
                
        else:
            print("Opção inválida")
                

    def opções(self, opcao:str):
        print()
        
        if opcao == '1':
                self.aumentar_volume()
            
        elif opcao == '2':
                self.diminuir_volume()
            
        elif opcao == '3':
                self.trocar_canal()
            
        elif opcao == '4':
                self.selecionar_canal()
            
        elif opcao == '5':
                print("Saindo...")
                return True
            
        else:
                print("Opção inválida")
                
        return False
    
    
    
    def menu(self):
        
        while True:
            self.limpar_terminal()
            
            self._tv.imprimir_tv()
            
            print("1. Aumentar Volume")
            print("2. Diminuir Volume")
            print("3. Trocar de Canal")
            print("4. Selecionar Canal")
            print("5. Sair")
            
            if self.opções(input("Escolha uma opção: ")):
                break
            self.pausar()
            
    
    def limpar_terminal(self):
        # Para Windows
        if os.name == 'nt':
            os.system('cls')
        # Para Mac e Linux
        else:
            os.system('clear')

    def pausar(self):
            # Para Windows
            if os.name == 'nt':
                os.system('pause')
            # Para Mac e Linux
            else:
                os.system('read -p "Pressione enter para continuar"') 

            
            


tv = TELEVISAO(["Record", "SBT", "BAND", "GLOBO"])
controle = CONTROLE_REMOTO(tv)

controle.menu()