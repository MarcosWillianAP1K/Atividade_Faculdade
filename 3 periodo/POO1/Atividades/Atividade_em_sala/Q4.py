

def  valor_serie(n):
    
    if n <= 0:
        return 0
    
    valor_final = 1.0
    topo = 1
    base = 1
    
    print(f'{topo}/{base}', end='')
    
    while topo < n:
        topo += 1
        base += 2
        valor_final += topo/base
        
        print(f' + {topo}/{base}', end='')
    
    print("\n")
    
    
    return valor_final

print(valor_serie(10), end="\n\n")
    
    
    