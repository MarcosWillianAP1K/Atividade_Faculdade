def novo_index(lista, indice):
    
    if indice in lista and type(indice) != list:
        
        if type(indice) == str:
            tam = len(indice)
        else:
            tam = 1
    
        for i in range(len(lista)):
            # print(lista[i: tam+i])
            
            if indice in lista[i: tam+i]:
                return i
    
    return ValueError


def novo_find(lista, indice):
    
    if indice in lista and type(indice) == str:
        
        tam = len(indice)
    
        for i in range(len(lista)):
            # print(lista[i: tam+i])
            
            if indice in lista[i: tam+i]:
                return i
    
    return -1



print(novo_index("ola mundo", "ola"))

print(novo_find("ola mundo", "ola"))