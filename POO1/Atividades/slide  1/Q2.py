
try:
    
    peso_do_peixe = float(input("Digite o peso do peixe: "))

    if peso_do_peixe > 50:
        print(f"O peso do peixe excedeu o limite em {peso_do_peixe - 50:.2f}kg e a multa é de R${(peso_do_peixe - 50) * 4:.2f}")
    
    else:
        print("O peso do peixe não excedeu o limite")

except:
    print("Vc não digitou um número")