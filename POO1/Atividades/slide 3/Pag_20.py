import random


def verificar(lista):
    
    for i in lista:
        
        if lista.count(i) > 1:
            return False
        
    return True
            
            
    

def sortear( inicio, fim, quant):
    lista = []
    
    
    for i in range(quant):
        lista.append( random.randint(inicio, fim))
        
        if not verificar(lista):
            lista.pop()
            
    return lista
        
        


while True:

    try:
    
        valor_inicial = int(input("Digite o inicio: "))
        valor_final = int(input("Digite o valor final: "))
        quant = int(input("Quantos sortear?: "))
        
        lista = sortear(valor_inicial, valor_final, quant)
        
        break
        
    except:
        print("Valor incompativel\n")
        
        
print(f"\n{lista}")