
def soma(a,b):
    print(a + b)

def sub(a,b):
    print(a - b)

def mult(a,b):
    print(a * b)
    
def div(a,b):
    if b != 0:
        print(a / b)
    else:
        print("Divisão por zero, impossivel")



while True:

    try:
        print("Digite dois valores")
        a = float(input())
        b = float(input())

        while True:
            
            opcao = int(input("\n1-soma\n2-sub\n3-mult\n4-div\n5-digitar outros numeros\n6-sair\n"))
            print()
            
            if opcao == 1:
                soma(a,b)
                
            elif opcao == 2:
                sub(a,b)
                
            elif opcao == 3:
                mult(a,b)
                
            elif opcao == 4:
                div(a,b)
                
            elif opcao == 5:
                print()
                break
                
            elif opcao == 6:
                break
                
            else:
                print("Opcao invalida\n")
      
      
        if opcao == 6:
            break
    except:
        continue

