armazem = {"Teste" : [10.0, 5, "10/10/2021"]}



    
def verificar_se_ja_existe(nome):
    if nome in armazem:
        return True
    else:
        return False
    
    
def digitar_produto():
    try:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        print("Digite a data de validade")
        dia = int(input("dia: "))
        mes = int(input("mês: "))
        ano = int(input("ano: "))
        
        
        data_validade = f"{dia:02d}/{mes:02d}/{ano:04d}"
        return {nome: [preco, quantidade, data_validade]}
        
        
    except:
        print("Erro ao digitar o produto")
        return None


def adicionar_produto(produto):
    
    if verificar_se_ja_existe(list(produto.keys())[0]):
        print("Produto já cadastrado")
    else:
        armazem.update(produto)
    
def listar_produtos():
    for i in armazem:
        print(f"\nNome: {i}\nPreço: {armazem[i][0]}\nQuantidade: {armazem[i][1]}\nData de validade: {armazem[i][2]}\n")
    print()

def buscar_produto(nome):
        if nome in armazem:
            print(f"\nNome: {nome}\nPreço: {armazem[nome][0]}\nQuantnomedade: {armazem[nome][1]}\nData de valnomedade: {armazem[nome][2]}\n")
        else:
            print("Produto não encontrado")
            

def remover_produto(nome):
    if nome in armazem:
        del armazem[nome]
        print("Produto removido com sucesso")
    else:
        print("Produto não encontrado")            



def menu():
    
    
    
    while True:
        
        try:
            opcao = int(input("\nSelecione uma das opções\n1-Adicionar um novo produto.\n2-Listar todos os produtos cadastrados.\n3-Buscar um produto específico pelo nome.\n4-Remover um produto pelo nome.\n5-Sair do programa.\n"))

            
            if opcao == 1:
                adicionar_produto(digitar_produto())
                
            elif opcao == 2:
                listar_produtos()
                
            elif opcao == 3:
                produto = input("Digite o nome do produto que deseja buscar: ")
                buscar_produto(produto)
                
            elif opcao == 4:
                produto = input("Digite o nome do produto que deseja remover: ")
                remover_produto(produto)
                
            elif opcao == 5:
                print("Programa finalizado")
                break
            else:
                print("Opção invalida")
            
        except:
            print("ERROR")
            
            
menu()