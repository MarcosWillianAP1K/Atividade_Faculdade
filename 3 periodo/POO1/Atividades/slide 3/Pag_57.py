import random

resultados = []


for i in range(100):
    resultados.append(random.randint(1, 6))
    
print(f"1: {resultados.count(1)}")
print(f"2: {resultados.count(2)}")
print(f"3: {resultados.count(3)}")
print(f"4: {resultados.count(4)}")
print(f"5: {resultados.count(5)}")
print(f"6: {resultados.count(6)}")