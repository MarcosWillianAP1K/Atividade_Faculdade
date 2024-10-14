def ordenar (palavra):
    
    if type(palavra) == str:
        palavra = list(palavra)
        
        c = 0
        tam = len(palavra)
        
        while c < tam-1:
            
            if palavra[c] > palavra[c+1] and c >= 0:
                palavra[c], palavra[c+1] = palavra[c+1], palavra[c]
                c -=1
            else:
                c += 1
                
        return "".join(palavra)
        
        
        
        
print(ordenar("ola mundo"))