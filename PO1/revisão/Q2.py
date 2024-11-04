def raiz (num):
    estimativa = 1
    anterior = num
    
    while estimativa != anterior:
        anterior =  estimativa
        estimativa = (estimativa + (num/estimativa))/2
        
    return estimativa

resultado = raiz(9)

print(resultado)