import random as rand


def joguinho():
    
    numero_sorteado = rand.randint(0,100)
    
    print(f"O número sorteado era {numero_sorteado}")
    
    i = 0
    while i < 10:
        try:
            n = int(input(f"Tentativa {i+1} : "))
        
            if n == numero_sorteado:
                print("Parabéns, você acertou!")
                break
            i += 1
        
        except ValueError:
            print("Digite um número válido")
    
    print(f"O número sorteado era {numero_sorteado}")
    
        
        

joguinho()