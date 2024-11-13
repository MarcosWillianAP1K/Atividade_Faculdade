
def verificar_se_o_nome_existe(nome):
    if nome in Agenda:
        return True
    else:
        return False


def verificar_se_o_ja_telefone_existe(agenda, telefone):

    for i in agenda:
        if telefone in agenda[i]:
            return True
    return False
    

def digitar_nome():
    nome = input("Digite o nome: ")
    return nome
    

def digitar_telefone():
    while True:
        
        telefone = input("Digite o telefone: ")
        
        if len(telefone) != 11 or not telefone.isdigit():
            print("Telefone inválido")
        else:
            return telefone


def Adicionar_telefone(nome, telefone):
    Agenda[nome].append(telefone)


def Adicionar_nome(nome):
    Agenda[nome] = []


def Deseja_adicionar_nome():
    while True:
        print("Deseja Adiciona-lo?\n1-Sim\n2-Não")
        try:
            opcao = int(input())
            
            if opcao == 1:
                return True
                
            elif opcao == 2:
                return False
                
            else:
                print("Opção inválida")
                    
        except:
            print("Opção inválida")


def Excluir_nome_e_telefone(nome):
     del Agenda[nome]


def Qual_telefone_excluir(Lista_com_os_telefones: list) -> None:
    
    print("Selecione um desses telefones para excluir")
    for i in range(len(Lista_com_os_telefones)):
        print(f"{i+1}: {Lista_com_os_telefones[i]}")
        
    while True:   
        try:
            opcao = int(input())
            
            if opcao > 0 and opcao <= len(Lista_com_os_telefones):
                break
            else:
                print("Opção errada")
                
        except:
            print("Opção errada")
            
    del Lista_com_os_telefones[opcao-1]
    
    return Lista_com_os_telefones


def printar_nome_e_telefone(nome):
    print("\nNome: ", nome, "\nTelefones:")
    
    for i in Agenda[nome]:
        print(i)
        
    print()





def Incluir_novo_nome():
    
    nome = digitar_nome()
        
    if verificar_se_o_nome_existe(nome):
        print("Nome já existe\n")
    else:
        telefone = digitar_telefone()
            
        if  verificar_se_o_ja_telefone_existe(Agenda, telefone):
            print("Este telefone ja esta cadastrado na agenda")
        else:
            Adicionar_nome(nome)
            Adicionar_telefone(nome, telefone)
            
        
def Incluir_telefone():
    
    nome = digitar_nome()
    
    if verificar_se_o_nome_existe(nome):
        telefone = digitar_telefone()
        
        if  verificar_se_o_ja_telefone_existe(Agenda, telefone):
            print("Este telefone ja esta cadastrado na agenda")
        else:
            Adicionar_telefone(nome, telefone)
            
    else:
        if Deseja_adicionar_nome():
            Adicionar_nome(nome)
            Adicionar_telefone(nome, digitar_telefone())


def Excluir_telefone():
    
    nome = digitar_nome()
    
    if verificar_se_o_nome_existe(nome):
        if len(Agenda[nome]) > 1:
            Agenda[nome] = Qual_telefone_excluir(Agenda[nome])
        else:
            Excluir_nome_e_telefone(nome)
    
    else:
        print("Nome não existe")


def Excluir_nome():
    nome = digitar_nome()
    
    if verificar_se_o_nome_existe(nome):
        Excluir_nome_e_telefone(nome)
    else:
        print("Nome não existe")

            
def Consultar_telefone():
    nome = digitar_nome()
    
    if verificar_se_o_nome_existe(nome):
        printar_nome_e_telefone(nome)
    else:
        print("Nome não existe")
        
        
            
def main():
    
    while True:
        try:
            # print(Agenda)
            print("1-Incluir novo nome\n2-Incluir Telefone\n3-Excluir telefone\n4-Excluir nome\n5-Consultar telefone\nNegativo para sair")
            opcao = int(input())
            
            if opcao == 1:
                Incluir_novo_nome()
            elif opcao == 2:
                Incluir_telefone()
            elif opcao == 3:
                Excluir_telefone()
            elif opcao == 4:
                Excluir_nome()
            elif opcao == 5:
                Consultar_telefone()
            elif opcao < 0:
                break
            else:
                print("Opção inválida")
        except:
            print("Opção errada")        
        
        print()
    
    
Agenda = {} 
    
main()