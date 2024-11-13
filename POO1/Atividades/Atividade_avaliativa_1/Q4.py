def primo(n):
    
    if n <= 1:
        return False
    
    for i in range(2, n):
        
        if n % i == 0:
            return False
    
    return True


def printar(n1, n2):
    
    for i in range(n1, n2+1):
        
        if primo(i):
            print(f"{i} ", end="")
            
            
            
try:
    
    n = int(input())
    
    if primo(n):
        print("É primo")
        
    else:
        print("Não é primo")
        
    print()
        
    n1 = int(input())
    n2 = int(input())
    
    print()
    printar(n1, n2)
    
except:
    print("deu ruim")