
try:
    
    numero = int(input("Digite um número: "))
    inicio = int(input("Digite o inicio: "))
    fim = int(input("Digite o fim: "))
    
    print()
    for i in range(inicio, fim+1):
        print(f"{numero} x {i} = {numero*i}")
    
    print()
except:
    print("erro")