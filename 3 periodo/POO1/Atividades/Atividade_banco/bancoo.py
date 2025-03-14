import random
import time
import os


# Os parametros com "= none", é para eu poder poder testar, ja mandando valores direto inves de ficar escrevendo.


class Conta:
    
    
    def __init__(self, carteira: float, titular: str, data_criação: str = time.ctime()):
        self._carteira = carteira
        self._titular = titular
        self._data_criação = data_criação
        self._historico = []


    @property
    def Historico(self):
        return self._historico
    
    @Historico.setter
    def Historico(self, registro):
        self._historico.append(registro)
    
    
    @property
    def Saldo(self):
        return self._carteira
    

    @property
    def Depositar():
        pass
    
    
    @Depositar.setter
    def Depositar(self, quanto: float):
        self._carteira += float(quanto)
                
        
    @property
    def Sacar():
        pass
        
        
    @Sacar.setter
    def Sacar(self, quanto: float):
        self._carteira -= float(quanto)
                   
        
    @property
    def Titular(self):
        return self._titular
    
    @property
    def Data_criação(self):
        return self._data_criação
    
    



class Banco:
    
    def __init__(self):
        self._contas_armazenadas = {}
        
    
    @property
    def contas(self):
        return self._contas_armazenadas
    
    
    def criar_num_conta(self):
        while True:
            num = ""
            
            for _ in range(3):
                num = num + str(random.randint(0, 9))
                
            
            if num not in self._contas_armazenadas:
                return num


    @property
    def criar_conta(self):
        num_conta = self.criar_num_conta()
        self._contas_armazenadas[num_conta] = Conta(0, "teste")
        return num_conta
    
    
    @criar_conta.setter
    def criar_conta(self, nome=None):
        if nome == None:
            nome = input("Digite o nome do titular: ")
        
        num_conta = self.criar_num_conta()
        self._contas_armazenadas[num_conta] = Conta(0, nome)
        
        print("Conta criada com sucesso\n")
        
        
    def selecionar_conta(self):
        num_conta = input("Digite o numero da conta: ")
        
        if num_conta in self._contas_armazenadas:
            return num_conta
        else:
            print("Conta não encontrada\n")
            return None


    def add_historico(self, conta, data, operação, valor):
        self._contas_armazenadas[conta].Historico = (f"{data}\nTipo:{operação}\nValor: {valor}\n")


    def listar_contas(self):
        for i in self._contas_armazenadas:
            print("Numero da conta: ", i)
            print("Titular: ", self._contas_armazenadas[i].Titular)
            print("Saldo: ", self._contas_armazenadas[i].Saldo)
            print()

        if len(self._contas_armazenadas) == 0:
            print("Nenhuma conta cadastrada\n")
            
        print()

    
    def validar_valor(self, num_conta, tipo, valor):
        try:
            valor = float(valor)
                    
            if valor > self._contas_armazenadas[num_conta].Saldo and tipo == "S":
                    print("Saldo insuficiente\n")
            elif valor <= 0:
                        print("Valor inválido\n")
            else:
                return True
                    
        except ValueError:
            print("Valor inválido\n")
        return False
    

    def sacar(self, num_conta=None, valor=None):
        
        if num_conta is None:
            num_conta = self.selecionar_conta()
        
        if valor is None and num_conta != None:
            valor = input("Digite o valor a ser sacado: ")
        
        if num_conta != None and valor != None:
            
            if self.validar_valor(num_conta, "S", valor):
                
                self._contas_armazenadas[num_conta].Sacar = valor
                print("Saque realizado com sucesso\n")
                self.add_historico(num_conta, time.ctime(), "Saque", valor)
                            

    def depositar(self, num_conta=None, valor=None):
        
        if num_conta == None:
            num_conta = self.selecionar_conta()
            
        if valor == None and num_conta != None:
            valor = input("Digite o valor a ser depositado: ")
        
        if num_conta != None and valor != None:
            
            if self.validar_valor(num_conta, "D", valor):
                self._contas_armazenadas[num_conta].Depositar = valor
                print("Deposito realizado com sucesso\n")
                self.add_historico(num_conta, time.ctime(), "Deposito", valor)
                
    
    def tranferir(self,  conta_origem=None, conta_destino=None, valor=None):
         
        if conta_origem == None:
            print("Selecione a conta de origem e a conta de destino respectivamente")
            conta_origem = self.selecionar_conta()
        
        
        if conta_destino == None and conta_origem != None:
            conta_destino = self.selecionar_conta()
        
        
        if valor == None and conta_origem != None and  conta_destino != None:
            valor = input("Digite o valor a ser transferido: ")
            
        
        if  conta_origem != None and  conta_destino != None and valor != None: 
                
            if self.validar_valor(conta_origem, "S", valor):
                self._contas_armazenadas[conta_origem].Sacar = valor
                self._contas_armazenadas[conta_destino].Depositar = valor
            
                print("Transferência realizada com sucesso\n")
                    
                self.add_historico(conta_origem, time.ctime(), "Transferência enviada", valor)
                self.add_historico(conta_destino, time.ctime(), "Transferência recebida", valor)
                

    def printar_saldo(self, num_conta=None):
        if num_conta == None:
            num_conta = self.selecionar_conta()
        print("Saldo: ", self._contas_armazenadas[num_conta].Saldo)


    def printar_historico(self, num_conta=None):
        if num_conta == None:
            num_conta = self.selecionar_conta()
        
        if num_conta == None:
            return
        
        print("Data de criação: ", self._contas_armazenadas[num_conta].Data_criação, end="\n\n")
        
        for i in self._contas_armazenadas[num_conta].Historico:
            print(i, end="\n\n")


    @property
    def excluir_conta():
        pass
    
    
    @excluir_conta.setter
    def excluir_conta(self, num_conta=None):
        if num_conta is None:
            num_conta = self.selecionar_conta()
        
        if num_conta != None:
            del self._contas_armazenadas[num_conta]
            print("Conta excluída com sucesso\n")

        
        
banco = Banco()

def teste():
    num_conta = banco.criar_conta
    banco.depositar(num_conta, 1000)

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
    
    

def menu():
    teste() 
    
    limpar_terminal()
    
    while True:
        print("1 - Criar conta")
        print("2 - Listar contas")
        print("3 - Sacar")
        print("4- Depositar")
        print("5- Transferir")
        print("6 - Ver saldo")
        print("7 - Historico")
        print("8 - Excluir conta")
        print("9 - Sair")
        
        escolha = input("Escolha: ")
        limpar_terminal()
        
        
        if escolha == "1":
            banco.criar_conta = None
            
        elif escolha == "2":
            banco.listar_contas()
            
        elif escolha == "3":
            banco.listar_contas()
            banco.sacar()
            
        elif escolha == "4":
            banco.listar_contas()
            banco.depositar()
            
        elif escolha == "5":
            banco.listar_contas()
            banco.tranferir()
        
        elif escolha == "6":
            banco.listar_contas()
            banco.printar_saldo()
        
        elif escolha == "7":
            banco.listar_contas()
            banco.printar_historico()
        
        elif escolha == "8":
            banco.listar_contas()
            banco.excluir_conta = None
        
        elif escolha == "9":
            break
        
        else:
            print("Escolha inválida\n")
            
            
        pausar()
        limpar_terminal()




menu()
            