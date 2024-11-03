
class Conta:
    
    def __init__(self, carteira) -> float:
        self.carteira = carteira
        
    
    def Depositar(self, quanto) -> float:
        self.carteira += quanto
        
    def Sacar(self, quanto) -> float:
        
        if quanto > self.carteira:
            print("saldo insuficiente\n")
        else:
            self.carteira -= quanto
    
    def Printar_saldo(self):
        print(self.carteira)
    
            
carteira_teste = Conta(100)
contas_armazenadas = {"teste": carteira_teste}





def Menu(conta: Conta):
    
    try:
    
        while True:
            
            print("\n1-Sacar\n2-depositar\n3-extrato\n4-sair")
            opcao = int(input("Opção: "))
            
            if opcao == 1:
                quanto = float(input("Quanto deseja sacar? "))
                conta.Sacar(quanto)
            elif opcao == 2:
                quanto = float(input("Quanto deseja depositar? "))
                conta.Depositar(quanto)
            elif opcao == 3:
                conta.Printar_saldo()
            elif opcao == 4:
                break
            else:
                print("Opção inválida")
        
    
    except:
        print("error")
        
        
def verificar_login_existe(login):
    if login in contas_armazenadas.keys():
        print("Ja existe login")
        return True
    return False
 
        
def criar_conta():
    
    try:
        login = input("crie um login: ")
        
        if verificar_login_existe(login):
            return
        
        valor_inicial = float(input("Deposite um valor inicial: "))
        opcao = int(input("As informações estão corretas? 1-Sim/2-Não : "))
        
        if opcao == 1:
            carteira = Conta(valor_inicial)
            adicionar = {login: carteira}
            contas_armazenadas.update(adicionar)
            print("cadastro finalizado")
        else:
            print("cadastro falhou")
        
    except:
        print("cadastro falhou")
        

def procurar_login():
    
    login = input("Digite o login: ")
    
    if login in contas_armazenadas.keys():
        Menu(contas_armazenadas[login])
    else:
        print("Não existe cadastro com esse login")


def inicio():
    
    while True:
        try:
            
            opcao = int(input("\n1-fazer login\n2-criar conta\n3-sair\nOpção: "))
            
            if opcao == 1:
                procurar_login()
            elif opcao == 2:
                criar_conta()
            elif opcao == 3:
                break
            else:
                print("Opção errada")

        except:
            print("error")
                
                
inicio()               
