def fatorial_recursiva(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return n * fatorial_recursiva(n-1)


n = 3
p = 2

print(f"A = {fatorial_recursiva(n) / fatorial_recursiva(n - p)}")
print(f"B = {fatorial_recursiva(n) / (fatorial_recursiva(p) * fatorial_recursiva(n - p))}")