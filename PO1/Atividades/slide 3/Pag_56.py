
def funcao(parametro):
    return parametro

def apenas_pares(lista):
    return [num for num in lista if num % 2 == 0]

def apenas_negativos(lista):
    return [num for num in lista if num < 0]

lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

print(max(lista), end="\n\n")

print(min(lista), end="\n\n")

print(apenas_pares(lista), end="\n\n")

print(lista[0], "tem ", lista.count(lista[0]), " desse numero", end="\n\n")

print(sum(lista) / len(lista),end="\n\n")

print(sum(apenas_negativos(lista)),end="\n\n")