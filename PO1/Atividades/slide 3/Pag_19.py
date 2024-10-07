
lista = []

while  True:
    
    try:
        n = int(input("Numero: "))
        
        if n < 0:
            break
        
        elif n == 0:
            if len(lista) == 1 and lista[0] % 2 == 0:
                lista.insert(1, 0)
            
            else:
                lista.insert((len(lista) // 2), 0)
            
        elif n % 2 == 0:
            lista.insert(0, n)
            
        else:
            lista.append(n)
            
        print(f"{lista}\n")
        
        
    except:
        continue
    
    
# print(f"\n{lista}")