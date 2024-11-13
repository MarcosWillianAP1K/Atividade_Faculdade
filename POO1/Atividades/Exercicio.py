
try:
    a = float(input())
    b = float(input())
    c = float(input())
    
    if (a < (b + c)) or (b < (a + c)) or (c < (a + b)):
        
        if a == b and b == c and a == c:
            print("\nTriangulo equilatero")
            
        elif a == b or b == c or a == c:
            print("\nTriangulo isosceles")
            
        elif a != b and b != c and a != c:
            print("\nTriangulo escaleno")
    
    else:
        print("Não forma um triangulo")
        

except:
    print("Vc não digitou um número")