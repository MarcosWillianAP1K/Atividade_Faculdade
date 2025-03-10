lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
lista2= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
resultado = []

for i in range(10):
    resultado.append(lista1[i] * lista2[i])
    
print(resultado)