print("Digite as notas")
notas = []

while True:
    try:
        nota = float(input())
        
        if nota < 0:
            break
        
        notas.append(nota)
        
    except ValueError:
        continue

print(notas)
print(sum(notas) / len(notas) if notas else 0)
