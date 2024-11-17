import random
import time

contas_armazenadas = {}

class Conta:
    
    def __init__(self, carteira: float, titular: str, data_criação: str = time.ctime()):
        self.carteira = carteira
        self.titular = titular
        self.data_criação = data_criação
        self.historico = []


        
    def Historico(self, data, operação, valor):
        self.historico.append(f"{data}\nTipo:{operação}\nValor: {valor}\n")
        
        
    def Depositar(self, quanto):
        
        try:
            quanto = float(quanto)
            self.carteira += quanto 
            return True
        
        except ValueError:
            print("Valor inválido\n")
            return False
        
        
    def Sacar(self, quanto):
        try:
            quanto = float(quanto)
            
            if quanto > self.carteira:
                print("saldo insuficiente\n")
                return False
            else:
                self.carteira -= quanto
                return True
        
        except ValueError:
            print("Valor inválido\n")
            return False
            
        
       
    
    
    
    
    def Printar_saldo(self):
        return self.carteira
    
    def Printar_titular(self):
        return self.titular
    
    def Printar_data_criação(self):
        return self.data_criação
    
    def Printar_data_criação(self):
        return self.data_criação
    
    def Printar_historico(self):
        return self.historico
    








def criar_num_conta():
    while True:
        num = ""
        
        i = 0
        while i < 3:
            num = num + str(random.randint(0, 9))
            i += 1
        
        if num not in contas_armazenadas:
            return num


def selecionar_conta():
    num_conta = input("Digite o numero da conta: ")
    
    if num_conta in contas_armazenadas:
        return num_conta
    else:
        print("Conta não encontrada\n")
        return None


def add_historico(conta: Conta, data, operação, valor):
    contas_armazenadas[conta].Historico(data, operação, valor)





def criar_conta():
    nome = input("Digite o nome do titular: ")
    contas_armazenadas[criar_num_conta()] = Conta(0, nome)
    
    print("Conta criada com sucesso\n")


def listar_contas():
    for i in contas_armazenadas:
        print("Numero da conta: ", i)
        print("Titular: ", contas_armazenadas[i].Printar_titular())
        print("Saldo: ", contas_armazenadas[i].Printar_saldo())
        print()

    if len(contas_armazenadas) == 0:
        print("Nenhuma conta cadastrada\n")
        
    print()


def sacar():
    
    conta = selecionar_conta()
    valor = input("Digite o valor a ser sacado: ")
    
    if contas_armazenadas[conta].Sacar(valor) == True:
        print("Saque realizado com sucesso\n")
        add_historico(conta, time.ctime(), "Saque", valor)
    

def depositar():
    conta = selecionar_conta()
    valor = input("Digite o valor a ser depositado: ")
    
    if contas_armazenadas[conta].Sacar(valor) == True:
        print("Deposito realizado com sucesso\n")
        add_historico(conta, time.ctime(), "Deposito", valor)

    
def tranferir():
    print("Selecione a conta de origem e a conta de destino respectivamente")
    conta_origem = selecionar_conta()
    
    if conta_origem == None:
        return
    
    conta_destino = selecionar_conta()
    
    if conta_destino == None:
        return
    
    try:
        valor = float(input("Digite o valor a ser transferido: "))
        
        operação = contas_armazenadas[conta_origem].Sacar(valor)
        
        if operação != False:
            contas_armazenadas[conta_destino].Depositar(valor)
        
        
        print("Transferência realizada com sucesso\n")
        
        add_historico(conta_origem, time.ctime(), "Transferência enviada", valor)
        add_historico(conta_destino, time.ctime(), "Transferência recebida", valor)
    except ValueError:
        print("Valor inválido\n")


def printar_saldo():
    print("Saldo: ", contas_armazenadas[selecionar_conta()].Printar_saldo())


def printar_historico():
    conta = selecionar_conta()
    
    if conta == None:
        return
    
    print("Data de criação:", contas_armazenadas[conta].Printar_data_criação(), end="\n\n")
    
    for i in contas_armazenadas[conta].Printar_historico():
        print(i, end="\n\n")
    
        
def excluir_conta():
    conta = selecionar_conta()
    
    if conta != None:
        del contas_armazenadas[conta]
        print("Conta excluída com sucesso\n")

        


    
def menu():
    
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
        print()
        
        if escolha == "1":
            criar_conta()
            
        elif escolha == "2":
            listar_contas()
            
        elif escolha == "3":
            sacar()
            
        elif escolha == "4":
            depositar()
            
        elif escolha == "5":
            tranferir()
        
        elif escolha == "6":
            printar_saldo()
        
        elif escolha == "7":
            printar_historico()
            
        
        elif escolha == "8":
            excluir_conta()
        
        elif escolha == "9":
            break
        
        else:
            print("Escolha inválida\n")
            
        print()



        
def teste():
    carteira_teste = Conta(0, "teste")
    carteira_teste.Depositar(1000)
    conta = criar_num_conta()
    contas_armazenadas.update({conta: carteira_teste})
    add_historico(conta, time.ctime(), "Deposito", 1000)
    
    # print(conta)
    # printar_historico()
        

        
teste()

menu()
            