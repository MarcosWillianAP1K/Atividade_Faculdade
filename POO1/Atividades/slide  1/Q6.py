
try:
    numero = int(input("Digite um número: "))
    
    total = numero
    
    for i in range(1, numero):
        total = total * i
    
    print(f"O resultado é: {total}")
    
except:
    print("erro")