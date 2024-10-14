
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("antes: ", lista)


for i in range(len(lista) // 2):
    lista[i], lista[-i-1] = lista[-i-1], lista[i]
    
    
print("depois: ", lista)