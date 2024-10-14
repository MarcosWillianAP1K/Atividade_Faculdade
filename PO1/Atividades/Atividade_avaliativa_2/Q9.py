#testando o uso de classes
class Pessoa:
    def dados_prontos():
        return {"nome": "teste", "endereco": "teste", "bairro": "teste", "telefone": "teste", "CEP": "teste"}
   
    def inserir_dados():
        
        nome = input("Digite o nome: ")
        endereco = input("Digite o endereço: ")
        bairro = input("Digite o bairro: ")
        telefone = input("Digite o telefone: ")
        CEP = input("Digite o CEP: ")
        
        return {"nome": nome, "endereco": endereco, "bairro": bairro, "telefone": telefone, "CEP": CEP}

    

lista_pessoas = []

for i in range(10):
    
    if i < 2:
        lista_pessoas.append(Pessoa.inserir_dados())
        print()
        
    else:
        lista_pessoas.append(Pessoa.dados_prontos())
    

lista_pessoas.reverse()

for i in lista_pessoas:
    for j in i:
        print(f"{j}: {i[j]}")
    print()
    
    
    