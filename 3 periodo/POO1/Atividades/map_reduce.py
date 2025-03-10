import functools as ft


l= [1,2,3,4,5,6]

resultado = ft.reduce(lambda x, y: x + y, map(lambda x: x * 2, filter(lambda x: x % 2 == 0, l)))

print(resultado)

lista = [[[[[[[[[[[[[["bah"]]]]]]]]]]]]]]

print(lista[0][0][0][0][0][0][0][0][0][0][0][0][0][0])

print(lista)