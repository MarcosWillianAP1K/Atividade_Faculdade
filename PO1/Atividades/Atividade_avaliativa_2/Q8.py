import random as rand

def gerar_numeros():
    
    lista = []
    
    for i in range(13):
        lista.append(rand.randint(1,3))
        
    return lista


def conferir_cartao(cartao, numeros_sorteados):
    
    acertos = 0
    
    print(cartao)
    
    for i in range(len(cartao)):
        if cartao[i] == numeros_sorteados[i]:
            acertos += 1
            
    return acertos
    
        
numeros_da_loteria = gerar_numeros()

print(numeros_da_loteria)

cartoes = {
    1: gerar_numeros(),
    2: gerar_numeros(),
    3: gerar_numeros(),
}

for i in cartoes:

    if conferir_cartao(cartoes[i], numeros_da_loteria) == 13:
        print(f"O cartão {i} foi o vencedor!")
else:
    print("Nenhum cartão foi o vencedor")
    