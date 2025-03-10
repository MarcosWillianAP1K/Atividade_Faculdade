
try: 
    litro = float(input("Digite a quantidade de litros: "))
    combustivel = input("G gasolina\nA alcool\n")
    
    if combustivel == "G" or combustivel == "g":
        if litro <= 20:
            preco_final = (litro * 4.53) - (litro * 4.53) * 0.03
            
        else:
            preco_final = (litro * 4.53) - (litro * 4.53) * 0.05
    
        print(f"Pagara R${preco_final:.2f}")
        
    elif combustivel == "A" or combustivel == "a":
        
        if litro <= 20:
            preco_final = (litro * 3.45) - (litro * 3.45) * 0.04
            
        else:
            preco_final = (litro * 3.45) - (litro * 3.45) * 0.06
        
        print(f"Pagara R${preco_final:.2f}")
    else:
        print("Combustivel invalido")
        
except:
    print("erro")