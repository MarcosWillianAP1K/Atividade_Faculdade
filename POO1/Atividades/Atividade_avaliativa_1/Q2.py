def fatorial_interata(n):
    
    if n == 0:
        return 0
    
    total = 1
    for i in range(1, n+1):
        total *= i
    
    return total
    
def fatorial_recursiva(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return n * fatorial_recursiva(n-1)
    
    
try:
    n = int(input())
    
    print(f"Fatorial interativo: {fatorial_interata(n)}\nFatorial recursivo: {fatorial_recursiva(n)}")
    
except:
    print("deu ruim")