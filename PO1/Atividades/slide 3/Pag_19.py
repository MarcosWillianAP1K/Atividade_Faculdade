
lista = []

while  True:
    
    try:
        n = int(input("Numero: "))
        
        if n < 0:
            break
        
        elif n == 0:
            
            try:
                if lista[-1] % 2 == 0:
                    lista.insert((len(lista) // 2) + 1, 0)
                
                elif lista[0] % 2 != 0 or lista[0] == 0:
                    lista.insert(0, 0)
                
                else:
                    lista.insert((len(lista) // 2), 0)
            except:
                lista.append(0)
            
        elif n % 2 == 0:
            lista.insert(0, n)
            
        else:
            lista.append(n)
            
        print(f"{lista}\n")
        
        
    except:
        continue
    
    
# print(f"\n{lista}")
