import random as rand

def media(lista):
    return sum(lista)/len(lista)

def mediana(lista):
    lista.sort()
    tam = len(lista)
    
    if tam % 2 == 0:
        return (lista[tam//2] + lista[tam//2 - 1]) / 2
    else:
        return lista[tam//2]


def variancia(lista, media_lista):
    
    soma = 0
    for i in lista:
        soma += (i - media_lista)**2
        
    return soma / len(lista)


def desvio_padrao(varaincia_lista):
    return  variancia_lista ** 0.5


lista = []

for i in range(100):
    lista.append(rand.randint(1,100))
    
    
media_lista = media(lista)
mediana_lista = mediana(lista)
variancia_lista = variancia(lista, media_lista)
desvio_padrao_lista = desvio_padrao(variancia_lista)

print(lista)
print(f"Media: {media_lista}")
print(f"Mediana: {mediana_lista}")
print(f"Variancia: {variancia_lista}")
print(f"Desvio padrão: {desvio_padrao_lista}")
