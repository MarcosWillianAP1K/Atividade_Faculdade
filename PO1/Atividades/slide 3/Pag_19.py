
lista = []

while  True:
    
    try:
        n = int(input("Numero: "))
        
        if n < 0:
            break
        
        elif n == 0:
            lista.insert(len(lista) // 2, 0)
            
        elif n % 2 == 0:
            lista.insert(0, n)
            
        else:
            lista.append(n)
        
        
    except:
        continue
    
    
print(f"\n{lista}")