



    



try:
    base = float(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    
    total = 1
    
    for i in range(expoente):
        total *= base
    
    print(f"O resultado é: {total}")
    
except:
    print("erro")