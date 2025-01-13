import math as m


def raiz_quadrada(num):

    anterior =  num
    estimativa = 1

    while estimativa != anterior:
        anterior = estimativa
        estimativa = (estimativa + (num/estimativa))/2
        
    return estimativa


num = int(input("Digite um numero: "))

    
print(raiz_quadrada(num))

print(m.sqrt(num))
