
class quadrado:
    
    def digitar_quadrado():
        lado = float(input("Digite o lado do quadrado"))
        
        return lado * lado
        
class triangulo:
    
    def digitar_triangulo():
        print("Digite os 3 lados respectivos")
        lado1 = float(input())
        lado2 = float(input())
        lado3 = float(input())
        
        if (lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2)) :  
            return (lado1 + lado2 + lado3) / 2
      
        return "Invalido"


class circulo:
    
    def digitar_circulo():
        raio = float(input("Digite o raio do circulo\n"))
        
        return 3.14 * (raio**2)
    

while True:
    
    try:
        opcao = int(input("1-Quadrado\n2-Triangulo\n3-Circulo\n4-Sair\n"))
        
        try:    
            if opcao == 1:
                print(f"Area do quadrado: {quadrado.digitar_quadrado()}\n")
        
            elif opcao == 2:
                print(f"Area do triangulo: {triangulo.digitar_triangulo()}\n")
            
            elif opcao == 3:
                print(f"Area do circulo: {circulo.digitar_circulo()}\n")
        
            elif opcao == 4:
                break
        
            else:
                print("opção errada\n")
                
        except:
            print("valor invalido\n")
        
    except:
        print("Valor invalido\n")